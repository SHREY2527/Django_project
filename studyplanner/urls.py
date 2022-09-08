from django.urls import path
from . import views

urlpatterns=[
 path('<day>',views.weekly_timetable)
 ]