# Generated by Django 2.2.11 on 2020-04-12 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0008_membershipinformation_desired_tier'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscriptioninformation',
            options={'ordering': ['-start']},
        ),
    ]