from datetime import date
import numpy as np
import matplotlib.pyplot as plt
import snowflake.connector
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.title("Patient Performance trajectory")
with st.form(key = "form1"):
        study_selection = st.selectbox('Select a Study', options=[15218191, 15224811, 15224428, 15224679])
        patient_selection = st.text_input('Input a Patient ID', '1')
        day_selection = st.text_input("Input a day to see a patient's progress upto", '-1')
        m1_selection = st.text_input('Input an efficacy weight', '60')
        m2_selection = st.text_input('Input a risk weight', '30')
        m3_selection = st.text_input('Input a toxicity weight', '10')
        submit_button = st.form_submit_button(label = "Enter")

        "Hello, **World**!"
