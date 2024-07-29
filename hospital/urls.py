from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.authentication import TokenAuthentication
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf.urls.static import static

from product.views import ProductViewSet, AppointmentViewSet, TalonViewSet

# from category.views import CategoryViewSet
# from product.views import ProductViewSet
#
router = DefaultRouter()

router.register("product", ProductViewSet)
router.register("appointment", AppointmentViewSet)
router.register("talon", TalonViewSet)






schema_view = get_schema_view(
   openapi.Info(
      title="Hospital API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
    authentication_classes=(TokenAuthentication,)
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/account/', include('account.urls')),
    path('category/', include('category.urls')),
    path("api/order/", include("order.urls")),

    path("api/", include(router.urls)),
    # path('product/', include('product.urls')),

    path(
            "swagger/",
            schema_view.with_ui("swagger", cache_timeout=0),
            name="schema-swagger-ui",
        ),

]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

