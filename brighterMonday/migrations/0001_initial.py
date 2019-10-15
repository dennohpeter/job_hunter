# Generated by Django 2.2.5 on 2019-10-15 15:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('job_function', models.CharField(max_length=100, null=True)),
                ('company_logo', models.URLField(null=True)),
                ('company_logo_alt', models.CharField(max_length=50, null=True)),
                ('category', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('employer', models.CharField(max_length=50)),
                ('salary', models.CharField(max_length=50)),
                ('job_type', models.CharField(ma    x_length=50)),
                ('first_seen', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('summary_title', models.CharField(max_length=100, null=True)),
                ('summary', models.TextField(null=True)),
                ('description_title', models.CharField(max_length=100, null=True)),
                ('requirements', models.TextField(null=True)),
            ],
        ),
    ]
