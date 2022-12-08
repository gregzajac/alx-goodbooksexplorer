from django.contrib import admin
from posts.models import Bio, Author, Post, Tag


# Register your models here.


class BioAdmin(admin.ModelAdmin):
    pass


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "full_name"]
    readonly_fields = ["full_name"]

    def get_fieldsets(self, request, obj=None):
        fieldsets = (
            ("From db", {
                'fields': ("first_name", "last_name",)
            }),
            ("Bio", {
                'fields': ("bio", "b_year",)
            }),

            ('Calculated', {
                'classes': ('collapse',),
                'fields': ('full_name',),
            }),
        )
        return fieldsets

    # def full_name(self, obj):
    #     return f"{obj.first_name} {obj.last_name}"


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    filter_horizontal = ["tags"]
    search_fields = ["title", "tags__name",]
    list_filter = ['is_ready']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Bio, BioAdmin)
