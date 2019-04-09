from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import *
from django.shortcuts import render,redirect
from django.http  import HttpResponse
import datetime as dt
from .models import Profile,Comments,Image


# Create your views here.

def index(request):
    return render(request,'index.html', locals())
