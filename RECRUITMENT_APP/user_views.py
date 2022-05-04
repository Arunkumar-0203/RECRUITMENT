from django.shortcuts import redirect, render
from django.views.generic import TemplateView, View

from RECRUITMENT_APP.models import user, Company, category, Requirement, application, Aptitude_questions, \
    group_discussion, one_to_one, offerletter, Feedback


class IndexView(TemplateView):
    template_name = 'user/user_index.html'

class profile(TemplateView):
    template_name = 'user/profile.html'
    def get_context_data(self, **kwargs):
        context = super(profile,self).get_context_data(**kwargs)
        id = self.request.user.id
        USERS =user.objects.get(user_id=id)
        context['USERS']=USERS
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
        try:
             users = user.objects.get(user_id=self.request.user.id)
             users.name=fullname
             users.phone =phone
             users.age =age
             users.qualification = qualification
             users.address =address
             users.location = location
             users.email = email
             users.place =place
             users.qualification = qualification
             users.save()
             return redirect('login')
        except:
             return redirect(request.META['HTTP_REFERER'])

class view_companies(TemplateView):
    template_name = 'user/view_companies.html'
    def get_context_data(self, **kwargs):
        context = super(view_companies,self).get_context_data(**kwargs)
        company =Company.objects.all()
        context['company']=company
        return context

class view_vacancy_category(TemplateView):
    template_name = 'user/view_vacancy_category.html'
    def get_context_data(self, **kwargs):
        context = super(view_vacancy_category,self).get_context_data(**kwargs)
        Category = category.objects.all()
        context['Category'] =Category
        return context

class user_job_posted_list_search(TemplateView):
    template_name = 'user/view_jobpost.html'
    def get_context_data(self, **kwargs):
        context = super(user_job_posted_list_search,self).get_context_data(**kwargs)
        id =self.request.GET['categ_id']
        requirement = Requirement.objects.filter(Categorys_id=id)
        if Requirement.objects.filter(Categorys_id=id):
            context['requirement'] =requirement
            return context
        else:
            context['messages'] ='No job post'
            return context

class job_details(TemplateView):
    template_name = 'user/job_details.html'
    def get_context_data(self, **kwargs):
        context = super(job_details,self).get_context_data(**kwargs)
        id= self.request.GET['id']
        requirement = Requirement.objects.filter(id=id)
        context['requirement'] =requirement
        return context

class application_apply(TemplateView):
    template_name = 'user/application_status.html'
    def dispatch(self, request, *args, **kwargs):
        id= self.request.GET['id']
        USER = user.objects.get(user_id= self.request.user.id)
        try:
            if application.objects.filter(user_id=USER.id):
                result =application.objects.all()
                return render(request,'user/application_status.html',{'messages':'already job apply successfully','result':result})
            else:
                us_id =self.request.user.id
                USER =user.objects.get(user_id=us_id)
                Application =application()
                Application.requirement_id=id
                Application.user_id=USER.id
                Application.status = 'apply'
                Application.save()
                result =application.objects.all()
                return render(request,'user/application_status.html',{'messages':'job apply successfully','result':result})

        except:
                us_id =self.request.user.id
                USER =user.objects.get(user_id=us_id)
                Application =application()
                Application.requirement_id=id
                Application.user_id=USER.id
                Application.status = 'apply'
                Application.save()
                result =application.objects.all()
                return render(request,'user/application_status.html',{'messages':'job apply successfully','result':result})


class application_status(TemplateView):
    template_name = 'user/application_status.html'
    def get_context_data(self, **kwargs):
        context = super(application_status,self).get_context_data(**kwargs)
        USER=user.objects.get(user_id =self.request.user.id)
        result =application.objects.filter(user_id=USER.id)
        context['result'] =result
        return context

class aptitude_test(TemplateView):
    template_name = 'user/aptitude.html'
    def get_context_data(self, **kwargs):
        context = super(aptitude_test,self).get_context_data(**kwargs)
        try:
            USER =user.objects.get(user_id=self.request.user.id)
            result =application.objects.get(user_id=USER.id,status1='approved')
            context['result'] =result
            return context
        except:

            context['messages'] ='application not accepted'
            return context


class view_question(TemplateView):
    template_name = 'user/view_questions.html'
    def get_context_data(self, **kwargs):
        context = super(view_question,self).get_context_data(**kwargs)
        request_id = self.request.GET['id']
        USER =user.objects.get(user_id=self.request.user.id)
        Question =Aptitude_questions.objects.get(form_id=request_id,USER_id=USER.id)
        context['result'] =Question
        return context
    def post(self,request,*args,**kwargs):
        answer1 =request.POST['Answer1']
        answer2 =request.POST['Answer2']
        answer3 =request.POST['Answer3']
        answer4 =request.POST['Answer4']
        answer5 =request.POST['Answer5']
        answer6 =request.POST['Answer6']
        request_id = request.POST['applicat_id']
        USER =user.objects.get(user_id=self.request.user.id)
        Question =Aptitude_questions.objects.get(id=request_id,USER_id=USER.id)
        Question.answer1 = answer1
        Question.answer2 = answer2
        Question.answer3 = answer3
        Question.answer4 = answer4
        Question.answer5 = answer5
        Question.answer6 = answer6
        Question.save()
        return redirect(request.META['HTTP_REFERER'])

class group_discussions(TemplateView):
    template_name = 'user/group_discussion.html'
    def get_context_data(self, **kwargs):
        context = super(group_discussions,self).get_context_data(**kwargs)
        GD = group_discussion.objects.filter(form_id__user_id__user_id__id=self.request.user.id)
        context['result'] =GD
        return context

class view_onetoone_link(TemplateView):
    template_name = 'user/OneToOne.html'
    def get_context_data(self, **kwargs):
        context = super(view_onetoone_link,self).get_context_data(**kwargs)
        GD = one_to_one.objects.filter(form_id__user_id__user_id__id=self.request.user.id)
        context['result'] =GD
        return context

class result_view(TemplateView):
    template_name = 'user/result.html'
    def get_context_data(self, **kwargs):
        context = super(result_view,self).get_context_data(**kwargs)
        USER=user.objects.get(user_id =self.request.user.id)
        result =application.objects.filter(user_id=USER.id)
        context['result'] =result
        return context

class offer_latter_view(TemplateView):
    template_name = 'user/offer_letter_view.html'
    def get_context_data(self, **kwargs):
        context = super(offer_latter_view,self).get_context_data(**kwargs)
        result = offerletter.objects.filter(USER__user_id=self.request.user.id)
        context['result'] =result
        return context

class feedback(TemplateView):
    template_name = 'user/feedback.html'
    def get_context_data(self, **kwargs):
        context = super(feedback,self).get_context_data(**kwargs)
        FFEDBACK=Feedback.objects.filter(USER_id=self.request.user.id)
        context['feedback'] =FFEDBACK
        return context
    def post(self, request,*args,**kwargs):
        FEEDBACK=request.POST['feedback']
        feedback_db = Feedback()
        feedback_db.USER_id=self.request.user.id
        feedback_db.feedback = FEEDBACK
        feedback_db.save()
        return redirect(request.META['HTTP_REFERER'])

class delete_feedback(View):
    def dispatch(self, request, *args, **kwargs):
        id =self.request.GET['id']
        Feedback.objects.get(id=id).delete()
        return redirect(request.META['HTTP_REFERER'])
