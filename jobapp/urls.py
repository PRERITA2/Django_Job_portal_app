from django.urls import path
from jobapp import views

urlpatterns = [
    path('',views.job_list,name="jobs_home"),
    path('job/<int:id>-<slug>',views.job_detail,name="jobs_detail")
]