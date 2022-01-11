from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponseNotFound
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.

monthly_challenges = {
    "january": "this is jan",
    "february": "this is feb",
    "march": "Try something cool this month niga!",
    "april": "this is april",
    "may": "Make yourself in may yo!",
    "june": "relax man",
    "july": "july go to street",
    "augest": "something for august",
    "september": "Take a coffie",
    "october": "Yey, october here bro, cool!",
    "november": "uffff, winter is here",
    "december": "december is a cold month bro"

}

def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {           # определяет, что рендерить - темплейт index.html в подпапке challenges этого приложения (app)
        "months": months
    })         

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        indexlink = ""
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month": month,
            "indexlink": indexlink
        })
    except:
        raise Http404()         # ищет именно 404.html файл (файл хранится в директоии, которая указана в настройках проекта Templates

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("wrong month")
    else:
        redirect_month = months[month-1]
        redirect_path = reverse("month_challenge", args=[redirect_month])          # /challenge/<january> по имени возврщает path приложения (модуля), через args - передача аргумента <month>
        return HttpResponseRedirect(redirect_path)
