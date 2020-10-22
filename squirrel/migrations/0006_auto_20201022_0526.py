# Generated by Django 3.1.2 on 2020-10-22 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squirrel', '0005_auto_20201018_0403'),
    ]

    operations = [
        migrations.AddField(
            model_name='squirrel',
            name='Approaches',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='Chasing',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='Climbing',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='Eating',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='Foraging',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='Indifferent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='Kuks',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='Location',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='Moans',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='Other_Activities',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='Primary_Fur_Color',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='Quaas',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='Running',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='Runs_from',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='Specific_Location',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='Tail_flags',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='Tail_twitches',
            field=models.BooleanField(default=False),
        ),
    ]
