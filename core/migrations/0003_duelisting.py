# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-18 04:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_auto_20170517_0033'),
    ]

    operations = [
        migrations.CreateModel(
            name='DueListing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(blank=True, max_length=50)),
                ('debt_status', models.CharField(choices=[(b'full', b'Fully Paid'), (b'partial', b'Partially Paid'), (b'none', b'Not Paid')], max_length=50)),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='due_listing_customer', to=settings.AUTH_USER_MODEL)),
                ('debtor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='due_listing_debtor', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'tbl_due_listing',
            },
        ),
    ]
