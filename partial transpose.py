import numpy as np
import sympy as sp
def partial_transpose(rho,dimA,dimB):
    rho_tensor=np.array(rho).reshape((dimA,dimB,dimA,dimB))
    rho_pt_tensor=rho_tensor.transpose(0,2,1,3)
    rho_pt=rho_pt_tensor.reshape((dimA*dimB, dimA*dimB))
    return sp.Matrix(rho_pt)
  A1, B1, C1, D1 = sp.symbols('A1 B1 C1 D1')
B2, E1, F1, G1 = sp.symbols('B2 E1 F1 G1')
C2, F2, H1, I1 = sp.symbols('C2 F2 H1 I1')
D2, G2, I2, J1 = sp.symbols('D2 G2 I2 J1')
rho = sp.Matrix([
    [A1, B1, C1, D1],
    [B2, E1, F1, G1],
    [C2, F2, H1, I1],
    [D2, G2, I2, J1]
])
dimA=2
dimB=2
rho_pt = partial_transpose(rho, dimA, dimB)
print("Original density Matrix:")
sp.pprint(rho)
print("\nPartially transposed density Matrix:")
sp.pprint(rho_pt)
