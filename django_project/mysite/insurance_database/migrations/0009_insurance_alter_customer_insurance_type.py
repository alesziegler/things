# Generated by Django 4.2.1 on 2024-05-27 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insurance_database', '0008_alter_customer_insurance_type_delete_insurance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insurance_type', models.CharField(max_length=80, verbose_name='Druh pojisteni')),
            ],
        ),
        migrations.AlterField(
            model_name='customer',
            name='insurance_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='insurance_database.insurance'),
        ),
    ]
