# Generated by Django 4.2.1 on 2023-06-22 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('pass1', models.CharField(max_length=30)),
                ('pass2', models.CharField(max_length=30)),
            ],
        ),
    ]