from django.http import HttpResponseNotFound
from django.shortcuts import redirect, render
from django.urls import reverse

from jobapp.models import JobPost

# Create your views here.
def job_list(request):
    jobs = JobPost.objects.all()
    return render(request,'jobapp/index.html',{'jobs':jobs})

def job_detail(request, id, slug):
    try:
        if id==0:
            return redirect(reverse('jobs_home'))
        job=JobPost.objects.get(id = id)
        return render(request,'jobapp/job_detail.html',{'job':job})
    except:
        return HttpResponseNotFound('Not found')