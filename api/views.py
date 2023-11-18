from urllib import request
from django.shortcuts import render

# Create your views here.
class Home(request):
    template_name="index.html"
    def get(self, request):
        return render(request, self.template_name)
    
class Login(request):
    template_name="login.html"
    def get(self, request):
        return render(request, self.template_name)
    
class SignIn(request):
    template_name="signup.html"
    def get(self, request):
        return render(request, self.template_name)