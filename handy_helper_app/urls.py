from django.urls import path
from . import views

urlpatterns = [
    path("", views.show_main_page),
    path("register", views.register),
    path("login", views.login),
    path("logout", views.logout),
    path("dashboard", views.show_dashboard),
    path("jobs/new", views.show_create_job_page),
    path("create_job", views.create_job),
    path("jobs/<int:job_id>", views.show_job),
    path("jobs/edit/<int:job_id>", views.edit_job),
    path("jobs/delete/<int:job_id>", views.delete_job),
    path("update_job/<int:job_id>", views.update_job),
]