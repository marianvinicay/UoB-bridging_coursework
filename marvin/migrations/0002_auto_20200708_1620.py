# Generated by Django 2.2.14 on 2020-07-08 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marvin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='link',
            field=models.CharField(max_length=200),
        ),
    ]
