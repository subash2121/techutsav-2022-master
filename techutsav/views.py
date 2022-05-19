from django.shortcuts import render
from .models import *
from backend.settings import MEDIA_URL, BASE_DIR
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
import pyrebase
from datetime import datetime, timedelta
import os
from django.urls import reverse
from django.shortcuts import redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from user.models import *
from django.core import serializers
from .serializers import *
from rest_framework import status, generics
from rest_framework.views import APIView
from django.db.models import Q
from django.core import serializers
from techutsav import models as paymentmodel
from user import models as usermodel
from .forms import *
from django.views.generic import (   
    CreateView,   
)
report_dep = {
    'admin-mech': 'Mechanical',
    'admin-mechatronics': 'Mechtronics',
    'admin-civil': 'Civil',
    'admin-eee': 'EEE',
    'admin-ece': 'ECE',
    'admin-cse': 'CSE',
    'admin-it': 'IT',
    'admin-mca': 'MCA',
    'admin-arch': 'Arch',
}


deptsss_choices = {
    'admin-mech': 'MECH',
    'admin-mechatronics': 'MECHATRONICS',
    'admin-civil': 'CIVIL',
    'admin-eee': 'EEE',
    'admin-ece': 'ECE',
    'admin-cse': 'CSE',
    'admin-it': 'IT',
    'admin-mca': 'MCA',
    'admin-arch': 'ARCH',
}


class DashboardPaymentSerializerList(generics.ListAPIView):
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Payment.objects.all()
        elif self.request.user.is_staff:
            try:
                return Payment.objects.filter(org_dept=report_dep[str(self.request.user)])
            except:
                return Payment.objects.all()
    serializer_class = DashboardPaymentSerializer


class DashboardUserSerializerList(generics.ListAPIView):
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Profile.objects.all()
        elif self.request.user.is_staff:
            try:
                return Profile.objects.filter(department=deptsss_choices[str(self.request.user)])
            except:
                return Profile.objects.all()
    serializer_class = DashboardUserSerializer


class RobotUserSerializerList(generics.ListAPIView):
    def get_queryset(self):
        # if self.request.user.is_superuser:
        #     return TcePay.objects.all()
        if self.request.user.is_superuser:
            try:
                return TcePay.objects.filter(event_dept='robot')
            except:
                return TcePay.objects.all()
    serializer_class = RobotUserSerializer


class PaymentSerializerList(generics.ListAPIView):  
    def get_queryset(self):
        if self.request.user.is_superuser:
            if self.kwargs.get('dept') == 'all':
                return Payment.objects.all()
            return Payment.objects.filter(org_dept=self.kwargs.get('dept'))
    serializer_class = PaymentSerializer


def userfn(request, val):
    if request.user.is_superuser:
        return HttpResponse(User.objects.all().values(val))


config = {
  "apiKey": "AIzaSyBt2fK7VkCCH9ypPqPnYeB0x4D9oFxeE5g",
  "authDomain": "techutsav-2022.firebaseapp.com",
  "databaseURL": "https://techutsav-2022-default-rtdb.firebaseio.com",
  "projectId": "techutsav-2022",
  "storageBucket": "techutsav-2022.appspot.com",
  "messagingSenderId": "23846651386",
  "appId": "1:23846651386:web:586d3f5bd6eaabba671043",
  "measurementId": "G-9FX65618NZ"
}


firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

# Create your views here.
get_dep = {
    'mech': 'DEPARTMENT OF MECHANICAL ENGINEERING',
    'mechatronics': 'DEPARTMENT OF MECHATRONICS',
    'civil': 'DEPARTMENT OF CIVIL ENGINEERING',
    'eee': 'DEPARTMENT OF ELECTRICAL AND ELECTRONICS ENGINEERING',
    'ece': 'DEPARTMENT OF ELECTRONICS AND COMMUNICATION ENGINEERING',
    'cse': 'DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING',
    'it': 'DEPARTMENT OF INFORMATION TECHNOLOGY',
    'mca': 'MASTER OF COMPUTER APPLICATION and DATA SCIENCE',
    'arch': 'DEPARTMENT OF ARCHITECTURE',
    'robot': 'ROBOTICS CLUB',
    'test': 'DEPARTMENT OF TEST ENGINEERING',
}

db_dep = {
    'mech': ME,
    'mechatronics': MA,
    'civil': CIVIL,
    'eee': EEE,
    'ece': ECE,
    'cse': CSE,
    'it': IT,
    'mca': MCA,
    'arch': ARCH,
    'test': TEST,
    'robot': ROBOT,
}


def index(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            try:
                if Payment.objects.filter(Q(ph_number=Profile.objects.filter(user_name=request.user)[0].phno) | Q(email=request.user.email)).exists():
                    return render(request, 'techutsav/index.html', {'has_to_pay': False})
                else:
                    return render(request, 'techutsav/index.html', {'has_to_pay': True})
            except:
                return render(request, 'techutsav/index.html', {'has_to_pay': False})
        else:
            return render(request, 'techutsav/index.html', {'has_to_pay': False})


def register(request):
    if request.method == 'GET':
        return render(request, 'techutsav/register.html', {})


def backup(request, bk_key):
    if bk_key == "sql" and request.user.is_superuser:
        ti = datetime.now() + timedelta(hours=5, minutes=30)
        x = "db_" + ti.strftime("%m_%d_%Y_%H_%M_%S")+".sqlite3o"
        storage.child(x).put(os.path.join(BASE_DIR, 'db.sqlite3o'))
        return HttpResponse(x)
        # data = serializers.serialize("json", usermodel.Profile.objects.all())
        # # print(data)
        # out = open("users.json", "w")
        # out.write(data)
        # out.close()
        # inp=open("users.json", "r")
        # x = "db_user_" + ti.strftime("%m_%d_%Y_%H_%M_%S")+".json"
        # storage.child(x).put(inp)
        # payment=serializers.serialize("json", paymentmodel.Payment.objects.all())
        # out = open("payment.json", "w")
        # out.write(payment)
        # out.close()
        # inp=open("payment.json", "r")
        # x = "db_payment_" + ti.strftime("%m_%d_%Y_%H_%M_%S")+".json"
        # storage.child(x).put(inp)
        # return HttpResponse("hi")


def dept(request, dept):
    if request.method == 'GET':
        data = db_dep[dept].objects.all()
        event = db_dep[dept].objects.filter(type_of_event='Events')
        workshop = db_dep[dept].objects.filter(type_of_event='Workshops')
        if(workshop.count() > 0):
            iswork = True
        else:
            iswork = False
        return render(request, 'techutsav/dept.html', {'full': get_dep[dept], 'isworksop': iswork, 'short': dept, 'data': data, 'events': event, 'workshops': workshop, 'MEDIA_URL': MEDIA_URL})

def workshop(request):
    if request.method == 'GET':
        data = Workshop.objects.all()
        print(data)

        return render(request, 'techutsav/workshop.html', {'workshops': data, 'short': 'cse', 'MEDIA_URL': MEDIA_URL,'data':data})

class project(CreateView):
    model = Project
    template_name = 'techutsav/project.html'
    fields = ['project_name','no_of_participants','phone_number','teammates','abstract']
    success_url = '/'
    def form_valid(self, form):
        return super().form_valid(form)

def department(request):
    if request.method == 'GET':
        return render(request, 'techutsav/department.html', {})


@login_required
def payment(request, pk, dept):
    if request.method == 'POST':

        TcePay.objects.create(user_name=request.user,
                              event_dept=dept, event_id=pk,)
        if dept == 'robot':
            return redirect(reverse('index'))
        else:
            return HttpResponseRedirect('https://eazypay.icicibank.com/homePage')
    else:
        return render(request, 'techutsav/instruction.html', {'MEDIA_URL': MEDIA_URL})


@login_required
def payments(request):
    if request.method == 'POST':
        TcePay.objects.create(user_name=request.user,
                              event_dept='direct', event_id='direct',)
        return HttpResponseRedirect('https://eazypay.icicibank.com/homePage')
    else:
        return render(request, 'techutsav/instruction.html', {'MEDIA_URL': MEDIA_URL})


def error_404(request, exception):
    return render(request, 'techutsav/error.html', {'MEDIA_URL': MEDIA_URL}, status=404)


def error_500(request):
    return render(request, 'techutsav/error.html', {'MEDIA_URL': MEDIA_URL}, status=500)


@login_required
def addNewReport(request):
    if request.method == 'POST' and request.FILES['myfile'] and request.user.is_superuser:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        # print(os.path.join(os.path.join(BASE_DIR, 'media'), filename))
        f = open(os.path.join(os.path.join(BASE_DIR, 'media'), filename))
        f.readline()
        data = f.readlines()
        for x in data:
            temp = x.strip().split('|')
            Payment.objects.create(
                icid=temp[0],
                name=temp[1],
                ph_number=temp[2],
                email=temp[3],
                roll=temp[4],
                college=temp[5],
                dept=temp[6],
                org_dept=temp[7],
                event=temp[8],
                workshop=temp[9],
                both=temp[10],
                txnid=temp[11],
                tnxdate=temp[12],
                mode_of_payment=temp[13],
                status=temp[14],
                base_amount=temp[15],
                process_fee=temp[16],
                recon_date=temp[17],
                settle_date=temp[18],
                txn_amt=temp[19],
                txn_initated_on=temp[20],
                late_fee=temp[21],
                early_fee=temp[22],
                cgst=temp[23],
                sgst=temp[24],
                igst=temp[25],
                jkgst=temp[26],
                utgst=temp[27],
                ctcess=temp[28],
                stcess=temp[29],
                payer_processing_fee=temp[30],
                payer_cgst=temp[31],
                payer_sgst=temp[32],
                payer_igst=temp[33],
                payer_jkgst=temp[34],
                payer_utgst=temp[35],
                payer_ctcess=temp[36],
                payer_stcess=temp[37],
            )
            # print(temp)
        return redirect(reverse('index'))
    return render(request, 'techutsav/upload.html')


def report(request, type_report):
    if request.method == 'GET' and request.user.is_staff:
        if (type_report == 'chart'):
            if str(request.user) == 'admin-dean' or request.user.is_superuser:
                res = [['Department', 'Events', 'Workshop', 'both'], ]
                for x in ['Mechanical', 'Mechtronics', 'Civil', 'EEE', 'ECE', 'CSE', 'IT', 'MCA', 'Arch']:
                    data = [x, ]
                    for y in ['300', '550']:
                        data.append(Payment.objects.filter(
                            org_dept=x, base_amount=y).count())
                    res.append(data)
                # print(res)
                return render(request, 'techutsav/chart.html', {'data': res})
        elif type_report == 'payment':
            return render(request, 'techutsav/report.html', {'url': '/dashboard/payment/', "data1": "ph_number", "data2": "org_dept", "report": "Paid User"})
        elif type_report == 'user':
            return render(request, 'techutsav/report.html', {'url': '/dashboard/user/', 'data1': "phno", 'data2': "status", "report": "Registred User"})


@login_required
def payments(request):
    if request.method == 'POST':
        TcePay.objects.create(user_name=request.user,
                              event_dept='direct', event_id='direct',)
        return HttpResponseRedirect('https://eazypay.icicibank.com/homePage')
    else:
        return render(request, 'techutsav/instruction.html', {'MEDIA_URL': MEDIA_URL})
