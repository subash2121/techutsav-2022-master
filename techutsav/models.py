from django.db import models
from django.contrib.auth.models import User

event_choices = (
    ('Events', 'Events'),
    ('Workshops', 'Workshops'),
)

dept_choices = (
    ('mech', 'mech'),
    ('mechatronics', 'mechatronics'),
    ('civil', 'civil'),
    ('eee', 'eee'),
    ('ece', 'ece'),
    ('cse', 'cse'),
    ('it', 'it'),
    ('mca', 'mca'),
    ('arch', 'arch'),
)

class Project(models.Model):
    pid = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=60, null=True, blank=True)
    no_of_participants = models.CharField(
        max_length=60, null=True, blank=True, default="Max 3")
    phone_number = models.CharField(max_length=100, null=True, blank=True)
    teammates = models.TextField(null=True, blank=True)
    abstract = models.TextField(null=True, blank=True)

    date_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.project_name)

class Workshop(models.Model):
    eid=models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=60, null=True, blank=True)
    is_prize=models.BooleanField(default=True)
    event_more = models.CharField(max_length=60, null=True, blank=True)
    event_max_participants = models.CharField(
        max_length=60, null=True, blank=True, default="Not Mentioned")
    event_extra = models.TextField(null=True, blank=True)
    event_rules = models.TextField(null=True, blank=True)

    event_phno = models.CharField(max_length=100, null=True, blank=True)
    event_venue = models.CharField(
        max_length=100, null=True, blank=True, default="Soon")
    event_timing = models.CharField(
        max_length=100, null=True, blank=True, default="Soon")

    thumbnail_front = models.URLField(blank=True, null=True)
    thumbnail_back = models.FileField(
        upload_to='workshops/', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.event_name)
class Department(models.Model):
    eid = models.AutoField(primary_key=True)
    type_of_event = models.CharField(
        max_length=30, choices=event_choices, null=True, blank=True)
    event_name = models.CharField(max_length=60, null=True, blank=True)
    is_prize=models.BooleanField(default=True)
    event_more = models.CharField(max_length=60, null=True, blank=True)
    event_max_participants = models.CharField(
        max_length=60, null=True, blank=True, default="Not Mentioned")
    event_extra = models.TextField(null=True, blank=True)
    event_rules = models.TextField(null=True, blank=True)
    event_phno = models.CharField(max_length=100, null=True, blank=True)
    event_venue = models.CharField(
        max_length=100, null=True, blank=True, default="Soon")
    event_timing = models.CharField(
        max_length=100, null=True, blank=True, default="Soon")

    thumbnail_front =models.URLField(blank=True, null=True)
    thumbnail_back = models.FileField(
        upload_to='events/', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.event_name)


class CSE(models.Model):
    eid = models.AutoField(primary_key=True)
    type_of_event = models.CharField(
        max_length=30, choices=event_choices, null=True, blank=True)
    event_name = models.CharField(max_length=60, null=True, blank=True)
    is_prize=models.BooleanField(default=True)
    event_more = models.CharField(max_length=60, null=True, blank=True)
    event_max_participants = models.CharField(
        max_length=60, null=True, blank=True, default="Not Mentioned")
    event_extra = models.TextField(null=True, blank=True)
    event_rules = models.TextField(null=True, blank=True)

    event_phno = models.CharField(max_length=100, null=True, blank=True)
    event_venue = models.CharField(
        max_length=100, null=True, blank=True, default="Soon")
    event_timing = models.CharField(
        max_length=100, null=True, blank=True, default="Soon")

    thumbnail_front =models.URLField(blank=True, null=True)
    thumbnail_back = models.FileField(
        upload_to='events/', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.event_name)


class CIVIL(models.Model):
    eid = models.AutoField(primary_key=True)
    type_of_event = models.CharField(
        max_length=30, choices=event_choices, null=True, blank=True)
    event_name = models.CharField(max_length=60, null=True, blank=True)
    is_prize=models.BooleanField(default=True)
    event_more = models.CharField(max_length=60, null=True, blank=True)
    event_max_participants = models.CharField(
        max_length=60, null=True, blank=True, default="Not Mentioned")
    event_extra = models.TextField(null=True, blank=True)
    event_rules = models.TextField(null=True, blank=True)

    event_phno = models.CharField(max_length=100, null=True, blank=True)
    event_venue = models.CharField(
        max_length=100, null=True, blank=True, default="Soon")
    event_timing = models.CharField(
        max_length=100, null=True, blank=True, default="Soon")

    thumbnail_front =models.URLField(blank=True, null=True)
    thumbnail_back = models.FileField(
        upload_to='events/', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.event_name)


class IT(models.Model):
    eid = models.AutoField(primary_key=True)
    type_of_event = models.CharField(
        max_length=30, choices=event_choices, null=True, blank=True)
    event_name = models.CharField(max_length=60, null=True, blank=True)
    is_prize=models.BooleanField(default=True)
    event_more = models.CharField(max_length=60, null=True, blank=True)
    event_max_participants = models.CharField(
        max_length=60, null=True, blank=True, default="Not Mentioned")
    event_extra = models.TextField(null=True, blank=True)
    event_rules = models.TextField(null=True, blank=True)

    event_phno = models.CharField(max_length=100, null=True, blank=True)
    event_venue = models.CharField(
        max_length=100, null=True, blank=True, default="Soon")
    event_timing = models.CharField(
        max_length=100, null=True, blank=True, default="Soon")

    thumbnail_front =models.URLField(blank=True, null=True)
    thumbnail_back = models.FileField(
        upload_to='events/', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.event_name)


class ECE(models.Model):
    eid = models.AutoField(primary_key=True)
    type_of_event = models.CharField(
        max_length=30, choices=event_choices, null=True, blank=True)
    event_name = models.CharField(max_length=60, null=True, blank=True)
    is_prize=models.BooleanField(default=True)
    event_more = models.CharField(max_length=60, null=True, blank=True)
    event_max_participants = models.CharField(
        max_length=60, null=True, blank=True, default="Not Mentioned")
    event_extra = models.TextField(null=True, blank=True)
    event_rules = models.TextField(null=True, blank=True)

    event_phno = models.CharField(max_length=100, null=True, blank=True)
    event_venue = models.CharField(
        max_length=100, null=True, blank=True, default="Soon")
    event_timing = models.CharField(
        max_length=100, null=True, blank=True, default="Soon")

    thumbnail_front =models.URLField(blank=True, null=True)
    thumbnail_back = models.FileField(
        upload_to='events/', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.event_name)


class EEE(models.Model):
    eid = models.AutoField(primary_key=True)
    type_of_event = models.CharField(
        max_length=30, choices=event_choices, null=True, blank=True)
    event_name = models.CharField(max_length=60, null=True, blank=True)
    is_prize=models.BooleanField(default=True)
    event_more = models.CharField(max_length=60, null=True, blank=True)
    event_max_participants = models.CharField(
        max_length=60, null=True, blank=True, default="Not Mentioned")
    event_extra = models.TextField(null=True, blank=True)
    event_rules = models.TextField(null=True, blank=True)

    event_phno = models.CharField(max_length=100, null=True, blank=True)
    event_venue = models.CharField(
        max_length=100, null=True, blank=True, default="Soon")
    event_timing = models.CharField(
        max_length=100, null=True, blank=True, default="Soon")

    thumbnail_front =models.URLField(blank=True, null=True)
    thumbnail_back = models.FileField(
        upload_to='events/', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.event_name)


class ME(models.Model):
    eid = models.AutoField(primary_key=True)
    type_of_event = models.CharField(
        max_length=30, choices=event_choices, null=True, blank=True)
    event_name = models.CharField(max_length=60, null=True, blank=True)
    is_prize=models.BooleanField(default=True)
    event_more = models.CharField(max_length=60, null=True, blank=True)
    event_max_participants = models.CharField(
        max_length=60, null=True, blank=True, default="Not Mentioned")
    event_extra = models.TextField(null=True, blank=True)
    event_rules = models.TextField(null=True, blank=True)

    event_phno = models.CharField(max_length=100, null=True, blank=True)
    event_venue = models.CharField(
        max_length=100, null=True, blank=True, default="Soon")
    event_timing = models.CharField(
        max_length=100, null=True, blank=True, default="Soon")

    thumbnail_front =models.URLField(blank=True, null=True)
    thumbnail_back = models.FileField(
        upload_to='events/', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.event_name)


class MA(models.Model):
    eid = models.AutoField(primary_key=True)
    type_of_event = models.CharField(
        max_length=30, choices=event_choices, null=True, blank=True)
    event_name = models.CharField(max_length=60, null=True, blank=True)
    is_prize=models.BooleanField(default=True)
    event_more = models.CharField(max_length=60, null=True, blank=True)
    event_max_participants = models.CharField(
        max_length=60, null=True, blank=True, default="Not Mentioned")
    event_extra = models.TextField(null=True, blank=True)
    event_rules = models.TextField(null=True, blank=True)

    event_phno = models.CharField(max_length=100, null=True, blank=True)
    event_venue = models.CharField(
        max_length=100, null=True, blank=True, default="Soon")
    event_timing = models.CharField(
        max_length=100, null=True, blank=True, default="Soon")

    thumbnail_front =models.URLField(blank=True, null=True)
    thumbnail_back = models.FileField(
        upload_to='events/', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.event_name)


class ARCH(models.Model):
    eid = models.AutoField(primary_key=True)
    type_of_event = models.CharField(
        max_length=30, choices=event_choices, null=True, blank=True)
    event_name = models.CharField(max_length=60, null=True, blank=True)
    is_prize=models.BooleanField(default=True)
    event_more = models.CharField(max_length=60, null=True, blank=True)
    event_max_participants = models.CharField(
        max_length=60, null=True, blank=True, default="Not Mentioned")
    event_extra = models.TextField(null=True, blank=True)
    event_rules = models.TextField(null=True, blank=True)

    event_phno = models.CharField(max_length=100, null=True, blank=True)
    event_venue = models.CharField(
        max_length=100, null=True, blank=True, default="Soon")
    event_timing = models.CharField(
        max_length=100, null=True, blank=True, default="Soon")

    thumbnail_front =models.URLField(blank=True, null=True)
    thumbnail_back = models.FileField(
        upload_to='events/', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.event_name)


class MCA(models.Model):
    eid = models.AutoField(primary_key=True)
    type_of_event = models.CharField(
        max_length=30, choices=event_choices, null=True, blank=True)
    event_name = models.CharField(max_length=60, null=True, blank=True)
    is_prize=models.BooleanField(default=True)
    event_more = models.CharField(max_length=60, null=True, blank=True)
    event_max_participants = models.CharField(
        max_length=60, null=True, blank=True, default="Not Mentioned")
    event_extra = models.TextField(null=True, blank=True)
    event_rules = models.TextField(null=True, blank=True)

    event_phno = models.CharField(max_length=100, null=True, blank=True)
    event_venue = models.CharField(
        max_length=100, null=True, blank=True, default="Soon")
    event_timing = models.CharField(
        max_length=100, null=True, blank=True, default="Soon")

    thumbnail_front =models.URLField(blank=True, null=True)
    thumbnail_back = models.FileField(
        upload_to='events/', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.event_name)


class TEST(models.Model):
    eid = models.AutoField(primary_key=True)
    type_of_event = models.CharField(
        max_length=30, choices=event_choices, null=True, blank=True)
    event_name = models.CharField(max_length=60, null=True, blank=True)
    is_prize=models.BooleanField(default=True)
    event_more = models.CharField(max_length=60, null=True, blank=True)
    event_max_participants = models.CharField(
        max_length=60, null=True, blank=True, default="Not Mentioned")
    event_extra = models.TextField(null=True, blank=True)
    event_rules = models.TextField(null=True, blank=True)

    event_phno = models.CharField(max_length=100, null=True, blank=True)
    event_venue = models.CharField(
        max_length=100, null=True, blank=True, default="Soon")
    event_timing = models.CharField(
        max_length=100, null=True, blank=True, default="Soon")

    thumbnail_front =models.URLField(blank=True, null=True)
    thumbnail_back = models.FileField(
        upload_to='events/', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.event_name)


class ROBOT(models.Model):
    eid = models.AutoField(primary_key=True)
    type_of_event = models.CharField(
        max_length=30, choices=event_choices, null=True, blank=True)
    event_name = models.CharField(max_length=60, null=True, blank=True)
    is_prize=models.BooleanField(default=True)
    event_more = models.CharField(max_length=60, null=True, blank=True)
    event_max_participants = models.CharField(
        max_length=60, null=True, blank=True, default="Not Mentioned")
    event_extra = models.TextField(null=True, blank=True)
    event_rules = models.TextField(null=True, blank=True)

    event_phno = models.CharField(max_length=100, null=True, blank=True)
    event_venue = models.CharField(
        max_length=100, null=True, blank=True, default="Soon")
    event_timing = models.CharField(
        max_length=100, null=True, blank=True, default="Soon")

    thumbnail_front =models.URLField(blank=True, null=True)
    thumbnail_back = models.FileField(
        upload_to='events/', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.event_name)


class TcePay(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    event_dept = models.CharField(max_length=50, null=True, blank=True)
    event_id = models.CharField(max_length=10, null=True, blank=True)
    date_created = models.DateTimeField(editable=True, auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


class Payment(models.Model):
    icid = models.CharField(max_length=250, null=True, blank=True)
    name = models.CharField(max_length=250, null=True, blank=True)
    ph_number = models.CharField(max_length=250, null=True, blank=True)
    email = models.CharField(max_length=250, null=True, blank=True)
    roll = models.CharField(max_length=250, null=True, blank=True)
    college = models.CharField(max_length=250, null=True, blank=True)
    dept = models.CharField(max_length=250, null=True, blank=True)
    org_dept = models.CharField(max_length=250, null=True, blank=True)
    reg_fee = models.CharField(max_length=250, null=True, blank=True)
    event = models.CharField(max_length=250, null=True, blank=True)
    workshop = models.CharField(max_length=250, null=True, blank=True)
    both = models.CharField(max_length=250, null=True, blank=True)
    txnid = models.CharField(max_length=250, null=True, blank=True)
    tnxdate = models.CharField(max_length=250, null=True, blank=True)
    mode_of_payment = models.CharField(max_length=250, null=True, blank=True)
    status = models.CharField(max_length=250, null=True, blank=True)
    base_amount = models.CharField(max_length=250, null=True, blank=True)
    process_fee = models.CharField(max_length=250, null=True, blank=True)
    recon_date = models.CharField(max_length=250, null=True, blank=True)
    settle_date = models.CharField(max_length=250, null=True, blank=True)
    txn_amt = models.CharField(max_length=250, null=True, blank=True)
    txn_initated_on = models.CharField(max_length=250, null=True, blank=True)
    late_fee = models.CharField(max_length=250, null=True, blank=True)
    early_fee = models.CharField(max_length=250, null=True, blank=True)
    cgst = models.CharField(max_length=250, null=True, blank=True)
    sgst = models.CharField(max_length=250, null=True, blank=True)
    igst = models.CharField(max_length=250, null=True, blank=True)
    jkgst = models.CharField(max_length=250, null=True, blank=True)
    utgst = models.CharField(max_length=250, null=True, blank=True)
    ctcess = models.CharField(max_length=250, null=True, blank=True)
    stcess = models.CharField(max_length=250, null=True, blank=True)
    payer_processing_fee = models.CharField(
        max_length=250, null=True, blank=True)
    payer_cgst = models.CharField(max_length=250, null=True, blank=True)
    payer_sgst = models.CharField(max_length=250, null=True, blank=True)
    payer_igst = models.CharField(max_length=250, null=True, blank=True)
    payer_jkgst = models.CharField(max_length=250, null=True, blank=True)
    payer_utgst = models.CharField(max_length=250, null=True, blank=True)
    payer_ctcess = models.CharField(max_length=250, null=True, blank=True)
    payer_stcess = models.CharField(max_length=250, null=True, blank=True)
    date_created = models.DateTimeField(editable=True, auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.org_dept + "-"+ self.ph_number + "-"+ self.email+"-"+self.base_amount
