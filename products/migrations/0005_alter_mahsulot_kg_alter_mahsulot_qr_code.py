# Generated by Django 4.0.2 on 2022-02-24 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_mahsulot_qr_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mahsulot',
            name='kg',
            field=models.IntegerField(default=0, verbose_name="Mahsulot og'irligi(kg)"),
        ),
        migrations.AlterField(
            model_name='mahsulot',
            name='qr_code',
            field=models.ImageField(blank=True, null=True, upload_to='QR_codes/%Y/%m/%d/', verbose_name='Mahsulot QR codi'),
        ),
    ]