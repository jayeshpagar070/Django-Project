from django.contrib import admin

# Register your models here.

from Service.models import Service
from Service.models import tab

class Service_admin (admin.ModelAdmin):
    list_display = ('service_icon','service_title','service_desc')


admin.site.register(Service,Service_admin)

class tabs_admin(admin.ModelAdmin):
    list_show = ('tabs_title')

admin.site.register(tab,tabs_admin)

