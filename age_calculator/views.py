# from django.shortcuts import render

# Create your views here.
from datetime import datetime, timedelta, date
from rest_framework.response import Response
from rest_framework.decorators import api_view, throttle_classes
from rest_framework.throttling import AnonRateThrottle
from rest_framework import status


@api_view(['GET'])
@throttle_classes([AnonRateThrottle])
def calculate_age(request):
    try:
        dob = float(request.GET['dob'])
    except (KeyError,  ValueError) as e:
        content = {'error': 'bad dob query'}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)
    try:
        date_time = datetime.fromtimestamp(dob)
    except (OverflowError, ValueError) as e:
        content = {'error': 'Wrong dob value'}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)

    year = date_time.year
    month = date_time.month
    day = date_time.day
    dob = date(year, month, day)
    age = datetime.now().date() - dob
    age_years = age // timedelta(days=365)
    content = {'timestamp': date_time, 'year': year,
               'month': month, 'day': day, 'age': age_years}
    return Response(content, status.HTTP_200_OK)
