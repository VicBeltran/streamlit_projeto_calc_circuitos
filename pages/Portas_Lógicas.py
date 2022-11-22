import streamlit as st
import streamlit_toggle as tog
from PIL import Image


def not_gate():
    image = Image.open('images/not.PNG')
    newsize = (150, 70)
    image = image.resize(newsize)
    with st.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            st.text("\n")
            a = tog.st_toggle_switch("A", key="anot")
        with col2:
            st.image(image, caption='Porta NOT')
        with col3:
            if a:
                st.text("\n")
                st.markdown(">0")
            else:
                st.text("\n")
                st.markdown(">1")
        st.markdown("""---""")


def and_gate():
    image = Image.open('images/and.PNG')
    newsize = (150, 100)
    image = image.resize(newsize)
    with st.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            a = tog.st_toggle_switch("A", key="aand")
            b = tog.st_toggle_switch("B", key="band")
        with col2:
            st.image(image, caption='Porta AND')
        with col3:
            if a and b:
                st.text("\n")
                st.markdown(">1")
            else:
                st.text("\n")
                st.markdown(">0")
        st.markdown("""---""")


def or_gate():
    image = Image.open('images/or.PNG')
    newsize = (150, 100)
    image = image.resize(newsize)
    with st.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            a = tog.st_toggle_switch("A", key="aor")
            b = tog.st_toggle_switch("B", key="bor")
        with col2:
            st.image(image, caption='Porta OR')
        with col3:
            if a or b:
                st.text("\n")
                st.markdown(">1")
            else:
                st.text("\n")
                st.markdown(">0")
        st.markdown("""---""")


def nand():
    image = Image.open('images/nand.PNG')
    newsize = (150, 100)
    image = image.resize(newsize)
    with st.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            a = tog.st_toggle_switch("A", key="anand")
            b = tog.st_toggle_switch("B", key="bnand")
        with col2:
            st.image(image, caption='Porta NAND')
        with col3:
            if not (a and b):
                st.text("\n")
                st.markdown(">1")
            else:
                st.text("\n")
                st.markdown(">0")
        st.markdown("""---""")

def nor_gate():
    image = Image.open('images/nor.PNG')
    newsize = (150, 100)
    image = image.resize(newsize)
    with st.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            a = tog.st_toggle_switch("A", key="anor")
            b = tog.st_toggle_switch("B", key="bnor")
        with col2:
            st.image(image, caption='Porta NOR')
        with col3:
            if not (a or b):
                st.text("\n")
                st.markdown(">1")
            else:
                st.text("\n")
                st.markdown(">0")
        st.markdown("""---""")

def xor_gate():
    image = Image.open('images/xor.PNG')
    newsize = (150, 100)
    image = image.resize(newsize)
    with st.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            a = tog.st_toggle_switch("A", key="axor")
            b = tog.st_toggle_switch("B", key="bxor")
        with col2:
            st.image(image, caption='Porta XOR')
        with col3:
            if a and b or (not a and not b):
                st.text("\n")
                st.markdown(">0")
            elif a or b:
                st.text("\n")
                st.markdown(">1")
        st.markdown("""---""")

def nxor_gate():
    image = Image.open('images/xnor.PNG')
    newsize = (150, 100)
    image = image.resize(newsize)
    with st.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            a = tog.st_toggle_switch("A", key="anxor")
            b = tog.st_toggle_switch("B", key="bnxor")
        with col2:
            st.image(image, caption='Porta NXOR')
        with col3:
            if a and b or (not a and not b):
                st.text("\n")
                st.markdown(">1")
            else:
                st.text("\n")
                st.markdown(">0")
        st.markdown("""---""")

def main_ports():
    st.title("""Portas Lógicas""")
    st.markdown("""Neste programa, podemos simular as seguintes portas lógicas: AND,
                OR, NAND, NOT, NOR, XOR, NXOR. Abaixo detemos os diagramas das portas lógicas
                de maneira interativa para análise de outputs e inputs. No campo mais a direita
                temos os inputs (A e B) os quais servem para alimentar a porta lógica, no centro,
                a representação da porta lógica e mais à direita, o output do circuito.""")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""**INPUTS**""")
    with col2:
        st.markdown("""**GATE**""")
    with col3:
        st.markdown("""**OUTPUT**""")
    not_gate()
    and_gate()
    or_gate()
    nand()
    nor_gate()
    xor_gate()
    nxor_gate()


main_ports()