# Generated by Django 3.1.1 on 2020-09-06 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covidtrace', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='citymun',
            name='cmclass',
        ),
        migrations.AlterField(
            model_name='barangay',
            name='blevel',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='barangay',
            name='estpop',
            field=models.IntegerField(null=True),
        ),
    ]
