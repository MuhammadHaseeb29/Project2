# Generated by Django 4.1 on 2022-10-20 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDataForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.CharField(max_length=20)),
                ('eemail', models.CharField(max_length=20)),
                ('epassword1', models.CharField(max_length=100)),
                ('epassword2', models.CharField(max_length=20)),
            ],
        ),
    ]