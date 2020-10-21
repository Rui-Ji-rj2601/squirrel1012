import csv

from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

from .models import Squirrel
from .forms import squirrelForm

def home(request):
    return render(request, 'squirrel/home.html')

def index(request):
    squirrels = Squirrel.objects.all()
    context = {
        'squirrels': squirrels,
    }
    return render(request, 'squirrel/index.html', context)

#def detail (request, squirrel_id)
def update(request, squirrel_id):
    obj = get_object_or_404(Squirrel, Unique_Squirrel_ID=squirrel_id)
    form = squirrelForm(request.POST or None, instance=obj)
    context = {'form': form}
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        return redirect('/sightings/')
    else:
        context = {'form': form}
        return render(request, 'squirrel/update.html',context)

def stats(request):
    total_sightings = Squirrel.objects.all().count()
    morning_sightings = Squirrel.objects.filter(Shift='AM').count()
    afternoon_sightings = Squirrel.objects.filter(Shift='PM').count()
    young_squirrel = Squirrel.objects.filter(Age='Juvenile').count()
    adult_squirrel = Squirrel.objects.filter(Age='Adult').count()
    context = {
        "total_sightings": total_sightings,
        'morning_sightings':morning_sightings,
        'afternoon_sightings': afternoon_sightings,
        'young_squirrel': young_squirrel,
        'adult_squirrel': adult_squirrel,
    }
    return render(request, 'squirrel/stats.html', context)

def map(request):

    sightings=Squirrel.objects.all()
    squirrel_show=[]
    for i in range (100):
        squirrel_show.append(sightings)
        sightings=squirrel_show
        context = {
            'sightings': sightings,
        }
    return render(request, 'squirrel/map.html', context)

def add(request):
    if request.method == 'POST':
        form = squirrelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/sightings/')

    else:
        form = squirrelForm()
        context = {'form': form,}
        return render(request, 'squirrel/add.html', context)

def export(request):
    response=HttpResponse(content_type='text/csv')
    writer=csv.writer(response)
    writer.writerow(['Latitude','Longitude','Unique_Squirrel_ID','Shift','Date','Age'])

    for squirrels in Squirrel.objects.all().values_list('Latitude','Longitude','Unique_Squirrel_ID','Shift','Date','Age'):
        writer.writerow(squirrels)
        response['Content-Disposition']='attachment;filename="Squirrels.csv"'
        return response






# Create your views here.
