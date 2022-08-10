from email.headerregistry import Group
from django import forms
from django.contrib import messages
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import*
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required,user_passes_test


# Create your views here.
def Index(request):
    return render(request,'register.html')


def Register(request):
    if request.method=="POST":


     
        name = request.POST['name']
        author= request.POST['author']
        isbn=request.POST['isbn']
        publisher= request.POST['publisher']
        
      


        std = Book.objects.create(name =name,
                                  author =author,
                                  isbn=isbn,
                                  publisher=publisher,
                                   
                            )

    return redirect("showdata")    
   


def Showdata(request):
    a = Book.objects.all()
    return render(request,"show.html",{'user':a}) 


def Deletedata(request,id):
    b = Book.objects.get(id=id)
    b.delete()
    return redirect("showdata")  

def Editpage(request,pk):
    c = Book.objects.get(id=pk)
    return render(request,"update.html",{'user':c})

def Update(request,id):
    e = Book.objects.filter(id=id)
    if e.count() > 0:
        e.update(
            name= request.POST['name'], 
            author= request.POST['author'], 
            isbn = request.POST['isbn'], 
            publisher= request.POST['publisher'], 
            
        )
    return redirect("showdata")    


def adminsignup_view(request):
    form=forms.AdminSigupForm()
    if request.method=='POST':
        form=forms.AdminSigupForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()


            my_admin_group = Group.objects.get_or_create(name='ADMIN')
            my_admin_group[0].user_set.add(user)

            return HttpResponseRedirect('adminlogin')
    return render(request,'library/adminsignup.html',{'form':form})   

def viewbook_view(request):
    books=models.Book.objects.all()
    return render(request,'viewbook.html',{'books':books})

def login(request):
    return render(request,'adminlogin.html')
    
def registration(request):
    return render(request,'registration.html')


def loginpage(request):
    return render(request,'login.html')  

def studentclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'studentclick.html')


def Login_user(request):
    try:
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']

            user = Book.objects.get(email = email)
            if email:
                if user.password == password:
                    return redirect('showdata')
                else:
                    
                    messages.error(request,"Incorrect password")
                    return redirect('loginpage')
            else:
                messages.error(request,"Email Id is not registered")
                return redirect('loginpage')
    except:
       messages.error(request,"Email Id not found")
       return redirect('loginpage')