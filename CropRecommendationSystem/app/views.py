from django.shortcuts import render
import joblib as jb
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import os
import json

from app.models import Crop

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Create your views here.
from django.shortcuts import render

scaler: StandardScaler = jb.load(f"{BASE_DIR}/app/Models/scaler.joblib")
model: RandomForestClassifier = jb.load(f"{BASE_DIR}/app/Models/modelv1.joblib")


def home(request):
    return render(request, 'home.html', {})


def bylocation(request):
    return render(request, 'bylocation.html', {})


def services(request):
    return render(request, 'services.html')


def bysoil(request):
    return render(request, 'bysoil.html')


def bycrop(request):
    if request.method == "GET":
        return render(request, 'bycrop.html')
    if request.method == "POST":
        data = request.body
        data_scaled = scaler.transform(data["N"], data["P"], data["K"], data["temperature"], data["humidity"],
                                       data["ph"], data["rainfall"])
        prediction = model.predict_proba(data_scaled)
        output = [[model.classes_[index], round(value * 100, 2)] for index, value in enumerate(prediction[0])]
        output.sort(key=lambda x: x[1], reverse=True)
        return render(request, "bycrop.html", context={"data": output})
