# Generated by Django 3.1 on 2021-04-23 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hfcapp', '0004_delete_gellaryimg'),
    ]

    operations = [
        migrations.AddField(
            model_name='transformationimg',
            name='Category',
            field=models.CharField(default='', max_length=100),
        ),
    ]
