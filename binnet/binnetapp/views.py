from django.shortcuts import redirect, render
from .models import Bin, Measurement
from .forms import BinForm, MeasurementForm

def index(request):

    # Form for Mülleimer
    if request.method == "POST":
        formBin = BinForm(request.POST)
        if formBin.is_valid():
            formBin.save()
            return redirect("index")
    else:
        formBin = BinForm()
    
    # Form for Messung
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
    
    # Change Form object to list 
    data = [[m.id, m.lat, m.lon] for m in Bin.objects.all()] 

    context = {
        "title": "Binnet - Home",
        "formBin": formBin,
        "formMeasurement": formMeasurement,
        "data": data,
    }
    
    return render(request, "binnetapp\index.html", context)


def detail(request):

    bins = Bin.objects.all()
    context = {
        "bins": bins,
        "title": "Binnet - Detail",
    }

    return render(request, "binnetapp\detail.html", context)