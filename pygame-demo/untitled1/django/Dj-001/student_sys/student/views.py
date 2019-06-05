from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View

from .models import Student
from .forms import StudentForm

if 0:#·Çclass-based view×ö·¨
    def index(request):
        students = Student.get_all()
        if  request.method == "POST":
            form = StudentForm(request.POST)
            if form.is_valid():
                """
                cleande_data = form.cleaned_data
                student = Student()
                student.name = cleande_data["name"]
                student.sex = cleande_data["sex"]
                student.email = cleande_data["email"]
                student.profession = cleande_data["profession"]
                student.qq = cleande_data["qq"]
                student.phone = cleande_data["phone"]
                """
                form.save()
                return HttpResponseRedirect(reverse("index"))
        else:
            form = StudentForm()
        context = {
            "students":students,
            "form":form
        }
        return render(request,'index.html',context=context)

class IndexView(View):

    template_name = "index.html"

    def get_context(self):
        students = Student.get_all()
        context = {
            "students" : students,
        }
        return context

    def get(self,request):
        context = self.get_context()
        form = StudentForm()
        context.update({
            "form" : form
        })
        return render(request,self.template_name,context=context)

    def post(self,request):
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))
        context = self.get_context()
        context.update({
            "form" : form
        })
        return render(request,self.template_name,context=context)