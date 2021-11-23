# Generated by Django 3.2.9 on 2021-11-16 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nexfac_core_api', '0005_alter_task_task_inputs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='users',
            field=models.ManyToManyField(null=True, to='nexfac_core_api.User'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='users',
            field=models.ManyToManyField(null=True, to='nexfac_core_api.User'),
        ),
        migrations.AlterField(
            model_name='task',
            name='areas',
            field=models.ManyToManyField(null=True, to='nexfac_core_api.Area'),
        ),
        migrations.AlterField(
            model_name='task',
            name='assets',
            field=models.ManyToManyField(null=True, to='nexfac_core_api.Asset'),
        ),
    ]