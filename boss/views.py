from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from django.contrib.auth import get_user_model

from .serializers import BossSerializer


class BossList(ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = BossSerializer

class BossDetail(RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = BossSerializer
