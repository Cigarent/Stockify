# Generated by Django 2.1 on 2018-08-23 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_auto_20180823_2145'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('phone', models.TextField(verbose_name='phone')),
            ],
        ),
    ]
