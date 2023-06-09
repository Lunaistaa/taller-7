# Generated by Django 4.2.1 on 2023-05-28 23:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nombre_de_la_aplicacion', '0002_rename_descripción_tipodocumento_descripción_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.RenameField(
            model_name='tipodocumento',
            old_name='descripción',
            new_name='descripcion',
        ),
        migrations.AlterField(
            model_name='tipodocumento',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('documento', models.CharField(max_length=100)),
                ('fechanacimiento', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=20)),
                ('usuario', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('idtipodocumento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nombre_de_la_aplicacion.tipodocumento')),
                ('lugarresidencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nombre_de_la_aplicacion.ciudad')),
            ],
        ),
    ]
