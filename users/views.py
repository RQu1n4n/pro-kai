from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import authenticate, login, logout
from serpapi import GoogleSearch
import json
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.views.generic import TemplateView, ListView, View


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
class author_profile(View):

    template_name = 'users/profile.html'

    def get(self, request, author_id):

        params = {
          "api_key": "425d6fb5ad378e6887055b328dad42d7ff166d2476aaefd7b2c6a814312ed22f",
          "author_id": author_id,
          "engine": "google_scholar_author",
          "hl": "en",
        
        }

        search = GoogleSearch(params) # Assuming GoogleSearch is your model to interact with the API
        results = search.get_dict()
        author = results.get("author", {})
        articles = results.get("articles", [{}])

        return render (request, self.template_name, {'author': author,'articles': articles} )
    
class ProfileDetailView(View):
    
    template_name = 'users/profile.html'

    def get(self, request, author_id):
        params = {
            "engine": "google_scholar_author",
            "author_id": author_id,
            "api_key": "425d6fb5ad378e6887055b328dad42d7ff166d2476aaefd7b2c6a814312ed22f"
        }
        search = GoogleSearch(params)  # Assuming GoogleSearch is your model to interact with the API
        results = search.get_dict()
        author = results.get("author", {})
        articles = results.get("articles", [{}])
        
        return render(request, self.template_name, {'author': author, 'articles': articles})

def user_login(request):
    if request.method == 'POST':
        form = UserUpdateForm(request, data=request.POST)
        print('this is authenticated')
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('home')
        else:
            return render(request, 'kaizen_web/error403.html', {'title': 'error403'})
    else:
        form = UserUpdateForm()
        return render(request, 'users/login.html', {'form': form})

def error403(request):
    return render(request, "core/error403.html", {'title':'error403'})

def user_logout(request):
    logout(request)
    return redirect('login')

def profile(request):
    
    if request.method == "POST":
        results = request.POST['results']
        user_profile = request.POST['profile']
        response_data = {'status':'success'}
      
    return render(request, 'users/profile.html')

#     params = {
#     "api_key": "a88eda312e3c45af4a84767846dd8bb81b488550e47d93346b5c8525fdf77ce2",
#     "engine": "google_scholar_profiles",
#     "hl": "en",
#     "mauthors":  "richard" ,
#     #"mauthors":  request.user.profile ,
#     #"mauthors":  "*"
# }

    # search = GoogleSearch(params)
    # results = search.get_dict()
    # profiles_json =json.dumps(results["profiles"])
    # profiles = json.loads(profiles_json)

    #    return render(request, self.template_name, {'profiles': profiles})



        # print("richard is here")
    # if request.method == 'POST':
    #     u_form = UserUpdateForm(request.POST, instance=request.user)
    #     p_form = ProfileUpdateForm(request.POST,
    #                                request.FILES,
    #                                instance=request.user.profile)
    #     if u_form.is_valid() and p_form.is_valid():
    #         u_form.save()
    #         p_form.save()
    #         messages.success(request, f'Your account has been updated!')
    #         return redirect('profile')
        
    
    # else:
    #     u_form = UserUpdateForm(instance=request.user)
    #     p_form = ProfileUpdateForm(instance=request.user.profile)
    #       qH7tacgAAAAJ request.user.username
    
#     params = {
#     "api_key": "a88eda312e3c45af4a84767846dd8bb81b488550e47d93346b5c8525fdf77ce2",
#     "engine": "google_scholar_profiles",
#     # "mauthors": "jonathan",
#     "mauthors":  request.user.first_name + " " + request.user.last_name
# }
   # print(request.user.first_name + " " + request.user.last_name)
   # print(request.user.last_name)
    # print(request.user.profile)

    # profiles_json =json.dumps(results["profiles"])
    # profiles = json.loads(profiles_json)
    #print("obet")

    #    return render(request, self.template_name, {'profiles': profiles})

            # 'u_form': u_form,
        # 'p_form': p_form,
            # return render (request, self.template_name, {'author': author, 'articles': articles})

            # class  author_profile(request):
#     def get(self, request, author_id):
# params = {
#             "api_key": "425d6fb5ad378e6887055b328dad42d7ff166d2476aaefd7b2c6a814312ed22f",
#             "author_id": author_id,
#             "engine": "google_scholar_author",
#             "hl": "en",
#         }

#         search = GoogleSearch(params) # Assuming GoogleSearch is your model to interact with the API
#         results = search.get_dict()
#         author = results.get("author", {})
#         articles = results.get("articles", [{}])

#     context = {
#     'author': author, 
#     'articles': articles,
#     }
#         return render(request, 'users/profile.html', context)