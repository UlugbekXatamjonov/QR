from django.urls import path, include
from .views import UserList, UserDetail
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
# from rest_auth.registration.views import VerifyEmailView, RegisterView


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
	path('auth/', include('rest_framework.urls')),
	path('dj-rest-auth/', include('dj_rest_auth.urls')),
	path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('dj-rest-auth/registration/account_confirm_email/', include('dj_rest_auth.registration.urls')),
    # re_path(r'^account-confirm-email/', VerifyEmailView.as_view(), name='account_email_verification_sent'),
    # re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$', VerifyEmailView.as_view(), name='account_confirm_email'),
	path('allauth', include('allauth.urls')),

	path('<int:year>/<int:month>/<int:day>/<int:pk>', UserDetail.as_view(), name='detail'),
    path('', UserList.as_view(), name='list'),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-radoc'),
]


