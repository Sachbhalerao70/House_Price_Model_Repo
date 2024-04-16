

from django.shortcuts import render,redirect
from .models import Get_Data_From_User_Model

from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, 'House_Price_Model/index.html')
def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user =authenticate(request,username=username,password=password)

        if user is not None:
            login(request, user)
            #return redirect('login_user')
            url = "/House_Price_Model/Price/?username={}".format(username)
            return HttpResponseRedirect(url)  # Redirect to price view with username parameter
        else:
            return HttpResponse('Check your email and password')


    return render(request,'House_Price_Model/login.html')
def register(request):
    if request.method == 'POST':

        username=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        if pass1!=cpassword:
            return HttpResponse('pass and cpassword not matched')
        else:

            myuser=User.objects.create_user(username,email,pass1)
            myuser.save()

            return redirect('log_in')






    return render(request,'House_Price_Model/register.html')

def login_user(r):
    # u=r.GET.get('username')


    return render(r,'House_Price_Model/login_user.html')

def log_out(r ):
    logout(r)
    return redirect('index')

#----------------------------------------------------------

def Price_Field(r):
    if r.method == 'POST':
        u = r.GET.get('username')
        area_type=r.POST.get('area_type')
        availability=r.POST.get('availability')
        location=r.POST.get('location')
        size=r.POST.get('size')
        society=r.POST.get('society')
        total_sqft=r.POST.get('total_sqft')
        bath=r.POST.get('bath')
        balcony=r.POST.get('balcony')
       # print(area_type,availability,location,size,society,total_sqft,total_sqft,bath,balcony)
        store_data = Get_Data_From_User_Model(username=u, area_type=area_type, availability=availability, location=location, size=size,
                           society=society, total_sqft=total_sqft, bath=bath, balcony=balcony)
        store_data.save()
        return redirect('login_user')
    return render(r,'House_Price_Model/Price_Field.html')





