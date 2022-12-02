
import streamlit as st
from utils.utilities import circ2_meia_onda, circ2_center_tape, circ2_onda_completa
from PIL import Image


def reset():
    """
    Retorna a página para estado inicial.
    Input:
        None
    Output:
        None
    """
    st.session_state["meia_onda"] = False
    del st.session_state["meia_onda"]
    st.session_state["onda_completa"] = False
    st.session_state["center_tape"] = False


def initialize_circ(img_name, label):
    """
    Gera a imagem do circuito na interface
    Input:
        None
    Output:
        None
    """
    image = Image.open(img_name)
    newsize = (600, 300)
    image2 = image.resize(newsize)
    st.image(image2, caption=label)


def init_params():
    """
    Inicializa a interface para inserção de parâmetros
    Input:
        None
    Output:
        r1 -> Resistência em ohms do resistor 1
        c1 -> Capacitância do capacitor 1
        v1 -> Tensão da fonte
        n2 -> Número de espiras em n2 (saída)
        n1 -> Número de espiras em n1 (entrada)
        freq -> Frequência da fonte
        bt -> Objeto botão de calcular
    """

    with st.sidebar:
        st.title("""Selecionador de parâmetros""")
        r1 = st.number_input('Insira a resistência em R1 (Ω)')
        v1 = st.number_input('Indique a tensão na fonte (V)')
        freq = st.number_input('Insira a frequência da fonte (Hz)')
        n1 = st.number_input('Insira o número de espiras em n1', format= "%d", value=0)
        n2 = st.number_input('Insira o número de espiras em n2', format= "%d", value=0)
        c1 = st.number_input('Insira a capacitância (F)', format= "%f")
        col1, col2 = st.columns(2)
        with col1:
            bt = st.button("Calcular", type='primary')
        with col2:
            st.button("Voltar ao menu", on_click=reset)
    return r1, v1, freq, n1, n2, c1, bt


def meia_onda():
    """
    Gera a interface e faz call para função de
    cálculo para retificadores de meia onda
    Input:
        None
    Output:
        None
    """

    st.session_state["meia_onda"] = True
    r1, v1, freq, n1, n2, c1, bt = init_params()
    initialize_circ('images/meia-onda.jpg', "Circuito Retificador de Meia Onda")
    st.markdown("## Resultados do cálculo: ")
    placeholder = st.empty()
    with placeholder.container():
        st.markdown("""Para obter resultados para o circuito desejado,
                insira os valores na sidebar e clique em calcular.""")
    try:
        if bt:
            with st.spinner("Calculando. . ."):
                result = circ2_meia_onda(0.7, r1, c1, v1, n2, n1, freq)
                with placeholder.container():
                    st.success("Cálculos realizados com sucesso!", icon="✅")
                    st.markdown("Os resultados para o circuit são respectivamente:")
                    st.dataframe(result)
    except Exception as e:
        st.error(f"Por favor, insira valores válidos para o cálculo - {e}")


def center_tape():
    """
    Gera a interface e faz call para função de
    cálculo para retificadores de center tape
    Input:
        None
    Output:
        None
    """
    st.session_state["center_tape"] = True
    r1, v1, freq, n1, n2, c1, bt = init_params()
    initialize_circ('images/center-tape.jpg', "Circuito Retificador com Center Tape")
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
    except Exception as e:
        st.error(f"Por favor, insira valores válidos para o cálculo - {e}")


def onda_completa():
    """
    Gera a interface e faz call para função de
    cálculo para retificadores de onda completa
    Input:
        None
    Output:
        None
    """
    st.session_state["onda_completa"] = True
    r1, v1, freq, n1, n2, c1, bt = init_params()
    initialize_circ('images/onda-completa.jpg', "Circuito Retificador de Onda Completa")
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
    except Exception as e:
        st.error(f"Por favor, insira valores válidos para o cálculo - {e}")


def main_rectifier():
    st.title("""CALCULADORA DE CIRCUITOS RETIFICADORES""")
    placeholder = st.empty()

    # Verifica se estados já foram inicializados para cáculos - basicamente evita bugs
    if 'meia_onda' not in st.session_state:
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
                initialize_circ('images/meia-onda.jpg', "Circuito Retificador Meia Onda")
                b1 = st.button("Retificador Meia Onda")
            with col2:
                initialize_circ('images/center-tape.jpg',"Circuito Retificador com Center Tape")
                b2 = st.button("Retificador com Center Tape")
            with col3:
                initialize_circ('images/onda-completa.jpg',"Circuito Retificador Onda Completa")
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

# Loop de execução principal
main_rectifier()