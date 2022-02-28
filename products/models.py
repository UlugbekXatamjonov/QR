from django.db import models
from django.utils.html import mark_safe
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
from django.urls import reverse
from datetime import datetime

 
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
    qr_code= models.ImageField(upload_to='QR_codes/%Y/%m/%d/', verbose_name='Mahsulot QR codi', null=True, blank=True)
    sana = models.DateTimeField(auto_now_add=True, verbose_name='Ishlab chiqarilgan sana') # Ishlab chiqarilgan vaqti
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
    
	