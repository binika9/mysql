from django.contrib import admin

from employee_module.models import Employee, registration, next_of_kin

# Register your models here.
admin.site.register(Employee)
admin.site.register(registration)
admin.site.register(next_of_kin)
