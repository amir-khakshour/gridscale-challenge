# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-12-28 09:45
from __future__ import unicode_literals

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_no', models.BigIntegerField(unique=True, verbose_name='Order number')),
                ('customer', models.PositiveIntegerField(verbose_name='Customer')),
                ('product', models.PositiveIntegerField(verbose_name='Product')),
                ('quantity', models.PositiveIntegerField(verbose_name='Quantity')),
                ('price_net', models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))], verbose_name='Net price')),
                ('price_gross', models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))], verbose_name='Gross price')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
                'ordering': ['quantity'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='order',
            unique_together=set([('customer', 'product', 'quantity')]),
        ),
    ]
