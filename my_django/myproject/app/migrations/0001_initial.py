# Generated by Django 4.0.1 on 2022-01-06 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=50, unique=True)),
                ('passWord', models.CharField(max_length=100)),
                ('createdDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
