from django.contrib import admin
from .models import  Company, User, Template, Equipment ,Record, CheckPoint,Team
from v1.admin import admin_site

from searchadmin.admin import SelectModelAdmin


# class DataMasterAdmin(SelectModelAdmin):
 ##25     search_fields = ('title','remark','distributor',)
 #26     list_display = ('master_code','title','remark', 'distributor', )
 #27     fields = ('master_code','title_show','title','img_show',
 #28         'img_url', 'scan_show','describe','describe_show', 'tel','company','master_uuid',
 #29         'remark', 'distributor', 'redirect_url','redirect_on',
 #30         'feedback_show',
 #31         )


class EquipmentAdmin(SelectModelAdmin):
    readonly_fields = ('url',)

admin_site.register(Company)
admin_site.register(User)
admin_site.register(Template)
admin_site.register(Equipment,EquipmentAdmin)
admin_site.register(Record)
admin_site.register(CheckPoint)
admin_site.register(Team)

 

# Register your models here.
