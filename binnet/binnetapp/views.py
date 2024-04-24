from django.shortcuts import redirect, render

from .models import Bin, Measurement, Ranking
from .forms import BinForm, MeasurementForm

from .calculate import *

import datetime


def processDateTime(values, binId, date, time) -> list[Measurement]:
    # Creates Measurement objects based on the input data from MeasurementForm

    measurements = []

    # Convert date and time to datetime objects for easier handling
    date_obj = datetime.datetime.strptime(date, "%Y-%m-%d")
    time_obj = datetime.datetime.strptime(time, "%H:%M")

    # Iterate over all measurement values
    for value in values:

        # Create Measurement object
        measurements.append(
            Measurement(value=float(value), 
                        bin=Bin(id = binId), 
                        measureTime = time_obj.time(), 
                        measureDate = date_obj.date()
                        ))
        
        # Add one hour to time
        time_obj += datetime.timedelta(hours = 1)

        # Add one day to date if time is 00:00
        if time_obj.hour == 0:
            date_obj += datetime.timedelta(days = 1)

    # Return list of measurement objects
    return measurements

def binFormHandler(request):
    # Handle form data for BinForm
    if "bin_submit" in request.POST:
        formBin = BinForm(request.POST)
        if formBin.is_valid():

            # Save data to table
            formBin.save()

            # Automatically create Ranking objects of new Bin for each weekday
            Ranking.objects.bulk_create([Ranking(bin = Bin.objects.last(), weekday = i) for i in range(1, 8)])

            return redirect("index")
    else:
        formBin = BinForm()

def measurementFormHandler(request):
    # Handle form data for MeasurementForm
    if "measurement_submit" in request.POST:
        formMeasurement = MeasurementForm(request.POST)
        if formMeasurement.is_valid():

            # Process data 
            values = formMeasurement.data["values"].split(" ")
            binId = formMeasurement.data["bin"]
            date = formMeasurement.data["startingDate"]
            time = formMeasurement.data["startingTime"]
            
            # Create multiple entries of Measurement
            measurements = processDateTime(values, binId, date, time)
            Measurement.objects.bulk_create(measurements)
            
            # Alter bin color based on calculation
            rankingData = calculateRanking(measurements)
            
            # Update Ranking objects with new data
            for key, value in rankingData.items():
                if len(value) != 0:
                    ranking = Ranking.objects.get(bin = binId, weekday = key)
                    ranking.color = value[1]
                    ranking.fillrate = value[0]
                    ranking.save()

            return redirect("index")
    else:
        formMeasurement = MeasurementForm()
    
# Views for the application
def index(request):
    formBin = BinForm()
    formMeasurement = MeasurementForm()

    # Form for Bins
    if request.method == "POST":

        # Check which form was submitted
        # 1. Bin form
        binFormHandler(request)
        
        # 2. Measurement form
        measurementFormHandler(request)


    # Change Form object to list for displaying markers on map
    binData = [[m.id, m.latitude, m.longitude, Ranking.objects.get(bin = m.id, weekday = datetime.datetime.now().weekday()).color] for m in Bin.objects.all()] 

    context = {
        "title": "Binnet - Home",
        "formBin": formBin,
        "formMeasurement": formMeasurement,
        "data": binData,
    }
    return render(request, "binnetapp\index.html", context)



def detail(request):
    # Render all information about the bins 

    bins = Bin.objects.all()

    # Format values of rankings for table: E.g. {1: [RED, ORANGE, GREEN, ...], 2: [GREEN, RED, ...}
    rankings = {ranking.bin: [(r.color, r.fillrate) for r in Ranking.objects.filter(bin = ranking.bin)] for ranking in Ranking.objects.all()}
    
    context = {
        "title": "Binnet - Detail",
        "bins": bins,
        "rankings": rankings,
    }
    return render(request, "binnetapp\detail.html", context)