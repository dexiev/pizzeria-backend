# Generated by Django 5.0.6 on 2024-06-04 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='message',
        ),
    ]