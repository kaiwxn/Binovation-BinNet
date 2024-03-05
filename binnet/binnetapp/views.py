from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        "title": "Binnet - Home",
    }

    return render(request, "binnetapp\index.html", context)

def create(request):
    context = {
        "title": "Binnet - Create",
    }

    return render(request, "binnetapp\create.html", context)

def overview(request):
    context = {
        "title": "Binnet - Overview",
    }

    return render(request, "binnetapp\overview.html", context)

def detail(request):
    context = {
        "title": "Binnet - Detail",
    }

    return render(request, "binnetapp\detail.html", context)