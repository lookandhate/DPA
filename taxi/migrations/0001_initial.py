# Generated by Django 4.2.1 on 2023-06-06 17:28

import common.model_fields
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('departure_longitude', common.model_fields.LongitudeField(decimal_places=15, max_digits=18, validators=[django.core.validators.MinValueValidator(-180), django.core.validators.MaxValueValidator(180)], verbose_name='Долгота старта')),
                ('departure_latitude', common.model_fields.LatitudeField(decimal_places=15, max_digits=18, validators=[django.core.validators.MinValueValidator(-90), django.core.validators.MaxValueValidator(90)], verbose_name='Широта старта')),
                ('arriving_longitude', common.model_fields.LongitudeField(decimal_places=15, max_digits=18, validators=[django.core.validators.MinValueValidator(-180), django.core.validators.MaxValueValidator(180)], verbose_name='Долгота точки назначения')),
                ('arriving_latitude', common.model_fields.LatitudeField(decimal_places=15, max_digits=18, validators=[django.core.validators.MinValueValidator(-90), django.core.validators.MaxValueValidator(90)], verbose_name='Широта точки назначения')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Цена поездки')),
                ('time_in_road', models.IntegerField(verbose_name='Время в пути')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('discount', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='payment.discount', verbose_name='Скидка использованная в поездке')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='driver_rides', to=settings.AUTH_USER_MODEL)),
                ('payment_method', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='payment_method_rides', to='payment.paymentmethod')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
