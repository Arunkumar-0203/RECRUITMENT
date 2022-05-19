from django.urls import path


from RECRUITMENT_APP.user_views import IndexView, profile, view_companies, view_vacancy_category,user_job_posted_list_search, \
    job_details, application_apply, application_status, aptitude_test, view_question, group_discussions, \
      view_onetoone_link, result_view, offer_latter_view, feedback, delete_feedback, comp_complaint, delete_complaint

urlpatterns = [

      path('',IndexView.as_view()),
      path('profile',profile.as_view()),
      path('view_companies',view_companies.as_view()),
      path('view_vacancy_category',view_vacancy_category.as_view()),
      path('user_job_posted_list_search',user_job_posted_list_search.as_view()),
      path('job_details',job_details.as_view()),
      path('application_apply',application_apply.as_view()),
      path('application_status',application_status.as_view()),
      path('aptitude_test',aptitude_test.as_view()),
      path('view_question',view_question.as_view()),
      path('group_discussion',group_discussions.as_view()),
      path('view_onetoone_link',view_onetoone_link.as_view()),
      path('result',result_view.as_view()),
      path('offer_latter_view',offer_latter_view.as_view()),
      path('USER_feedback',feedback.as_view()),
      path('delete_feedback',delete_feedback.as_view()),
      path('comp_complaint',comp_complaint.as_view()),
      path('delete_complaint',delete_complaint.as_view()),





      ]
def urls():
      return urlpatterns,'user', 'user'