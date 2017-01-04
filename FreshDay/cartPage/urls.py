from django.conf.urls import include, url
import views

urlpatterns=[
    url(r'^site$',views.user_center_site),

]