from django.contrib import admin
from django.forms import ModelForm
from django.http import HttpResponseRedirect
from django.urls import path

from .models import *
from django.utils import timezone
from django.utils import timezone
from django.db.models import Count
from import_export.admin import ImportExportModelAdmin
from custom_admin.resources import CommentResource


class CommentsInline(admin.TabularInline):
    model = Comment
    extra = 0


class BlogAdmin(admin.ModelAdmin):
    change_list_template = 'custom_admin/blog/change_list.html'
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

        # Фильтрация по связанным полям
        # queryset = queryset.annotate(with_comments=Count('comments')).filter(with_comments__gt=0)

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

    def get_urls(self):
        urls = super(BlogAdmin, self).get_urls()
        custom_urls = [
            path('toggle_blogs/', self.toggle_blogs_by_comments, name='change_slug'),
        ]
        return custom_urls + urls

    def toggle_blogs_by_comments(self, request):
        return HttpResponseRedirect('../')

    class Media:
        css = {
            'all': ('custom_admin/css/sort_non_comments.css',)
        }
        js = ('custom_admin/js/change_bool.js',)


class CommentAdminForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if not instance.is_active:
            self.fields['active_name'].widget.attrs.update({
                'readonly': True, 'style': 'background-color:lightgray'
            })


class CommentListFilter(admin.SimpleListFilter):
    def queryset(self, request, queryset):
        if self.value() == 'low':
            return queryset.filter(price__lte=100)
        elif self.value() == 'medium':
            return queryset.filter(price__gt=100,
                                   price__lt=500)
        elif self.value() == 'high':
            return queryset.filter(price__gte=500)

    title = 'Hey'
    parameter_name = 'HEY'

    def lookups(self, request, model_admin):
        return (
            ('low', 'Низкая цена'),
            ('middle', 'Средняя цена'),
            ('high', 'Высокая цена')
        )


class CommentAdmin(ImportExportModelAdmin):
    form = CommentAdminForm
    change_form_template = 'custom_admin/form_for_active.html'
    list_display = ('blog', 'body', 'date_created', 'price', 'is_active', 'get_html_photo',)
    list_editable = ('body', 'is_active',)
    list_filter = (CommentListFilter,)
    fields = ('blog', 'body', ('active_name', 'is_active',), 'get_html_photo',)
    readonly_fields = ('date_created', 'get_html_photo',)

    # Чтобы создать импотр экспорт качаешь django-import-export
    # создаёшь файл resources (смотри туда), и потом сюда экстендишь
    resource_class = CommentResource
    list_select_related = True

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src = '{object.photo.url}' width=50px> ")

    get_html_photo.short_description = "Миниатюра"


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)

admin.site.register(Comment, CommentAdmin)
