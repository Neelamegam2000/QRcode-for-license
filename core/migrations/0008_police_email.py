# Generated by Django 3.2 on 2021-05-25 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_police_userallowed'),
    ]

    operations = [
        migrations.AddField(
            model_name='police',
            name='Email',
            field=models.EmailField(default='', max_length=254),
        ),
    ]
