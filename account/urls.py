from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import (RegistrationView, ActivationView, LoginView, UserListView,
                    LogoutView, UserDoctorView, UserSerializer, ActivationDocView,
                    DoctorSerializer, DashboardView, )
urlpatterns = [
    path('register/', RegistrationView.as_view()),
    path('activate/', ActivationView.as_view()),
    path('doc-activate/',ActivationDocView.as_view()),
    path('doc-register/', RegistrationView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('users/', UserListView.as_view()),
    path('refresh/',TokenRefreshView.as_view()),
    path('doctor/', UserDoctorView.as_view()),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),

    # path('appointment1/', AppointmentViewSet.as_view()),
    # path('appointment2/',AppointmentView.as_view()),

]

