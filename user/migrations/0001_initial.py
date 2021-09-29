# Generated by Django 3.2.7 on 2021-09-27 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=1000)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('birthdate', models.DateField()),
                ('username', models.CharField(max_length=100)),
            ],
        ),
    ]
