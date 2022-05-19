from django.views.generic import TemplateView

from RECRUITMENT_APP.models import Requirement, Company, category


class IndexView(TemplateView):
    template_name = 'guest/index.html'


class view_companie(TemplateView):
    template_name = 'Guest/view_companies.html'
    def get_context_data(self, **kwargs):
        context = super(view_companie,self).get_context_data(**kwargs)
        company =Company.objects.all()
        context['company']=company
        return context

class view_vacancy_category(TemplateView):
    template_name = 'Guest/view_vacancy_category.html'
    def get_context_data(self, **kwargs):
        context = super(view_vacancy_category,self).get_context_data(**kwargs)
        id =self.request.GET['id']
        Category = category.objects.all()
        context['Category'] =Category
        context['id'] =id
        return context

class user_job_posted_list_search(TemplateView):
    template_name = 'Guest/view_jobpost.html'
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
    template_name = 'Guest/job_details2.html'
    def get_context_data(self, **kwargs):
        context = super(job_details,self).get_context_data(**kwargs)
        id= self.request.GET['id']
        requirement = Requirement.objects.filter(id=id)
        context['requirement'] =requirement
        return context