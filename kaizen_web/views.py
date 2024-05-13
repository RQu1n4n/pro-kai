from django.shortcuts import render, redirect
from django.http import HttpResponse
from serpapi import GoogleSearch
import json
from django.contrib.auth.decorators import login_required
# Create your views here.

# View for the home Page

# def home(request):
#     return render(request, 'kaizen_web/home.html', {})

@login_required
def home(request):


    params = {
        "api_key": "a88eda312e3c45af4a84767846dd8bb81b488550e47d93346b5c8525fdf77ce2",
        "engine": "google_scholar_profiles",
        "hl": "en",
        "mauthors": '"Jonathan V Taylar" OR "Menchie Miranda" OR "Cris Paulo Hate" OR "Roman M Richard" OR "Ryan Francisco" OR "Alonica Villanueva"  OR "Verlyn Nojor" OR "Cecilia A.Venal" '
        }

    search = GoogleSearch(params)
    results = search.get_dict()
    profiles = results["profiles"]
    context = {
        'all_profiles': profiles,
    }
    
    return render(request, 'kaizen_web/home.html', context)

def about(request):
    return render(request, 'kaizen_web/about.html', {})

def about(request):
    return render(request, 'kaizen_web/about.html', {'title': 'About'})

def error403(request):
    return render(request, 'kaizen_web/error403.html', {'title':'error403'})

# def contact(request):
#     return render(request, 'kaizen/contact.html', {'title': 'Contact'})
