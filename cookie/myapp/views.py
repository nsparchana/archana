from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def setcookie(requset):
    response=HttpResponse("cookie set")
    response.set_cookie('priya','nz.com')
    return response
def getcookie(request):
    tutorial=request.COOKIES['java-tutorial']
    return HttpResponse("java tutorial@:"+tutorial)