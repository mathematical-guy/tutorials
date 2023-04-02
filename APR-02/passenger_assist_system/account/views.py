from django.shortcuts import render
from datetime import datetime
from dateutil import tz
from pytz import timezone



def login_page(request):
    now = datetime.now().astimezone(timezone('Asia/Kolkata'))
    hour = now.time().hour 
    
    if hour > 16:
        greet = "Good Evening"
    else:
        greet = "Good morning"

    mydata = {
        "name": "Mohit",
        "age": 25,  
        "print": False,
        "now": now,
        "greet": greet,
    }

    return render(request, "login.html", mydata)
    

