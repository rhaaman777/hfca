# Generated by Django 3.1 on 2021-04-26 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hfcapp', '0017_morepackages'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='couplePricea',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='orders',
            name='montha',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='orders',
            name='select',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AddField(
            model_name='orders',
            name='singlePricea',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='orders',
            name='phone',
            field=models.IntegerField(default=0),
        ),
    ]
