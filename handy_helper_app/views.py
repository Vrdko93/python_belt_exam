from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt

from .models import *

# Create your views here.
def show_main_page(request):
    return render(request, "login_and_reg.html")

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for value in errors.values():
            messages.error(request, value)
        return redirect("/")

    pw_hash = bcrypt.hashpw(request.POST["password"].encode(), bcrypt.gensalt()).decode()

    user = User.objects.create(   
        first_name = request.POST["first_name"], 
        last_name = request.POST["last_name"],
        email = request.POST["email"],
        password = pw_hash
        )

    request.session["user_id"] = user.id

    return redirect("/dashboard")

def login(request):
    potential_user = User.objects.filter(email = request.POST["email"])
    if len(potential_user) == 0:
        messages.error(request, "Please check your email and password")
        return redirect("/")
    
    user = potential_user[0]

    if not bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
        messages.error(request, "Please check your email and password")
        return redirect("/")
    
    request.session["user_id"] = user.id

    return redirect("/dashboard")

def logout(request):
    request.session.pop("user_id")
    return redirect("/")

def show_dashboard(request):
    if "user_id" not in request.session:
        messages.error(request, "You are not logged in")
        return redirect("/")
        
    context = {
        'user': User.objects.get(id=request.session["user_id"]),
        'jobs': Job.objects.all(),
    }
    return render(request, "dashboard.html", context)

def show_create_job_page(request):
    context = {
        'user': User.objects.get(id=request.session["user_id"]),
    }
    return render(request, "create_job.html", context)

def create_job(request):
    errors = Job.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for value in errors.values():
            messages.error(request, value)
        return redirect("/jobs/new")

    user = User.objects.get(id=request.session["user_id"])
    Job.objects.create(title = request.POST["title"], description = request.POST["description"], location = request.POST["location"], uploaded_by=user)

    return redirect("/dashboard")

def show_job(request, job_id):
    context = {
        'user': User.objects.get(id=request.session["user_id"]),
        'job': Job.objects.get(id=job_id),
    }
    return render(request, "show_job.html", context)
    

def edit_job(request, job_id):
    context = {
        'user': User.objects.get(id=request.session["user_id"]),
        'job': Job.objects.get(id=job_id),
    }
    
    return render(request, "edit_job.html", context)

def update_job(request, job_id):
    errors = Job.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for value in errors.values():
            messages.error(request, value)
        return redirect(f"/jobs/edit/{job_id}")

    job = Job.objects.get(id=job_id)
    job.title = request.POST["title"]
    job.description = request.POST["description"]
    job.location = request.POST["location"]
    job.save()

    return redirect("/dashboard")

def delete_job(request, job_id):
    job = Job.objects.get(id=job_id)
    job.delete()

    return redirect("/dashboard")






    
    

    