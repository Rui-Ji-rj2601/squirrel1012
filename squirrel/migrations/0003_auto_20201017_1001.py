# Generated by Django 3.1.2 on 2020-10-17 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squirrel', '0002_auto_20201016_0458'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='squirrel',
            name='id',
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Unique_Squirrel_ID',
            field=models.CharField(help_text='unique squirrel id with location, date and time', max_length=20, primary_key=True, serialize=False),
        ),
    ]