from django.contrib import admin

from books.models import Author, Book, Images, Category

admin.site.site_header = "BOOKMARKET"
admin.site.site_title = "Панель администрирования"
admin.site.index_title = "Welcome to admin panel"

admin.site.register(Author)
admin.site.register(Images)
admin.site.register(Category)


@admin.register(Book)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'categories', 'year']
    ordering = ('-year',)
    search_fields = ['title']
    list_filter = (
        ('description', admin.EmptyFieldListFilter),
        ('pdf', admin.EmptyFieldListFilter),
    )
    actions = ['mark_as_visible']

    @admin.action(description='Сделать видимым')
    def mark_as_visible(self, request, queryset):
        queryset.update(is_visible=True)


