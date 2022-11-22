import streamlit as st
import time
from utils.utilities import calc
from PIL import Image

st.title("""Documentação""")
image = Image.open('PIC_Schema.PNG')
st.image(image, caption='Circuito')