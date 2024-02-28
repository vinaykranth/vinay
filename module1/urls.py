from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
   # path('admin/', admin.site.urls),
     path('hello/', hello, name='hello'),
     path('',NewHomePage, name='NewHomePage'),
     path('Travel/', Travel, name='Travel'),
     path('print_to_console/',print_to_console,name='print_to_console'),
     path('p/',print1,name='print'),
     path('otp/',randomcall1,name="randomcall1"),
     path('otplogic/',randomcall,name="randomcall"),
     path('getdate1/',getdate1,name="getdate1"),
     path('get_date/',get_date,name="get_date"),
     path('registerlogin/', registerlogin, name='registerlogin'),
     path('registerloginfunction/', registerloginfunction, name='registerloginfunction'),
     path('pie_chart/',pie_chart,name='pie_chart'),
     path('PieChartForm1/', PieChartForm1, name='PieChartForm1'),
     path('car/',car,name='car'),
     path('weatherpagecall/',weatherpagecall,name='weatherpagecall'),
     path('weatherlogic/',weatherlogic,name='weatherlogic'),
     path('feedback/', feedback, name='feedback'),
     path('feedbackfunction/', feedbackfunction, name='feedbackfunction'),
     path('logout/',logout,name='logout'),
     path('signup/', signup, name='signup'),
     path('login/', login, name='login'),
     path('signup1/', signup1, name='signup1'),
     path('login1/', login1, name='login1'),
]