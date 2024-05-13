from django.shortcuts import render, redirect
from django.http import HttpResponse
from serpapi import GoogleSearch
import json
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
# Create your views here.

# View for the home Page

# def home(request):
#     return render(request, 'kaizen_web/home.html', {})

@login_required
class home(TemplateView):
     
    template_name = 'kaizen_web/home.html'

    def get(request, author_id):

        params = {
            "api_key": "425d6fb5ad378e6887055b328dad42d7ff166d2476aaefd7b2c6a814312ed22f",
            "author_id": author_id,
            "engine": "google_scholar_author",
            "hl": "en",
            "mauthors": '"Jonathan V Taylor" OR "Menchi Miranda" OR "Cris Paulo Hate" OR "Roman M Richard" OR "Ryan Francisco" OR "ALONICA VILLANUEVA"                    OR "Verlyn Nojor" OR "Ma.Cecilia A.Venal" '
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
