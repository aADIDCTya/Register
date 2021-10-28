from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login,logout,authenticate
from .models import Form
from .forms import StudentForm
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request,'forms/home.html')

@login_required
def register(request):
    if request.method =='GET':
            return render(request,'forms/register.html',{'form':StudentForm()})
    else:
        
        form = StudentForm(request.POST)
        newForm = form.save(commit=False)
        newForm.user = request.user
        newForm.save()
        return redirect('viewform')
        
    

def signupuser(request):
    if request.method == 'GET':    
        return render(request,'forms/signupuser.html',{'form':UserCreationForm()})
    #create a new user
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'],password = request.POST['password1'])
                user.save()
                login(request,user)
                return  redirect('viewform')

            except IntegrityError:
                return render(request,'forms/signupuser.html',{'form':UserCreationForm(),'error':'Username has been already taken'})


        else:
        #password didn't matched
            return render(request,'forms/signupuser.html',{'form':UserCreationForm(),'error':'password didnt matched'})
        
def loginuser(request):
    if request.method == 'GET':    
        return render(request,'forms/loginuser.html',{'form':AuthenticationForm()})
    #create a new user
    else:
        user = authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request,'forms/loginuser.html',{'form':AuthenticationForm(),'error':'Username and password did not matched'})
        else:
             login(request,user)
             return  redirect('register')

                

    

@login_required
def currentforms(request):
    deats =Form.objects.filter(user = request.user)
    return render(request,'forms/currentforms.html',{'deats':deats})


@login_required
def viewform(request):
    deats =Form.objects.filter(user = request.user)
    
    return render(request,'forms/viewform.html',{'deats':deats})



@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
    return redirect('home')

