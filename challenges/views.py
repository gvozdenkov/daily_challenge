from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

monthly_challenges = {
    "january": "this is jan",
    "february": "this is feb",
    "march": "this is march",
    "april": "this is april",
}

def index(request):
    list_item = ""
    months = list(monthly_challenges.keys())
    
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month_challenge", args=[month])
        list_item += f"<li><a href='{month_path}'>{capitalized_month}</a></li>"
    
    response_data = f"<ul>{list_item}</ul>"
    return HttpResponse(response_data)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        string = f"here is {month} with challenge: {challenge_text}"
        return HttpResponse(string)
    except:
        return HttpResponseNotFound("month not found")


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("wrong month")
    else:
        redirect_month = months[month-1]
        redirect_path = reverse("month_challenge", args=[redirect_month])          # /challenge/<january> по имени возврщает path приложения (модуля), через args - передача аргумента <month>
        return HttpResponseRedirect(redirect_path)
