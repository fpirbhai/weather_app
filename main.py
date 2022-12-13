import streamlit as st
import plotly.express as px
import backend
from PIL import Image


def get_img(weather):
    img = Image.open(f"Images/{weather}")
    st.image(img, width=200)


st.title('Weather Forecast  for the next days')

place = st.text_input("Place: ")

days = st.slider('', min_value=1, max_value=5, help ='Select the number of forecasted days')

option = st.selectbox('Select data to view', options=['Temperature', 'Sky'])

msg = f"Temperature for the next {days} days in {place}"

st.subheader(msg)


if place and option == 'Temperature':
    try:
        dates, temperatures = backend.get_data(place=place,forecast_days= days, kind=option)
        figure = px.line(x=dates,y=temperatures, labels={'x': 'Dates', 'y': 'Temperatures' })
        st.plotly_chart(figure)
    except TypeError:
        st.text('Place name is incorrect.')
    except NameError:
        st.text('Place name is incorrect.')



elif place and option == 'Sky':
    try:
        dates, weather = backend.get_data(place=place,forecast_days= days, kind=option)
        images = {'Clouds': 'Images/cloud.png', 'Clear': 'Images/clear.png', 'Snow': 'Images/snow.png', 'Rain': 'Images/rain.png'}
        img_paths = [images[condition] for condition in weather] 
        print(img_paths) 
        st.image(img_paths, width=110, caption= dates)
    except TypeError:
        st.text('Place name is incorrect.')
    except TypeError:
        st.text('Place name is incorrect.')
    
    



  
