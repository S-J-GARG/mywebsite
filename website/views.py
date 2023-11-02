from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User,Testimonials,Work,Skills,ContactForm,myBlog,EducationCertificate,Portfolio
from .forms import ContactUsform
# Create your views here.
def index(request):
# Replace this with your specific query, such as filtering or retrieving all users
    users = User.objects.all()  # Example: Retrieve all User objects
# Get the IDs of the User objects in the QuerySet
    user_ids = [user.id for user in users]
    my_id=user_ids[0] # Retrieving number from list
    my_data=User.objects.get(pk=my_id) #Since I am the only user
    context={
        'my':my_data
    }
    return render(request, 'website/index.html', context)
def contact(request):
    if request.method == 'POST':
        form = ContactUsform(request.POST)
        if form.is_valid():
            form.save()
            # You can add code here to send an email, show a thank you page, etc.
            return redirect('thank_you_page')

    else:
        form = ContactUsform()

    return render(request, 'website/contactus.html', {'form': form})
