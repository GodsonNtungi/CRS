import joblib as jb
import streamlit as st
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import sklearn

scaler = jb.load("scaler.joblib")
model: RandomForestClassifier = jb.load("modelv1.joblib")

st.header("Crop Recommender Model")

form = st.form(key="form1")
N = form.slider(label="Amount of Nitrogen", min_value=0, max_value=300, step=1, value=150)
K = form.slider(label="Amount of Potassium", min_value=0, max_value=300, step=1, value=150)
P = form.slider(label="Amount of Phosphorus", min_value=0, max_value=300, step=1, value=150)
temperature = form.slider(label="Temperature (°C)", min_value=0, max_value=50, step=1, value=25)
humidity = form.slider(label="Humidity", min_value=0, max_value=300, step=1, value=150)
ph = form.slider(label="Ph", min_value=0, max_value=14, step=1, value=7)
rainfall = form.slider(label="Amount of Rainfall", min_value=0, max_value=300, step=1, value=150)
submit = form.form_submit_button()

if submit:

    data_scaled = scaler.transform([[N, P, K, temperature, humidity, ph, rainfall]])
    prediction = model.predict_proba(data_scaled)
    output = [[model.classes_[index], round(value * 100, 2)] for index, value in enumerate(prediction[0])]
    output.sort(key=lambda x: x[1], reverse=True)
    font_size = 25
    print(model.classes_)
    for output_list in output:
        if font_size != 12:
            font_size -= 2
        if output_list[1] > 0:
            # st.text(f"{output_list[0]} {output_list[1]}%",)
            st.markdown(f"<h1 style='font-size: {font_size}px;'>{output_list[0]} {output_list[1]}%</h1>",
                        unsafe_allow_html=True)
