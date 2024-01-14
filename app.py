import streamlit as st 
import pickle 
import numpy as np 

with open("decision_tree.pkl", "rb") as file:
    D_tree = pickle.load(file)

st.title("Apollo Drug Prediction")
drug_dct = {0:"drugA",1:"drugB",2:"drugC",3:"drugX",
            4:"drugY"}

def predict_function(Age,Sex,Bp,Chelosterol,Na_to_K):
    input_array = np.array([[Age,Sex,Bp,Chelosterol,Na_to_K]])
    prediction = D_tree.predict(input_array)
    prediction = drug_dct[prediction[0]]
    return prediction

Age = st.slider('Age',min_value=1, max_value=100, value= 50)
Sex = st.selectbox('Sex', ['Male','Female'])
Bp = st.selectbox('Blood Pressure', ['Low','Normal','High'])
Chelosterol = st.selectbox('Chelosterol', ['Normal','High'])
Na_to_K = st.slider('Na_to_K',min_value=1, max_value=50, value= 22)

Sex = 1 if Sex == "Female" else 0
bp_mapping = {'Low':0,'Normal' : 1, 'High':2}
Chelosterol_mapping = {'Normal' : 0, 'High':1}
Bp = bp_mapping[Bp]
Chelosterol = Chelosterol_mapping[Chelosterol]

if st.button("Predict"):
    prediction = predict_function(Age,Sex,Bp,Chelosterol,Na_to_K)
    st.write(f"The prescribed drug for this subject is {prediction}")