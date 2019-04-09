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

def signup(request):
    return redirect('/accounts/login/')
    return render(request, 'registration_form.html')


def profile(request):
    prof = Profile.objects.all()
    return render(request,'profile.html', locals())

def search_results(request):

    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Profile.search_by_profile_name(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"searched_articles": searched_articles})

    else:
        message = "please enter a name"
        return render(request, 'search.html',{"message":message})
