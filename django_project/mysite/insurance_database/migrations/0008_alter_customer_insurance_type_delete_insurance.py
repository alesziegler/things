# Generated by Django 4.2.1 on 2024-05-27 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance_database', '0007_customer_insurance_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='insurance_type',
            field=models.CharField(choices=[(1, 'Jaderny vybuch'), (2, 'Zombie apokalypsa'), (3, 'Vzpoura robotu'), (4, 'Sovetsky svaz')], default=1, max_length=50),
        ),
        migrations.DeleteModel(
            name='Insurance',
        ),
    ]
