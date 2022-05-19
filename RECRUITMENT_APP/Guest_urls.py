from django.urls import path

from RECRUITMENT_APP.Guest_views import IndexView, view_companie, user_job_posted_list_search, view_vacancy_category, \
      job_details

urlpatterns = [

      path('',IndexView.as_view()),
      # path('profile',profile.as_view()),
      path('view_companies',view_companie.as_view()),
      path('view_vacancy_category',view_vacancy_category.as_view()),
      path('user_job_posted_list_search',user_job_posted_list_search.as_view()),
      path('job_details',job_details.as_view()),
      #
      ]
def urls():
      return urlpatterns,'Guest', 'Guest'