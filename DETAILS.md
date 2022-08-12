# How does this work

## Language: Python

## Libraries

    + Dajngo : A python library for writhing backend web application.
    + Dajngo REST Framework: A python library used for writing REST APIs. For this project, was used to achieve Throtling( Request rate limit) or 3 request/minutes/user.
    + gunicorn : A python library for running wsgi application when deployed in the server environmnet.

## Host environment: Digital Ocean

## API endpoint: <https://whale-app-k2ovo.ondigitalocean.app/howold/>

## Request method: GET

## Query name: dob

## Query value: timestamp

## Summary of calculate_age function

The calculate_age function accept a timestamp parameter and return a json string in the below format:
{'timestamp': The inputed timestamp value from the request query in timestamp format
'year': The year avluated from the request query timestamp,
'month': The month avluated from the request query timestamp,
'day': The day avluated from the request query timestamp,
'age': The difference between the present  and the request timestamp value in years.
}

## Handled Exceptions

+ OverflowError and ValueError: Negative timestamp values, for this case, values that evalutes to less than the year 1970
+ KeyError: Null, empty query string and wrong data type for timestamp values
