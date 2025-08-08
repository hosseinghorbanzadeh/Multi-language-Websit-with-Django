from django.contrib import admin
from blog.models import Contact,Newsletter






class ContactAdmin(admin.ModelAdmin):
    date_hierarchy="created_date"
    list_display = ["subject", "name"]
    search_fields=['subject','name']
    list_filter = ('subject',)



admin.site.register(Contact,ContactAdmin)
admin.site.register(Newsletter)
