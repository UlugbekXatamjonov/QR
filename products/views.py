from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from .models import Mahsulot
from .serializers import MahsulotSerializer

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

