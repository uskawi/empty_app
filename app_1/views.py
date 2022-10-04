from django.shortcuts import render

# Create your views here.


from django.shortcuts import render


def index(request):
    """ A view to return the index page """

    return render(request, 'app_1/index.html')
