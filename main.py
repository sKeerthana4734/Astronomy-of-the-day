import requests
import streamlit as st
import os

apiKey = os.environ.get("API_KEY")
url = f"https://api.nasa.gov/planetary/apod?api_key={apiKey}"
print(apiKey, url)

response = requests.get(url)
data = response.json()

title = data["title"]
image_url = data["url"]
explanation = data["explanation"]

image_file = "image.jpg"
resultImg = requests.get(image_url)
with open(image_file, "wb") as file:
    file.write(resultImg.content)

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        # header {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)


st.title("Astronomy Image of the Day")
st.write(f"**{title}**")
st.image(image_file)
st.write(explanation)
st.write("Have a good day!")
st.write("Regards, Keerthana 😊")
