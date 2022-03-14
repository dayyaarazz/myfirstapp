import streamlit as st
import numpy as np
import string
import pickle
st.set_option('depreciation.showfileUploaderEncoding', False)
model = pickle.load(open('model_pkl.pkl', 'rb'))


def main():
  st.sidebar.header("Stroke Risk Prediction")
  st.sidebar.text("This app will tell you the predicted wether you will have stroke or not.")
  st.sidebar.header("Fill in the information below")
  st.sidebar.text("The GaussianNaiveBayes Classifier was used.")



  age = st.slider("Input your age", 0,100)
  hypertension = st.slider("Input if you have hypertension with 0 for no and 1 for yes", 0,1)
  heartdisease = st.slider("Input if you have heartdisease with 0 for no and 1 for yes", 0,1)
  sugar = st.slider("Put your average glucose level", 150.0, 300.000)
  bmi = st.slider ("Input your BMI", 0.0,70.0)

  inputs = [[age, hypertension, heartdisease, sugar, bmi]]

  if st.button('Predict'):
    result = model.predict(inputs)
    updated_res = result.flatten().astype(int)
    if updated_res ==0:
      st.write("Not very likely you will have a stroke soon but still take a good care of yourself regardless")
    else:
      st.write("It is likely you might have a stroke soon so you should take better care of yourself")  