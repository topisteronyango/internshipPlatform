from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Job
from .forms import JobForm, ApplyForm
from django.contrib.auth.decorators import login_required
from .filter import JobFilter
from django.core.paginator import Paginator

def joblist(request):
    jobs = Job.objects.all()

    #myfilter
    myfilter = JobFilter(request.GET, queryset=jobs)
    jobs = myfilter.qs # qs == queryset

    #pagenation
    paginator = Paginator(jobs, 5) # Show 3 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "jobs": page_obj, 
        "myfilter": myfilter
    }
    return render(request, "joblist.html", context)
    
@login_required
def job_detail(request, slug):
    job_detail = Job.objects.get(slug=slug) # will retrieve on job
    # job_detail = Job.object.filter() # will retrieve on job from a list according to some filtration

    # Django bootstrap:  https://django-bootstrap4.readthedocs.io/en/latest/quickstart.html
    if request.method=='POST':
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
                    myform = form.save(commit=False)
                    myform.job = job_detail
                    myform.save()
                    print('Posted Successfully')

    else:
        form = ApplyForm()


    context = {
         'job' : job_detail ,
           'form' : form
           }
    return render(request,'jobdetail.html', context)

@login_required
def add_job(request):
    if request.method=='POST':
        pass
        form = JobForm(request.POST , request.FILES) # request.FILES if theres any pic <form method="POST" enctype="multipart/form-data">
        if form.is_valid(): # to make sure the form is valid
            myform = form.save(commit=False) # save the form but not in the db because i need to add the person who added the job
            myform.owner = request.user
            myform.save()
            return redirect(reverse('jobs:job-list')) # after saving redirect to the job list REVERSE takes the urls (project:app)

    else:
        form = JobForm()
    return render(request,'addjob.html', {'form': form})