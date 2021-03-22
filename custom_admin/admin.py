from django.contrib import admin
from .models import *
from django.utils import timezone
from django.utils import timezone
from django.db.models import Count
from import_export.admin import ImportExportModelAdmin
from custom_admin.resources import CommentResource


class CommentsInline(admin.TabularInline):
    model = Comment
    classes = ('collapse',)
    extra = 1


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'last_modified', 'body', 'date_created', 'is_draft', 'day_since_creation', 'no_of_comments',)
    list_filter = ('is_draft',)
    ordering = ('title',)
    search_fields = ('body',)
    prepopulated_fields = {'slug': ('title',)}
    list_per_page = 50
    actions = ('change_draft',)
    date_hierarchy = 'date_created'
    # fields=(('title','slug'),'body','is_draft')
    fieldsets = (
        ('HEY', {
            "fields": (
                ('title', 'slug'), 'body',),
        }),
        ('Advanced options', {
            "fields": ('is_draft', 'category',),
            'description': 'custom fieldset description'
        }),
    )
    inlines = [
        CommentsInline,
    ]
    filter_horizontal = ('category',)

    def get_queryset(self,
                     request):  # создаёшь ф-ю кот-я возвращ нужные даныне и потом метод (ниже), котор вставляет их в поле
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(comments_count=Count('comments'))
        return queryset

    def no_of_comments(self, blog):  # вызываешь его в блогАдмин оно передает инстанс блог и в нем находишь кол-во
        return blog.comments_count

    no_of_comments.admin_order_field = 'comments_count'  # сортировка по клику

    def day_since_creation(self, blog):
        diff = timezone.now() - blog.date_created
        return 23

    day_since_creation.short_description = 'short descr'

    def get_ordering(self, request):
        if request.user.is_superuser:
            return ('title',)
        return ('body',)

    def change_draft(self, request, queryset):
        count = queryset.update(is_draft=False)
        self.message_user(request, f'Success message {count}')


class CommentAdmin(ImportExportModelAdmin):
    list_display = ('blog', 'body', 'date_created', 'is_active',)
    list_editable = ('body', 'is_active',)
    list_filter = ('body',)

    # Чтобы создать импотр экспорт качаешь django-import-export
    # создаёшь файл resources (смотри туда), и потом сюда экстендишь
    resource_class = CommentResource
    list_select_related = True


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)

admin.site.register(Comment, CommentAdmin)
