# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-03 15:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0011_jacobsdata_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otherDegrees', models.TextField(blank=True, null=True)),
                ('spokenLanguages', models.TextField(blank=True, null=True)),
                ('programmingLanguages', models.TextField(blank=True, null=True)),
                ('areasOfInterest', models.TextField(blank=True, help_text='E.g. Start-Ups, Surfing, Big Data, Human Rights, etc', null=True)),
                ('alumniMentor', models.BooleanField(default=False, help_text='I would like to sign up as an alumni mentor')),
                ('member', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='alumni.Alumni')),
            ],
        ),
    ]