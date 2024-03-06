from django import forms
from employee_module.models import Employee, registration, next_of_kin


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['fullname', 'email', 'emp_code', 'mobile_no', 'position']


class registrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = registration
        fields = ['first_name', 'last_name', 'phone_no', 'password']


class next_of_kin_Form(forms.ModelForm):
    class Meta:
        model = next_of_kin
        fields = ['fullname', 'employee_name', 'id_no', 'phone_no']
