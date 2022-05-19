from django.urls import path

from RECRUITMENT_APP.admin_views import IndexView, view_candidates, view_accepted_candidates, view_rejected_candidates, \
   accepted_candidates, rejected_candidates, accepted_candidates_reject, rejected_candidates_accepted, view_companies, \
   view_accepted_companies, view_rejected_companies, accepted_companies, rejected_companies, accepted_companies_reject, \
    rejected_companies_accepted, add_requirement, delete_requirement, view_requirement, view_feedback, add_category, \
    delte_category, delete_feedback, application_satatus_view, view_complaint, add_state, add_district, delete_complaint, \
   delte_district

urlpatterns =[
   path('',IndexView.as_view()),
   path('view_candidates',view_candidates.as_view()),
   path('view_accepted_candidates',view_accepted_candidates.as_view()),
   path('view_rejected_candidates',view_rejected_candidates.as_view()),
   path('accepted_candidates',accepted_candidates.as_view()),
   path('rejected_candidates',rejected_candidates.as_view()),
   path('accepted_candidates_reject',accepted_candidates_reject.as_view()),
   path('rejected_candidates_accepted',rejected_candidates_accepted.as_view()),


   path('view_companies',view_companies.as_view()),
   path('view_accepted_companies',view_accepted_companies.as_view()),
   path('view_rejected_companies',view_rejected_companies.as_view()),
   path('accepted_companies',accepted_companies.as_view()),
   path('rejected_companies',rejected_companies.as_view()),
   path('accepted_companies_reject',accepted_companies_reject.as_view()),
   path('rejected_companies_accepted',rejected_companies_accepted.as_view()),
   path('IndexView',IndexView.as_view()),
   path('delete_requirement',delete_requirement.as_view()),
   path('add_requirement',add_requirement.as_view()),
   path('view_requirement',view_requirement.as_view()),
   path('view_feedback',view_feedback.as_view()),

   path('add_category',add_category.as_view()),
   path('delte_category',delte_category.as_view()),

   path('delete_feedback',delete_feedback.as_view()),
   path('application_satatus_view',application_satatus_view.as_view()),


   path('view_complaint',view_complaint.as_view()),


   path('add_district',add_district.as_view()),
   path('add_state',add_state.as_view()),

   path('delete_complaint',delete_complaint.as_view()),
   path('delte_district',delte_district.as_view())


]
def urls():
      return urlpatterns,'admin', 'admin'