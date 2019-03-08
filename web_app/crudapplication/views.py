from django.shortcuts import render, redirect
from crudapplication.forms import EmployeeForm
from crudapplication.models import Employee

def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/getAll")
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request, "add.html", {'form':form})

#Get All data 
def getAll(request):
    employees = Employee.objects.raw("select * from employee")
    return render(request, "index.html", {'employees':employees})

def edit(request,id):
    employees = Employee.objects.get(id=id)
    return render(request, "edit.html", {'employees':employees})


def update(request, id):
    employees = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance = employees)
    if form.is_valid():
            try:
                form.save()
                return redirect("/getAll")
            except:
                pass
    return render(request, "edit.html", {'employees':employees})


def delete(request, id):
    employees = Employee.objects.get(id=id)
    employees.delete()
    return redirect("/getAll")



    