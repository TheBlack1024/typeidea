from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,FileResponse
from django.template import Template,Context
import os

def hello(request):
    return render(request,"mooc_1.htmlcss")

def homeproc(request):
    response = HttpResponse()
    response.write("<h1>这是首页，具体功能请访问<a href='./index2'>这里</a></h1>")
    response.write("<h1>这里是第二行，访问<a href='./index'>这里</a></h1>")
    return response
    #return HttpResponse("<h1>这是首页，具体功能请访问<a href='./index2'>这里</a></h1>")

def homeproc1(request): #JsonResponse响应，返回字典
    response = JsonResponse({"key":"valua1"})
    return response

def homeproc2(request): #FileResponse响应,返回文件
    cwd = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    response = FileResponse(open(cwd + "/hello2app/templates/beijin.jpg","rb"))
    response["Content-Type"] = "application/octet-stream"
    response["Content-Disposition"] = "attachment;filename='beijin.jpg'"
    return response

def pgproc(requset): #渲染
    template = Template("<h1>这个程序的名字是{{ name }}</h1>")
    context = Context({"name":"实验平台"})
    return HttpResponse(template.render(context))
