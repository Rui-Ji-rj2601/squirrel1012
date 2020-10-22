import csv
import datetime
from django.core.management.base import BaseCommand, CommandError
from squirrel.models import Squirrel

class Command(BaseCommand):
    help='Get Squirrel Data'

    def add_arguments (self,parser):
        parser.add_argument('squirrel_data', help='file has squirrel data')

    def handle (self,*args,**options):
        file_path=options['squirrel_data']
        # msg=f'You are importing from {file }'

        try:
            with open(file_path, encoding='utf-8') as fp:
                reader=csv.DictReader(fp)

                for item in reader:
                    obj = Squirrel(
                        Latitude=item['Y'],
                        Longitude=item['X'],
                        Unique_Squirrel_ID=item['Unique Squirrel ID'],
                        Shift=item['Shift'],
                        Date=datetime.date(int(item['Date'][-4:]),int(item['Date'][:2]), int(item['Date'][2:4])),
                        Age=item['Age'],
                        # Primary_Fur_Color=item['Primary_Fur_Color'],
                        # Location=item['Location'],
                        # Specific_Location=item['Specific_Location'],
                        # Running=item['Running'].upper(),
                        # Chasing=item['Chasing'].upper(),
                        # Climbing=item['Climbing'].upper(),
                        # Eating=item['Eating'].upper(),
                        # Foraging=item['Foraging'].upper(),
                        # Other_Activities=item['Other_Activities'],
                        # Kuks=item['Kuks'].upper(),
                        # Quaas=item['Quaas'].upper(),
                        # Moans=item['Moans'].upper(),
                        # Tail_flags=item['Tail_flags'].upper(),
                        # Tail_twitches=item['Tail_twitches'].upper(),
                        # Approaches=item['Approaches'].upper(),
                        # Indifferent=item['Indifferent'].upper(),
                        # Runs_from=item['Runs_from'].upper(),
                    )
                    obj.save()
            msg = f'You are importing from {file_path}'
            self.stdout.write(self.style.SUCCESS(msg))
        except:
            raise CommandError('Import failed')
