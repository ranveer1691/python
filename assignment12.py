#ASSIGNMENT-12

#Question-1
import requests
data=requests.get("https://api.forismatic.com/api/1.0/method=getQuote&key=457653&format=xml&lang=en")
import json
lv=data.json()
print(lv)