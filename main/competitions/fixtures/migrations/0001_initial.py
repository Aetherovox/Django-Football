# Generated by Django 3.2.6 on 2021-10-06 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('competitions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fixture',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('venue', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MatchStatus',
            fields=[
                ('short', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('full', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(blank=True, max_length=200, null=True)),
                ('short_name', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TeamScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('score', models.IntegerField(blank=True, null=True)),
                ('half_time_score', models.IntegerField(blank=True, null=True)),
                ('team', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='competitions_fixtures.team')),
            ],
        ),
        migrations.CreateModel(
            name='Prediction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score_a', models.PositiveSmallIntegerField()),
                ('score_h', models.PositiveSmallIntegerField()),
                ('teamwin', models.IntegerField(choices=[('DRAW', 0), ('HOME', 1), ('AWAY', 2)])),
                ('fixture', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='predictions', to='competitions_fixtures.fixture')),
                ('participant', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='predictions', to='competitions.participant')),
            ],
        ),
        migrations.AddField(
            model_name='fixture',
            name='away_team',
            field=models.ForeignKey(default=999, on_delete=django.db.models.deletion.CASCADE, related_name='fixtures_away', to='competitions_fixtures.teamscore'),
        ),
        migrations.AddField(
            model_name='fixture',
            name='home_team',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='fixtures_home', to='competitions_fixtures.teamscore'),
        ),
        migrations.AddField(
            model_name='fixture',
            name='league',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fixtures', to='competitions.competition'),
        ),
        migrations.AddField(
            model_name='fixture',
            name='status',
            field=models.ForeignKey(db_column='status_id', default='FT', on_delete=django.db.models.deletion.PROTECT, related_name='statuses', to='competitions_fixtures.matchstatus'),
        ),
    ]
