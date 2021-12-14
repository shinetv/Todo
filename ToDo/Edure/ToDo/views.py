from django.core.exceptions import RequestAborted
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import *
import easygui

# Create your views here.

def login(request):
    if request.method=="POST":
        User_name=request.POST['User_name']
        Password=request.POST['Password']
        User=User_reg.objects.filter(User_name=User_name,Password=Password)
        if User:
            for x in User:
                request.session['id'] = x.id
                request.session['User_name'] = x.User_name
                request.session['std_type'] = x.std_type
                request.session['Password'] = x.Password

                print("________________________", request.session['id'])
            return HttpResponseRedirect('/dashboard/')
        else:
            return render(request, 'login.html', {'msg': 'Invalid login credentials.!'})    
    return render(request,'login.html')

def sign(request):
    if request.method=='POST':
        if User_reg.objects.filter(User_name=request.POST['User_name']):
            easygui.msgbox("USERNAME ALREADY TAKEN !")
        else:
            users=User_reg()
            users.User_name=request.POST['User_name']
            users.Mail_id=request.POST['Mail_id']
            users.gender=request.POST['gender']
            users.Password=request.POST['Password']
            users.Confirm_password=request.POST['Confirm_password']
            users.std_type='User'
            if users.Password == users.Confirm_password:
                users.save() 
                easygui.msgbox("You Are Welcome !")
                return redirect(login)
            else:
                
                return render(request,'signup.html',{'msg':'oops!Check both Password'})   
    return render(request,'signup.html')    

def dashboard(request):
    SessionId     =request.session['id']
    sid              = User_reg.objects.all().get(id=SessionId)
    user_task=tasks.objects.all().filter(task_IDD=sid)
    if request.method=="POST":
        task=tasks()
        task.user_task=request.POST['user_task']
        task.percentage=request.POST['percentage']
        task.dates=request.POST['dates']
        task.task_IDD=sid
        task.save()
        easygui.msgbox("Task added !")
        return redirect(dashboard)
    return render(request,'dashboard.html',{'user_task':user_task})    

def logout(request):
    if request.session.has_key('id'):
        del request.session['id']
        logout(request)
        return redirect(login)

def update(request,id):
    edit=tasks.objects.get(id=id)
    return render(request,'update.html',{'edit':edit})


def updateedit(request,id):
    
    SessionId     =request.session['id']
    sid              = User_reg.objects.all().get(id=SessionId)
    user_task=request.POST['user_task']
    percentage=request.POST['percentage']
    dates=request.POST['dates']
    task_IDD=sid
    edit=tasks.objects.all().filter(id=id).update(user_task=user_task,percentage=percentage,dates=dates,task_IDD=task_IDD)
                            
                      
   
    easygui.msgbox("UPDATED!")
    return redirect(dashboard)

def delete(request,id):
    var2=tasks.objects.get(id=id)
    return render(request,'delete.html',{'var2':var2})

def deletetask(request,id):
    var2=tasks.objects.get(id=id)
    var2.delete()
    easygui.msgbox("DELETED !")
    return redirect(dashboard)








