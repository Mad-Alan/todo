# Generated by Django 3.1.3 on 2021-01-23 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210123_1701'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='library',
            name='date',
        ),
        migrations.AlterField(
            model_name='library',
            name='author',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='library',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='library',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='library',
            name='year',
            field=models.DateField(),
        ),
    ]
