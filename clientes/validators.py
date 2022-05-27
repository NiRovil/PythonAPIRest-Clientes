def cpf(cpf):
    return len(cpf) != 11

def nome(nome):
    return nome.isalpha()

def rg(rg):
    return len(rg) != 9

def celular(celular):
    return len(celular) < 11