# Generated by Django 5.0.1 on 2024-01-17 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('year', models.IntegerField()),
            ],
            options={
                'db_table': 'cars',
            },
        ),
    ]