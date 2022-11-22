import streamlit as st
import time
from utils.utilities import calc
from PIL import Image

st.title("""CALCULADORA DE CIRCUITO""")
image = Image.open('PIC_Schema.PNG')
st.image(image, caption='Circuito')


with st.sidebar:

    st.title("""Selecionador de parâmetros""")

    resistencia = st.number_input('Insira a resistência')
    v1 = st.number_input('Insira a tensão de entrada')
    num_espiras = st.number_input('Insira número de espiras')
    capacitancia = st.number_input('Insira capacitância')
    tipo_diodo = st.radio("Selecione tipo de diodo",('Ge','Si'))

    st.write('')
    bt = st.button("Calcular")

if bt:
    with st.spinner("Calculando parâmetros do circuito"):
        time.sleep(2)
        ret = calc(resistencia, v1, capacitancia, tipo_diodo)
        st.dataframe(ret)
    with st.sidebar:
        st.success("Feito!", icon="✅")