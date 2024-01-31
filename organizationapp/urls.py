from django.contrib import admin
from django.urls import path
from organizationapp import views


urlpatterns = [
    path('api/org/register/',views.registeration_api_view),
    path('signup',views.signup_view,name='signuppage'),
    path('login',views.login_view,name='loginpage'),
    path('',views.home_view,name='homepage'),
    path('logout',views.logout_view,name='logout'),
    path('dashboard',views.dashboard_view,name='dashboardpage'),
    path('dashboard/plans',views.plans_view,name='planspage'),
    path('hello', views.helloApiview.as_view(), name ='hello'), 
    path("api/organizatinos",views.orgsApiview.as_view(),name='orgs'),
]