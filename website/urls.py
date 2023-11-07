from django.urls import path
from . import views
from django.conf import settings  
from django.conf.urls.static import static
app_name="website"
urlpatterns=[
path('',views.index,name="index"),
path('contact/',views.contact,name='contact'),
path('blog/',views.blog,name='blog'),

path('aboutme/',views.aboutme,name='aboutme'),

]
  