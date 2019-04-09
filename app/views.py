from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import *
from django.shortcuts import render,redirect
from django.http  import HttpResponse
import datetime as dt
from .models import Profile,Comments,Image


# Create your views here.

def index(request):
    if request.method == 'POST':
        form = UploadForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form =UploadForm()
    query_img = Image.objects.all()

    return render(request,'index.html', locals())
