import csv
import datetime
from django.core.management.base import BaseCommand, CommandError
from squirrel.models import Squirrel

class Command(BaseCommand):
    help='Export Existing Squirrel Data'

    def add_arguments (self,parser):
        parser.add_argument('export_to', help='exporting the most up-to-date squirrel data')

    def handle (self,*args,**options):
        try:
            file_path=options['export_to']
            with open(file_path, 'w') as fp:
                writer = csv.DictWriter(
                    fp,
                    delimiter = ',',
                    fieldnames = [
                        'Latitude',
                        'Longitude',
                        'Unique_Squirrel_ID',
                        'Shift',
                        'Date',
                        'Age',
                        'Primary_Fur_Color',
                        'Location',
                        'Specific_Location',
                        'Running',
                        'Chasing',
                        'Climbing',
                        'Eating',
                        'Foraging',
                        'Other_Activities',
                        'Kuks',
                        'Quaas',
                        'Moans',
                        'Tail_flags',
                        'Tail_twitches',
                        'Approaches',
                        'Indifferent',
                        'Runs_from',
                    ]
                )
                writer.writeheader()

                for row in Squirrel.objects.all():
                    if row.Date:
                        str_date = row.Date.strftime('%Y%m%d')
                    writer.writerow({
                        'Latitude': row.Latitude,
                        'Longitude': row.Longitude,
                        'Unique_Squirrel_ID': row.Unique_Squirrel_ID,
                        'Shift': row.Shift,
                        'Date': row.Date,
                        'Age': row.Age,
                        'Primary_Fur_Color': row.Primary_Fur_Color,
                        'Location': row.Location,
                        'Specific_Location': row.Specific_Location,
                        'Running': row.Running,
                        'Chasing': row.Chasing,
                        'Climbing': row.Climbing,
                        'Eating': row.Eating,
                        'Foraging': row.Foraging,
                        'Other_Activities': row.Other_Activities,
                        'Kuks': row.Kuks,
                        'Quaas': row.Quaas,
                        'Moans': row.Moans,
                        'Tail_flags': row.Tail_flags,
                        'Tail_twitches': row.Tail_twitches,
                        'Approaches': row.Approaches,
                        'Indifferent': row.Indifferent,
                        'Runs_from': row.Runs_from,
                    })
            msg = f'You have export the Squirrel Data to {file_path}'
            self.stdout.write(self.style.SUCCESS(msg))
        except:
            raise CommandError('Export failed')
