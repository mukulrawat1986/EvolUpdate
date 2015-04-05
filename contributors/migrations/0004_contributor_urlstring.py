# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contributors', '0003_auto_20150214_1436'),
    ]

    operations = [
        migrations.AddField(
            model_name='contributor',
            name='urlstring',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
    ]
