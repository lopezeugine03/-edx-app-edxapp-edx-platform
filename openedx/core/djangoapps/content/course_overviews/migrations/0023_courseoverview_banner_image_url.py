# Generated by Django 2.2.16 on 2020-09-22 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_overviews', '0022_courseoverviewtab_is_hidden'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseoverview',
            name='banner_image_url',
            field=models.TextField(),
        ),
        migrations.AddField(
            model_name='historicalcourseoverview',
            name='banner_image_url',
            field=models.TextField(),
        ),
    ]