# Generated by Django 2.2.2 on 2020-10-17 22:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tenders', '0003_client_computed_field'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'verbose_name': 'Клиент', 'verbose_name_plural': 'Клиенты'},
        ),
    ]
