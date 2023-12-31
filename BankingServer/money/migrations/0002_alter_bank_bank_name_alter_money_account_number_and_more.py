# Generated by Django 4.2 on 2023-09-11 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('money', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank',
            name='bank_name',
            field=models.CharField(blank=True, default='', max_length=20, null=True, verbose_name='은행'),
        ),
        migrations.AlterField(
            model_name='money',
            name='account_number',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='계좌번호'),
        ),
        migrations.AlterField(
            model_name='money',
            name='bank_name',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='money.bank'),
        ),
    ]
