# Generated by Django 4.0 on 2021-12-19 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NIR_UD', '0005_alter_academicperformance_student_mark_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecturehalls',
            name='lesson_index_number',
            field=models.IntegerField(max_length=2),
        ),
        migrations.AlterField(
            model_name='students',
            name='parent_phone_number',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='students',
            name='phone_number',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='phone_number',
            field=models.CharField(max_length=10),
        ),
    ]
