# Generated by Django 4.2.1 on 2024-05-24 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance_database', '0002_alter_film_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('contact', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Film',
        ),
    ]
