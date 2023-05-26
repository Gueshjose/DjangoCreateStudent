from django.shortcuts import render,redirect
from .models import Student
from students.forms import StudentForm
# Create your views here.
def home(request):
    return render(request,"students/home.html",{'students':Student.objects.all().values()})

def store(request):
    if request.method == "POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            student = form.sav()
            return redirect('home')
    else:
        form=StudentForm()
    return render(request,'students/studentForm.html',{'form':form})