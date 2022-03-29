from django.urls import path
from .views import *

app_name = "products"

urlpatterns = [
    path('<int:year>/<int:month>/<int:day>/<int:pk>',DetailMahsulot.as_view(), name='detail'),
    path('',ListMahsulot.as_view(), name='list'),
    # path('user/<int:pk>/', UserDetail.as_view()),
    # path('user/', UserList.as_view()),
]
