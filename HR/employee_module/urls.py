from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employeeform/', views.employee_form, name='employee_form'),
    path('registration/', views.registration, name='registration'),
    path('next_of_kin/', views.next_of_kin, name='next_of_kin'),
    path('employeelist/', views.employee_list, name='employee_list'),
    path('<int:id>/', views.employee_form, name='employee_update'),
    path('delete/<int:id>/', views.employee_delete, name='employee_delete')
]
