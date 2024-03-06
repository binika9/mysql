from django.shortcuts import render, redirect

from employee_module.forms import EmployeeForm, registrationForm, next_of_kin_Form
from employee_module.models import Employee


# Create your views here.
def employee_form(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = EmployeeForm()
        # return render(request, 'employee_form.html', {'form': form})
        else:
            employee = Employee.objects.get(pk=id)  # PK-PRIMARY KEY
            form = EmployeeForm(instance=employee)
        return render(request, 'employee_form.html', {'form': form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            # EmployeeForm()
        return redirect('/employee/employeelist/')


def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request, 'employee_list.html', context)


def registration(request):
    if request.method == 'GET':
        form = registrationForm()
        return render(request, 'registration.html', {'form': form})
    else:
        form = registrationForm(request.POST)
        if form.is_valid():
            form.save()
            registrationForm()
            return redirect('registration')


def next_of_kin(request):
    if request.method == 'GET':
        form = next_of_kin_Form()
        return render(request, 'next_of_kin.html', {'form': form})
    else:
        form = next_of_kin_Form(request.POST)
        if form.is_valid():
            form.save()
            next_of_kin_Form(request.POST)
            return redirect('next_of_kin')


def employee_delete(request, id=0):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/employeelist/')
