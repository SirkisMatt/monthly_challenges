
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, response
from django.urls import reverse

monthly_challenges = {
    "january": "Eat no meat",
    "february": "Send it down a mtb track everyday",
    "march": "Learn Django for at least 1 hour everyday",
    "april": "Do some stuff",
    "may": "Do some more things",
    "june": "Eat some good food",
    "july": "Just be, yuh know man",
    "august": "Hike and look at blooming flowers",
    "september": "Smell all the new flowers",
    "october": "Go swimming in glacial rivers",
    "november": "Learn to surf",
    "december": "Take beautiful naps in the shade"
}

# Create your views here.
def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    return HttpResponse(f"<ul>{list_items}</ul>")


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid Month")
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month.capitalize()
        })
    except:
        return HttpResponseNotFound("<h1>This month is not supported</h1>")
    