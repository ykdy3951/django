from django.contrib import admin
from .models import Kuser
# Register your models here.


class KuserAdmin(admin.ModelAdmin):
    list_display = ('email', 'nickname')


admin.site.register(Kuser, KuserAdmin)
