import numpy as np
import pandas as pd

ROTULOS_C2 = ["Tensão de saída, Tensão pico de saída, Tensão pico no capacitor",
              "Corrente na carga", "Tensão de Ripple", "Tensão média na carga"]


def circ1(r1, r2, r3, r4, r5, r6, v1, v2):
    equations = np.array([[(r1+r3+r4), (r2), 0], [0, (-r2), (-r5-r6)], [-1,1,-1]])
    results = np.array([v1, (-v2), 0])
    solution = np.linalg.solve(equations, results)

    return solution


def pot(i1,i2,i3,r1,r2,r3,r4,r5,r6, e1, e2):
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


def circ2_meia_onda(d1, r1, c1, v1, n2, n1, freq):
    valores_ret = []
    v2 = valores_ret.append(str(f"{((v1 * n2)/n1):.2f}V"))
    peak_v2 = valores_ret.append(str(f"{(v2*np.sqrt(2)):.2f}V"))
    peak_c1 = valores_ret.append(str(f"{(peak_v2 - d1):.2f}V")) # OBJECTIVE A
    i_carga = valores_ret.append(str(f"{(peak_c1/r1):.2f}A"))
    ripple = valores_ret.append(str(f"{(i_carga/(freq*c1)):.2f}")) # OBJECTIVE B
    valores_ret.append(str(f"{((peak_c1 + (peak_c1-ripple))/2):.2f}")) # OBJECTIVE C
    data_frame = {"Rótulo de medida": ROTULOS_C2, "Valores": valores_ret}
    return pd.DataFrame.from_dict(data_frame)


def circ2_center_tape(d1, r1, c1, v1, n2, n1, freq):
    valores_ret = []
    v2 = valores_ret.append(str(f"{((v1 * n2)/n1):.2f}V"))
    peak_v2 = valores_ret.append(str(f"{(v2*np.sqrt(2)):.2f}V"))
    peak_c1 = valores_ret.append(str(f"{((peak_v2/2) - d1):.2f}V")) # OBJECTIVE A
    i_carga = valores_ret.append(str(f"{(peak_c1/r1):.2f}A"))
    ripple = valores_ret.append(str(f"{(i_carga/(freq*c1*2)):.2f}")) # OBJECTIVE B
    valores_ret.append(str(f"{((peak_c1 + (peak_c1-ripple))/2):.2f}")) # OBJECTIVE C
    data_frame = {"Rótulo de medida": ROTULOS_C2, "Valores": valores_ret}
    return pd.DataFrame.from_dict(data_frame)

def circ2_onda_completa(d1, r1, c1, v1, n2, n1, freq):
    valores_ret = []
    v2 = (v1 * n2)/n1
    peak_v2 = valores_ret.append(str(f"{(v2*np.sqrt(2)):.2f}V"))
    peak_c1 = valores_ret.append(str(f"{(peak_v2 - (2*d1)):.2f}V")) # OBJECTIVE A
    i_carga = valores_ret.append(str(f"{(peak_c1/r1):.2f}A"))
    ripple = valores_ret.append(str(f"{(i_carga/(freq*c1*2)):.2f}")) # OBJECTIVE B
    valores_ret.append(str(f"{((peak_c1 + (peak_c1-ripple))/2):.2f}")) # OBJECTIVE C
    data_frame = {"Rótulo de medida": ROTULOS_C2, "Valores": valores_ret}
    return pd.DataFrame.from_dict(data_frame)

# circ1(0.5,0.5,1,0.5,0.5,3,20,6)
# circ2_meia_onda(0.7,1000,100*pow(10,(-6)),127,1,10, 60)
# circ2_center_tape(0.7,4000,100*pow(10,(-6)),200,200,1000, 60)
# circ2_onda_completa(0.7,5000,100*pow(10,(-6)),500,400,1000, 60)