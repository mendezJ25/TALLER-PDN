# Generated by Django 4.2.2 on 2023-06-18 02:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0004_medico'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='medico',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pacientes.medico'),
        ),
    ]
