# Generated by Django 3.2.6 on 2021-10-06 23:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('competitions_fixtures', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teamscore',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competitions_fixtures.team'),
        ),
    ]
