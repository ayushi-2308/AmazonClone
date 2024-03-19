from django.contrib import admin
from service.models import Mediaa

# Register your models here.
@admin.register(Mediaa)
class Use(admin.ModelAdmin):
    list_display=('obj1','obj2')