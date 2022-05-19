from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
# Create your views here.
from django.views.generic import TemplateView

from RECRUITMENT_APP.models import UserType, Company, user, Requirement, category, guest, district


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
                else:
                    return redirect('/Guest')
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
    def get_context_data(self, **kwargs):
        context = super(user_signup,self).get_context_data(**kwargs)
        ds=district.objects.all()
        context['district'] =ds
        return context

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


class guest_signup(TemplateView):
    template_name = 'guest_signup.html'
    def get_context_data(self, **kwargs):
        context = super(guest_signup,self).get_context_data(**kwargs)
        ds=district.objects.all()
        context['district'] =ds
        return context
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
        username = request.POST['username']
        print(username)
        password = request.POST['password']
        print(fullname)
        try:
             USERS = User.objects.create_user(username=username,password=password,first_name=fullname,email=email,last_name=1)
             USERS.save()
             users = guest()
             users.name=fullname
             users.phone =phone
             users.address =address
             users.location = location
             users.email = email
             users.place =place
             users.status = 'registered'
             users.user_id = USERS.id
             users.username = username
             users.password =password
             usertype = UserType()
             usertype.user = USERS
             usertype.type = "Guest"
             usertype.save()
             users.save()
             return redirect('login')
        except:
             messages = "Register Successfully"
             return render(request,'registration.html',{'messages':messages})




class company_signup(TemplateView):
    template_name = 'company_signup.html'
    def get_context_data(self, **kwargs):
        context = super(company_signup,self).get_context_data(**kwargs)
        ds=district.objects.all()
        context['district'] =ds
        return context
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

class view_jobs(TemplateView):
    template_name = 'view_jobpost.html'
    def get_context_data(self, **kwargs):
        context = super(view_jobs,self).get_context_data(**kwargs)
        id =self.request.GET['categ_id']
        requirement = Requirement.objects.filter(Categorys_id=id)
        if Requirement.objects.filter(Categorys_id=id):
            context['requirement'] =requirement
            return context
        else:
            context['messages'] ='No job post'
            return context

class view_company(TemplateView):
    template_name = 'view_companies.html'
    def get_context_data(self, **kwargs):
        context = super(view_company,self).get_context_data(**kwargs)
        company =Company.objects.all()
        context['company']=company
        return context


class view_vacancy_category(TemplateView):
    template_name = 'view_vacancy_category.html'
    def get_context_data(self, **kwargs):
        context = super(view_vacancy_category,self).get_context_data(**kwargs)
        id =self.request.GET['id']
        Category = category.objects.all()
        context['Category'] =Category
        context['id'] =id
        return context

class user_job_posted_list_search(TemplateView):
    template_name = 'view_jobpost.html'
    def get_context_data(self, **kwargs):
        context = super(user_job_posted_list_search,self).get_context_data(**kwargs)
        id =self.request.GET['categ_id']
        s_id=self.request.GET['id']
        comp_id = Company.objects.get(id=s_id)
        try:
            if Requirement.objects.get(Categorys_id=id,company_id=comp_id):
                requirement = Requirement.objects.filter(Categorys_id=id,company_id=comp_id)
                context['requirement'] =requirement
                return context
            else:
                context['messages'] ='No job post'
                return context
        except:
             context['messages'] ='No job post'
             return context

class job_details(TemplateView):
    template_name = 'job_details2.html'
    def get_context_data(self, **kwargs):
        context = super(job_details,self).get_context_data(**kwargs)
        id= self.request.GET['id']
        requirement = Requirement.objects.filter(id=id)
        context['requirement'] =requirement
        return context

class about(TemplateView):
    template_name = 'about.html'