from django.shortcuts import redirect, render

from .models import Bin, Measurement
from .forms import BinForm, MeasurementForm

# Views for the application

def index(request):

    # Form for Bins
    if request.method == "POST":
        formBin = BinForm(request.POST)
        if formBin.is_valid():

            # Save data to table
            formBin.save()
            return redirect("index")
    else:
        formBin = BinForm()
    

    # Form for Measurements
    if request.method == "POST":
        formMeasurement = MeasurementForm(request.POST)
        if formMeasurement.is_valid():

            # Process data 
            values = formMeasurement.data["values"].split(" ")
            
            # Create multiple entries of Measurement 
            Measurement.objects.bulk_create(
                [Measurement(value=float(value), bin=Bin(id = formMeasurement.data["bin"])) for value in values]
            )
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