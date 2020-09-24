
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Movies REST API",
      default_version='v1',
      description="API for React mentoring programm",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="maksim_karsakou1@epam.com"),
      license=openapi.License(name="MIT"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('movies.urls')),
    path('auth/', include('authentication.urls')),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
