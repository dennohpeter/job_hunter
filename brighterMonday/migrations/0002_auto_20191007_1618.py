# Generated by Django 2.2.5 on 2019-10-07 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brighterMonday', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='company_logo',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='company_logo_alt',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
