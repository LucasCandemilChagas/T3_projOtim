contador = 0
def salao(n,b,c):
    if not verifica_quant(n,b,c):
        return 0

    salao = [['.' for _ in range(n)] for _ in range(n)]

    pistoleiro = 'b'

    posiciona(salao,n,b,c,pistoleiro)

def posiciona(salao,n,b,c,pistoleiro):
    if b > 0:
        for linha in range(n):
            for coluna in range(n):
                if verifica_adj(salao,n,linha,coluna,pistoleiro):
                    salao[linha][coluna] = pistoleiro
                    posiciona(salao,n,b-1,c,pistoleiro)
                    salao[linha][coluna] = '.'
    elif c > 0:
        for linha in range(n):
            for coluna in range(n):
                pass

def verifica_companheiro(salao,n,l,c,pistoleiro):
    for linha in range(l):
        if salao[linha][c] == pistoleiro:
            return False
    
    for linha in range(l+1,n):
        if salao[linha][c] == pistoleiro:
            return 
def verifica_adj(salao,n,l,c,pistoleiro):
    if salao[l+1][c] == pistoleiro:
        return False
    if salao[l-1][c] == pistoleiro:
        return False
    
    if salao[l][c+1] == pistoleiro:
        return False
    if salao[l][c-1] == pistoleiro:
        return False
    
    if salao[l-1][c-1] == pistoleiro:
        return False
    if salao[l+1][c-1] == pistoleiro:
        return False
    
    if salao[l-1][c+1] == pistoleiro:
        return False
    if salao[l+1][c+1] == pistoleiro:
        return False
    
    return True

def verifica_quant(n,b,c):
    if n < 3:
        return False
    if b < 2 or c < 2:
        return False
    
    return True