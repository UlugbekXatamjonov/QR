# Generated by Django 4.0.2 on 2022-03-12 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_user_birth_date_alter_user_created_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]