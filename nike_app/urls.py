from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('logout/',views.logout_user,name='logout'),
    path('detail/<int:id>/',views.detail,name='detail'),
    path('card',views.card,name="card"),
    path('home',views.home,name='home'),



]
