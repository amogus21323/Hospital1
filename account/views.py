from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView

from .models import Doctor
from .serializers import RegistrationSerializer, ActivationSerializer, UserSerializer, DoctorSerializer

from rest_framework.response import Response
from .send_email import send_confirmation_email
from rest_framework.generics import GenericAPIView, get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import permissions, viewsets
from rest_framework.generics import ListAPIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.decorators import action
User = get_user_model()

# def index(request):
#     return render(request,'dashboard')

class RegistrationView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        if user:
            try:
                send_confirmation_email(user.email,
                                        user.activation_code)
            except:
                return Response({'message': "Зарегистрировался, но на почту код не отправился",
                                 'data': serializer.data}, status=201)
        return Response(serializer.data, status=201)

class ActivationDocView(GenericAPIView):
    serializer_class = RegistrationView

    def get(self, request):
        code = request.GET.get('u')
        user = get_object_or_404(Doctor, activation_code=code, )
        user.is_active = True
        user.activation_code = ''
        user.save()
        return Response('Успешно активирован', status=200)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('Успешно активирован', status=200)

class ActivationView(GenericAPIView):
    serializer_class = ActivationSerializer

    def get(self, request):
        code = request.GET.get('u')
        user = get_object_or_404(User, activation_code=code, )
        user.is_active = True
        user.activation_code = ''
        user.save()
        return Response('Успешно активирован', status=200)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('Успешно активирован', status=200)

class LoginView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)

class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)
class UserDoctorView(ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = (permissions.IsAuthenticated,)


class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)


class DashboardView(View):
    template_name = "account/dashboard.html"

    # def get(self, request):
    #     return render(request, self.template_name)
    #
    # def post(self, request):
    #     action = request.POST.get("action", None)
    #
    #     if action == "login":
    #         return redirect("login")
    #     elif action == "register":
    #         return redirect("registration")
    #     else:
    #         return render(request, self.template_name, {"error": "Invalid action"})

# class AppointmentView(APIView):
#
#    ...
#
# class AppointmentViewSet(viewsets.ModelViewSet):
#     queryset = Appointment.objects.all()
#     serializer_class = AppointmentSerializer

    # def get_permissions(self):
    #     if self.action in ['update' , 'partial_update' , 'create' , 'destroy']:
    #         return (permissions.IsAdminUser(),)
    #     return (permissions.AllowAny(),)



# def doctorclick_view(request):
#     if request.user.is_authenticated:
#         return
