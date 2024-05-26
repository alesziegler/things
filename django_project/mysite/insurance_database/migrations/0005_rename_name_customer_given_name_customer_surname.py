# Generated by Django 4.2.1 on 2024-05-26 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance_database', '0004_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='name',
            new_name='given_name',
        ),
        migrations.AddField(
            model_name='customer',
            name='surname',
            field=models.CharField(default='whatever', max_length=200),
            preserve_default=False,
        ),
    ]
