# Generated by Django 4.0.5 on 2022-06-06 13:02

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
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('birt_date', models.DateTimeField()),
                ('GPA', models.DecimalField(decimal_places=1, max_digits=4)),
            ],
        ),
    ]
