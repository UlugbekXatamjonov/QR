from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Mahsulot, CostomUser

class MahsulotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mahsulot
        fields = ('id','tur','nom','rang','rasm','narx','son','kompania','mudat','kg','qr_code','izoh','sana')
    

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CostomUser
        fields = ('photo','birth_date',) # 'id','username', 'first_name', 'last_name','email',    