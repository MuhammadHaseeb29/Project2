# Generated by Django 4.1 on 2022-10-31 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_userdataform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdataform',
            name='eemail',
            field=models.EmailField(max_length=254),
        ),
    ]
