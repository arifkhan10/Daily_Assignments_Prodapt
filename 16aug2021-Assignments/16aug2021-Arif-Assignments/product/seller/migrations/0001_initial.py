# Generated by Django 3.2.6 on 2021-08-16 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('scode', models.IntegerField()),
                ('sadd', models.CharField(max_length=25)),
                ('snum', models.IntegerField()),
            ],
        ),
    ]
