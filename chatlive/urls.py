
from django.contrib import admin
from django.urls import path, re_path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="LiveChat API",
        default_version="v1",
        description="websocket api built with django and channels",
        terms_of_service="for test",
        contact=openapi.Contact(email="nchidimnm4@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('ws/chat/', include('chatapp.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('rest_auth.urls')),
    path('auth/registration/', include('rest_auth.registration.urls')),
    re_path(r'api/v1/docs', schema_view.with_ui('redoc', cache_timeout=0), name="schema_redoc")
]
