from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Employee, UserDataForm
from .forms import EmployeeForm, NewUserForm
from django.contrib.auth import logout
from django.contrib import messages

def index(request):
    return render(request,"index.html")


def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Account created successfully')
            form.save()
    else:
        form = NewUserForm()
    return render(request, 'register.html', {'form': form})



def register_user_data(request):
    
    name = request.POST['username']
    mail = request.POST['email']
    pswd1 = request.POST['password1']
    pswd2 = request.POST['password2']

    print(name)
    print(mail)
    print(pswd1)
    print(pswd2)

    a = UserDataForm(eid=name, eemail=mail, epassword1=pswd1, epassword2=pswd2)
    a.save()
    return HttpResponse("user registered successfully.")
   
            
    
def login(request):
  
    return render(request,"login.html")


def welcome(request):

    mail = request.POST['eemail']
    pswd = request.POST['epassword1']

    print(mail)
    print(pswd)
    
    user = UserDataForm.objects.all()
    for eid in user:
        print(eid)

        if eid.eemail in mail and eid.epassword1 in pswd:
            return render(request,"welcome.html",{'user': user})
        
    return HttpResponse("Invalid Data or user is not registered.")



def load_form(request):
    form=EmployeeForm
    return render(request,"add.html",{'form': form})



def add(request):
    form=EmployeeForm(request.POST)
    form.save()
    return redirect('/show')


def show(request):
    employee = Employee.objects.all()
    return render(request, 'show.html', {'employee': employee})



def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, 'edit.html', {'employee': employee})



def update(request, id):
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance=employee)
    form.save()
    return redirect('/show')



def delete(request, id):
    employee = Employee.objects.get(id=id)  
    employee.delete()
    return redirect('/show')

# if you don't want your search to be case sensitive use iexact with ename

# if you want it to search similar names use icontains with ename

def search(request):
    given_name = request.POST['name']
    employee = Employee.objects.filter(ename__icontains=given_name)
    return render(request,'show.html', {'employee': employee})



def user_logout(request):
    logout(request)
    return redirect('/index')
