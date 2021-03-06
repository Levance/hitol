# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-05 22:13
from __future__ import unicode_literals

import DjangoUeditor.models
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField(default=1, verbose_name='\u7ae0\u8282\u53f7')),
                ('name', models.CharField(max_length=100, verbose_name='\u7ae0\u8282\u540d\u79f0')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u7ae0\u8282',
                'verbose_name_plural': '\u7ae0\u8282',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='\u8bfe\u7a0b\u540d')),
                ('category', models.CharField(choices=[('co', '\u516c\u9009\u8bfe'), ('li', '\u9650\u9009\u8bfe')], default='co', max_length=2, verbose_name='\u8bfe\u7a0b\u7c7b\u522b')),
                ('tag', models.CharField(default='', max_length=50, verbose_name='\u8bfe\u7a0b\u6807\u7b7e')),
                ('is_banner', models.BooleanField(default=False, verbose_name='\u662f\u5426\u8f6e\u64ad')),
                ('desc', models.CharField(max_length=300, verbose_name='\u8bfe\u7a0b\u63cf\u8ff0')),
                ('detail', DjangoUeditor.models.UEditorField(default='', verbose_name='\u8bfe\u7a0b\u8be6\u60c5')),
                ('degree', models.CharField(choices=[('ju', '\u521d\u7ea7'), ('mi', '\u4e2d\u7ea7'), ('hi', '\u9ad8\u7ea7')], default='ju', max_length=2, verbose_name='\u96be\u5ea6')),
                ('learn_times', models.IntegerField(default=0, verbose_name='\u5b66\u4e60\u65f6\u957f')),
                ('image', models.ImageField(default='course/default.png', upload_to='course/%Y/%m', verbose_name='\u5c01\u9762\u56fe')),
                ('need_know', models.CharField(default='', max_length=300, verbose_name='\u8bfe\u7a0b\u987b\u77e5')),
                ('teacher_tell', models.CharField(default='', max_length=300, verbose_name='\u6559\u5e08\u544a\u8bc9\u4f60')),
                ('learn_nums', models.IntegerField(default=0, verbose_name='\u5b66\u4e60\u4eba\u6570')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='\u6536\u85cf\u4eba\u6570')),
                ('click_nums', models.IntegerField(default=0, verbose_name='\u70b9\u51fb\u6570')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('school', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='school.School', verbose_name='\u8bfe\u7a0b\u9662\u7cfb')),
                ('teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='school.Teacher', verbose_name='\u6559\u5e08')),
            ],
            options={
                'verbose_name': '\u8bfe\u7a0b',
                'verbose_name_plural': '\u8bfe\u7a0b',
            },
        ),
        migrations.CreateModel(
            name='CourseNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(default='', verbose_name='\u8bfe\u7a0b\u516c\u544a')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u53d1\u5e03\u65f6\u95f4')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course', verbose_name='\u8bfe\u7a0b')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Teacher', verbose_name='\u6559\u5e08')),
            ],
            options={
                'verbose_name': '\u8bfe\u7a0b\u516c\u544a',
                'verbose_name_plural': '\u8bfe\u7a0b\u516c\u544a',
            },
        ),
        migrations.CreateModel(
            name='CourseResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='\u6587\u4ef6\u540d')),
                ('download', models.FileField(upload_to='course/resource/%Y/%m', verbose_name='\u8d44\u6e90\u6587\u4ef6')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course', verbose_name='\u8bfe\u7a0b')),
            ],
            options={
                'verbose_name': '\u8bfe\u7a0b\u8d44\u6e90',
                'verbose_name_plural': '\u8bfe\u7a0b\u8d44\u6e90',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField(default=1, verbose_name='\u8bfe\u65f6\u5e8f\u53f7')),
                ('name', models.CharField(max_length=100, verbose_name='\u8bfe\u65f6\u540d\u79f0')),
                ('url', models.CharField(default='', max_length=200, verbose_name='\u89c6\u9891\u94fe\u63a5')),
                ('video', models.FileField(default='', max_length=300, upload_to='course/video/%Y/%m', verbose_name='\u89c6\u9891\u6587\u4ef6')),
                ('time', models.IntegerField(default=0, verbose_name='\u89c6\u9891\u65f6\u957f')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Chapter', verbose_name='\u7ae0\u8282')),
            ],
            options={
                'verbose_name': '\u8bfe\u65f6',
                'verbose_name_plural': '\u8bfe\u65f6',
            },
        ),
        migrations.AddField(
            model_name='chapter',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course', verbose_name='\u8bfe\u7a0b'),
        ),
        migrations.CreateModel(
            name='BannerCourse',
            fields=[
            ],
            options={
                'verbose_name': '\u8f6e\u64ad\u8bfe\u7a0b',
                'proxy': True,
                'verbose_name_plural': '\u8f6e\u64ad\u8bfe\u7a0b',
            },
            bases=('course.course',),
        ),
    ]
