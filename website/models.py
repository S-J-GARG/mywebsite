from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
  name=models.CharField(max_length=200,default="", editable=False)
  tag_line=models.CharField(max_length=200,default="", editable=False)
  currently_work_as=models.CharField(max_length=100,default="", editable=False)
   
  mob_number=models.IntegerField(default=0) 
  email_id=models.CharField(max_length=100,default="", editable=False)
  home_address=models.CharField(max_length=200,default="", editable=False)
  work_address=models.CharField(max_length=200,default="", editable=False)
  def __str__(self):
    return self.name

class Testimonials(models.Model):
  Clinet_name=models.CharField(max_length=100)
  comment=models.CharField(max_length=300)
  stasified_with_work=models.TextField(max_length=100)
  def __str__(self):
    return self.Clinet_name
  

class Work(models.Model):
  comp_name=models.CharField(max_length=100)
  work_date=models.DateTimeField("Join date")
  for_position=models.CharField(max_length=100)
  def __str__(self):
    return self.comp_name

class Skills(models.Model):
  skills=models.ForeignKey(User,on_delete=models.CASCADE)
  my_skills=models.CharField(max_length=100)
  level=models.IntegerField(default=70)
  def __str__(self):
    return self.my_skills
  
  class EducationCertificate(models.Model):
    degree=models.CharField(max_length=100)
    insititute=models.CharField(max_length=100)
    year_date=models.DateTimeField("Year")
    def __str__(self):
     return self.degree
  
  class portfolio(models.Model):
        project_name=models.CharField(max_length=100)
        about_project=models.CharField(max_length=250)
        def __str__(self):
          return self.project_name
        
  class Blog(models.Model):
    article_name=models.CharField(max_length=200,default="", editable=False)
    pub_date=models.DateTimeField("Publish date")
    description=models.TextField(max_length=1000)
    def __str__(self):
     return self.article_name
class contact(models.Model):
  cont_name=models.CharField(max_length=200,default="", editable=False)
  cont_email=models.CharField(max_length=200,default="", editable=False)
  query=models.CharField(max_length=500)
  def __str__(self):
     return self.cont_name

    