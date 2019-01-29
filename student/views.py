from django.shortcuts import render
from . import forms
from .models import *
# Create your views here.
def index(request):
    if request.method == 'POST':
        form= forms.Student_form(request.POST)
        if form.is_valid:
            form.save()
            return render(request,'thanks.html')
    else:
        form= forms.Student_form()
    student_info=Student.objects.all()
    context={'student_info':student_info,'form':form}
    return render(request,'index.html',context)



"""

job_list=Jobs.objects.all()
my_dict2={'jobs_list':job_list}
return render (request,'files/jobs.html',context=my_dict2)
"""
