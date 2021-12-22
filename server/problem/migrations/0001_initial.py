# Generated by Django 3.2.7 on 2021-12-22 06:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import problem.models
import utils.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contest', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProblemTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
            options={
                'db_table': 'problem_tag',
            },
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.TextField(db_index=True)),
                ('is_public', models.BooleanField(default=False)),
                ('title', models.TextField()),
                ('description', utils.models.RichTextField()),
                ('input_description', utils.models.RichTextField()),
                ('output_description', utils.models.RichTextField()),
                ('samples', models.JSONField()),
                ('test_case_id', models.TextField()),
                ('test_case_score', models.JSONField()),
                ('hint', utils.models.RichTextField(null=True)),
                ('languages', models.JSONField()),
                ('template', models.JSONField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('last_update_time', models.DateTimeField(null=True)),
                ('time_limit', models.IntegerField()),
                ('memory_limit', models.IntegerField()),
                ('io_mode', models.JSONField(default=problem.models._default_io_mode)),
                ('spj', models.BooleanField(default=False)),
                ('spj_language', models.TextField(null=True)),
                ('spj_code', models.TextField(null=True)),
                ('spj_version', models.TextField(null=True)),
                ('spj_compile_ok', models.BooleanField(default=False)),
                ('visible', models.BooleanField(default=False)),
                ('difficulty', models.TextField()),
                ('source', models.TextField(null=True)),
                ('total_score', models.IntegerField(default=0)),
                ('submission_number', models.BigIntegerField(default=0)),
                ('accepted_number', models.BigIntegerField(default=0)),
                ('statistic_info', models.JSONField(default=dict)),
                ('share_submission', models.BooleanField(default=False)),
                ('contest', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contest.contest')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(to='problem.ProblemTag')),
            ],
            options={
                'db_table': 'problem',
                'ordering': ('create_time',),
                'unique_together': {('_id', 'contest')},
            },
        ),
    ]
