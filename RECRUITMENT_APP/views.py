from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
# Create your views here.
from django.views.generic import TemplateView

from RECRUITMENT_APP.models import UserType, Company, user


class home_page(TemplateView):
    template_name = 'index.html'

class loginview(TemplateView):
    template_name = 'login.html'
    def post(self,request,*args,**kwargs):
        username=request.POST['username']
        password = request.POST['password']
        users = authenticate(username=username,password=password)
        if users is not None:
            login(request,users)
            if users.last_name == '1':
                if users.is_superuser:
                    return redirect('/admin')
                elif UserType.objects.get(user_id=users.id).type == "user":
                    return redirect('/user')
                elif UserType.objects.get(user_id=users.id).type == "company":
                    return redirect('/company')
                # else:
                #     return redirect('/employee')
            else:
                return render(request,'login.html',{'message':" User Account Not Authenticated"})
        else:
            return render(request,'login.html',{'message':"Invalid Username or Password"})


class ContactView(TemplateView):
    template_name = 'contact.html'

class registration(TemplateView):
    template_name = 'registration.html'

class user_signup(TemplateView):
    template_name = 'users_signup.html'
    def post(self, request,*args,**kwargs):
        fullname = request.POST['name']
        print(fullname)
        phone = request.POST['phone']
        print(phone)
        address = request.POST['Address']
        print(address)
        email = request.POST['email']
        print(email)
        place = request.POST['place']
        print(place)
        location = request.POST['location']
        print(location)
        age = request.POST['age']
        print(age)
        qualification = request.POST['qualification']
        print(qualification)
        image= request.FILES['image']
        F = FileSystemStorage()
        IMAGES = F.save(image.name, image)

        cv_doc= request.FILES['cv_doc']
        G = FileSystemStorage()
        CV = G.save(cv_doc.name, cv_doc)
        print(CV)
        username = request.POST['username']
        print(username)
        password = request.POST['password']
        print(fullname)
        try:
             USERS = User.objects.create_user(username=username,password=password,first_name=fullname,email=email,last_name=0)
             USERS.save()
             users = user()
             users.name=fullname
             users.phone =phone
             users.age =age
             users.qualification = qualification
             users.address =address
             users.location = location
             users.email = email
             users.place =place
             users.photo=IMAGES
             users.cv_doc =CV
             users.status = 'registered'
             users.user_id = USERS.id
             users.qualification = qualification
             users.username = username
             users.password =password
             users.age = age
             usertype = UserType()
             usertype.user = USERS
             usertype.type = "user"
             usertype.save()
             users.save()
             return redirect('login')
        except:
             messages = "Register Successfully"
             return render(request,'registration.html',{'messages':messages})


class company_signup(TemplateView):
    template_name = 'company_signup.html'
    def post(self, request,*args,**kwargs):
        fullname = request.POST['company_name']
        print(fullname)
        phone = request.POST['company_phone']
        print(phone)

        address = request.POST['company_Address']
        print(address)
        email = request.POST['company_email']
        print(email)
        place = request.POST['company_place']
        print(place)
        location = request.POST['company_location']
        print(location)
        image= request.FILES['company_image']
        F = FileSystemStorage()
        IMAGES = F.save(image.name, image)
        print(IMAGES)
        Description = request.POST['company_Description']
        print(Description)
        username = request.POST['username']
        print(username)
        password = request.POST['password']
        print(fullname)
        try:
             user = User.objects.create_user(username=username,password=password,first_name=fullname,email=email,last_name=0)
             user.save()
             comp = Company()
             comp.name=fullname
             comp.phone =phone
             comp.address =address
             comp.description =Description
             comp.location = location
             comp.email = email
             comp.place =place
             comp.photo=IMAGES
             comp.status = 'registered'
             comp.user_id = user.id
             usertype = UserType()
             usertype.user = user
             usertype.type = "company"
             usertype.save()
             comp.save()
             return redirect('login')
        except:
             messages = "Register Successfully"
             return render(request,'registration.html',{'messages':messages})
