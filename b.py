import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import time
import dateutil

with st.spinner('loading'):time.sleep(2)
df=sns.load_dataset('penguins')

st.title('My data analytics dashboard')
st.header('dataset')
st.subheader('subheader')
st.write('write data')
st.image('https://images.pexels.com/photos/86405/penguin-funny-blue-water-86405.jpeg?cs=srgb&dl=pexels-pixabay-86405.jpg&fm=jpg')#for addingimages
#st.video('')#for adding Video
if st.checkbox('acknowledge'):st.write(df)

if st.button('click'):st.write(df.describe())


st.radio('gender',['female','male','other'])
st.multiselect('languages',['javascript','php','python'])


a=st.slider('select rating',0,10)
st.write(a)

st.number_input('pick',0,100)

b=st.text_input('enter your name')
st.write(b)
st.date_input('dob')
st.balloons()