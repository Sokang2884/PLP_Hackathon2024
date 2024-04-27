from django.shortcuts import render
import requests

def home(request):
    return render(request, 'templates/index.html', {
        'facts': facts,
        'activity': activity,
        'dog': dog
    })
  
        # Make a request and get the response
  
r1=requests.get('https://uselessfacts.jsph.pl/random.json?language=en')
res1=r1.json()
facts=res1['text']

r2=requests.get('https://www.boredapi.com/api/activity')
res2=r2.json()
activity=res2['activity']

r3=requests.get('https://dog.ceo/api/breeds/image/random')
res3=r3.json()
dog=res3['message']
