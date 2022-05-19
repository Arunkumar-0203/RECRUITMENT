"""RECRUITMENT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from RECRUITMENT import settings
from RECRUITMENT_APP import admin_urls,user_urls,company_urls,Guest_urls
from RECRUITMENT_APP.views import home_page, loginview, ContactView, registration, user_signup, company_signup, \
    view_jobs, view_company, view_vacancy_category, user_job_posted_list_search, job_details, about, guest_signup

urlpatterns = [
    path('',home_page.as_view()),
    path('login',loginview.as_view()),
    path('about',about.as_view()),
    path('contact',ContactView.as_view()),
    path('view_jobs',view_jobs.as_view()),
    path('job_details',job_details.as_view()),
    path('view_company',view_company.as_view()),
    path('view_vacancy_category',view_vacancy_category.as_view()),
    path('user_job_posted_list_search',user_job_posted_list_search.as_view()),
    path('registration',registration.as_view()),
    path('user_signup',user_signup.as_view()),
    path('company_signup',company_signup.as_view()),
    path('admin/',admin_urls.urls()),
    path('user/',user_urls.urls()),
    path('Guest/',Guest_urls.urls()),
    path('company/',company_urls.urls()),
    path('guest_signup',guest_signup.as_view())
]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
