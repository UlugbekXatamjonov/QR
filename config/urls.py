from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
# from rest_auth.registration.views import VerifyEmailView, RegisterView
from products.views import *


app_name= 'users'

schema_view = get_schema_view(
    openapi.Info(
        title='Blog API',
        description='oddiy API loyixasi', 
        default_version='v1',
        terms_of_service='https://google.com.policies.terms',
        contact=openapi.Contact(email="xatamjonovulugbek17@gmail.com"),
        license=openapi.License('Blog API litsenziasi'),
        ),
        public=True,
        permission_classes=(permissions.AllowAny, ),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls'), name='products'),
    path('user/<int:pk>/', UserDetail.as_view()),
    path('user/', UserList.as_view()),
    
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),

    # path('auth/account-confirm-email/(?P<key>[-:\w]+)/$', VerifyEmailView.as_view(), name='account_confirm_email'),
    # path('auth/account-confirm-email/',  .as_view(), name='account_email_verification_sent'),

    path('auth/', include('rest_framework.urls')),
    path('allauth/', include('allauth.urls')),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-radoc'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    