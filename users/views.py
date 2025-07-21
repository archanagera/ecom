from django.shortcuts import redirect, render
#from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.contrib import messages 
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.method=="POST":
        # form=UserCreationForm(request.POST)
        form=RegisterForm(request.POST)
        if form.is_valid():
                username=form.cleaned_data.get('username')
                print(username)
                str=f'WElcome {username} , Your account is created successfully'
                form.save()
                messages.success(request,str)
                return redirect('login')
                #return redirect('food:index')
    else:

        #form=UserCreationForm()
        form=RegisterForm()
    return render(request,'users/register.html',{'form':form})

# def register(request):  
#     #2nd
#     if request.method=="POST":
#         form=UserCreationForm(request.POST)
#         if form.is_valid():
#             username=form.cleaned_data.get('username')
#             messages.success(request,f'Welcome {username}, your account is created')
#             return redirect('food:index')
#     else:
#         form=UserCreationForm()
    
#     return render(request,'users/register.html',{'form':form})

def custom_logout(request):
    logout(request)
    #return render(request,'users/logout.html')
    return redirect('login')

@login_required
def profilepage(request):
     return render(request,'users/profile.html')