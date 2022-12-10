import streamlit as st


st.title('Weather Forecast  for the next days')

place = st.text_input("Place: ")

days = st.slider('', min_value=1, max_value=5, help ='Select the number of forecasted days')

option = st.selectbox('Select data to view', options=['Temperature', 'Sky'])

msg = f"Temperature for the next {days} days in {place}"

st.subheader(msg)
