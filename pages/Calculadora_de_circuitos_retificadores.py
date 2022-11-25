
import streamlit as st
from utils.utilities import circ2_meia_onda, circ2_center_tape, circ2_onda_completa
from PIL import Image

def reset():
    st.session_state["meia_onda"] = False
    del st.session_state["meia_onda"]
    st.session_state["onda_completa"] = False
    st.session_state["center_tape"] = False


def initialize_circ(img_name, label):
    image = Image.open(img_name)
    st.image(image, caption=label)


def init_params():
    with st.sidebar:
        st.title("""Selecionador de parâmetros""")
        r1 = st.number_input('Insira a resistência em R1 (Ω)')
        v1 = st.number_input('Indique a tensão na fonte (V)')
        freq = st.number_input('Insira a frequência da fonte (Hz)')
        n1 = st.number_input('Insira o número de espiras em n1', format= "%d", value=0)
        n2 = st.number_input('Insira o número de espiras em n2', format= "%d", value=0)
        c1 = st.number_input('Insira a capacitância (F)', format= "%f")
        bt = st.button("Calcular")
    return r1, v1, freq, n1, n2, c1, bt


def meia_onda():
    st.session_state["meia_onda"] = True
    r1, v1, freq, n2, n1, c1, bt = init_params()
    initialize_circ('images/meiaonda.jpeg', "Circuito Retificador de Meia Onda")
    st.markdown("## Resultados do cálculo: ")
    placeholder = st.empty()
    with placeholder.container():
        st.markdown("""Para obter resultados para o circuito desejado,
                insira os valores na sidebar e clique em calcular.""")
    if 0 == 0:
        if bt:
            with st.spinner("Calculando. . ."):
                result = circ2_meia_onda(0.7, r1, c1, v1, n2, n1, freq)
                print(result)
                with placeholder.container():
                    st.success("Cálculos realizados com sucesso!", icon="✅")
                    st.markdown("Os resultados para o circuit são respectivamente:")
                    st.dataframe(result)
                    st.button("Escolher outro retificador", on_click=reset)
    else:
        st.error(f"Por favor, insira valores válidos para o cálculo")


def center_tape():
    st.session_state["center_tape"] = True
    r1, v1, freq, n2, n1, c1, bt = init_params()
    initialize_circ('images/meiaonda.jpeg', "Circuito Retificador com Center Tape")
    st.markdown("## Resultados do cálculo: ")
    placeholder = st.empty()
    with placeholder.container():
        st.markdown("""Para obter resultados para o circuito desejado,
                insira os valores na sidebar e clique em calcular.""")
    try:
        if bt:
            with st.spinner("Calculando. . ."):
                result = circ2_center_tape(0.7, r1, c1, v1, n2, n1, freq)
                with placeholder.container():
                    st.success("Cálculos realizados com sucesso!", icon="✅")
                    st.markdown("Os resultados para o circuit são respectivamente:")
                    st.dataframe(result)
                    st.button("Escolher outro retificador", on_click=reset)
    except Exception as e:
        st.error(f"Por favor, insira valores válidos para o cálculo")


def onda_completa():
    st.session_state["onda_completa"] = True
    r1, v1, freq, n2, n1, c1, bt = init_params()
    initialize_circ('images/meiaonda.jpeg', "Circuito Retificador de Onda Completa")
    st.markdown("## Resultados do cálculo: ")
    placeholder = st.empty()
    with placeholder.container():
        st.markdown("""Para obter resultados para o circuito desejado,
                insira os valores na sidebar e clique em calcular.""")
    try:
        if bt:
            with st.spinner("Calculando. . ."):
                result = circ2_onda_completa(0.7, r1, c1, v1, n2, n1, freq)
                with placeholder.container():
                    st.success("Cálculos realizados com sucesso!", icon="✅")
                    st.markdown("Os resultados para o circuit são respectivamente:")
                    st.dataframe(result)
                    st.button("Escolher outro retificador", on_click=reset)
    except Exception as e:
        st.error(f"Por favor, insira valores válidos para o cálculo")


def main_rectifier():
    st.title("""CALCULADORA DE CIRCUITOS RETIFICADORES""")
    placeholder = st.empty()

    if 'meia_onda' not in st.session_state:
        print("Aqui")
        st.session_state["meia_onda"] = False
        st.session_state["onda_completa"] = False
        st.session_state["center_tape"] = False

    if st.session_state["meia_onda"]:
        meia_onda()
    elif st.session_state["onda_completa"]:
        onda_completa()
    elif st.session_state["center_tape"]:
        center_tape()
    else:
        with placeholder.container():
            st.markdown("""Para usar a calculadora, selecione um dos tipos de circuito abaixo para efetuar os cálculos:""")
            col1, col2, col3 = st.columns(3)
            with col1:
                initialize_circ('images/meiaonda.jpeg', "Circuito Retificador Meia Onda")
                b1 = st.button("Retificador Meia Onda")
            with col2:
                initialize_circ('images/meiaonda.jpeg',"Circuito Retificador com Center Tape")
                b2 = st.button("Retificador com Center Tape")
            with col3:
                initialize_circ('images/meiaonda.jpeg',"Circuito Retificador Onda Completa")
                b3 = st.button("Retificador Onda Completa")
            
        if b1:
            placeholder.empty()
            meia_onda()
        elif b2:
            placeholder.empty()
            center_tape()
        elif b3:
            placeholder.empty()
            onda_completa()

main_rectifier()