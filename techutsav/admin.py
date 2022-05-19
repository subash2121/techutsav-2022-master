from django.contrib import admin
from .models import *


class DateView(admin.ModelAdmin):
    readonly_fields = ('date_created', 'date_updated', )


admin.site.register(Department, DateView)
admin.site.register(ME, DateView)
admin.site.register(MA, DateView)
admin.site.register(CIVIL, DateView)
admin.site.register(EEE, DateView)
admin.site.register(ECE, DateView)
admin.site.register(CSE, DateView)
admin.site.register(IT, DateView)
admin.site.register(MCA, DateView)
admin.site.register(ARCH, DateView)
admin.site.register(ROBOT, DateView)
admin.site.register(TEST, DateView)
admin.site.register(TcePay, DateView)
admin.site.register(Payment, DateView)
admin.site.register(Workshop, DateView)
admin.site.register(Project)



