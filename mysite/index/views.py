from django.shortcuts import render, redirect
from django.http import  HttpResponse
from django.views import  View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import G_Image
from django.core.paginator import Paginator


# Create your views here.
class Index(View):

    def get(self, request):
        catagory_fil = G_Image.objects.filter(catagory='Lord Ganesha')
        catagory_H = G_Image.objects.filter(catagory='Lord Hanuman')

        return render(request, 'index/index.html', {'gan': catagory_fil, 'han':catagory_H})

def gallery(request):

    laod_images = G_Image.objects.all().order_by('img_id')
    paginator = Paginator(laod_images, 12)
    page_no = request.GET.get('page')
    page_obj = paginator.get_page(page_no)

    img_params = {'imgContent':page_obj}
    
    return render(request, 'index/gallery.html', img_params)

class Register(View):

     def post(self, request):
        user_name = request.POST['user']
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        email = request.POST['email']
        password1 = request.POST['pass1']
        password2 = request.POST['pass2']
        try:
            if password1 == password2:
                user = User.objects.create_user(username=user_name, first_name=firstname, last_name=lastname, email=email, password=password1)
                user.save()
                messages.success(request, 'User Registered Successfully')
            else:
                messages.error(request, 'Password not matched')
            return redirect('/')
        except Exception as e:
            messages.error(request, 'Unable To Register User')
            return redirect('/')

class Login_View(View):
    def post(self, request):
        username = request.POST.get('user')
        password = request.POST.get('pass')
        auth_user = authenticate(username=username, password=password)
        if auth_user is not None:
            login(request, auth_user)
            messages.success(request, 'Login is Successfull')
        else:
            messages.error(request, 'Login Failed')
        return redirect('/')

class LogoutMethod(View):

    def get(self, request):
        logout(request)
        messages.success(request, 'Logged Out Successfully')
        return redirect('/')
        








