from django.shortcuts import render
from django.http import HttpResponse

def weekly_timetable(request,day):
    text = ""
    if day == "monday":
        text="work for python"
    elif day == "tuesday":
        text="work for data structure"
    elif day == "wednesday":
        text="work for big data"
    elif day == "thursday":
        text="work for Django"
    elif day == "friday":
        text="work for data analysis"
    elif day == "saturday":
        text="don't work for anything"
    return HttpResponse(text)
   