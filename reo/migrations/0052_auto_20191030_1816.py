# Generated by Django 2.2.6 on 2019-10-30 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reo', '0051_copy_profile_seconds_to_fixed_float_fields'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profilemodel',
            name='parse_run_outputs_seconds',
        ),
        migrations.RemoveField(
            model_name='profilemodel',
            name='pre_setup_scenario_seconds',
        ),
        migrations.RemoveField(
            model_name='profilemodel',
            name='reopt_bau_seconds',
        ),
        migrations.RemoveField(
            model_name='profilemodel',
            name='reopt_seconds',
        ),
        migrations.RemoveField(
            model_name='profilemodel',
            name='setup_scenario_seconds',
        ),
    ]