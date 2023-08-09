import requests
import streamlit as st

apiKey = "Be7JiWBAUUgsEBXWrEwEooKX2zCTKMFTFeofLWht"
url = "https://api.nasa.gov/planetary/apod?api_key=Be7JiWBAUUgsEBXWrEwEooKX2zCTKMFTFeofLWht"

response = requests.get(url)
data = response.json()

title = data["title"]
image_url = data["url"]
explanation = data["explanation"]

image_file = "image.jpg"
resultImg = requests.get(image_url)
with open(image_file, "wb") as file:
    file.write(resultImg.content)

st.title("Astronomy Image of the Day")
st.image(image_file)
st.write(explanation)