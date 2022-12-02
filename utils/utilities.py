import numpy as np
import pandas as pd

# Definição rótulos globais para circuito retificador
ROTULOS_C2 = ["Tensão de saída", "Tensão pico de saída", "Tensão pico no capacitor",
              "Corrente na carga", "Tensão de Ripple", "Tensão média na carga"]


def circ1(r1: float, r2: float, r3: float, r4: float, r5: float, r6: float, v1: float, v2: float) -> np.ndarray:
    """
    Resolve o sistema de equações para o circuito simples
    e retorna uma ndarray com os resultados das variáveis
    Input:
        r1 -> Valor da resistência em r1
        r2 -> Valor da resistência em r2
        r3 -> Valor da resistência em r3
        r4 -> Valor da resistência em r4
        r5 -> Valor da resistência em r5
        r6 -> Valor da resistência em r6
        v1 -> Valor da tensão do gerador/receptor e1
        v2 -> Valor da tensão do gerador/receptor e2
    Output
        solution -> Array com os valores de correntes i1, i2 e i3
    """
    equations = np.array([[(r1+r3+r4), (r2), 0], [0, (-r2), (-r5-r6)], [-1,1,-1]])
    results = np.array([v1, (-v2), 0])
    solution = np.linalg.solve(equations, results)

    return solution


def pot(i1: float, i2: float, i3: float, r1: float, r2: float, r3: float, r4: float, r5: float, r6: float, e1: float, e2: float) -> pd.DataFrame:
    """
    Calcula a potência para cada um dos componentes e
    retorna um DataFrame com os valores correspondentes
    Input
        i1 -> Corrente i1
        i2 -> Corrente i2
        i3 -> Corrente i3
        r1 -> Valor da resistência em r1
        r2 -> Valor da resistência em r2
        r3 -> Valor da resistência em r3
        r4 -> Valor da resistência em r4
        r5 -> Valor da resistência em r5
        r6 -> Valor da resistência em r6
        e1 -> Valor da tensão do gerador/receptor e1
        e2 -> Valor da tensão do gerador/receptor e2
    Output:
        data_frame -> DataFrame com os valores de potências
                      em relação aos componentes
    """
    pot_values = []
    pot_values.append(str(f"{(r1*i1**2):.2f}W"))
    pot_values.append(str(f"{(r2*i2**2):.2f}W"))
    pot_values.append(str(f"{(r3*i1**2):.2f}W"))
    pot_values.append(str(f"{(r4*i1**2):.2f}W"))
    pot_values.append(str(f"{(r5*i3**2):.2f}W"))
    pot_values.append(str(f"{(r6*i3**2):.2f}W"))
    pot_values.append(str(f"{(e1*i1):.2f}W"))
    pot_values.append(str(f"{(e2*i3):.2f}W"))
    labels= ["R"+str(i) for i in range(6)]
    labels.append("E1")
    labels.append("E2")
    data_frame = {"Componente": labels, "Potência": pot_values}
    return pd.DataFrame.from_dict(data_frame)


def circ2_meia_onda(d1: float, r1: float, c1: float, v1: float, n2: int, n1: int, freq: float) -> pd.DataFrame:
    """
    Calcula valores designados na váriável ROTULOS_C2 de
    acordo com o retificador de meia onda e agrega os
    valores em um dataframe
    Input:
        d1 -> Tensão do diodo
        r1 -> Resistência em ohms do resistor 1
        c1 -> Capacitância do capacitor 1
        v1 -> Tensão da fonte
        n2 -> Número de espiras em n2 (saída)
        n1 -> Número de espiras em n1 (entrada)
        freq -> Frequência da fonte
    Output:
        data_frame -> DataFrame para com resultados dos cálculos
    """
    valores_ret = []
    v2 = (v1 * n2)/n1
    valores_ret.append(str(f"{v2:.2f}V"))
    peak_v2 = v2*np.sqrt(2)
    valores_ret.append(str(f"{peak_v2:.2f}V"))
    peak_c1 = peak_v2 - d1
    valores_ret.append(str(f"{peak_c1:.2f}V")) # OBJECTIVE A
    i_carga = (peak_c1/r1)
    valores_ret.append(str(f"{i_carga:.4f}A"))
    ripple = i_carga/(freq*c1)
    valores_ret.append(str(f"{ripple:.2f}V")) # OBJECTIVE B
    valores_ret.append(str(f"{((peak_c1 + (peak_c1-ripple))/2):.2f}V")) # OBJECTIVE C
    data_frame = {"Rótulo de medida": ROTULOS_C2, "Valores": valores_ret}
    return pd.DataFrame.from_dict(data_frame)


def circ2_center_tape(d1: float, r1: float, c1: float, v1: float, n2: int, n1: int, freq: float) -> pd.DataFrame:
    """
    Calcula valores designados na váriável ROTULOS_C2 de
    acordo com o retificador com center tape e agrega os
    valores em um dataframe
    Input:
        d1 -> Tensão do diodo
        r1 -> Resistência em ohms do resistor 1
        c1 -> Capacitância do capacitor 1
        v1 -> Tensão da fonte
        n2 -> Número de espiras em n2 (saída)
        n1 -> Número de espiras em n1 (entrada)
        freq -> Frequência da fonte
    Output:
        data_frame -> DataFrame para com resultados dos cálculos
    """
    valores_ret = []
    v2 = (v1 * n2)/n1
    valores_ret.append(str(f"{(v2):.2f}V"))
    peak_v2 = v2*np.sqrt(2)
    valores_ret.append(str(f"{peak_v2:.2f}V"))
    peak_c1 = (peak_v2/2) - d1
    valores_ret.append(str(f"{peak_c1:.2f}V")) # OBJECTIVE A
    i_carga = peak_c1/r1
    valores_ret.append(str(f"{i_carga:.4f}A"))
    ripple = i_carga/(freq*c1*2)
    valores_ret.append(str(f"{ripple:.2f}V")) # OBJECTIVE B
    valores_ret.append(str(f"{((peak_c1 + (peak_c1-ripple))/2):.2f}V")) # OBJECTIVE C
    data_frame = {"Rótulo de medida": ROTULOS_C2, "Valores": valores_ret}
    return pd.DataFrame.from_dict(data_frame)


def circ2_onda_completa(d1: float, r1: float, c1: float, v1: float, n2: int, n1: int, freq: float) -> pd.DataFrame:
    """
    Calcula valores designados na váriável ROTULOS_C2 de
    acordo com o retificador de onda completa e agrega os
    valores em um dataframe
    Input:
        d1 -> Tensão do diodo
        r1 -> Resistência em ohms do resistor 1
        c1 -> Capacitância do capacitor 1
        v1 -> Tensão da fonte
        n2 -> Número de espiras em n2 (saída)
        n1 -> Número de espiras em n1 (entrada)
        freq -> Frequência da fonte
    Output:
        data_frame -> DataFrame para com resultados dos cálculos
    """
    valores_ret = []
    v2 = (v1 * n2)/n1
    valores_ret.append(str(f"{v2:.2f}V"))
    peak_v2 = v2*np.sqrt(2)
    valores_ret.append(str(f"{peak_v2:.2f}V"))
    peak_c1 = peak_v2 - (2*d1)
    valores_ret.append(str(f"{peak_c1:.2f}V")) # OBJECTIVE A
    i_carga = peak_c1/r1
    valores_ret.append(str(f"{i_carga:.4f}A"))
    ripple = i_carga/(freq*c1*2)
    valores_ret.append(str(f"{ripple:.2f}V")) # OBJECTIVE B
    valores_ret.append(str(f"{((peak_c1 + (peak_c1-ripple))/2):.2f}V")) # OBJECTIVE C
    data_frame = {"Rótulo de medida": ROTULOS_C2, "Valores": valores_ret}
    return pd.DataFrame.from_dict(data_frame)


# Exemplos de uso e inputs
# circ1(0.5,0.5,1,0.5,0.5,3,20,6)
# circ2_meia_onda(0.7,1000,100*pow(10,(-6)),127,1,10, 60))
# circ2_center_tape(0.7,4000,100*pow(10,(-6)),200,200,1000, 60)
# circ2_onda_completa(0.7,5000,100*pow(10,(-6)),500,400,1000, 60)