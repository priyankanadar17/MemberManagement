# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-18 22:10
from __future__ import unicode_literals

import alumni.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0004_auto_20180114_1158'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentinformation',
            name='payment_type',
            field=alumni.fields.PaymentTypeField(choices=[('card', 'Credit or Debit Card'), ('sepa', 'SEPA bank transfer')], default='card', help_text='Payment Type', max_length=4),
        ),
    ]
