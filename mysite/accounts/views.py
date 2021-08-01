from django.http.response import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from accounts.forms import RegisterMember
from accounts.models import Member, UserMembers

# Create your views here.

def Register(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['pass1']
        password2 = request.POST['pass2']
        firstname = request.POST['fname']
        lastname = request.POST['lname']

        user = User.objects.create_user(username=username, email=email, password=password1, first_name=firstname, last_name=lastname)
        user.save()
        messages.success(request, 'User Registered Successfully')
        return redirect('/accounts/login')

    return render(request, 'accounts/register.html')

def LoginHandle(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        myuser = authenticate(username=username, password=password)
        if myuser is not None:
            login(request, myuser)
            messages.success(request, 'Welcome '+ myuser.first_name)
            
            return redirect('/')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('/accounts/login')

    return render(request, 'accounts/login.html')

def Contact(request):

    return render(request, 'accounts/contact.html')

def HandleLogout(request):

    logout(request)
    messages.success(request, 'Logout done')
    return redirect('/')

def members(request):
    if request.method == 'POST':
        reg = RegisterMember(request.POST)
        if reg.is_valid():
            name = reg.cleaned_data['member_name']
            email = reg.cleaned_data['member_email']
            contact = reg.cleaned_data['member_contact']
            memb = Member(member_name=name, member_email=email, member_contact=contact)
            memb.save()

            
        return redirect('/accounts/members/')

    reg = RegisterMember()
    memb = Member.objects.all()
    return render(request, 'accounts/members.html', {'Member':memb,'forms':reg})

def Delete_members(request, mem_id):

    if request.method == 'POST':
        mem = Member.objects.get(pk=mem_id)
        mem.delete()
        return redirect('/accounts/members/')
    return HttpResponseBadRequest()

def update_members(request, id):
    if request.method == 'POST':
        up = Member.objects.get(pk=id)
        reg = RegisterMember(request.POST, instance=up)
        if reg.is_valid():
            reg.save()
        return redirect('/accounts/members/')
    up = Member.objects.get(pk=id)
    reg = RegisterMember(instance=up)
    return render(request, 'accounts/update.html', {'forms':reg})

def user_member(request, id):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email1')
        gender = request.POST.get('gender')
        desc = request.POST.get('text_desc')
        us = User.objects.get(pk=id)
        um = UserMembers(user_id=us, user_name=name, user_email=email, user_gender=gender, user_desc=desc)
        um.save()
        return redirect('/')
    us = User.objects.get(pk=id)
    user_mem = UserMembers.objects.filter(user_id=us.id)
    return render(request, 'accounts/usermembers.html',{'userdata':user_mem})



