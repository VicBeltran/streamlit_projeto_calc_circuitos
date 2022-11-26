import streamlit as st
from PIL import Image

image_no = Image.open('images/nó.PNG')
image_circ_doc = Image.open('images/circuito_docs1.PNG')


st.title("""Documentação""")
st.markdown(""" ## Sobre o Projeto <br /> 
O projeto visa resolver os problemas propostos pelo professor em sala de aula, utilizando todo o conhecimento dado através das aulas pelo professor, juntamente com conhecimentos adquiridos também fora de sala de aula por parte dos alunos.

O projeto foi desenvolvido utilizando a linguagem de programação Python, tanto para a interface visual quanto para o tratamento dos dados e cálculos. E isto foi possível por intermédio de 4 bibliotecas, Streamlit, Pandas, NumPy e Pillow. 

O Streamlit, uma biblioteca voltada à ciência de dados, foi utilizado para desenvolver a interface visual do programa, permitindo que não fosse necessária a utilização de uma linguagem front-end para tal, Pandas foi utilizada para manipular e trabalhar os dados fornecidos para os cálculos, o NumPy foi utilizado por conta das equações, que por serem complexas, foi-se necessário a utilização do tal, e o Pillow foi utilizado para ser uma biblioteca das imagens que aparecem na interface conforme a interação do usuário.
""", unsafe_allow_html=True)

st.markdown(""" ## Sobre os Cálculos <br /> 
O projeto em si tem como instrumentos de cálculo as leis de Kirchhoff, e Lei de Ohm, ambas foram adaptadas e escritas em linguagem Python.""", unsafe_allow_html=True)

st.markdown(""" #### Lei de Kirchhoff <br /> 
Como explicado em aula e aplicado nos exemplos e exercícios, a Lei de Kirchhoff, é dividida em duas leis, sendo a primeira a “Lei dos Nós” e a segunda “Lei das Malhas”.
A lei dos Nós, de maneira simplificada, aponta que a soma das correntes que chegam a um nó é igual a soma das correntes que saem. 
No exemplo a seguir, as correntes i1 e i2 estão chegam e as correntes i3 e i4 estão saindo, sendo assim:
""", unsafe_allow_html=True)

st.write(r"""$$
i_{1}+i_{2} = i_{3} + i_{4}
$$
""")

col1, col2, col3 = st.columns(3)

with col2:
    st.image(image_no, caption='Exemplo de Nó')


st.markdown("""
**Obs**: Em um circuito, o número de vezes que devemos aplicar a Lei dos Nós é igual ao número de nós do circuito menos 1. Por exemplo, se no circuito existir 4 nós, vamos usar a lei 3 vezes (4 - 1).
A Lei das Malhas, de maneira simplificada, é uma consequência da conservação da energia e ela aponta que quando percorremos uma malha em um dado sentido, a soma algébrica das diferenças de potencial (ddp ou tensão) é igual a zero.
Para aplicar a Lei das Malhas, devemos definir o sentido que iremos percorrer no circuito.A tensão poderá ser positiva ou negativa, de acordo com o sentido que arbitramos para a corrente e para percorrer o circuito.
Para isso, vamos considerar que o valor da ddp em um resistor é dado por R . i, sendo positivo se o sentido da corrente for o mesmo do sentido do percurso, e negativo se for no sentido contrário.Para o gerador (fem) e receptor (fcem) utiliza-se o sinal de entrada no sentido que adotamos para a malha.
Veja no exemplo a seguir:

""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col2:
    st.image(image_circ_doc, caption='Circuito exemplo')

st.write(r"""Aplicando a lei das malhas para esse trecho do circuito, teremos: <br />
$$ 
UAB + UBE + UEF + UFA = 0 
$$ 
Para substituir os valores de cada trecho, devemos analisar os sinais das tensões:
$ε_{1}$: positivo; $R_{1}.i_{1}$: positivo; $R{2}.i_{2}$: negativo; $ε_{2}$: negativo; $R_{3}.i_{1}$: positivo; $R_{4}.i_{1}$: positivo.<br />
Considerando o sinal da tensão em cada componente, podemos escrever a equação desta malha como: <br />
$$
ε_{1} + R_{1}.i_{1} - R{2}.i_{2} - ε_{2} + R_{3}.i_{1} + R_{4}.i_{1} = 0
$$

""", unsafe_allow_html= True)

st.markdown(""" #### Lei de Ohm""")
st.write(r"""
A Lei de Ohm também é dividida em duas “partes”.
A Primeira Lei de Ohm postula que um condutor ôhmico (resistência constante) mantido à temperatura constante, a intensidade (i) de corrente elétrica será proporcional à diferença de potencial (ddp) aplicada entre suas extremidades.
Ou seja, sua resistência elétrica é constante. Ela é representada pela seguinte fórmula:

$$
R= \frac{U}{I}
$$
$$
ou
$$
$$
U= R.i
$$
Onde:<br />
R: resistência, medida em Ohm (Ω)<br />
U: diferença de potencial elétrico (ddp), medido em Volts (V)<br />
I: intensidade da corrente elétrica, medida em Ampére (A).<br /><br />
A Segunda Lei de Ohm estabelece que a resistência elétrica de um material é diretamente proporcional ao seu comprimento, inversamente proporcional à sua área de secção transversal.
Além disso, ela depende do material do qual é constituída.É representada pela seguinte fórmula:

$$
R = \frac{\rho.L}{A}
$$
Onde:<br />
R: resistência (Ω)<br />
ρ: resistividade do condutor (depende do material e de sua temperatura, medida em Ω.m)<br />
L: comprimento (m)<br />
A: área de secção transversal (mm2)<br />
""", unsafe_allow_html= True)

st.markdown(""" ## Detalhes
A interface visual do código foi feita, como dito antes, utilizando o Streamlit onde foi dividido em 3 páginas, uma para resolução do circuito, outra para resolver os circuitos com retificadores e outra para as portas lógicas. Assim como proposto, os dados são manipuláveis e podem variar de acordo com a resposta esperada. 
As imagens utilizadas foram para que a visualização dos cálculos feitas pelo programa ficassem mais simplificadas ao usuário, sendo possível fazer isso, como dito anteriormente, por intermédio da biblioteca Pillow. Tendo imagens para as portas lógicas, para os circuitos e para os leds.
Foram separados para uma classe específica os cálculos, onde as variáveis estão instanciadas (resistores, diodos, capacitores, tensões, frequência, etc…) e manipuladas utilizando os conceitos aprendidos em sala de aula somados com os conhecimentos nossos de programação, sendo isto possível, como informado anteriormente, por intermédio da biblioteca NumPy e funções da própria linguagem Python também.
Todo o projeto foi versionado e está disponível na plataforma [GitHub](https://github.com) e terá o link disponibilizado para análise do professor responsável.
""", unsafe_allow_html= True)

st.markdown(""" ## Conclusão
Sob influxo de todos os dados acima pode-se concluir que, o projeto atende aos requisitos esperados e consegue executar os cálculos com assertividade e precisão, em um tempo de processamento inferior a 1ms, 
o que faz ter uma performance ótima. Através dos conhecimentos adquiridos em sala de aula para realização de todos os cálculos e resoluções, juntamente com conhecimentos prévios dos alunos foi possível realizar tal tarefa com maestria e competência.
""", unsafe_allow_html= True)

st.markdown(""" ## Links Úteis
Repositório do projeto: [link do projeto](https://github.com/VicBeltran/streamlit_projeto_calc_circuitos) <br />
Bibliotecas utilizadas:
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [NumPy](https://numpy.org/)
- [Pillow](https://pypi.org/project/Pillow/)
""", unsafe_allow_html= True)