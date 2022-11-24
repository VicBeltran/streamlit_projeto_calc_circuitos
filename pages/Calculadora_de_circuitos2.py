import streamlit as st
from utils.utilities import circ2_meia_onda, circ2_center_tape, circ2_onda_completa
from PIL import Image

st.title("""CALCULADORA DE CIRCUITO 2""")
image = Image.open('PIC_Schema.PNG')
st.image(image, caption='Circuito')


with st.sidebar:

    st.title("""Selecionador de parâmetros""")

    r1 = st.number_input('Insira a resistência em R1 (Ω)')
    v1 = st.number_input('Insira a tensão de E1 (V)')
    v2 = st.number_input('Insira a tensão de E2 (V)')

    st.write('')
    bt = st.button("Calcular")

if bt:
    with st.spinner("Calculando parâmetros do circuito"):
        ret = calc1(r1,r2,r3,r4,r5,r6,v1,v2)
        st.markdown(ret)
    with st.sidebar:
        st.success("Feito!", icon="✅")