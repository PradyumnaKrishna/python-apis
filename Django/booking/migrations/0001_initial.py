# Generated by Django 3.1.5 on 2021-01-14 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('slot', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
