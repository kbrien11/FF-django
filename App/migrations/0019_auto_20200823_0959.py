# Generated by Django 3.1 on 2020-08-23 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0018_runningback'),
    ]

    operations = [
        migrations.RenameField(
            model_name='runningback',
            old_name='Projected_OUTLOOK',
            new_name='projected_OUTLOOK',
        ),
        migrations.RenameField(
            model_name='runningback',
            old_name='Projected_fpts',
            new_name='projected_fpts',
        ),
        migrations.RenameField(
            model_name='runningback',
            old_name='Projected_rec_td',
            new_name='projected_rec_td',
        ),
        migrations.RenameField(
            model_name='runningback',
            old_name='Projected_rec_yards',
            new_name='projected_rec_yards',
        ),
        migrations.RenameField(
            model_name='runningback',
            old_name='Projected_receptions',
            new_name='projected_receptions',
        ),
        migrations.RenameField(
            model_name='runningback',
            old_name='Projected_rush_td',
            new_name='projected_rush_td',
        ),
        migrations.RenameField(
            model_name='runningback',
            old_name='Projected_rush_yards',
            new_name='projected_rush_yards',
        ),
    ]