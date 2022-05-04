from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.core.mail import EmailMessage
from django.conf import settings
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from RECRUITMENT_APP.models import Requirement, postJob, Company, category, Feedback, user, application, \
    Aptitude_questions, group_discussion, one_to_one, offerletter


class IndexView(TemplateView):
    template_name = 'company/company_index.html'

class view_requirement(TemplateView):
    template_name = 'company/view_requirement.html'
    def get_context_data(self, **kwargs):
        context = super(view_requirement,self).get_context_data(**kwargs)
        user =Company.objects.get(user_id=self.request.user.id)
        requirement = Requirement.objects.filter(company_id=user.id)
        context['requirement'] =requirement
        return context

class post_jobs(TemplateView):
    template_name = 'company/view_requirement.html'
    def dispatch(self, request, *args, **kwargs):
        id =self.request.GET['id']
        company = Company.objects.get(user_id=self.request.user.id)
        try:
            if postJob.objects.get(requirement_id=id,company_id=company.id):
                return render(request,'company/view_requirement.html',{'messages':'already job posted'})
            else:
                PostJob = postJob()
                PostJob.status='job posted'
                PostJob.requirement_id=id
                PostJob.company_id=company.id
                PostJob.save()
                return render(request,'company/view_requirement.html',{'messages':'job posted successfully'})
        except:
                PostJob = postJob()
                PostJob.status='job posted'
                PostJob.requirement_id=id
                PostJob.company_id=company.id
                PostJob.save()
                return render(request,'company/view_requirement.html',{'messages':'job posted successfully'})

class job_posted_list(TemplateView):
    template_name = 'company/job_posted_list.html'
    def get_context_data(self, **kwargs):
        context = super(job_posted_list,self).get_context_data(**kwargs)

        Category = category.objects.all()
        context['Category'] =Category
        return context


class job_posted_list_search(TemplateView):
    template_name = 'company/view_jobpost.html'
    def get_context_data(self, **kwargs):
        context = super(job_posted_list_search,self).get_context_data(**kwargs)
        id =self.request.GET['categ_id']
        requirement = Requirement.objects.filter(Categorys_id=id)
        if Requirement.objects.filter(Categorys_id=id):
            context['requirement'] =requirement
            return context
        else:
            context['messages'] ='No job post'
            return context

class feedback(TemplateView):
    template_name = 'company/feedback.html'
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

class view_candidate(TemplateView):
    template_name = 'company/view_candidates.html'

class view_candidates(TemplateView):
    template_name = 'company/view_candidates.html'
    def get_context_data(self, **kwargs):
        context = super(view_candidates,self).get_context_data(**kwargs)
        users = user.objects.filter(user__last_name='1',status='accepted')
        context['users']=users
        return context

class accepted_candidates_reject(View):
    def dispatch(self, request, *args, **kwargs):
        id =self.request.GET['id']
        USERS = User.objects.get(id=id,last_name='1')
        users=user.objects.get(user_id=id,status='accepted')
        users.status='reject'
        USERS.last_name="0"
        USERS.save()
        users.save()
        return redirect(request.META['HTTP_REFERER'])

class view_rejected_candidates(TemplateView):
    template_name = 'company/view_rejected_candidates.html'
    def get_context_data(self, **kwargs):
        context = super(view_rejected_candidates,self).get_context_data(**kwargs)
        users = user.objects.filter(user__last_name='0',status='reject')
        context['users']=users
        return context

class rejected_candidates_accepted(View):
    def dispatch(self, request, *args, **kwargs):
        id =self.request.GET['id']
        USERS = User.objects.get(id=id,last_name='0')
        users=user.objects.get(user_id=id,status='reject')
        users.status='accepted'
        USERS.last_name="1"
        USERS.save()
        users.save()
        return redirect(request.META['HTTP_REFERER'])

class application_status(TemplateView):
    template_name = 'company/application_status.html'
    def get_context_data(self, **kwargs):
        context = super(application_status,self).get_context_data(**kwargs)
        Companyid =Company.objects.get(user_id=self.request.user.id)
        Requirements =Requirement.objects.get(company_id=Companyid.id)
        result =application.objects.filter(requirement_id=Requirements.id )
        context['result'] =result
        return context

class applicationlist(TemplateView):
    template_name = 'company/applicationlist.html'
    def get_context_data(self, **kwargs):
        context = super(applicationlist,self).get_context_data(**kwargs)
        Companyid =Company.objects.get(user_id=self.request.user.id)
        Requirements =Requirement.objects.get(company_id=Companyid.id)
        result =application.objects.filter(requirement_id=Requirements.id,status='apply')
        context['result'] =result
        return context


class approveapplication(View):
    def dispatch(self, request, *args, **kwargs):
        id =self.request.GET['id']
        result =application.objects.get(id=id )
        result.status='application accepted'
        result.status1 = 'approved'
        result.save()
        return redirect(request.META['HTTP_REFERER'])

class aptitude(TemplateView):
    template_name = 'company/aptitude.html'
    def get_context_data(self, **kwargs):
        context = super(aptitude,self).get_context_data(**kwargs)
        Companyid =Company.objects.get(user_id=self.request.user.id)
        Requirements =Requirement.objects.get(company_id=Companyid.id)
        result =application.objects.filter(requirement_id=Requirements.id,status1='approved')
        context['result'] =result
        return context

class give_questions(TemplateView):
    template_name = 'company/give_questions.html'
    def get_context_data(self, **kwargs):
        context = super(give_questions,self).get_context_data(**kwargs)
        id =self.request.GET['id']
        Companyid =Company.objects.get(user_id=self.request.user.id)
        Requirements =Requirement.objects.get(company_id=Companyid.id)
        result =application.objects.get(requirement_id=Requirements.id,id=id)
        Question =Aptitude_questions.objects.filter(form_id=result.id)
        context['result'] =Question
        return context
    def post(self , request,*args,**kwargs):
        id =self.request.GET['id']
        Companyid =Company.objects.get(user_id=self.request.user.id)
        Requirements =Requirement.objects.get(company_id=Companyid.id)
        result =application.objects.get(requirement_id=Requirements.id,id=id)
        Question1=request.POST['question1']
        print(Question1)
        Question2=request.POST['question2']
        print(Question2)
        Question3=request.POST['question3']
        print(Question3)
        Question4=request.POST['question4']
        print(Question4)
        Question5=request.POST['question5']
        print(Question5)
        Question6 = request.POST['question6']
        print(Question6)

        Question =Aptitude_questions()
        Questions =Aptitude_questions.objects.filter(status='test',form_id=id)
        if Aptitude_questions.objects.filter(status='test',form_id=id):
            for i in Questions:
                if i.USER_id==result.user_id:
                    return render(request,'company/give_questions.html',{'messages':'already question added'})
                else:
                    Question.Question1 = Question1
                    Question.Question2 = Question2
                    Question.Question3 = Question3
                    Question.Question4 = Question4
                    Question.Question5 = Question5
                    Question.Question6 = Question6
                    Question.form_id=id
                    Question.USER_id=result.user_id
                    Question.save()
                    return redirect(request.META['HTTP_REFERER'])
        else:
            Question.Question1 = Question1
            Question.Question2 = Question2
            Question.Question3 = Question3
            Question.Question4 = Question4
            Question.Question5 = Question5
            Question.Question6 = Question6
            Question.form_id=id
            Question.USER_id=result.user_id
            Question.save()
            return redirect(request.META['HTTP_REFERER'])


class aptitude_pass(View):
    def dispatch(self, request, *args, **kwargs):
        id =self.request.GET['id']
        result =application.objects.get(id=id )
        result.status='aptitude pass'
        result.save()
        return redirect(request.META['HTTP_REFERER'])

class aptitude_notpass(View):
    def dispatch(self, request, *args, **kwargs):
        id =self.request.GET['id']
        result =application.objects.get(id=id )
        result.status='aptitude failed'
        result.save()
        return redirect(request.META['HTTP_REFERER'])

class group_dicussion(TemplateView):
    template_name = 'company/group_discussion.html'
    def get_context_data(self, **kwargs):
        context = super(group_dicussion,self).get_context_data(**kwargs)
        Companyid =Company.objects.get(user_id=self.request.user.id)
        Requirements =Requirement.objects.get(company_id=Companyid.id)
        result =application.objects.filter(requirement_id=Requirements.id,status='aptitude pass')
        context['result'] =result
        return context

class providelink(TemplateView):
    template_name = 'company/provide_link.html'
    def get_context_data(self, **kwargs):
        context = super(providelink,self).get_context_data(**kwargs)
        Companyid =Company.objects.get(user_id=self.request.user.id)
        Requirements =Requirement.objects.get(company_id=Companyid.id)
        result =application.objects.filter(requirement_id=Requirements.id,status='aptitude pass')
        GD = group_discussion.objects.filter(form_id__requirement_id__company_id__user_id=self.request.user.id)
        context['result'] =GD
        return context
    def post(self , request,*args,**kwargs):
        Companyid =Company.objects.get(user_id=self.request.user.id)
        Requirements =Requirement.objects.get(company_id=Companyid.id)
        result =application.objects.filter(requirement_id=Requirements.id)
        for i in result:
            print(1)
            if group_discussion.objects.filter(form_id=i.id,status='link added'):
                continue
            else:
                time= request.POST['time']
                date= request.POST['time']
                link = request.POST['link']
                gd = group_discussion()
                gd.form_id=i.id
                gd.USER_id=i.user_id
                gd.date=date
                gd.time =time
                gd.link = link
                gd.status ="link added"
                gd.save()
                print(2)
                print(i.user.user.email,'aaaaaaaaaaaaaaaaaaaaaaa')
                email = EmailMessage(
                'join GD using this link',
                link,
                settings.EMAIL_HOST_USER,
                [i.user.user.email],
                 )
                email.fail_silently = False
                email.send()
                return redirect(request.META['HTTP_REFERER'])


class GD_pass(View):
    def dispatch(self, request, *args, **kwargs):
        id =self.request.GET['id']
        result =application.objects.get(id=id )
        result.gd='gd pass'
        result.save()
        return redirect(request.META['HTTP_REFERER'])

class GD_notpass(View):
    def dispatch(self, request, *args, **kwargs):
        id =self.request.GET['id']
        result =application.objects.get(id=id )
        result.gd='gd failed'
        result.save()
        return redirect(request.META['HTTP_REFERER'])

class onetoone(TemplateView):
    template_name = 'company/OneToOne.html'
    def get_context_data(self, **kwargs):
        context = super(onetoone,self).get_context_data(**kwargs)
        Companyid =Company.objects.get(user_id=self.request.user.id)
        Requirements =Requirement.objects.get(company_id=Companyid.id)
        result =application.objects.filter(requirement_id=Requirements.id,gd='gd pass')
        print(result,"1234567890")
        context['result'] =result
        return context

class onetoone_link(TemplateView):
    template_name = 'company/give_oneto_link.html'
    def get_context_data(self, **kwargs):
        context = super(onetoone_link,self).get_context_data(**kwargs)
        Companyid =Company.objects.get(user_id=self.request.user.id)
        Requirements =Requirement.objects.get(company_id=Companyid.id)
        result =application.objects.filter(requirement_id=Requirements.id,status='aptitude pass')
        one_to = one_to_one.objects.filter(form_id__requirement_id__company_id__user_id=self.request.user.id)
        context['result'] =one_to
        return context
    def post(self , request,*args,**kwargs):
        Companyid =Company.objects.get(user_id=self.request.user.id)
        Requirements =Requirement.objects.get(company_id=Companyid.id)
        result =application.objects.filter(requirement_id=Requirements.id)
        for i in result:
            print(1)
            if one_to_one.objects.filter(form_id=i.id,status='link added'):
                continue
            else:
                time= request.POST['time']
                date= request.POST['time']
                link = request.POST['link']
                gd = one_to_one()
                gd.form_id=i.id
                gd.USER_id=i.user_id
                gd.date=date
                gd.time =time
                gd.link = link
                gd.status ="link added"
                gd.save()
                email = EmailMessage(
                'join GD using this link',
                link,
                settings.EMAIL_HOST_USER,
                [i.user.user.email],
                 )
                email.fail_silently = False
                email.send()
                return redirect(request.META['HTTP_REFERER'])

class onetoone_pass(View):
    def dispatch(self, request, *args, **kwargs):
        id =self.request.GET['id']
        result =application.objects.get(id=id )
        result.one_TO_one='pass'
        result.save()
        return redirect(request.META['HTTP_REFERER'])

class onetoone_notpass(View):
    def dispatch(self, request, *args, **kwargs):
        id =self.request.GET['id']
        result =application.objects.get(id=id )
        result.one_TO_one='failed'
        result.save()
        return redirect(request.META['HTTP_REFERER'])

class send_offer_latter(TemplateView):
    template_name = 'company/send_offer_letter.html'
    def get_context_data(self, **kwargs):
        context = super(send_offer_latter,self).get_context_data(**kwargs)
        Companyid =Company.objects.get(user_id=self.request.user.id)
        Requirements =Requirement.objects.get(company_id=Companyid.id)
        result =application.objects.filter(requirement_id=Requirements.id,one_TO_one='pass')
        context['result'] =result
        return context
    def post(self,request,*args,**kwargs):

        id=request.POST['id']
        letters = request.FILES['latter']
        print(letters,"1234567890")
        F = FileSystemStorage()
        LETTER = F.save(letters.name, letters)
        result =application.objects.get(id=id)
        result.final_status = 'send offer letter'
        result.save()
        offer_letter =offerletter()
        offer_letter.form_id=id
        offer_letter.letter = LETTER
        offer_letter.USER_id=result.user_id
        offer_letter.status = 'send offer letter'
        offer_letter.save()
        return redirect(request.META['HTTP_REFERER'])


class send_offer_latter_list(TemplateView):
     template_name = 'company/send_offer_letter_list.html'
     def get_context_data(self, **kwargs):
        context = super(send_offer_latter_list,self).get_context_data(**kwargs)
        # Companyid =Company.objects.get(user_id=self.request.user.id)
        # Requirements =Requirement.objects.get(company_id=Companyid.id)
        # result =application.objects.filter(requirement_id=Requirements.id,one_TO_one='pass')
        result = offerletter.objects.filter(form__requirement__company__user_id=self.request.user.id)
        context['result'] =result
        return context
