from django.urls import path
from . import views

urlpatterns = [

    path('login/' , views.login_view , name='login_page_user'),
    path('logout/' , views.logout_view , name='logout_page_user'),
    path('dashboard/' , views.user_dashboard , name='dashboard_user'),
    path('appointments/' , views.hospital_selection , name='hospital_selection'),
    path('appointments/registration_form' , views.registration_view , name='registration_form'),
    path('appointments/confirmation' , views.confirmation , name='confirmation_page'),
]