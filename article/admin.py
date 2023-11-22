from django.contrib import admin

from .models import BlogArticle, ContactRequest


class AdminPermissions:
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False


class BlogArticleAdmin(AdminPermissions, admin.ModelAdmin):
    list_display = ("title", "author", "publication_datetime", "publish_online")
    prepopulated_fields = {"slug": ("title",)}


class ContactRequestAdmin(AdminPermissions, admin.ModelAdmin):
    list_display = ("name", "email", "date")


admin.site.register(BlogArticle, BlogArticleAdmin)
admin.site.register(ContactRequest, ContactRequestAdmin)
