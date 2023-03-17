import requests
import streamlit as st

api_key = st.secrets.GIPHY_KEY.api_key

url = 'https://api.giphy.com/v1/gifs/search'

gif = st.text_input('Choose a gif that makes you happy!', value='dog')

params = {'api_key':api_key,
          'q':gif}

response = requests.get(url, params = params).json()

giphy = response['data'][0]['embed_url']

st.write(f"<iframe src={giphy}>", unsafe_allow_html=True)
