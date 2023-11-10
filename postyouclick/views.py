from django.shortcuts import render,redirect
import uuid
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordChangeForm,PasswordResetForm,SetPasswordForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.
from.models import Newuser,NewImage
from.forms import Create_New_User,Add_image_post,Edit_user
from .email import send_email_verify,send_reset_password

from django.views.decorators.csrf import csrf_exempt




@login_required(login_url='login')
@csrf_exempt
def index(request):
    q = request.GET.get('q')
    if q:
        allimage = NewImage.objects.filter(Q(post__contains=q)|Q(post__icontains=q))
        
    else: 
        allimage = NewImage.objects.all()
    
    return render(request,'image_post/index.html',{'allimage':allimage})

@csrf_exempt
def user_sigin(request):
    userform = Create_New_User()
    if request.method =="POST":
        form = Create_New_User(request.POST,request.FILES)
        if form.is_valid():
            user=form.save(commit=False)
            user.email = request.POST['email']
            user.token = str(uuid.uuid4())
            send_email_verify(user.email,user.token)
            user.save() 
            return HttpResponse("<h1> check your mail for verification </h1>")
        else:
            return render(request,'image_post/create_user.html',{'user':form})
    
    return render(request,'image_post/create_user.html',{'user':userform})

@csrf_exempt
def email_verify(request,token):
    user = Newuser.objects.filter(token=token).first()
    if user is not None:
        user.is_active = True
        user.save()
        return redirect('login')
    else:
        messages.info(request,'Unable to Verify')
        return render('login')
    
@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            return render(request,'image_post/login.html',{'message':' Invalid Credentials '})
            
    return render(request,'image_post/login.html')


@login_required(login_url='login')
@csrf_exempt
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
@csrf_exempt
def add_post(request):
    context = {'form':Add_image_post()}
    if request.method =="POST":
        form = Add_image_post(request.POST,request.FILES)
        if form.is_valid():
            user=form.save(commit=False)
            user.name=request.user
            user.save()
            return redirect('index')
        else:
             form = context[form]
    return render(request,'image_post/add_post.html',context)

@login_required(login_url='login')
@csrf_exempt
def edit_post(request,id):
    edit = NewImage.objects.get(pk=id)
    if request.user == edit.name:
        context = {'form':Add_image_post(instance=edit)}
        if request.method =="POST":
            form  = Add_image_post(request.POST,request.FILES,instance=edit)
            if form.is_valid():
                form.save()
                return redirect('index')
            else:
                form = context[form]
    else:
        return redirect('index')
    return render(request,'image_post/edit_post.html',context)



@login_required(login_url='login')
@csrf_exempt
def delete_post(request,id):
    post = NewImage.objects.get(pk=id)
    if request.method == 'POST':
        if request.user == post.name:
            post.delete()
            return redirect('index')
        else:
            return redirect('index')
    return render(request,'image_post/delete_post.html')

@login_required(login_url='login')
@csrf_exempt    
def view_post(request,id):
    user = NewImage.objects.get(pk=id)
    return render(request,'image_post/view.html',{'user':user})


@login_required(login_url='login')
@csrf_exempt
def user_posted(request,id):
    posted = NewImage.objects.filter(name_id=id)
    for user in posted:
        user= user
    return render(request,'image_post/user_posted.html',{"posted":posted,'user':user})


@login_required(login_url='login')
@csrf_exempt
def user_profile_views(request):
    return render(request,'image_post/user_profile_edit.html',)



@login_required(login_url='login')
@csrf_exempt
def user_profile_edit(request):
    user = Edit_user(instance=request.user)
    if request.method =="POST":
        form = Edit_user(request.POST,request.FILES,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('user_posted',request.user.id)
        else:
           return render(request,'image_post/edit_user.html',{'user':form})
    return render(request,'image_post/edit_user.html',{'user':user})


      
@login_required(login_url='login')
@csrf_exempt
def change_password(request):
    password = PasswordChangeForm(user=request.user)
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST,user=request.user)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request,'image_post/change_password.html',{'user':form})
    return render(request,'image_post/change_password.html',{'user':password})


@csrf_exempt
def reset_password(request):
    
    if request.method =="POST":
        mail = request.POST.get('email', False)
        user = Newuser.objects.filter(email=mail).first()
        if user:
            send_reset_password(user.email,user.token)
            return HttpResponse('password reset link has been sent to your email') 
        else:
            return render(request,'image_post/reset.html',{'message':'User does not exist'})
    return render(request,'image_post/reset.html')
    

def password_verify(request,id):
    new = Newuser.objects.get(token=id)
    if new:
        user = SetPasswordForm(user=new)
        if request.method =="POST":
            form = SetPasswordForm(data=request.POST,user=new)
            if form.is_valid():
                form.save()
                messages.info(request,'password change successfully')
                return redirect('login')
            else:
               return render(request,'image_post/reset_password.html',{'form':form})
    else:
        return HttpResponse('error in reset password ')   
        
    return render(request,'image_post/reset_password.html',{'form':user})
    

@login_required(login_url='login')
@csrf_exempt
def like_user(request,id):
    new = NewImage.objects.get(pk=id)
    if request.method =="POST":
        if new.like.filter(id=request.user.id).exists():
            new.like.remove(request.user)
            return redirect('index')
        else:
            new.like.add(request.user)
            return redirect('index')
        