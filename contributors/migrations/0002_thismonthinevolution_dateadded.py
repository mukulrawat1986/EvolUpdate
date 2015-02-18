# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contributors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='thismonthinevolution',
            name='dateadded',
            field=models.DateTimeField(null=True, verbose_name=b'Date Added', blank=True),
            preserve_default=True,
        ),
    ]
