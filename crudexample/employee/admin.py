from django.contrib import admin
from employee.models import Employee 

# Register your models here.
admin.site.site_header = 'Employee Management System'

class EmployeeFilterByName(admin.ModelAdmin):
    list_display = ('name','phonenumber','address','designation')
    list_filter = ('name',)
    search_fields = ('name', )
    list_editable = ['phonenumber']

admin.site.register(Employee,EmployeeFilterByName)
