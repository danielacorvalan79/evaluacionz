# Generated by Django 3.1.5 on 2021-01-29 01:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('run', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateField()),
                ('edad', models.IntegerField()),
                ('direccion', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100, null=True)),
                ('telefono', models.IntegerField()),
                ('patologias', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_indicacion', models.DateField()),
                ('nombre', models.CharField(max_length=50)),
                ('dosis', models.CharField(max_length=50)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='ExamenPerfill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('colesterol_total', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('trigliceridos', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='ExamenPerfilb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('glucosa', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('bilirrubina_total', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='ExamenHemograma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('hematocrito', models.DecimalField(decimal_places=2, max_digits=5)),
                ('hemoglobina', models.DecimalField(decimal_places=2, max_digits=5)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.paciente')),
            ],
        ),
    ]
