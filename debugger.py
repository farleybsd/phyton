""""
PDB => PYTHON DEBUGGER
"""
import pdb

def soma(a, b):
    pdb.set_trace()
    return a + b

resultado = soma(2, 3)
print(resultado)

# Comando Basicos PDB
# l (lista aonde estamos no codigo)
# n (proxima Linha)
# p (imprime variavel)
# c (continua - finaliza o debbing)
# python -m pdb seu_script.py