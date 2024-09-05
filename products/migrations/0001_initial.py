# Generated by Django 3.2.25 on 2024-09-05 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.FloatField()),
                ('image_url', models.CharField(blank=True, max_length=255, null=True)),
                ('stock', models.IntegerField(default=0)),
            ],
        ),
    ]
