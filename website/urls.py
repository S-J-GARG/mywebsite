from django.urls import path
from . import views
app_name="website"
urlpatterns=[
path('',views.index,name="index"),
path('contact/',views.contact,name='contact'),
path('blog/',views.blog,name='blog'),

]
