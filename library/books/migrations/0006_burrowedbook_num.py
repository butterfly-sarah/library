# Generated by Django 3.2.7 on 2021-09-16 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_adminn'),
    ]

    operations = [
        migrations.AddField(
            model_name='burrowedbook',
            name='num',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
