# Generated by Django 4.0 on 2022-02-20 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField(max_length=500)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('is_public', models.BooleanField(default=True)),
            ],
        ),
    ]
