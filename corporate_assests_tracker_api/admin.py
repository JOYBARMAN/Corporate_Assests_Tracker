from django.contrib import admin
from .models import *

class CompanyModelAdmin(admin.ModelAdmin):
    list_display = ('name','address', 'contact_info')
    list_filter = ('address',)
    search_fields = ('name',)

class EmployeeModelAdmin(admin.ModelAdmin):
    list_display = ('employee','company', 'job_title')
    list_filter = ('company__name',)
    search_fields = ('employee__name',)


class DeviceModelAdmin(admin.ModelAdmin):
    list_display = ('serial_number','company', 'model')
    list_filter = ('company__name',)
    search_fields = ('serial_number','model')


class AssignDeviceModelAdmin(admin.ModelAdmin):
    list_display = ('employee','device','assigned_date','return_date','assigned_condition','returned_condition',)
    list_filter = ('device__model',)
    search_fields = ('employee__name',)

# Now register the new Company Admin
admin.site.register(CompanyInfo,CompanyModelAdmin)

# Now register the new Employee Admin
admin.site.register(EmployeeInfo,EmployeeModelAdmin)

# Now register the new Device Admin
admin.site.register(Device,DeviceModelAdmin)

# Now register the Assign Device Admin
admin.site.register(AssignmentDevice,AssignDeviceModelAdmin)
