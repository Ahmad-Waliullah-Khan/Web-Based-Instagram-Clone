# Generated by Django 3.0.3 on 2020-03-07 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='caption',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
