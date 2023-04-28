from django.shortcuts import render
import joblib as jb
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import os
import json
import pandas as pd
from django.conf import settings

from app.models import Crop

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Create your views here.
from django.shortcuts import render

scaler: StandardScaler = jb.load(f"{BASE_DIR}/app/Models/scaler.joblib")
model: RandomForestClassifier = jb.load(f"{BASE_DIR}/app/Models/modelv1.joblib")
by_soil_data = pd.read_csv(f"{BASE_DIR}/app/Data/by_soil.csv")

f = open(f'{BASE_DIR}/app/Data/locations.json')

# images_loc =

by_location_data = json.load(f)


def cast_round(value):
    return round(float(value),2)

def home(request):
    return render(request, 'home.html', {})


def bylocation(request):
    if request.method == "GET":
        return render(request, 'bylocation.html')
    if request.method == "POST":
        crop = request.POST["crop"]
        print("do something")
        data = by_location_data[crop]
        return render(request, 'bylocation.html', {"location_data":data})


def services(request):
    return render(request, 'services.html')


def bysoil(request):
    if request.method == "GET":
        return render(request, 'bysoil.html')
    if request.method == "POST":
        crop = request.POST["crop"]
        print("do something")
        data = by_soil_data[by_soil_data["label"] == crop]
        complete_data = {
            "N": cast_round(data["N"]),
            "P": cast_round(data["P"]),
            "K": cast_round(data["K"]),
            "ph": cast_round(data["ph"]),
            "temperature": cast_round(data["temperature"]),
            "humidity": cast_round(data["humidity"]),
            "rainfall": cast_round(data["rainfall"]),

        }
        print(complete_data)
        return render(request, 'bysoil.html', {"soil_data":complete_data})


def bycrop(request):
    if request.method == "GET":
        print(BASE_DIR)
        return render(request, 'bycrop.html')
    if request.method == "POST":
        data = request.POST
        print(data)
        data_scaled = scaler.transform([[data["N"], data["P"], data["K"], data["temperature"], data["humidity"],
                                       data["ph"], data["rainfall"]]])
        prediction = model.predict_proba(data_scaled)
        output = [[model.classes_[index], round(value * 100, 2)] for index, value in enumerate(prediction[0])]
        output.sort(key=lambda x: x[1], reverse=True)
        print(output)
        output_list=[]
        for out in output:
            if out[1] > 0:
                output_dict = {"plant":out[0],"percent":out[1],"link":f"{settings.STATIC_URL}Images/{out[0]}.jpg"}
                output_list.append(output_dict)
        print(output_list)
        return render(request, "bycrop.html", {"output":output_list})
