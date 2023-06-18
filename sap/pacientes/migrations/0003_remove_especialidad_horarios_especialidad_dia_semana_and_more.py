# Generated by Django 4.2.2 on 2023-06-18 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0002_especialidad_paciente_especialidad'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='especialidad',
            name='horarios',
        ),
        migrations.AddField(
            model_name='especialidad',
            name='dia_semana',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='especialidad',
            name='hora_fin',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='especialidad',
            name='hora_inicio',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='especialidad',
            name='nombre',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
