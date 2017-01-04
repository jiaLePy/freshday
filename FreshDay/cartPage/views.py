from django.shortcuts import render

# Create your views here.
def user_center_site(request):
    return render(request,'cartPage/user_center_site.html')
