import time
import sys
import re
contador = 0
time_verificacao = 0
set_saloes = set()
def salao(n,b,c):
    if not verifica_quant(n,b,c):
        return 0

    salao = [['.' for _ in range(n)] for _ in range(n)]
    
    #posiciona(salao,n,b,c,id)
    posiciona(salao,n,b,c)
    
    return salao

def posiciona(salao,n,b,c):    
    if b > 0:
        for linha in range(n):
            for coluna in range(n):
                if salao[linha][coluna] == '.' and verifica_adj(salao,n,linha,coluna,'b'):
                    salao[linha][coluna] = 'b'
                    posiciona(salao,n,b-1,c)
                    salao[linha][coluna] = '.'
                    #if b == 1:  
                    #    return
    elif c > 0:
        for linha in range(n):
            for coluna in range(n):
                if salao[linha][coluna] == '.' and verifica_existe_companheiro(salao, n, linha, coluna, 'c'):
                    salao[linha][coluna] = 'c'
                    posiciona(salao,n,b,c-1)
                    salao[linha][coluna] = '.'
                    #if c == 1:  
                    #    return
    else:
        salao_tuple = tuple(map(tuple,salao))
        if salao_tuple not in set_saloes:
            if verifica_salao(salao,n):
                adiciona_set(salao,n) 
        
def verifica_existe_companheiro(salao, n, l, col, pistoleiro):
    # Verifica se existe algum companheiro acima dele
    for l1 in range(l-1, -1, -1):
        if salao[l1][col] == pistoleiro:
            return False
        elif salao[l1][col] != '.':
            break
        
    # Verifica se existe algum companheiro abaixo dele
    for l2 in range(l+1, n):
        if salao[l2][col] == pistoleiro:
            return False
        elif salao[l2][col] != '.':
            break
    
    # Verifica se existe algum companheiro à esquerda
    for c1 in range(col-1, -1, -1):
        if salao[l][c1] == pistoleiro:
            return False
        elif salao[l][c1] != '.':
            break
    
    # Verifica se existe algum companheiro à direita
    for c2 in range(col+1, n):
        if salao[l][c2] == pistoleiro:
            return False
        elif salao[l][c2] != '.':
            break
    
    # Verifica a diagonal superior esquerda
    for l3, c3 in zip(range(l-1, -1, -1), range(col-1, -1, -1)):
        if salao[l3][c3] == pistoleiro:
            return False
        elif salao[l3][c3] != '.':
            break
    
    # Verifica a diagonal superior direita
    for l4, c4 in zip(range(l-1, -1, -1), range(col+1, n)):
        if salao[l4][c4] == pistoleiro:
            return False
        elif salao[l4][c4] != '.':
            break
        
    # Verifica a diagonal inferior esquerda
    for l5, c5 in zip(range(l+1, n), range(col-1, -1, -1)):
        if salao[l5][c5] == pistoleiro:
            return False
        elif salao[l5][c5] != '.':
            break
    
    # Verifica a diagonal inferior direita
    for l6, c6 in zip(range(l+1, n), range(col+1, n)):
        if salao[l6][c6] == pistoleiro:
            return False
        elif salao[l6][c6] != '.':
            break

    # Se não encontrou companheiro em nenhuma direção, retorna True
    return True


def verifica_existe_inimigos(salao, n, l, col, pistoleiro):
    # Determina o inimigo com base no pistoleiro
    inimigo = 'c' if pistoleiro == 'b' else 'b'
    cont = 0  # Contador de inimigos encontrados

    # Verifica se há inimigos acima
    for l1 in range(l-1, -1, -1):
        if salao[l1][col] == inimigo:
            cont += 1
            break  # Para após encontrar um inimigo
    
    # Verifica se há inimigos abaixo
    for l2 in range(l+1, n):
        if salao[l2][col] == inimigo:
            cont += 1
            break
    
    # Verifica se há inimigos à esquerda
    for c1 in range(col-1, -1, -1):
        if salao[l][c1] == inimigo:
            cont += 1
            break
    
    # Verifica se há inimigos à direita
    for c2 in range(col+1, n):
        if salao[l][c2] == inimigo:
            cont += 1
            break
    
    # Verifica a diagonal superior esquerda
    for l3, c3 in zip(range(l-1, -1, -1), range(col-1, -1, -1)):
        if salao[l3][c3] == inimigo:
            cont += 1
            break
    
    # Verifica a diagonal superior direita
    for l4, c4 in zip(range(l-1, -1, -1), range(col+1, n)):
        if salao[l4][c4] == inimigo:
            cont += 1
            break
    
    # Verifica a diagonal inferior esquerda
    for l5, c5 in zip(range(l+1, n), range(col-1, -1, -1)):
        if salao[l5][c5] == inimigo:
            cont += 1
            break
    
    # Verifica a diagonal inferior direita
    for l6, c6 in zip(range(l+1, n), range(col+1, n)):
        if salao[l6][c6] == inimigo:
            cont += 1
            break
    
    return cont  # Retorna o número de inimigos encontrados


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

def validacao_pistoleiro(salao, n, linha, coluna, pistoleiro):
    if verifica_existe_companheiro(salao,n,linha,coluna,pistoleiro) and (verifica_existe_inimigos(salao, n, linha, coluna, pistoleiro) >= 2):
        return True
    return False

def verifica_salao(salao,n):
    
    for linha in range(n):
        for coluna in range(n):
            if salao[linha][coluna] != '.':
                if not validacao_pistoleiro(salao, n, linha, coluna, salao[linha][coluna]):
                    return False

    return True

def adiciona_set(salao,n):
    #print('Salao ')
    #adiciona_salao(salao)
    #adiciona_reflexoes_salao(salao,n)
    #adiciona_rotacoes_salao(salao)
    
    #add salao
    salao_tuple = tuple(map(tuple,salao))
    #print_salao(salao_tuple)
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
    
    
        
def adiciona_reflexoes_salao(salao,n):
    refl_h, refl_v, refl_c, refl_dc= reflexoes_salao(salao,n)
    #print('Reflexao H')
    adiciona_salao(refl_h)
    adiciona_rotacoes_salao(refl_h)
    #print('Reflexao V')
    adiciona_salao(refl_v)
    adiciona_rotacoes_salao(refl_v)
    #print('Reflexao C')
    adiciona_salao(refl_c)
    adiciona_rotacoes_salao(refl_c)
    #print('Reflexao DC')
    adiciona_salao(refl_dc)   
    adiciona_rotacoes_salao(refl_dc)

def adiciona_rotacoes_salao(salao):
    salao_90, salao_180, salao_270 = rotacoes_salao(salao)
    #print('Rotacao 90')
    adiciona_salao(salao_90)
    #print('Rotacao 180')
    adiciona_salao(salao_180)
    #print('Rotacao 270')
    adiciona_salao(salao_270)
    
def adiciona_salao(salao):
    salao_tuple = tuple(map(tuple,salao))
    #print_salao(salao_tuple)
    set_saloes.add(salao_tuple)
    
def rotacoes_salao(salao):
    #start_time = time.time()
    
    salao_90 = rotaciona_90(salao)
    salao_180 = rotacionar_180_graus(salao)
    salao_270 = rotacionar_270_graus(salao)
    #Current time after
    #end_time = time.time()

    #elapsed_time = end_time - start_time

    #print("Time Rotacoes: {r:1.3f}".format(r=elapsed_time))
    return salao_90, salao_180, salao_270   

def reflexoes_salao(salao,n):
    
    return refletir_verticalmente(salao), refletir_horizontalmente(salao), refletir_diagonal_crescente(salao,n), refletir_diagonal_decrescente(salao,n)
    
def rotaciona_90(salao):
    salao_transposto = list(zip(*salao))
    salao_rotacionado = [list(linha)[::-1] for linha in salao_transposto]
    return salao_rotacionado

def rotacionar_180_graus(matriz):
    return [linha[::-1] for linha in matriz[::-1]]

def rotacionar_270_graus(matriz):
    return list(zip(*matriz))[::-1]

def refletir_horizontalmente(salao):
    return [linha[::-1] for linha in salao]

def refletir_verticalmente(salao):
    return salao[::-1]

def refletir_diagonal_crescente(salao,n):
    return [[salao[j][i] for j in range(n)] for i in range(n)]

def refletir_diagonal_decrescente(salao,n):
    return [[salao[n - 1 - j][n - 1 - i] for j in range(n)] for i in range(n)]

def print_salao():
    with open('salao.txt', 'w+') as f:
        for salao in set_saloes:
        # 'salao' é uma tupla de tuplas, então iteramos sobre cada linha
            for linha in salao:
                f.write(' '.join(linha)+'\n')
            f.write('\n')  # Adiciona uma linha em branco entre os salões
    
# Current time before
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

#salao(4,3,3)

#print_salao()
print(len(set_saloes))

#Current time afters
end_time = time.time()

elapsed_time = end_time - start_time

print("Time: {r:1.3f}".format(r=elapsed_time))