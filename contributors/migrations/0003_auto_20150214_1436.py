# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contributors', '0002_thismonthinevolution_dateadded'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='authorinstitution',
            field=models.CharField(max_length=5000, verbose_name=b'Author Instution', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='mytitle',
            field=models.CharField(max_length=500, verbose_name=b'My Title', blank=True),
            preserve_default=True,
        ),
    ]
