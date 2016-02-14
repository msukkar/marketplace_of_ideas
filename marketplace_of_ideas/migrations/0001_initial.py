# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField()),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('amount', models.DecimalField(max_digits=10, decimal_places=2)),
                ('blog_post', models.ForeignKey(to='marketplace_of_ideas.BlogPost')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('followed_people', models.ManyToManyField(related_name='follows', to='marketplace_of_ideas.User')),
            ],
        ),
        migrations.AddField(
            model_name='transaction',
            name='payer',
            field=models.ForeignKey(related_name='payee', to='marketplace_of_ideas.User'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='receiver',
            field=models.ForeignKey(related_name='receivee', to='marketplace_of_ideas.User'),
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(to='marketplace_of_ideas.User'),
        ),
        migrations.AddField(
            model_name='comment',
            name='blog_post',
            field=models.ForeignKey(to='marketplace_of_ideas.BlogPost'),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='author',
            field=models.ForeignKey(to='marketplace_of_ideas.User'),
        ),
    ]
