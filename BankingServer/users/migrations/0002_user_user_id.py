# Generated by Django 4.2.2 on 2023-09-11 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_id',
            field=models.CharField(default='default_value_here', max_length=20, unique=True, verbose_name='아이디'),
        ),
    ]
