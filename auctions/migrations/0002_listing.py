# Generated by Django 5.0.1 on 2024-07-10 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('description', models.TextField()),
                ('starting_bid', models.DecimalField(decimal_places=4, max_digits=10)),
                ('url_image', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=30)),
            ],
        ),
    ]
