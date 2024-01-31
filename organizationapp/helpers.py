from organizationapp.models import *
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout


def plan_request_handler(request):
    user = request.user
    selected_plan_price = request.POST.get("plan-selected")
    if selected_plan_price is None:
        raise Exception("Selected Price not valid ")
    
    plan_obj = YearlyPlans.objects.get(price=selected_plan_price)
    org_details_obj = OrganizationDetails.objects.get(email=user)
    org_details_obj.location_count = plan_obj.locations_count
    org_details_obj.save()

    return redirect("/dashboard")    


def custom_authentication(request):
    email = request.POST.get("email")
    password = request.POST.get("password")
    user = authenticate(request,username=email,password=password)
    if user is not None :
        login(request=request,user=user)
        return redirect("/dashboard")
    return render(request,"organizationapp/login.html",{"error":"username or password not valid"})


def register_user(data):
    # --------  Credentials -----------
    email = data.get("email")
    password = data.get("password")

    user_obj = User(username=email)
    user_obj.set_password(password)
    user_obj.save()

    # --------  Details -----------
    org_name = data.get("organization-name")
    org_type = data.get("organization-type")
    phone_number = data.get("phone-number")
    license_number = data.get("license-number")

    details_obj = OrganizationDetails(email = user_obj,org_name=org_name,org_type=org_type,phone_number=phone_number,license_number= license_number)
    details_obj.save()

    # --------  Location -----------
    # total_address = data.get("address-counter")
    # for index in range(int(total_address)):
    #     landmark = data.get(f"landmark-{index+1}")
    #     full_address = data.get(f"full-address-{index+1}")
    #     location_obj = locationDetails(email=user_obj,location_name=landmark,location_address=full_address)
    #     location_obj.save()
    
    return redirect("/login")
