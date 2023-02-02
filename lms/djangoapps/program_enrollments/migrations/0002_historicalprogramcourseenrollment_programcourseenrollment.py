# Generated by Django 1.11.20 on 2019-04-19 16:48


import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import opaque_keys.edx.django.models
import simple_history.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_squashed_0031_auto_20200317_1122'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('program_enrollments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalProgramCourseEnrollment',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('course_key', opaque_keys.edx.django.models.CourseKeyField(max_length=255)),
                ('status', models.CharField(choices=[('active', 'active'), ('inactive', 'inactive')], max_length=9)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('course_enrollment', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='student.CourseEnrollment')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('program_enrollment', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='program_enrollments.ProgramEnrollment')),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical program course enrollment',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='ProgramCourseEnrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('course_key', opaque_keys.edx.django.models.CourseKeyField(max_length=255)),
                ('status', models.CharField(choices=[('active', 'active'), ('inactive', 'inactive')], max_length=9)),
                ('course_enrollment', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='student.CourseEnrollment')),
                ('program_enrollment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='program_enrollments.ProgramEnrollment')),
            ],
        ),
    ]
