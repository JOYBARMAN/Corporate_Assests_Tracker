from django.db import models
from account_api.models import User

''' This model will store the information about each company using the app.
It will have fields like name, address, and contact information. '''
class CompanyInfo(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

'''This model will store information about the employees of each company.
 It will have fields like name, email, and job title.'''
class EmployeeInfo(models.Model):
    employee = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(CompanyInfo, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.employee.name

'''This model will store information about the devices that are being tracked.
 It will have fields like serial number, model, and description.'''
class Device(models.Model):
    serial_number = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    description = models.TextField()
    company = models.ForeignKey(CompanyInfo, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.serial_number

'''This model will store information about the devices that are assigned to employees.
 It will have fields like the date the device was assigned, the date it was returned
  and the condition it was in when it was assigned and returned.'''
class AssignmentDevice(models.Model):
    employee = models.ForeignKey(EmployeeInfo, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    assigned_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    assigned_condition = models.CharField(max_length=255)
    returned_condition = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.device} - {self.employee}"
