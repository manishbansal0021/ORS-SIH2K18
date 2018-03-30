from django.urls import path
from . import views

urlpatterns = [
    path('login/' , views.login_view , name='login_page_mgnt'),
    path('logout/',views.logout_view,name='logout_page_mgnt'),
    path('register/',.views.register,name='hospital_registration'),
    path('dashboard/',views.hospital_dashboard,name='hospital_dashboard'),
]