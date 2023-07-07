from datetime import datetime, timedelta
from typing import Callable

from django.conf import settings
from django.contrib.auth import logout
from django.http import HttpRequest, HttpResponse

from django.utils import timezone

import re
from django.http import HttpRequest, HttpResponse

RE_EMPTY_STRING = r'\n\s*?\n'
RE_STRING_SPACE_PREFIX = r'\n\s+'


now = timezone.now()


def logout_on_timeout(get_response: Callable[[HttpRequest], HttpResponse]) -> Callable:
    ttl = settings.LOGOUT_TIMEOUT

    def middleware(request: HttpRequest) -> HttpResponse:
        user = request.user

        if not user.is_anonymous and user.last_login < now - timedelta(seconds=ttl):
            logout(request)

        response = get_response(request)
        return response

    return middleware


def html_optimize(get_response):
    def middleware(request: HttpRequest):
        response: HttpResponse = get_response(request)

        new_content = re.sub(RE_EMPTY_STRING, lambda *_: '\n', response.content.decode())
        new_content = re.sub(RE_STRING_SPACE_PREFIX, lambda *_: '\n', new_content)
        response.content = new_content.encode()
        response["Content-Length"] = len(response.content)

        return response

    return middleware
