# Generated by Django 2.1.3 on 2018-11-29 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailboxapp', '0007_auto_20181129_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='flat_number',
            field=models.SmallIntegerField(blank=True),
        ),
    ]
