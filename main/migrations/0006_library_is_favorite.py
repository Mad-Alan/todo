# Generated by Django 3.1.3 on 2021-01-24 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210123_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='library',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]