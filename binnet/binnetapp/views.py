from django.shortcuts import redirect, render
from .models import Bin
from .forms import BinForm, MeasurementForm

def index(request):

    # Form for Mülleimer
    formBin = BinForm()
    if request.method == "POST":
        formBin = BinForm(request.POST)
        if formBin.is_valid():
            formBin.save()
            return redirect("index")
    
    # Form for Messung
    formMeasurement = MeasurementForm()
    if request.method == "POST":
        formMeasurement = MeasurementForm(request.POST)
        if formMeasurement.is_valid():
            formMeasurement.save()
            return redirect("index")
    
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