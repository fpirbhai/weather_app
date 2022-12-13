import streamlit as st
import plotly.express as px
import pandas as pd

st.title('In Search for happiness')

x_axis = st.selectbox('Select the data for the x-axis', options=['GDP','Happiness', 'Generosity'])

y_axis = st.selectbox('Select the data for the y-axis', options=['GDP','Happiness', 'Generosity'])

st.subheader(f'{x_axis} and {y_axis}')

df = pd.read_csv('Data/happy.csv')


def get_axis(data):
    match data:
        case 'GDP':
            data = 'gdp'
        case 'Generosity':
            data = 'generosity'
        case 'Happiness':
            data = 'happiness'
        
    dat = df[data]
    return dat

x_data = get_axis(x_axis)
y_data = get_axis(y_axis)

plot1 = px.scatter(x=x_data, y=y_data,labels={'x':x_axis, 'y': y_axis})
st.plotly_chart(plot1)



