import streamlit as st
import requests
import pickle
import datetime
import pandas as pd

st.title('Flight Prediction System')
flight=pickle.load(open('flight.pkl','rb'))
data=pickle.load(open('data.pkl','rb'))

dep_date=st.date_input("Enter the departure date : ", datetime.date(2019, 7, 6))
# dep_day=pd.to_datetime(format="%Y/%m/%d").day
# st.write(dep_day)

dep_time = st.time_input('Enter the departure time : ', value="now",step=60)

arr_date=st.date_input("Enter the arrival date : ", datetime.date(2019, 7, 6))

arr_time = st.time_input('Enter the arrival time : ', value="now",step=60)

source = st.selectbox('Enter the Source : ',(data['Source'].value_counts().index  ))

destination = st.selectbox('Enter the destination : ',(data['Destination'].value_counts().index  ))

airline = st.selectbox('Enter the Airline : ',(data['Airline'].value_counts().index  ))