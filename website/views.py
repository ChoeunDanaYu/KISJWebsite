from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Event, ImportantDates
from datetime import datetime, timedelta
from .form import EventForm, ImportantDatesForm
import boto3
client = boto3.client('s3')

# Create your views here.
def index(request):
    context = {'daytype': generate_daytype(),'weektype': generate_weektype()}
    impdate = ImportantDates.objects.latest('id').content
    context['impdate'] = impdate
    return render(request, 'website/main.html', context)

@login_required(login_url='common:login')
def important_dates_edit(request):
    if request.method == 'POST':
        form = ImportantDatesForm(request.POST)
        if form.is_valid():
            impdate = form.save(commit=False)
            impdate.create_date = datetime.now()
            impdate.save()
            return redirect('website:index')
    else:
        form = ImportantDatesForm(initial={'content': ImportantDates.objects.latest('id').content})
    context = {'form': form}
    return render(request, 'website/important_dates_form.html',context)


"""
Functions for rendering
"""

def generate_daytype():
    start_date = datetime(2022, 8, 15, 0, 0, 0, 0)
    now = datetime.now()
    if (now-start_date).days % 2 == 0:
        return "A"
    else:
        return "B"

def generate_weektype():
    start_date = datetime(2022, 8, 15, 0, 0, 0, 0)
    now = datetime.now()
    monday = now - timedelta(days=now.weekday())
    if (monday-start_date).days % 2 == 0:
        return "A"
    else:
        return "B"

def check_weekend():
    now = datetime.now()
    if now.weekday() > 4:
        return True
    else:
        return False

