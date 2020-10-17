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


        with open(file_path, encoding='utf-8') as fp:
            reader=csv.DictReader(fp)

            for item in reader:
                obj = Squirrel(
                    Latitude=item['X'],
                    Longitude=item['Y'],
                    Unique_Squirrel_ID=item['Unique Squirrel ID'],
                    Shift=item['Shift'],
                    Date=datetime.date(int(item['Date'][-4:]),int(item['Date'][:2]), int(item['Date'][2:4])),
                    Age=item['Age']
                )
                # obj=Squirrel()
                # obj.Latitude=item['X']
                # obj.Longitude=item['Y']
                # obj.Unique_Squirrel_ID=item['Unique Squirrel ID']
                # obj.Shift=item['Shift']
                # obj.Date=datetime.date(int(item['Date'][-4:]),int(item['Date'][:2]), int(item['Date'][2:4]))
                # obj.Age=item['Age']
                obj.save()
