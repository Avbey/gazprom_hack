# Generated by Django 2.2.2 on 2020-10-17 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenders', '0002_auto_20201017_2039'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='computed_field',
            field=models.BooleanField(editable=False, null=True),
        ),
    ]
