from django.contrib.auth.models import User
from django.db import models

class UserType(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)

class Company(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,null=True)
    phone = models.CharField(max_length=100,null=True)
    email = models.CharField(max_length=100,null=True)
    address = models.CharField(max_length=100,null=True)
    place = models.CharField(max_length=100,null=True)
    location = models.CharField(max_length=100,null=True)
    photo = models.ImageField(upload_to='images/', null=True)
    description = models.CharField(max_length=100,null=True)
    username = models.CharField(max_length=100,null=True)
    password = models.CharField(max_length=100,null=True)
    status = models.CharField(max_length=100,null=True)


class user(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,null=True)
    age = models.CharField(max_length=100,null=True)
    qualification = models.CharField(max_length=100,null=True)
    phone = models.CharField(max_length=100,null=True)
    email = models.CharField(max_length=100,null=True)
    address = models.CharField(max_length=100,null=True)
    place = models.CharField(max_length=100,null=True)
    location = models.CharField(max_length=100,null=True)
    photo = models.ImageField(upload_to='images/', null=True)
    cv_doc = models.ImageField(upload_to='images/', null=True)
    username = models.CharField(max_length=100,null=True)
    password = models.CharField(max_length=100,null=True)
    status = models.CharField(max_length=100,null=True)


class category (models.Model):
    Categorys = models.CharField(max_length=100,null=True)
    status = models.CharField(max_length=100,null=True)


class Requirement(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE,null=True)
    Categorys = models.ForeignKey(category, on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=100,null=True)
    experience = models.CharField(max_length=100,null=True)
    vacancies = models.CharField(max_length=100,null=True)
    qualification = models.CharField(max_length=100,null=True)
    description = models.CharField(max_length=100,null=True)
    status = models.CharField(max_length=100,null=True)

class postJob (models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    requirement = models.ForeignKey(Requirement, on_delete=models.CASCADE)
    status = models.CharField(max_length=100,null=True)

class application(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    requirement = models.ForeignKey(Requirement, on_delete=models.CASCADE,null=True)
    status = models.CharField(max_length=100,null=True,default='null')
    status1 = models.CharField(max_length=100,null=True,default='not approved')
    aptitude =models.CharField(max_length=100,null=True,default='null')
    gd =models.CharField(max_length=100,null=True,default='null')
    one_TO_one =models.CharField(max_length=100,null=True,default='null')
    final_status = models.CharField(max_length=100,null=True,default='null')

class Feedback(models.Model):
    USER = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    feedback =  models.CharField(max_length=100,null=True)

class Aptitude_questions(models.Model):
    form = models.ForeignKey(application, on_delete=models.CASCADE,null=True)
    USER = models.ForeignKey(user, on_delete=models.CASCADE,null=True)
    Question1 =  models.CharField(max_length=400,null=True)
    answer1= models.CharField(max_length=400,null=True)
    Question2 =  models.CharField(max_length=400,null=True)
    answer2= models.CharField(max_length=400,null=True)
    Question3 =  models.CharField(max_length=400,null=True)
    answer3= models.CharField(max_length=400,null=True)
    Question4 =  models.CharField(max_length=400,null=True)
    answer4= models.CharField(max_length=400,null=True)
    Question5 =  models.CharField(max_length=400,null=True)
    answer5= models.CharField(max_length=400,null=True)
    Question6 =  models.CharField(max_length=400,null=True)
    answer6= models.CharField(max_length=400,null=True)
    status = models.CharField(max_length=400,default='test')


class group_discussion(models.Model):
    form = models.ForeignKey(application, on_delete=models.CASCADE,null=True)
    USER = models.ForeignKey(user, on_delete=models.CASCADE,null=True)
    time = models.TimeField(max_length=400,null=True)
    date = models.CharField(max_length=400,null=True)
    link = models.URLField(max_length=400,null=True,default='test')
    status = models.CharField(max_length=400,default='test')

class one_to_one(models.Model):
    form = models.ForeignKey(application, on_delete=models.CASCADE,null=True)
    USER = models.ForeignKey(user, on_delete=models.CASCADE,null=True)
    time = models.TimeField(max_length=400,null=True)
    date = models.CharField(max_length=400,null=True)
    link = models.URLField(max_length=400,null=True,default='test')
    status = models.CharField(max_length=400,default='test')

class offerletter(models.Model):
    form = models.ForeignKey(application, on_delete=models.CASCADE,null=True)
    USER = models.ForeignKey(user, on_delete=models.CASCADE,null=True)
    letter = models.ImageField(upload_to='images/', null=True)
    status = models.CharField(max_length=400,default='test')

