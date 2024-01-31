from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from organizationapp.helpers import *
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from organizationapp.models import YearlyPlans
# Create your views here.



@login_required(login_url="/login")
def dashboard_view(request):
    location_details_objs = list(locationDetails.objects.filter(email=request.user))
    org_details = OrganizationDetails.objects.get(email=request.user)
    org_location_count = int(org_details.location_count)
    active_location_count = len(location_details_objs)
    available_location_count = int(org_location_count-active_location_count)
    if request.method == "POST" and available_location_count > 0:
        print(request.POST.get("location-name"))
        print(request.POST.get("location-address"))
        loc_obj = locationDetails(email=request.user,location_name = request.POST.get("location-name"),location_address = request.POST.get("location-address"))
        loc_obj.save()
        location_details_objs.append(loc_obj)
        active_location_count += 1
        available_location_count -= 1
        redirect('/dashbaord')
    context = {
        "LocationDetails":location_details_objs,
        "org_details":org_details,
        "org_location_count":org_location_count,
        "available_location_count":available_location_count,
        "available_location_count_itr":range(available_location_count)
        }
    return render(request,'organizationapp/dashboard.html',context=context)


@login_required(login_url="/login")
def plans_view(request):
    if request.method == "POST":
        return plan_request_handler(request)
    yearly_plans = YearlyPlans.objects.all()
    return render(request,'organizationapp/plans.html',{"yearly_plans":yearly_plans})


def signup_view(request):
    if request.method == "POST":
        return register_user(request.POST)
    return render(request,'organizationapp/register.html',{})

def login_view(request):
    if request.method == "POST":
        return custom_authentication(request)
    return render(request,'organizationapp/login.html',{})

def home_view(request):
    return render(request,"organizationapp/home.html",{})

def logout_view(request):
    logout(request=request)
    return redirect('/login')

@api_view(['POST'])
def registeration_api_view(request):
    """
    """
    try:
        email = request.POST.get("email")
        password = request.POST.get("password")
        # helpers.py > register_user
        register_user(email,password)
    except Exception as e:
        print(e)
        return Response({"error":str(e)})
    return Response({})

from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated 

class helloApiview(APIView): 
    permission_classes = (IsAuthenticated, ) 
    
    def get(self, request): 
        content = {'message': 'take fetched details '} 
        return Response(content) 
class orgsApiview(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        orgs = OrganizationDetails.objects.all()
        orgs_list = []
        for org in orgs:
            org_json = {
                "Logged In user":request.user.username,
                "Email":org.email.username,
                "Location Counts":org.location_count,
                "License Number":org.license_number,
                "Contact Number":org.phone_number
            }
            orgs_list.append(org_json)
        content = {
            "Message":"Thanks for choosing TBI.",
            "Total Organizations":len(orgs),
            "Organization Details" : orgs_list
        }
        return Response(content)