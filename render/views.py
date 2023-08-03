from django.shortcuts import render

# Create your views here.
def photo(req):
    return render(req, "index.html")
