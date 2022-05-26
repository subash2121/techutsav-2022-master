from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from .models import *
from user.models import *


class DashboardPaymentSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    department = serializers.SerializerMethodField()
    year = serializers.SerializerMethodField()
    college = serializers.SerializerMethodField()
    reg_for = serializers.SerializerMethodField()
    no = serializers.SerializerMethodField()

    var = 0

    class Meta:
        model = Payment
        fields = ('no', 'name', 'department', 'year', 'college', 'ph_number',
                  'email', 'org_dept', 'reg_for', 'base_amount', 'txnid', 'tnxdate')

    def get_name(self, instance):
        try:
            return User.objects.filter(email=instance.email)[0].username
        except:
            return None

    def get_department(self, instance):
        try:
            return Profile.objects.filter(
                user_name=User.objects.get(email=instance.email))[0].department
        except:
            return None

    def get_year(self, instance):
        try:
            return Profile.objects.filter(user_name=User.objects.get(email=instance.email))[0].year
        except:
            return None

    def get_college(self, instance):
        try:
            return Profile.objects.filter(user_name=User.objects.get(email=instance.email))[0].college
        except:
            return None

    def get_reg_for(self, instance):
        if instance.base_amount:
            bal = instance.base_amount
            if instance.event == '300':
                return "Event"
            elif instance.workshop == '300':
                return "Workshop"
            elif bal == '500':
                return "Both Event and Workshop"
            else:
                return None
        else:
            return None

    def get_no(self, instance):
        self.var = self.var+1
        return self.var


class DashboardUserSerializer(serializers.ModelSerializer):
    email = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    txnid = serializers.SerializerMethodField()
    tnxdate = serializers.SerializerMethodField()
    base_amount = serializers.SerializerMethodField()
    reg_for = serializers.SerializerMethodField()
    no = serializers.SerializerMethodField()

    var = 0

    class Meta:
        model = Profile
        fields = ('no', 'name', 'department', 'year', 'college',
                  'phno', 'email', 'status', 'reg_for', 'base_amount', 'txnid', 'tnxdate')

    def get_name(self, instance):
        return User.objects.filter(username=instance.user_name)[0].username

    def get_email(self, instance):
        return User.objects.filter(username=instance.user_name)[0].email

    def get_status(self, instance):
        if Payment.objects.filter(email=User.objects.filter(username=instance.user_name)[0].email).exists():
            # return Payment.objects.filter(email=User.objects.filter(username=instance.user_name)[0].email)[0].org_dept
            return "Paid"
        else:
            return "Not Paid"

    def get_reg_for(self, instance):
        if Payment.objects.filter(email=User.objects.filter(username=instance.user_name)[0].email).exists():
            bal = Payment.objects.filter(
                email=User.objects.filter(username=instance.user_name)[0].email)[0].base_amount
            b=Payment.objects.filter(
                email=User.objects.filter(username=instance.user_name)[0].email)[0]
            if b.event == '300':
                return "Event"
            elif b.workshop == '300':
                return "Workshop"
            elif bal == '500':
                return "Both Event and Workshop"
            else:
                return None
        else:
            return None

    def get_txnid(self, instance):
        if Payment.objects.filter(email=User.objects.filter(username=instance.user_name)[0].email).exists():
            return Payment.objects.filter(email=User.objects.filter(username=instance.user_name)[0].email)[0].txnid
        else:
            return None

    def get_tnxdate(self, instance):
        if Payment.objects.filter(email=User.objects.filter(username=instance.user_name)[0].email).exists():
            return Payment.objects.filter(email=User.objects.filter(username=instance.user_name)[0].email)[0].tnxdate
        else:
            return None

    def get_base_amount(self, instance):
        if Payment.objects.filter(email=User.objects.filter(username=instance.user_name)[0].email).exists():
            return Payment.objects.filter(email=User.objects.filter(username=instance.user_name)[0].email)[0].base_amount
        else:
            return None

    def get_no(self, instance):
        self.var = self.var + 1
        return self.var


class RobotUserSerializer(serializers.ModelSerializer):
    email = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    txnid = serializers.SerializerMethodField()
    tnxdate = serializers.SerializerMethodField()
    base_amount = serializers.SerializerMethodField()
    reg_for = serializers.SerializerMethodField()
    no = serializers.SerializerMethodField()

    var = 0

    class Meta:
        model = TcePay
        fields = ('user_name', 'event_dept', 'event_id', 'date_created',
                  'date_updated', 'name', 'email', 'no', 'status', 'reg_for', 'base_amount', 'txnid', 'tnxdate')

    def get_name(self, instance):
        return User.objects.filter(username=instance.user_name)[0].username

    def get_email(self, instance):
        return User.objects.filter(username=instance.user_name)[0].email

    def get_status(self, instance):
        if Payment.objects.filter(email=User.objects.filter(username=instance.user_name)[0].email).exists():
            # return Payment.objects.filter(email=User.objects.filter(username=instance.user_name)[0].email)[0].org_dept
            return "Paid"
        else:
            return "Not Paid"

    def get_reg_for(self, instance):
        if Payment.objects.filter(email=User.objects.filter(username=instance.user_name)[0].email).exists():
            bal = Payment.objects.filter(
                email=User.objects.filter(username=instance.user_name)[0].email)[0].base_amount
            if bal == '250':
                return "Event"
            elif bal == '300':
                return "Workshop"
            elif bal == '550':
                return "Both Event and Workshop"
            else:
                return None
        else:
            return None

    def get_txnid(self, instance):
        if Payment.objects.filter(email=User.objects.filter(username=instance.user_name)[0].email).exists():
            return Payment.objects.filter(email=User.objects.filter(username=instance.user_name)[0].email)[0].txnid
        else:
            return None

    def get_tnxdate(self, instance):
        if Payment.objects.filter(email=User.objects.filter(username=instance.user_name)[0].email).exists():
            return Payment.objects.filter(email=User.objects.filter(username=instance.user_name)[0].email)[0].tnxdate
        else:
            return None

    def get_base_amount(self, instance):
        if Payment.objects.filter(email=User.objects.filter(username=instance.user_name)[0].email).exists():
            return Payment.objects.filter(email=User.objects.filter(username=instance.user_name)[0].email)[0].base_amount
        else:
            return None

    def get_no(self, instance):
        self.var = self.var + 1
        return self.var


class PaymentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Payment
        fields = ('name','ph_number','email','college','org_dept','txnid','base_amount',)
