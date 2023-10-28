# Generated by Django 4.2.6 on 2023-10-28 05:40

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
                ('index_number', models.PositiveIntegerField()),
                ('reg_number', models.CharField(max_length=10)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('field_of_study', models.CharField(max_length=150)),
                ('gpa', models.FloatField()),
            ],
        ),
    ]