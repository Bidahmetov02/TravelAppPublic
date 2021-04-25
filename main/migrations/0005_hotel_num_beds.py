# Generated by Django 3.2 on 2021-04-25 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210424_2313'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='num_beds',
            field=models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default=1, verbose_name='For how many people: '),
        ),
    ]
