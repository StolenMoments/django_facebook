# Generated by Django 2.2.2 on 2019-07-09 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facebook', '0002_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='name',
            field=models.CharField(default='호날두', max_length=120),
        ),
    ]
