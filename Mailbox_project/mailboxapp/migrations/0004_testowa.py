# Generated by Django 2.1.3 on 2018-11-28 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailboxapp', '0003_address_person_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testowa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=123)),
                ('name1', models.CharField(max_length=123)),
            ],
        ),
    ]
