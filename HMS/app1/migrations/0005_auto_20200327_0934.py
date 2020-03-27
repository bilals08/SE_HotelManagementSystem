# Generated by Django 3.0.3 on 2020-03-27 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_auto_20200327_0213'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='services',
            field=models.ManyToManyField(blank=True, null=True, to='app1.Services'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='desc',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]