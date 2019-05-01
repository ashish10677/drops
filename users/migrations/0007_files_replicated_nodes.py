# Generated by Django 2.0.13 on 2019-05-01 08:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_files_nodes'),
    ]

    operations = [
        migrations.AddField(
            model_name='files',
            name='replicated_nodes',
            field=models.CharField(max_length=100, null=True, validators=[django.core.validators.int_list_validator]),
        ),
    ]
