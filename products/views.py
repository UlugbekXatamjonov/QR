from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from django.contrib.auth import get_user_model
from .models import Mahsulot, CostomUser
from .serializers import MahsulotSerializer, UserSerializer

class ListMahsulot(ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated, )
    queryset = Mahsulot.objects.all()
    serializer_class = MahsulotSerializer
    template_name = 'list.html'

class DetailMahsulot(RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated, )
    queryset = Mahsulot.objects.all()
    serializer_class = MahsulotSerializer
    template_name = 'list.html'


class UserList(ListCreateAPIView):
    queryset = CostomUser.objects.all()
    serializer_class = UserSerializer

class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = CostomUser.objects.all()
    serializer_class = UserSerializer


