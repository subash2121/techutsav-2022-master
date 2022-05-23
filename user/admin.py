from django.contrib import admin
from .models import Profile
from import_export import resources
from import_export.admin import ImportExportModelAdmin
class Profiles(ImportExportModelAdmin):
    list_display = ('user_name','department','rollno','college','phno','year')

admin.site.register(Profile,Profiles)


