from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'home',views.index,name = 'index'),
    url(r'^$',views.signup, name='sign'),
    url(r'^profile/$',views.profile, name='profile'),
    url(r'^search/$',views.search_results, name='search'),


]
