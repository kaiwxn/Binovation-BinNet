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
    
    context = {
        "title": "Binnet - Home",
        "form": form,
    }
    
    return render(request, "binnetapp\index.html", context)

def detail(request):

    mülleimer = Mülleimer.objects.all()
    context = {
        "mülleimer": mülleimer,
        "title": "Binnet - Detail",
    }

    return render(request, "binnetapp\detail.html", context)