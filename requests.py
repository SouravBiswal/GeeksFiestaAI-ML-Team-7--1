import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={
    'Temperature':15.6,
    'Pressure':1005.2,
    'Rain':0.59,
    'Wind_Speed':1.3,
    })

print(r.json())