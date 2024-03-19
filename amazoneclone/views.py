from django.shortcuts import render
from service.models import Mediaa

def index(request):
    serv_data=Mediaa.objects.all()
    data={'key':serv_data}
    return render(request,"index.html",data)