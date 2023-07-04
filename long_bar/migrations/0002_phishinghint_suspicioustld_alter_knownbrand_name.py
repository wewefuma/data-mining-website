# Generated by Django 4.2.3 on 2023-07-04 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('long_bar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhishingHint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SuspiciousTLD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='knownbrand',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]