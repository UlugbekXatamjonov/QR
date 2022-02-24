# Generated by Django 4.0.2 on 2022-02-23 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_mahsulot_narx_alter_mahsulot_kg_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mahsulot',
            name='yangilanish',
            field=models.DateTimeField(auto_now=True, verbose_name="O'zgartirish kiritilgan sana"),
        ),
        migrations.AlterField(
            model_name='mahsulot',
            name='narx',
            field=models.IntegerField(default=0, verbose_name='Mahsulot natxi($)'),
        ),
    ]
