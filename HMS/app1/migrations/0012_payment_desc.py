# Generated by Django 3.0.3 on 2020-04-19 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_auto_20200419_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='desc',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
