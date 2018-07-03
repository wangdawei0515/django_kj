# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-01 12:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_ftest'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('c_id', models.AutoField(primary_key=True, serialize=False)),
                ('c_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('d_id', models.AutoField(primary_key=True, serialize=False)),
                ('d_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Stu_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('gender', models.BooleanField(default=1)),
                ('country', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('s_id', models.AutoField(primary_key=True, serialize=False)),
                ('s_name', models.CharField(max_length=30)),
                ('course', models.ManyToManyField(to='blog.Course')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Department')),
            ],
        ),
        migrations.AddField(
            model_name='stu_detail',
            name='s_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='blog.Student'),
        ),
    ]