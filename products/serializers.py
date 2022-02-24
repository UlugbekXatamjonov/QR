from rest_framework import serializers
from .models import Mahsulot

class MahsulotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mahsulot
        fields = ('id','tur','nom','rang','rasm','narx','son','kompania','mudat','kg','qr_code','sana')
    
    