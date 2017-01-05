from django.conf.urls import  url
import  views

urlpatterns = [
    url(r'^list/(\d*)$',views.list)
]
