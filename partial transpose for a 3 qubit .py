import numpy as np
import sympy as sp
def partial_transpose(rho,dimA,dimB):
    rho_tensor=np.array(rho).reshape((dimA,dimB,dimA,dimB))
    rho_pt_tensor=rho_tensor.transpose(0,2,1,3)
    rho_pt=rho_pt_tensor.reshape((dimA*dimB, dimA*dimB))
    return sp.Matrix(rho_pt)
  symbols = sp.symbols(' '.join(f'A{i}{j}' for i in range(1, 9) for j in range(1, 9)))
rho = sp.Matrix(8, 8, symbols)
dimA=4
dimB=2
rho_pt = partial_transpose(rho, dimA, dimB)
print("Original density Matrix:")
sp.pprint(rho)
print("\nPartially transposed density Matrix:")
sp.pprint(rho_pt)
