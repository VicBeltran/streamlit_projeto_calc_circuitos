from PIL import Image
import numpy as np
import pandas as pd

def calc(res, v1, capacitancia, tipo_diodo):
    proprieties = ['res', 'v1', 'capacitancia', 'tipo_diodo']
    results = []
    results.append(str(res+1))
    results.append(str(v1+2))
    results.append(str(capacitancia+3))
    results.append(str(tipo_diodo))

    concat = {"Propriedades": proprieties, "Valores": results}
    return pd.DataFrame(concat)
