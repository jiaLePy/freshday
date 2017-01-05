from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^cart$',views.cart),
    url(r'^order$',views.order),
]