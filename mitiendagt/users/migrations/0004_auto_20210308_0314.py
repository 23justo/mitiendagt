# Generated by Django 3.1.7 on 2021-03-08 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0002_auto_20210308_0313'),
        ('users', '0003_profile_stores'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='stores',
            field=models.ManyToManyField(null=True, to='stores.Store'),
        ),
    ]
