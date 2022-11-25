import streamlit as st
from utils.utilities import circ1, pot
from PIL import Image


def main_simple_circuit():
    st.title("""CALCULADORA DE CIRCUITO""")
    image = Image.open('images/meiaonda.jpeg')
    st.image(image, caption='Circuito')

    with st.sidebar:

        st.title("""Parâmetros do circuito""")

        r1 = st.number_input('Insira a resistência em R1 (Ω)')
        r2 = st.number_input('Insira a resistência em R2 (Ω)')
        r3 = st.number_input('Insira a resistência em R3 (Ω)')
        r4 = st.number_input('Insira a resistência em R4 (Ω)')
        r5 = st.number_input('Insira a resistência em R5 (Ω)')
        r6 = st.number_input('Insira a resistência em R6 (Ω)')
        v1 = st.number_input('Insira a tensão de E1 (V)')
        v2 = st.number_input('Insira a tensão de E2 (V)')

        st.write('')
        bt = st.button("Calcular")

    st.markdown("## Resultados do cálculo: ")
    placeholder = st.empty()
    with placeholder.container():
        st.markdown("""Para obter resultados para o circuito desejado,
                    insira os valores na sidebar e clique em calcular.""")

    if bt:
        try:
            with st.spinner("Calculando. . ."):
                circuit1 = circ1(r1,r2,r3,r4,r5,r6,v1,v2)
                pots = pot(circuit1[0], circuit1[1], circuit1[2], r1, r2, r3, r4, r5, r6, v1, v2)
                with placeholder.container():
                    st.success("Cálculos realizados com sucesso!", icon="✅")
                    st.markdown(f"""Para os valores inputados obtemos as seguintes correntes: <br />
                                i1 = {circuit1[0]:.2f}, i2 = {circuit1[1]:.2f}, i3 = {circuit1[2]:.2f} \n""", 
                                unsafe_allow_html=True)
                    st.markdown("A potência dos componentes são respectivamente:")
                    st.dataframe(pots)
        except Exception as e:
            st.error(f"Por favor, insira valores válidos para o cálculo - {e}")


# Loop de execução principal
main_simple_circuit()