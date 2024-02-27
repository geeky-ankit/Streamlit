from io import BytesIO
from PIL import Image
import requests
import streamlit as st

st.write("Welcome to Streamlit")

img_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTIkFuZS8SuA68sIurQObxCReuu6PJRhwvzmw&usqp=CAU"
response = requests.get(img_url)

image = Image.open(BytesIO(response.content))

st.image(image)