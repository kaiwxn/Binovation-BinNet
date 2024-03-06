from django.shortcuts import redirect, render
from .models import Mülleimer
from .forms import MülleimerForm

# Create your views here.
def index(request):

    form = MülleimerForm()

    if request.method == "POST":
        form = MülleimerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    
    data = [[m.id, m.lat, m.lon] for m in Mülleimer.objects.all()] 

    context = {
        "title": "Binnet - Home",
        "form": form,
        "data": data,
    }
    
    return render(request, "binnetapp\index.html", context)

def detail(request):

    mülleimer = Mülleimer.objects.all()
    context = {
        "mülleimer": mülleimer,
        "title": "Binnet - Detail",
    }

    return render(request, "binnetapp\detail.html", context)