# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=500)),
                ('pub_date', models.DateTimeField(verbose_name=b'Date Published')),
                ('reference', models.URLField(blank=True)),
                ('subject', models.CharField(max_length=300, blank=True)),
                ('organisms', models.CharField(max_length=300, blank=True)),
                ('datatypes', models.CharField(max_length=300, verbose_name=b'Data Types', blank=True)),
                ('journal', models.CharField(max_length=300, blank=True)),
                ('summary', models.CharField(max_length=5000, blank=True)),
                ('authors', models.CharField(max_length=5000, blank=True)),
                ('article', models.TextField(blank=True)),
                ('articlepic', models.ImageField(upload_to=b'ArticleImages', verbose_name=b'Article Picture', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('feedback', models.TextField(max_length=2000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=1000, blank=True)),
                ('rank', models.IntegerField(blank=True)),
                ('description', models.TextField()),
                ('picture', models.ImageField(upload_to=b'ContribImages', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HaveYouSeen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('theirtitle', models.CharField(max_length=300, verbose_name=b'Their Title', blank=True)),
                ('dateadded', models.DateTimeField(verbose_name=b'Date Added')),
                ('mytitle', models.CharField(max_length=300, verbose_name=b'My Title', blank=True)),
                ('reference', models.URLField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ThisMonthInEvolution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('headline', models.CharField(max_length=300)),
                ('summary', models.TextField()),
                ('thismonthpic', models.ImageField(upload_to=b'ThisMonth', verbose_name=b'This month picture', blank=True)),
                ('reference', models.URLField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='article',
            name='contrib',
            field=models.ForeignKey(blank=True, to='contributors.Contributor', null=True),
            preserve_default=True,
        ),
    ]
