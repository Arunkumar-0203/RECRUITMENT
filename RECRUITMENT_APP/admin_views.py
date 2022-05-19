from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.views.generic import TemplateView, View

from RECRUITMENT_APP.models import user, Company, Requirement, category, Feedback, application, Complaint, district


class IndexView(TemplateView):
    template_name = 'admin/admin_index.html'
#---------------------------------------candidatet----------------------------------------------------------
class view_candidates(TemplateView):
    template_name = 'admin/view_candidates.html'
    def get_context_data(self, **kwargs):
        context = super(view_candidates,self).get_context_data(**kwargs)
        users = user.objects.filter(user__last_name='0',status='registered')
        context['users']=users
        return context

class accepted_candidates(View):
    def dispatch(self, request, *args, **kwargs):
        id =self.request.GET['id']
        USERS = User.objects.get(id=id,last_name='0')
        users=user.objects.get(user_id=id,status='registered')
        users.status='accepted'
        USERS.last_name="1"
        USERS.save()
        users.save()
        return redirect(request.META['HTTP_REFERER'])

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

class rejected_candidates(View):
    def dispatch(self, request, *args, **kwargs):
        id =self.request.GET['id']
        USERS = User.objects.get(id=id,last_name='0')
        users=user.objects.get(user_id=id,status='registered')
        users.status='reject'
        USERS.last_name="0"
        USERS.save()
        users.save()
        return redirect(request.META['HTTP_REFERER'])



class view_accepted_candidates(TemplateView):
    template_name = 'admin/view_accepted_candidates.html'
    def get_context_data(self, **kwargs):
        context = super(view_accepted_candidates,self).get_context_data(**kwargs)
        users = user.objects.filter(user__last_name='1',status='accepted')
        context['users']=users
        return context

class view_rejected_candidates(TemplateView):
    template_name = 'admin/view_rejected_candidates.html'
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

#---------------------------------------companies----------------------------------------------------------
class view_companies(TemplateView):
    template_name = 'admin/view_companies.html'
    def get_context_data(self, **kwargs):
        context = super(view_companies,self).get_context_data(**kwargs)
        company = Company.objects.filter(user__last_name='0',status='registered')
        context['users']=company
        return context

class accepted_companies(View):
    def dispatch(self, request, *args, **kwargs):
        id =self.request.GET['id']
        USERS = User.objects.get(id=id,last_name='0')
        company=Company.objects.get(user_id=id,status='registered')
        company.status='accepted'
        USERS.last_name="1"
        USERS.save()
        company.save()
        return redirect(request.META['HTTP_REFERER'])

class accepted_companies_reject(View):
    def dispatch(self, request, *args, **kwargs):
        id =self.request.GET['id']
        USERS = User.objects.get(id=id,last_name='1')
        company=Company.objects.get(user_id=id,status='accepted')
        company.status='reject'
        USERS.last_name="0"
        USERS.save()
        company.save()
        return redirect(request.META['HTTP_REFERER'])

class rejected_companies(View):
    def dispatch(self, request, *args, **kwargs):
        id =self.request.GET['id']
        USERS = User.objects.get(id=id,last_name='0')
        company=Company.objects.get(user_id=id,status='registered')
        company.status='reject'
        USERS.last_name="0"
        USERS.save()
        company.save()
        return redirect(request.META['HTTP_REFERER'])



class view_accepted_companies(TemplateView):
    template_name = 'admin/view_accepted_campanies.html'
    def get_context_data(self, **kwargs):
        context = super(view_accepted_companies,self).get_context_data(**kwargs)
        company = Company.objects.filter(user__last_name='1',status='accepted')
        context['users']=company
        return context

class view_rejected_companies(TemplateView):
    template_name = 'admin/view_rejected_companies.html'
    def get_context_data(self, **kwargs):
        context = super(view_rejected_companies,self).get_context_data(**kwargs)
        company = Company.objects.filter(user__last_name='0',status='reject')
        context['users']=company
        return context

class rejected_companies_accepted(View):
    def dispatch(self, request, *args, **kwargs):
        id =self.request.GET['id']
        USERS = User.objects.get(id=id,last_name='0')
        company=Company.objects.get(user_id=id,status='reject')
        company.status='accepted'
        USERS.last_name="1"
        USERS.save()
        company.save()
        return redirect(request.META['HTTP_REFERER'])

class add_requirement(TemplateView):
    template_name = 'admin/add_requirement.html'
    def get_context_data(self, **kwargs):
        context = super(add_requirement,self).get_context_data(**kwargs)
        company = Company.objects.filter(user__last_name='1',status='accepted')
        requirement = Requirement.objects.all()
        CATEGORY = category.objects.all()
        context['users']=company
        context['CATEGORY']=CATEGORY
        context['requirement'] =requirement
        return context
    def post(self, request,*args,**kwargs):
        title =request.POST['title']
        qualification =request.POST['qualification']
        experience =request.POST['experience']
        vacancies = request.POST['vacancies']
        comp_id = request.POST['comp_id']
        cate_id = request.POST['cate_id']
        description = request.POST['description']
        requirement = Requirement()
        requirement.company_id = comp_id
        requirement.description = description
        requirement.vacancies = vacancies
        requirement.title = title
        requirement.status = 'active'
        requirement.Categorys_id =cate_id
        requirement.qualification =qualification
        requirement.experience = experience
        requirement.save()
        return redirect(request.META['HTTP_REFERER'])

class delete_requirement(View):
     def dispatch(self, request, *args, **kwargs):
        id =self.request.GET['id']
        Requirement.objects.get(id=id).delete()
        return redirect(request.META['HTTP_REFERER'])

class view_requirement(TemplateView):
    template_name = 'admin/view_requirements.html'
    def get_context_data(self, **kwargs):
        context = super(view_requirement,self).get_context_data(**kwargs)
        company = Company.objects.filter(user__last_name='1',status='accepted')
        requirement = Requirement.objects.all()
        context['users']=company
        context['requirement'] =requirement
        return context

class view_feedback(TemplateView):
    template_name = 'admin/view_feedback.html'
    def get_context_data(self, **kwargs):
        context = super(view_feedback,self).get_context_data(**kwargs)
        FFEDBACK=Feedback.objects.all()
        context['feedback'] =FFEDBACK
        return context
    def post(self,request,*args,**kwargs):
        id=request.POST['id']
        response =request.POST['response']
        FFEDBACK=Feedback.objects.get(id=id)
        FFEDBACK.reply =response
        FFEDBACK.save()
        return redirect(request.META['HTTP_REFERER'])



class delete_feedback(View):
    def dispatch(self, request, *args, **kwargs):
        id =self.request.GET['id']
        Feedback.objects.get(id=id).delete()
        return redirect(request.META['HTTP_REFERER'])


class delete_complaint(View):
    def dispatch(self, request, *args, **kwargs):
        id =self.request.GET['id']
        Complaint.objects.get(id=id).delete()
        return redirect(request.META['HTTP_REFERER'])

class add_category(TemplateView):
    template_name = 'admin/add_category.html'
    def get_context_data(self, **kwargs):
        context = super(add_category,self).get_context_data(**kwargs)
        CATEGORY = category.objects.all()
        context['CATEGORY']=CATEGORY
        return context

    def post(self,request,*args,**kwargs):
        Category =request.POST['category']
        CATEGORY = category()
        CATEGORY.status = 'active'
        CATEGORY.Categorys = Category
        CATEGORY.save()
        return redirect(request.META['HTTP_REFERER'])

class delte_category(View):
    def dispatch(self, request, *args, **kwargs):
        id = self.request.GET['id']
        category.objects.get(id=id).delete()
        return redirect(request.META['HTTP_REFERER'])

class application_satatus_view(TemplateView):
    template_name = 'admin/application_status.html'
    def get_context_data(self, **kwargs):
        context = super(application_satatus_view,self).get_context_data(**kwargs)
        result =application.objects.all()
        context['result'] =result
        return context

class view_complaint(TemplateView):
    template_name = 'admin/view_complaint.html'
    def get_context_data(self, **kwargs):
        context = super(view_complaint,self).get_context_data(**kwargs)
        Complaints=Complaint.objects.all()
        context['feedback'] =Complaints
        return context


class add_state(TemplateView):
    template_name = 'admin/add_state.html'

class add_district(TemplateView):
    template_name = 'admin/add_district.html'
    def get_context_data(self, **kwargs):
        context = super(add_district,self).get_context_data(**kwargs)
        ds=district.objects.all()
        context['district'] =ds
        return context
    def post(self,request,*args,**kwargs):
        dict =request.POST['district']
        d=district()
        d.DISTRICT=dict
        d.save()
        return redirect(request.META['HTTP_REFERER'])


class delte_district(View):
    def dispatch(self, request, *args, **kwargs):
        id = self.request.GET['id']
        district.objects.get(id=id).delete()
        return redirect(request.META['HTTP_REFERER'])
