# Generated by Django 2.1.3 on 2018-11-27 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mailboxapp', '0002_remove_address_person_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='person_address',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='mailboxapp.Person'),
            preserve_default=False,
        ),
    ]