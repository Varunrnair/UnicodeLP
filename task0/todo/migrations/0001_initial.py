# Generated by Django 4.1.1 on 2022-10-23 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('desc', models.TextField(default='', max_length=200)),
                ('Complete', models.BooleanField(default=False)),
            ],
        ),
    ]
