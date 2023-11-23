from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Reg
from .forms import Regform,LoginForm
# Create your views here.
class Home(View):
    def get(self,request):
        return render(request,"home.html")
class reginput(View):
    def get(self,request):
        condic={"regform":Regform()}
        return render(request,"input.html",context=condic)
class regview(View):
    def post(self,request):
        rf=Regform(request.POST)
        if rf.is_valid():
            r1=Reg(fristname=rf.cleaned_data["fristname"],
                   lastname=rf.cleaned_data["lastname"],
                   username=rf.cleaned_data["username"],
                   password=rf.cleaned_data["password"],
                   cpassword=rf.cleaned_data["cpassword"],
                   emailid=rf.cleaned_data["emailid"],
                   mobileno=rf.cleaned_data["mobileno"]
                   )
            r1.save()
            res=HttpResponse("<h1>REG SUCESS</h1>")
        return res
class Logininput(View):
    def get(self,request):
        condic={"logininput":LoginForm()}
        return  render(request,"logininput.html",context=condic)
class Login(View):
    def post(self,request):
        lf=LoginForm(request.POST)
        if lf.is_valid():
            objs=Reg.objects.filter(username=lf.cleaned_data["username"],
                                    password=lf.cleaned_data["password"])
            if objs:
                return HttpResponse("LOGIN SUCESS")
            else:
                return HttpResponse("LOGIN FAILED")
