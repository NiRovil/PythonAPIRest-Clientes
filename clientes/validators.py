import re
from validate_docbr import CPF

def cpf(numero_cpf):
    cpf = CPF()
    return cpf.validate(numero_cpf)

def nome(nome):
    return nome.isalpha()

def rg(rg):
    return len(rg) != 9

def celular(celular):
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, celular)
    return resposta