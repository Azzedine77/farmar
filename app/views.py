from django.shortcuts import render

from django.views.generic.base import View
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from .form import FarmerForm,FarmerLoginForm,FarmForm
from django.http import HttpResponseRedirect, Http404

# Create your views here.
from .models import Category,Farmer,Farm,Schedule_detail
class index(View):
  def get(self, request, *args, **kwargs):
        context = {
                "categorys":Category.objects.all(),
                "farms":Farm.objects.all()

        }
        return render(request, "index.html",context=context)
    

class register(View):
    def get(self, request, *args, **kwargs):
        if islogin(request):
                       return redirect('/')
        formset = FarmerForm()
        if request.method == "POST":
            formset = FarmerForm(
                request.POST)
            if formset.is_valid():
                formset.save()
                return HttpResponseRedirect("/")
        formset = FarmerForm()
        context = {
            "formset":formset,
        }
        return render(request, "register.html",context=context)
    def post(self, request, *args, **kwargs):
            if islogin(request):
                       return redirect('/')
            formset = FarmerForm(
                request.POST)
            if formset.is_valid():
                farm=formset.save()
                request.session['username'] =farm.id

                return redirect("/")
            messages.info(request, 'Wrong credentials')
            return HttpResponseRedirect("register")        # return SignInView(request)
# .html
class details(View):
    def get(self, request, *args, **kwargs):
        
        fff=Farm.objects.filter(farmer=int(request.session.has_key('username')))
        context = {
                "details":Schedule_detail.objects.filter(farm=fff.first()),
                 "categorys":Category.objects.all(),

        }
        return render(request, "blog-details.html",context=context)

    
class addFarm(View):
    def get(self, request, *args, **kwargs):
        if islogin(request)== False:
                       return redirect('login/')
        formset = FarmForm()
        
        formset = FarmForm()
        context = {
            "formset":formset,
        }
        return render(request, "farm.html",context=context)
    def post(self, request, *args, **kwargs):
            # raise Exception("Date provided can't be in the past")
            # if islogin(request):
                    #    return redirect('/')
            formset = FarmForm(
                request.POST)
            if formset.is_valid():
                # formset.save()
                # formset.farmer=request.session['username'];
                
                
                self.object =formset.save(commit=False)
                # self.object = frm.asave(commit=False)
                self.object.farmer = Farmer(id=int(request.session['username']))
                self.object.save()
                # request.session['username'] =farm.id

                return redirect("/")
            messages.info(request, 'Wrong credentials')
            return HttpResponseRedirect("addform")        # return SignInView(request)
# .html

def islogin(request):
   if request.session.has_key('username'):
    #   username = request.session['id']
    return True
    #   return render(request, 'loggedin.html', {"username" : username})
   else:
      return False
def SignInView(request):
    # data = request.POST
    # action = data.get("login")
    # print(action)
    # if action == "login":
        # print(email)
        # print(password)
    # ''' Sign in views '''
    # if request.method == 'POST':
        # email = request.POST.get('email')
        # password = request.POST.get('password')
        # request_dict = request.POST.dict()
    email = request.POST.get('email')
    password = request.POST.get('passowrd')
    print(email)
    print(password)

    user = Farmer.objects.filter(email=email , passowrd=password)
    if not user:
        messages.info(request, '%s Not found!' % email)
        return redirect('loginformar')
    else:
        request.session['username'] = user.first().id

        return redirect('/')
    profile = Farmer.objects.filter(email=email, passowrd=password)
    

    # auth_user = authenticate(email=email, password=password)
    # if profile is None:
    #     messages.info(request, 'Wrong credentials')
    #     return redirect('sign-in')
    # login(request, auth_user)
   
    # return render(request, 'login.html')
def login(request):
        if islogin(request):
            context = {
                "categorys":Category.objects.all()
                }
            # return render(request, "index.html",context=context)
            return redirect('/')
        login = FarmerLoginForm()
        print(request.method)
        # print(request.method == "POST")
        if request.method == "POST":
            
                context = {
                    "login":login
                }
                return SignInView(request)
        else:
            context = {
                "login":login
            }
            return render(request, "login.html",context=context)
            # return render(request, 'login.html')
class loginsss(View):
    def get(self, request, *args, **kwargs):
        # print(request.POST.get('email'))
        print(request.method == 'POST')
        if request.method == 'POST':
            return SignInView(request)
        return  HttpResponseRedirect("/")
    def post(self, request, *args, **kwargs):
        print(request.method == 'POST')

        # data = request.POST
        # print(data)
        return SignInView(request)
