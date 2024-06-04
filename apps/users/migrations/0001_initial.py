# Generated by Django 5.0.6 on 2024-05-23 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(db_index=True, max_length=20, verbose_name='username')),
                ('email', models.EmailField(db_index=True, max_length=200, verbose_name='email')),
                ('password', models.CharField(db_index=True, max_length=20, verbose_name='password')),
                ('token', models.CharField(db_index=True, max_length=300, verbose_name='token')),
                ('token_expires_at', models.DateTimeField(blank=True, null=True, verbose_name='token expires at')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]