from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Mahsulot
from .serializers import MahsulotSerializer

class ListMahsulot(ListAPIView):
    queryset = Mahsulot.objects.all()
    serializer_class = MahsulotSerializer
    template_name = 'list.html'

class DetailMahsulot(RetrieveAPIView):
    queryset = Mahsulot.objects.all()
    serializer_class = MahsulotSerializer
    template_name = 'list.html'

