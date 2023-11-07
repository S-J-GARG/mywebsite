from django.contrib import admin
from .models import User,Testimonials,Work,Skills,ContactForm,myBlog,EducationCertificate,Portfolio,MyImages
from ckeditor.widgets import CKEditorWidget

#Todo Register your models here.
# admin.site.register(User)
# admin.site.register(Skills)
#!You can customize the admin page to make it more user-friendly. You can create an admin CLASS for each model to define the display columns and filter options, among other things

class skillsInline(admin.StackedInline):
   model=Skills
   extra=2


class TestimonialsInline(admin.StackedInline):
   model=Testimonials
   extra=2


class WorkInline(admin.StackedInline):
   model=Work
   extra=2

class EductionkInline(admin.StackedInline):
   model=EducationCertificate
   extra=2

class PortfolioInline(admin.StackedInline):
   model=Portfolio
   extra=2
class blogInline(admin.ModelAdmin):
    list_display = ['blog_title', 'pub_date']
    list_filter = ['pub_date']
    search_fields = ['blog_title', 'content']
    formfield_overrides = {
        myBlog.content: {'widget': CKEditorWidget()},
    }
class MyImagesInLine(admin.ModelAdmin):
   model=MyImages
   extra=4
   list_display=['image_name','image_pic']


class userInline(admin.ModelAdmin):
   list_display=['name'] #display should of  User model not Skill model
   inlines=[skillsInline,TestimonialsInline,WorkInline,PortfolioInline]
admin.site.register(ContactForm)
admin.site.register(MyImages,MyImagesInLine)
admin.site.register(myBlog,blogInline)
admin.site.register(User,userInline)
