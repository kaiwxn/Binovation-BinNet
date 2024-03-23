from django.shortcuts import redirect, render

from .models import Bin, Measurement
from .forms import BinForm, MeasurementForm
from .calculate import calculateRanking
import datetime

def processDateTime(values, binId, date, time):
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


# Views for the application
def index(request):
    formBin = BinForm()
    formMeasurement = MeasurementForm()

    # Form for Bins
    if request.method == "POST":

        # Check which form was submitted
        # Bin form
        if "bin_submit" in request.POST:
            formBin = BinForm(request.POST)
            if formBin.is_valid():

                # Save data to table
                formBin.save()
                return redirect("index")
        else:
            formBin = BinForm()
        
        # Measurement form
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

                return redirect("index")
        else:
            formMeasurement = MeasurementForm()


    # Change Form object to list for displaying markers on map
    data = [[m.id, m.latitude, m.longitude] for m in Bin.objects.all()] 

    context = {
        "title": "Binnet - Home",
        "formBin": formBin,
        "formMeasurement": formMeasurement,
        "data": data,
    }
    return render(request, "binnetapp\index.html", context)


def detail(request):
    # Render all information about the bins 

    bins = Bin.objects.all()
    context = {
        "title": "Binnet - Detail",
        "bins": bins,
    }
    return render(request, "binnetapp\detail.html", context)