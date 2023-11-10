from django.contrib import admin
from django.urls import path
from api import views



urlpatterns = [

    path('admin/', admin.site.urls),
    #path('signup',views.HomePage,name='signup'),
    path('signup',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('home/',views.HomePage,name='home'),
    path('logout/',views.LogoutPage,name='logout'),
    path('encu/', views.Enc, name='encu'),
    

]


