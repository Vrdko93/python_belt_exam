from django.db import models
import re

# Create your models here.

class UserManager(models.Manager):
    def basic_validator(self, data):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(data["first_name"]) <= 3:
            errors["first_name"] = "First name needs to be at least 2 characters"

        if len(data["last_name"]) <= 3:
            errors["last_name"] = "Last name needs to be at least 2 characters"

        if not EMAIL_REGEX.match(data['email']):               
            errors["email"] = "Invalid email address!"

        if len(data["password"]) <= 3:
            errors["password"] = "Password needs to be at least 8 characters"
        elif data["password"] != data["confirm_password"]:
            errors["password"] = "Passwords do not match"

        return errors

class User(models.Model):
    first_name = models.CharField(max_length = 45)
    last_name = models.CharField(max_length = 45)
    email = models.CharField(max_length = 45)
    password = models.CharField(max_length = 45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class JobManager(models.Manager):
    def basic_validator(self, data):
        errors = {}
    
        if len(data["title"]) < 3:
            errors["title"] = "Job title needs to be at least 3 characters"

        if len(data["description"]) < 3:
            errors["description"] = "Job description needs to be at least 3 characters"

        if len(data["location"]) < 3:
            errors["location"] = "Job location needs to be at least 3 characters"

        return errors

class Job(models.Model):
    title = models.CharField(max_length = 45)
    description = models.CharField(max_length = 255)
    location = models.CharField(max_length = 255)
    uploaded_by = models.ForeignKey(User, related_name="uploaded_job", on_delete = models.CASCADE)
    users = models.ManyToManyField(User, related_name="jobs")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = JobManager() 



