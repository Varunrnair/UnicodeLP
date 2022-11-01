from . import views
from django.urls import path

urlpatterns = [
    path('',views.loginpage, name='loginpage'),
    path('register/',views.registerpage, name='registerpage'),  
    path('logout/',views.logoutuser, name='logout'),  
    path('func/',views.func ,name ='func'),
    path('showlist/',views.showlist,name='showlist'),
    path('func/<str:pk>', views.deletestuff, name='deletestuff'),
    path('func/update/<str:pk>', views.updatestuff, name='updatestuff'),
]