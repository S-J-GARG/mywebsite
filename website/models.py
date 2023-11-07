from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField


# Create your models here.
class User(models.Model):
  name=models.CharField(max_length=200,default="")
  tag_line=models.CharField(max_length=200,default="")
  currently_work_as=models.CharField(max_length=100,default="")
  mob_number=models.IntegerField(default=0) 
  email_id=models.EmailField()
  home_address=models.CharField(max_length=200,default="")
  work_address=models.CharField(max_length=200,default="")
  def __str__(self):
    return self.name
  def as_dict(self):
        # Return all fields as a dictionary
        return vars(self)
class MyImages(models.Model):
     image_name=models.CharField(max_length=100)
     image_pic=models.ImageField(upload_to='myimage',default='Logo')
     def __str__(self):
      return self.image_name
  
class Testimonials(models.Model):
  testmo=models.ForeignKey(User,on_delete=models.CASCADE,default='Testmonials')
  Clinet_name=models.CharField(max_length=100)
  comment=models.CharField(max_length=300)
  stasified_with_work=models.TextField(max_length=100)
  def __str__(self):
    return self.Clinet_name
  def as_dict(self):
        # Return all fields as a dictionary
        return vars(self)
  
class Work(models.Model):
  work=models.ForeignKey(User,on_delete=models.CASCADE,default='Work')

  comp_name=models.CharField(max_length=100)
  work_date=models.DateTimeField("Join date")
  for_position=models.CharField(max_length=100)
  def __str__(self):
    return self.comp_name
  def as_dict(self):
        # Return all fields as a dictionary
        return vars(self)
  
class Skills(models.Model):
  skills=models.ForeignKey(User,on_delete=models.CASCADE)
  my_skills=models.CharField(max_length=100,default="")
  level=models.IntegerField(default=70)
  def __str__(self):
    return self.my_skills
  def as_dict(self):
        # Return all fields as a dictionary
        return vars(self)
  
class EducationCertificate(models.Model):
    Education=models.ForeignKey(User,on_delete=models.CASCADE,default='Education')
    
    degree=models.CharField(max_length=100)
    insititute=models.CharField(max_length=100)
    year_date=models.DateTimeField("Year")
    def __str__(self):
     return self.degree
    def as_dict(self):
        # Return all fields as a dictionary
        return vars(self)
  
class Portfolio(models.Model):
        portfolio=models.ForeignKey(User,on_delete=models.CASCADE,default='Portfolio')
        project_name=models.CharField(max_length=100)
        about_project=models.CharField(max_length=350)
        def __str__(self):
          return self.project_name
        def as_dict(self):
        # Return all fields as a dictionary
         return vars(self)
class myBlog(models.Model):
    blog=models.ForeignKey(User,on_delete=models.CASCADE,default='0')
    article_name=models.CharField(max_length=200,default="")
    blog_title=models.CharField(max_length=200,default='')
    content = RichTextField(null=True)
    pub_date=models.DateTimeField(auto_now_add=True)
    description=models.TextField(max_length=5000)
    def __str__(self):
     return self.article_name
    def as_dict(self):
        # Return all fields as a dictionary
        return vars(self)

class ContactForm(models.Model):
  # contact_com=models.ForeignKey(User,on_delete=models.CASCADE,default=0)
  Name=models.CharField(max_length=100,default='Ram',null=True)
  Email=models.CharField(max_length=100,default='Ram',null=True)
  Message=models.CharField(max_length=500)
  def __str__(self):
     return self.Name
  def as_dict(self):
        # Return all fields as a dictionary
        return vars(self)

    