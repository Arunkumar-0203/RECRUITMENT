from django.urls import path

from RECRUITMENT_APP.company_views import IndexView, view_requirement, post_jobs, job_posted_list, \
    job_posted_list_search, feedback, delete_feedback, view_candidate, view_candidates, accepted_candidates_reject, \
    view_rejected_candidates, rejected_candidates_accepted, application_status, applicationlist, approveapplication, \
    aptitude, give_questions, aptitude_notpass, aptitude_pass, group_dicussion, providelink, GD_pass, GD_notpass, \
    onetoone, onetoone_link, onetoone_pass, onetoone_notpass, send_offer_latter, send_offer_latter_list, comp_complaint, \
    delete_complaint

urlpatterns = [
       path('',IndexView.as_view()),
       path('view_requirement',view_requirement.as_view()),
       path('post_jobs',post_jobs.as_view()),
       path('job_posted_list',job_posted_list.as_view()),
       path('job_posted_list_search',job_posted_list_search.as_view()),
       path('comp_feedback',feedback.as_view()),
       path('comp_complaint',comp_complaint.as_view()),
       path('delete_complaint',delete_complaint.as_view()),
       path('delete_feedback',delete_feedback.as_view()),
       path('view_candidate',view_candidate.as_view()),
       path('view_candidates',view_candidates.as_view()),
       path('accepted_candidates_reject',accepted_candidates_reject.as_view()),
       path('view_rejected_candidates',view_rejected_candidates.as_view()),
       path('rejected_candidates_accepted',rejected_candidates_accepted.as_view()),
       path('application_status',application_status.as_view()),
       path('applicationlist',applicationlist.as_view()),
       path('approveapplication',approveapplication.as_view()),
       path('aptitude',aptitude.as_view()),
       path('give_questions',give_questions.as_view()),
       path('aptitude_notpass',aptitude_notpass.as_view()),
       path('aptitude_pass',aptitude_pass.as_view()),
       path('group_discussion',group_dicussion.as_view()),
       path ('providelink',providelink.as_view()),
       path('GD_pass',GD_pass.as_view()),
       path('GD_notpass',GD_notpass.as_view()),
       path('onetoone',onetoone.as_view()),
       path('onetoone_link',onetoone_link.as_view()),
       path('onetoone_pass',onetoone_pass.as_view()),
       path('onetoone_notpass',onetoone_notpass.as_view()),
       path('send_offer_latter',send_offer_latter.as_view()),
       path('send_offer_latter_list',send_offer_latter_list.as_view()),


]
def urls():
      return urlpatterns,'company', 'company'
