import numpy as np
import pandas as pd


def circ1(r1, r2, r3, r4, r5, r6, v1, v2):
    equations = np.array([[(r1+r3+r4), (r2), 0], [0, (-r2), (-r5-r6)], [-1,1,-1]])
    results = np.array([v1, (-v2), 0])
    solution = np.linalg.solve(equations, results)
    print(f"\ni1 = {solution[0]:.2f}, i2 = {solution[1]:.2f}, i3 = {solution[2]:.2f} \n")

    return solution

def pot(i1,i2,i3,r1,r2,r3,r4,r5,r6, e1, e2):
    p1 = r1*i1**2
    p2 = r2*i2**2
    p3 = r3*i1**2
    p4 = r4*i1**2
    p5 = r5*i3**2
    p6 = r6*i3**2

    pe1 = e1*i1
    pe2 = e2*i3


def circ2_meia_onda(d1, r1, c1, v1, n2, n1, freq):
    v2 = (v1 * n2)/n1
    peak_v2 = v2*np.sqrt(2)
    peak_c1 = peak_v2 - d1 # OBJECTIVE A
    i_carga = peak_c1/r1
    ripple = i_carga/(freq*c1) # OBJECTIVE B
    v_med_carga = (peak_c1 + (peak_c1-ripple))/2 # OBJECTIVE C


def circ2_center_tape(d1, r1, c1, v1, n2, n1, freq):
    v2 = (v1 * n2)/n1
    peak_v2 = v2*np.sqrt(2)
    peak_c1 = (peak_v2/2) - d1 # OBJECTIVE A
    i_carga = peak_c1/r1
    ripple = i_carga/(freq*c1*2) # OBJECTIVE B
    v_med_carga = (peak_c1 + (peak_c1-ripple))/2 # OBJECTIVE C


def circ2_onda_completa(d1, r1, c1, v1, n2, n1, freq):
    v2 = (v1 * n2)/n1
    peak_v2 = v2*np.sqrt(2)
    peak_c1 = peak_v2 - (2*d1) # OBJECTIVE A
    i_carga = peak_c1/r1
    ripple = i_carga/(freq*c1*2) # OBJECTIVE B
    v_med_carga = (peak_c1 + (peak_c1-ripple))/2 # OBJECTIVE C
    print(v2)
    print(peak_v2)
    print(peak_c1)
    print(i_carga)
    print("rip",ripple)
    print(v_med_carga)


circ1(0.5,0.5,1,0.5,0.5,3,20,6)
circ2_meia_onda(0.7,1000,100*pow(10,(-6)),127,1,10, 60)
circ2_center_tape(0.7,4000,100*pow(10,(-6)),200,200,1000, 60)
circ2_onda_completa(0.7,5000,100*pow(10,(-6)),500,400,1000, 60)