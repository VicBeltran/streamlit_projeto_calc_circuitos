import streamlit as st
import time
from utils.utilities import calc
from PIL import Image

st.title("""CALCULADORA DE CIRCUITO""")
image = Image.open('PIC_Schema.PNG')
st.image(image, caption='Circuito')


with st.sidebar:

    st.title("""Selecionador de parâmetros""")

    r1 = st.number_input('Insira a resistência em R1')
    r2 = st.number_input('Insira a resistência em R2')
    r3 = st.number_input('Insira a resistência em R3')
    r4 = st.number_input('Insira a resistência em R4')
    r5 = st.number_input('Insira a resistência em R5')
    r6 = st.number_input('Insira a resistência em R6')
    v1 = st.number_input('Insira a tensão de E1')
    v2 = st.number_input('Insira a tensão de E2')

    st.write('')
    bt = st.button("Calcular")

if bt:
    with st.spinner("Calculando parâmetros do circuito"):
        time.sleep(2)
        ret = calc(r1,r2,r3,r4,r5,r6,v1,v2)
        st.markdown(ret)
    with st.sidebar:
        st.success("Feito!", icon="✅")