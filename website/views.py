from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Event, ImportantDates
from datetime import datetime, timedelta
import boto3
client = boto3.client('s3',aws_access_key_id='AKIA6CHE6EDK67W6A24K',aws_secret_access_key='h61XsC3Nndjny7Cq4eIaTHdQHWfrARXvOiul4dCg',region_name='ap-northeast-2')

# Create your views here.
def index(request):
    context = {'daytype': generate_daytype(),'weektype': generate_weektype()}
    return render(request, 'website/main.html', context)


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

