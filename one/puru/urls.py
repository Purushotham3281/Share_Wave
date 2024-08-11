from django.urls import path
from puru import views

urlpatterns=[
    path("",views.home,name="homepage"),
    path("login",views.logins,name="loginpage"),
    path("register",views.register,name="registerpage"),
    path("profile",views.profile,name="profilepage"),
    
    path("single",views.display,name="singlepage"),
    path("create",views.create,name="createpage"),
    path("delete/<int:pid>",views.delete,name="deletepage"),
    path("logout",views.logouts,name="logoutpage"),
]