from django.shortcuts import render
from dashboard.models import Collection

# Create your views here.


def feeds(request):
    all_coll = Collection.objects.all()
    return render(request, 'feeds/feeds.html', {
        'all_coll' : all_coll,
    })