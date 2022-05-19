from cmath import log
from distutils.log import Log
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import *
from .models import *
from techutsav.models import Payment
from django.db.models import Q
from cryptography.fernet import Fernet
import base64
import logging
import traceback
from django.conf import settings


def encrypt(pas):
    try:        
        pas = str(pas)
        cipher_pass = Fernet(settings.ENCRYPT_KEY)
        encrypt_pass = cipher_pass.encrypt(pas.encode('ascii'))
        encrypt_pass = base64.urlsafe_b64encode(encrypt_pass).decode("ascii") 
        return encrypt_pass
    except Exception as e:
        logging.getLogger("error_logger").error(traceback.format_exc())
        return None


def decrypt(pas):
    try:
        pas = base64.urlsafe_b64decode(pas)
        cipher_pass = Fernet(settings.ENCRYPT_KEY)
        decod_pass = cipher_pass.decrypt(pas).decode("ascii")     
        return decod_pass
    except Exception as e:
        logging.getLogger("error_logger").error(traceback.format_exc())
        return None


def register(request):
    form = UserRegisterForm()
    p_form = ProfileUpdateForm()
    if request.method == 'POST':
        data = request.POST.copy()
        dep = request.POST.copy()
        del data['rollno']
        del data['department']
        del data['year']
        del data['college']
        del data['phno']
        #print(data)
        form = UserRegisterForm(data)
        if form.is_valid():
            m = form.save()
            #print("yes")
            Profile.objects.create(
                user_name=m, department=dep['department'], rollno=dep['rollno'],  year=dep['year'], college=dep['college'], phno=dep['phno'])
            #print("yes")
            messages.success(
                request, f'Your account has been created! You are now able to log in')
            #print(request.POST)
            return redirect('login')
    return render(request, 'users/register.html', {'form': form, 'p_form': p_form, 'title': 'Register'})


@login_required
def profile(request):
    if request.method == 'GET':
        extra = Profile.objects.filter(user_name = request.user)
        payment =  Payment.objects.filter(Q(email = request.user.email)|  Q(ph_number = extra[0].phno ))
        # print(Fernet.generate_key())
        # try:
        #     payment = payment
        # except:
        #     payment = None
        #print(dir(extra))
        #print(len(extra))
        #print(encrypt(request.user.email))
        
        return render(request, 'users/profile.html', {'extra': extra,'payment':payment,'qr':encrypt(request.user.email)})

@login_required
def verify(request):
    if request.method == 'POST':
        decryptedval=decrypt(request.POST['qr'])
        print(decryptedval)
        extra = Profile.objects.filter(user_name = User.objects.filter(email=decryptedval).first()).first()
        payment =  Payment.objects.filter(Q(email = decryptedval)|  Q(ph_number = extra.phno ))
        curr=Profile.objects.filter(user_name = request.user).first()
        # print(extra.user_name.username)
        # print(extra.phno)
        if extra:
            if payment:
                if extra.recievedkit==True:
                    return render(request, 'users/result.html', {'extra': extra,'payment':payment,'status':False})
                else:
                    
                    print(extra.recievedkit)
                    extra.recievedkit=True
                    extra.save()
                    return render(request, 'users/result.html', {'extra': extra,'payment':payment,'status':True})

                
                
                
            else:
                #print("Payment not done yet")
                return render(request, 'users/result.html', {'extra': extra,'payment':payment,'status':'Payment Not Done'})

            

    if request.user.groups.filter(name='verification commitee') or request.user.is_superuser or request.user.is_staff:
        return render(request, 'users/verify.html', {})


    else:
        return render(request, 'techutsav/error.html', {})
