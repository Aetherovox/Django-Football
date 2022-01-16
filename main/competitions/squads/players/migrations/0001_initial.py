# Generated by Django 3.2.6 on 2021-09-16 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('second_name', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=20)),
                ('chance_of_playing_next_round', models.IntegerField(default=0)),
                ('chance_of_playing_this_round', models.IntegerField(default=0)),
                ('code', models.PositiveBigIntegerField(default=0)),
                ('cost_change_event', models.IntegerField(default=0)),
                ('cost_change_event_fall', models.IntegerField(default=0)),
                ('cost_change_start', models.IntegerField(default=0)),
                ('cost_change_start_fall', models.IntegerField(default=0)),
                ('dreamteam_count', models.IntegerField()),
                ('element_type', models.IntegerField(default=0)),
                ('ep_next', models.CharField(max_length=5)),
                ('ep_this', models.CharField(max_length=5)),
                ('event_points', models.IntegerField(default=0)),
                ('form', models.CharField(max_length=5)),
                ('in_dreamteam', models.BooleanField()),
                ('news', models.CharField(max_length=400)),
                ('news_added', models.CharField(max_length=20)),
                ('now_cost', models.IntegerField(default=0)),
                ('photo', models.CharField(max_length=20)),
                ('points_per_game', models.CharField(max_length=5)),
                ('selected_by_percent', models.CharField(max_length=5)),
                ('special', models.BooleanField()),
                ('squad_number', models.IntegerField(default=0)),
                ('status', models.CharField(max_length=1)),
                ('team', models.IntegerField(default=0)),
                ('team_code', models.IntegerField(default=0)),
                ('total_points', models.IntegerField(default=0)),
                ('transfers_in', models.IntegerField(default=0)),
                ('transfers_in_event', models.IntegerField(default=0)),
                ('transfers_out', models.IntegerField(default=0)),
                ('transfers_out_event', models.IntegerField(default=0)),
                ('value_form', models.CharField(max_length=5)),
                ('value_season', models.CharField(max_length=5)),
                ('web_name', models.CharField(max_length=20)),
                ('minutes', models.IntegerField(default=0)),
                ('goals_scored', models.IntegerField(default=0)),
                ('assists', models.IntegerField(default=0)),
                ('clean_sheets', models.IntegerField(default=0)),
                ('goals_conceded', models.IntegerField(default=0)),
                ('own_goals', models.IntegerField(default=0)),
                ('penalties_saved', models.IntegerField(default=0)),
                ('penalties_missed', models.IntegerField(default=0)),
                ('yellow_cards', models.IntegerField(default=0)),
                ('red_cards', models.IntegerField(default=0)),
                ('saves', models.IntegerField(default=0)),
                ('bonus', models.IntegerField(default=0)),
                ('bps', models.IntegerField(default=0)),
                ('influence', models.CharField(max_length=5)),
                ('creativity', models.CharField(max_length=5)),
                ('threat', models.CharField(max_length=5)),
                ('ict_index', models.CharField(max_length=5)),
                ('influence_rank', models.IntegerField(default=0)),
                ('influence_rank_type', models.IntegerField(default=0)),
                ('creativity_rank', models.IntegerField(default=0)),
                ('creativity_rank_type', models.IntegerField(default=0)),
                ('threat_rank', models.IntegerField(default=0)),
                ('threat_rank_type', models.IntegerField(default=0)),
                ('ict_index_rank', models.IntegerField(default=0)),
                ('ict_index_rank_type', models.IntegerField(default=0)),
                ('corners_and_indirect_freekicks_order', models.IntegerField(default=0)),
                ('corners_and_indirect_freekicks_text', models.CharField(max_length=200)),
                ('direct_freekicks_order', models.IntegerField(default=0)),
                ('direct_freekicks_text', models.CharField(max_length=200)),
                ('penalties_order', models.IntegerField(default=0)),
                ('penalties_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PlayerHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season_name', models.CharField(max_length=20)),
                ('element_code', models.IntegerField()),
                ('start_cost', models.IntegerField(default=0)),
                ('end_cost', models.IntegerField(default=0)),
                ('total_points', models.IntegerField(default=0)),
                ('minutes', models.IntegerField(default=0)),
                ('goals_scored', models.IntegerField(default=0)),
                ('assists', models.IntegerField(default=0)),
                ('clean_sheets', models.IntegerField(default=0)),
                ('goals_conceded', models.IntegerField(default=0)),
                ('own_goals', models.IntegerField(default=0)),
                ('penalties_saved', models.IntegerField(default=0)),
                ('penalties_missed', models.IntegerField(default=0)),
                ('yellow_cards', models.IntegerField(default=0)),
                ('red_cards', models.IntegerField(default=0)),
                ('saves', models.IntegerField(default=0)),
                ('bonus', models.IntegerField(default=0)),
                ('bps', models.IntegerField(default=0)),
                ('influence', models.CharField(max_length=5)),
                ('creativity', models.CharField(max_length=5)),
                ('threat', models.CharField(max_length=5)),
                ('ict_index', models.CharField(max_length=5)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='histories', to='competitions_squads_players.player')),
            ],
        ),
    ]
