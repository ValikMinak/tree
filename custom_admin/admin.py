from django.contrib import admin
from .models import *
from django.utils import timezone
from django.utils import timezone



class BlogAdmin(admin.ModelAdmin):
    list_display=('title','last_modified','body','date_created','is_draft','day_since_creation')
    list_filter=('is_draft',)
    ordering=('title',)
    search_fields=('body',)
    prepopulated_fields={'slug':('title',)}
    list_per_page=50
    actions=('change_draft',)
    date_hierarchy='date_created'
    # fields=(('title','slug'),'body','is_draft')
    fieldsets = (
        ('HEY', {
            "fields": (
                ('title','slug'),'body',),
        }),
         ('Advanced options', {
            "fields": ('is_draft',),
            'description':'custom fieldset description'
        }),
    )
    
    def day_since_creation(self,blog):
        diff=timezone.now() - blog.date_created
        return 23
    day_since_creation.short_description='short descr'
    def get_ordering(self,request):
        if request.user.is_superuser:
            return ('title',)
        return ('body',)



    def change_draft(self,request,queryset):
        count = queryset.update(is_draft=False)
        self.message_user(request,f'Success message {count}')



admin.site.register(Blog,BlogAdmin)