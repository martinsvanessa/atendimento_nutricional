# Generated by Django 2.0.10 on 2019-02-15 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atendimento', '0004_alimentos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alimentos',
            name='nome',
            field=models.CharField(max_length=120, verbose_name='Nome'),
        ),
    ]