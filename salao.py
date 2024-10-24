import time
import sys
import re
import cProfile
time_verificacao = 0
vet = []
set_saloes = set()
def salao(n,b,c):
    if not verifica_quant(n,b,c):
        return 0

    salao = [['.' for _ in range(n)] for _ in range(n)]
    
    posiciona(salao,n,b,c)
    
    return salao

def posiciona(salao,n,b,c):    
    if b > 0:
        for linha in range(n):
            for coluna in range(n):
                if salao[linha][coluna] == '.' and verifica_adj(salao,n,linha,coluna,'b'):
                    salao[linha][coluna] = 'b'
                    vet.append((linha,coluna))
                    posiciona(salao,n,b-1,c)
                    vet.remove((linha,coluna))
                    salao[linha][coluna] = '.'
    elif c > 0:
        for linha in range(n):
            for coluna in range(n):
                if salao[linha][coluna] == '.' and verifica_pistoleiros(salao, n, linha, coluna, 'c'):
                    salao[linha][coluna] = 'c'
                    posiciona(salao,n,b,c-1)
                    salao[linha][coluna] = '.'
    else:
        salao_tuple = tuple(map(tuple,salao))
        if salao_tuple not in set_saloes:
            if verifica_salao(salao,n,vet):
                adiciona_set(salao) 
        
def verifica_pistoleiros(salao, n, l, col, pistoleiro):
    inimigo = 'c' if pistoleiro == 'b' else 'b'
    cont = 0  

    # Verifica se há inimigos acima
    for l1 in range(l-1, -1, -1):
        if salao[l1][col] == pistoleiro:
            return False
        elif salao[l1][col] == inimigo:
            cont += 1
            break
    
    # Verifica se há inimigos abaixo
    for l2 in range(l+1, n):
        if salao[l2][col] == pistoleiro:
            return False
        elif salao[l2][col] == inimigo:
            cont += 1
            break
    
    # Verifica se há inimigos à esquerda
    for c1 in range(col-1, -1, -1):
        if salao[l][c1] == pistoleiro:
            return False
        elif salao[l][c1] == inimigo:
            cont += 1
            break
    
    # Verifica se há inimigos à direita
    for c2 in range(col+1, n):
        if salao[l][c2] == pistoleiro:
            return False
        elif salao[l][c2] == inimigo:
            cont += 1
            break
    
    # Verifica a diagonal superior esquerda
    for l3, c3 in zip(range(l-1, -1, -1), range(col-1, -1, -1)):
        if salao[l3][c3] == pistoleiro:
            return False
        elif salao[l3][c3] == inimigo:
            cont += 1
            break
    
    # Verifica a diagonal superior direita
    for l4, c4 in zip(range(l-1, -1, -1), range(col+1, n)):
        if salao[l4][c4] == pistoleiro:
            return False
        elif salao[l4][c4] == inimigo:
            cont += 1
            break
    
    # Verifica a diagonal inferior esquerda
    for l5, c5 in zip(range(l+1, n), range(col-1, -1, -1)):
        if salao[l5][c5] == pistoleiro:
            return False
        elif salao[l5][c5] == inimigo:
            cont += 1
            break
    
    # Verifica a diagonal inferior direita
    for l6, c6 in zip(range(l+1, n), range(col+1, n)):
        if salao[l6][c6] == pistoleiro:
            return False
        elif salao[l6][c6] == inimigo:
            cont += 1
            break
    
    if cont < 2:
        return False
    
    return True

def verifica_adj(salao,n,l,c,pistoleiro):
    if l+1 < n and salao[l+1][c] == pistoleiro:
        return False
    if l-1 >= 0 and salao[l-1][c] == pistoleiro:
        return False
    
    if c+1 < n and salao[l][c+1] == pistoleiro:
        return False
    if c-1 >= 0 and salao[l][c-1] == pistoleiro:
        return False
    
    if c-1 >= 0 and l-1 >= 0 and salao[l-1][c-1] == pistoleiro:
        return False
    if l+1 < n and c-1 >= 0 and salao[l+1][c-1] == pistoleiro:
        return False
    
    if c+1 < n and l-1 >= 0 and salao[l-1][c+1] == pistoleiro:
        return False
    if l+1 < n and c+1 < n and salao[l+1][c+1] == pistoleiro:
        return False
    
    return True

def verifica_quant(n,b,c):
    if n < 3:
        return False
    if b < 2 or c < 2:
        return False
    
    return True

def verifica_salao(salao,n,vet):
    for b in vet:
        if not verifica_pistoleiros(salao, n, b[0], b[1], salao[b[0]][b[1]]):
            return False
    return True

def adiciona_set(salao):
    #add salao
    salao_tuple = tuple(map(tuple,salao))
    set_saloes.add(salao_tuple)
    
    #90
    salao_transposto = list(zip(*salao))
    salao_90 = tuple(tuple(linha)[::-1] for linha in salao_transposto)
    set_saloes.add(salao_90)
    
    #180
    salao_180 = tuple(tuple(linha)[::-1] for linha in salao_90)
    set_saloes.add(salao_180)
    
    #270
    salao_270 = tuple(tuple(linha)[::-1] for linha in salao_180)
    set_saloes.add(salao_270)
    
    #Reflexao Horizontal
    refl_h = tuple(tuple(linha)[::-1] for linha in salao_tuple)
    set_saloes.add(refl_h)
    
    #90
    salao_transposto = tuple(zip(*refl_h))
    salao_90 = tuple(tuple(linha)[::-1] for linha in salao_transposto)
    set_saloes.add(salao_90)
    
    #180
    salao_180 = tuple(tuple(linha)[::-1] for linha in salao_90)
    set_saloes.add(salao_180)
    
    #270
    salao_270 = tuple(tuple(linha)[::-1] for linha in salao_180)
    set_saloes.add(salao_270)
    
    
    #Reflexao Vertical
    
    refl_v = tuple(tuple(linha)[::-1] for linha in salao_180)
    set_saloes.add(refl_v)
    
    #90
    salao_transposto = tuple(zip(*refl_v))
    salao_90 = tuple(tuple(linha)[::-1] for linha in salao_transposto)
    set_saloes.add(salao_90)
    
    #180
    salao_180 = tuple(tuple(linha)[::-1] for linha in salao_90)
    set_saloes.add(salao_180)
    
    #270
    salao_270 = tuple(tuple(linha)[::-1] for linha in salao_180)
    set_saloes.add(salao_270)
    
    #Reflexao Diagonal Crescente
    
    refl_c = tuple(tuple(linha)[::-1] for linha in salao_270)
    set_saloes.add(refl_c)
    
    #90
    salao_transposto = tuple(zip(*refl_c))
    salao_90 = tuple(tuple(linha)[::-1] for linha in salao_transposto)
    set_saloes.add(salao_90)
    
    #180
    salao_180 = tuple(tuple(linha)[::-1] for linha in salao_90)
    set_saloes.add(salao_180)
    
    #270
    salao_270 = tuple(tuple(linha)[::-1] for linha in salao_180)
    set_saloes.add(salao_270)
    
    #Reflexao Diagonal Decrescente
    
    refl_dc = tuple(tuple(linha)[::-1] for linha in salao_90)
    set_saloes.add(refl_dc)
    
    #90
    salao_transposto = tuple(zip(*refl_dc))
    salao_90 = tuple(tuple(linha)[::-1] for linha in salao_transposto)
    set_saloes.add(salao_90)
    
    #180
    salao_180 = tuple(tuple(linha)[::-1] for linha in salao_90)
    set_saloes.add(salao_180)
    
    #270
    salao_270 = tuple(tuple(linha)[::-1] for linha in salao_180)
    set_saloes.add(salao_270)
    
start_time = time.time()


if len(sys.argv) != 4:
    print(len(sys.argv))
    
    print("Digite: python salao.py <num1> <num2> <num3>")
    sys.exit(1)

try:
    if not re.fullmatch(r'[0-9]+',sys.argv[1]) or not re.fullmatch(r'[0-9]+',sys.argv[2]) or not re.fullmatch(r'[0-9]+',sys.argv[3]):
        raise ValueError
except ValueError:
    print("Valores incorretos, numeros devem serem compostos exclusivamente de 0 e 1")
    sys.exit(1)
  
num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
num3 = int(sys.argv[3])
salao(num1,num2,num3)


print(len(set_saloes))

end_time = time.time()

elapsed_time = end_time - start_time

print("Time: {r:1.3f}".format(r=elapsed_time))