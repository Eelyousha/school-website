# Generated by Django 4.0 on 2021-12-16 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NIR_UD', '0002_alter_academicperformance_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academicperformance',
            name='lesson_date',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='homework',
            name='deadline',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='students',
            name='student_id',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='teacher_id',
            field=models.CharField(max_length=11),
        ),
    ]
