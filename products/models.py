from django.db import models
from django.conf import settings
from django.utils.html import mark_safe
from django.contrib.auth.models import AbstractUser
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
from django.urls import reverse
from datetime import datetime
import barcode
from barcode.writer import ImageWriter 
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your models here.
RANG = (
    ('qora','Qora'),
    ('oq','Oq'),
    ('qizil','Qizil'),
    ('sariq','Sariq'),
    ('kulrang','Kulrang'),
    ('moviy','Moviy'),
    ('yashil','Yashil'),
    ('jigarang','Jigarang'),
    ('pushti','Pushti'),
    ('boshqa','Boshqa'),
)

TUR = (
    ('smartfon','Smartfon'),
    ('telefon','Telefon'),
    ('computer','Copmuter'),
    ('planshet','Planshet'),
    ('noutbook','Noutbook'),
    ('smartwatch','SmartWatch'),
)

KOMPANIA = (
    ('kompania','Ishlab chiqaruvchi nomi'),
)

MUDDAT = (
    ('x',''),
    ('0','cheklanmagan'),
    ('1/2','6 oy'),
    ('1',' 1 yil'),
    ('2','2 yil'),
    ('3','3 yil'),
    ('5','5 yil'),
    ('10','10 yil'),
)

class Mahsulot(models.Model):
    tur = models.CharField(max_length=150, choices=TUR, verbose_name='Mahsulot turi')
    nom = models.CharField(max_length=150, verbose_name='Mahsulot nomi')
    rang = models.CharField(max_length=50, choices= RANG, verbose_name='Mahsulot rangi', null=True, blank=True)
    rasm = models.ImageField(upload_to='mahsulotlar/%Y/%m/%d/', verbose_name='Mahsulot rasmi', null=True, blank=True)
    narx = models.IntegerField(default=0, verbose_name='Mahsulot natxi($)', null=True, blank=True)
    son = models.IntegerField(default=0, verbose_name='Mahsulot soni', null=True, blank=True)
    kompania = models.CharField(max_length=200, choices=KOMPANIA, default='kompania', verbose_name='Ishlab chiqaruvchi nomi ', null=True, blank=True ) # Ishlab chiqaruvchi nomi
    mudat  = models.CharField(max_length=150, choices=MUDDAT, default='x', verbose_name='Yaroqlilik mudati', null=True, blank=True)
    kg = models.IntegerField(default=0, verbose_name="Mahsulot og'irligi(kg)", null=True, blank=True)
    qr_code = models.ImageField(upload_to='QR_codes/%Y/%m/%d/', verbose_name='Mahsulot QR codi', null=True, blank=True)
    # shcode = models.ImageField(upload_to='Shtrx_codes/%Y/%m/%d/', verbose_name='Mahsulot Shtrx codi', null=True, blank=True)
    izoh = models.CharField(max_length=300, null=True, blank=True, verbose_name="Qo'shimcha izoh")
    sana = models.DateField(auto_now_add=False, auto_now=False, verbose_name='Omborga kelgan sana')
    yangilanish = models.DateTimeField(auto_now=True, verbose_name="O'zgartirish kiritilgan sana")
    
    def __str__(self): 
        return self.nom
    

    def get_absolute_url(self):
        return reverse('products:detail',
                       args=[self.sana.year,
                             self.sana.month,
                             self.sana.day,
                             self.pk])



    def avatar(self):
        return mark_safe('<img src="/media/%s" width="50" height="50" />' % (self.rasm) ) # default='<img src="/media/default_pictures/"'

    avatar.short_description = 'Mahsulot rasmi'

    # sana2 = sana.strftime('%Y/%m/%d, %H:%M:%S')

    # QR-code save funciation
    def save(self, *args, **kvargs):
        data = f"Turi: {self.tur.title()} \nNomi: {self.nom.title()} \nRangi: {self.rang} \
            \nNarxi: {self.narx}$ \nSoni: {self.son} dona \nIshlab chiqaruvchi: {self.kompania} \
            \nMuddati: {self.mudat} \nOg'irligi: {self.kg} kg \
            \nIshlab chiqarilgan vaqti: {self.sana}"

        data2 = f"\nUrl: {self.get_absolute_url}"
        qrcode_img = qrcode.make(data + data2)
        canvas = Image.new('RGB', (1000, 1000), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname = f'qr_code-{self.nom}.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kvargs)

        # # SHTRIX-code save funciation
        # EAN = shcode.get_shcode_class('ean13')
        # ean = EAN(f'qr_code-{self.nom}.png', writer=ImageWriter())
        # buffer1 = BytesIO()
        # ean.write(buffer1)
        # self.shcode.save('barcode.png', File(buffer1), save=False)
        # super().save(*args, **kvargs)


        # def save(self, *args, **kwargs):
        # EAN = barcode.get_barcode_class('ean13')
        # ean = EAN(f'{self.country_id}{self.manufacturer_id}{self.product_id}', writer=ImageWriter())
        # buffer = BytesIO()
        # ean.write(buffer)
        # self.barcode.save(f'{self.name}.png', File(buffer), save=False)
        # return super().save(*args, **kwargs)
        
class CostomUser(AbstractUser):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="customer")
    photo = models.ImageField(upload_to='Profile_pic/%Y/%m/%d/', verbose_name='Admin rasmi', null=True, blank=True)
    birth_date = models.DateField(auto_now=False, auto_now_add=False,  null=True, blank=True)
    position = models.CharField(max_length=100, null=True, blank=True)

    # REQUIRED_FIELDS = ['photo', 'birth_date', 'position']
    






    # def create(self, validated_data):
    #     user = User.objects.create(
    #         username=validated_data['username'],
    #         email=validated_data['email'],
    #         first_name=validated_data['first_name'],
    #         last_name=validated_data['last_name']
    #     )

    #     user.set_password(validated_data['password'])
    #     user.save()

    #     return user
        
