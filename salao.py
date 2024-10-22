import time
import sys
import re
contador = 0
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
                    salao[linha][coluna] = '.'
    elif c > 0:
        for linha in range(n):
            for coluna in range(n):
                if salao[linha][coluna] == '.' and verifica_existe_companheiro(salao, linha, coluna, vet, 'c'):
                    salao[linha][coluna] = 'c'
                    vet.append((linha,coluna))
                    posiciona(salao,n,b,c-1)
                    salao[linha][coluna] = '.'
    else:
        salao_tuple = tuple(map(tuple,salao))
        if salao_tuple not in set_saloes:
            if verifica_salao(salao,n):
                adiciona_set(salao,n) 
        
def verifica_existe_companheiro(salao, l, col, vet, pistoleiro):
    vet = sorted(vet)
    for tupla in vet:
        if l != tupla[0] or col != tupla[1]:
            if l == tupla[0] and col != tupla[1]:
                if salao[tupla[0]][tupla[1]] == pistoleiro:
                    return False
            elif col == tupla[1] and l != tupla[0]:
                if salao[tupla[0]][tupla[1]] == pistoleiro:
                    return False
            elif abs(col - tupla[1]) == abs(l - tupla[0]):
                if salao[tupla[0]][tupla[1]] == pistoleiro:
                    return False
     
    return True


def verifica_existe_inimigos(salao, l, col, vet, pistoleiro):
    inimigo = 'b'
    if pistoleiro == 'b':
        inimigo = 'c'
    cont = 0
    vet = sorted(vet)
    for tupla in vet:
        if l != tupla[0] and col != tupla[1]:
            if l == tupla[0] and col != tupla[1]:
                if salao[tupla[0]][tupla[1]] == inimigo:
                    cont+=1
            elif col == tupla[1] and l != tupla[0]:
                if salao[tupla[0]][tupla[1]] == inimigo:
                    cont+=1
            elif abs(col - tupla[1]) == abs(l - tupla[0]):
                if salao[tupla[0]][tupla[1]] == inimigo:
                    cont+=1
    
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

def validacao_pistoleiro(salao, linha, coluna, vet, pistoleiro):
    if verifica_existe_companheiro(salao,linha,coluna,vet,pistoleiro) and (verifica_existe_inimigos(salao, linha, coluna, vet, pistoleiro) >= 2):
        return True
    return False

def verifica_salao(salao,n):
    
    for linha in range(n):
        for coluna in range(n):
            if salao[linha][coluna] != '.':
                if not validacao_pistoleiro(salao, linha, coluna, vet, salao[linha][coluna]):
                    return False

    return True

def adiciona_set(salao,n):
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
    

def print_salao():
    with open('salao.txt', 'w+') as f:
        for salao in set_saloes:
        # 'salao' é uma tupla de tuplas, então iteramos sobre cada linha
            for linha in salao:
                f.write(' '.join(linha)+'\n')
            f.write('\n')  # Adiciona uma linha em branco entre os salões
    
# Current time before
start_time = time.time()


#if len(sys.argv) != 4:
#    print(len(sys.argv))
#    
#    print("Digite: python salao.py <num1> <num2> <num3>")
#    sys.exit(1)

#try:
#    if not re.fullmatch(r'[0-9]+',sys.argv[1]) or not re.fullmatch(r'[0-9]+',sys.argv[2]) or not re.fullmatch(r'[0-9]+',sys.argv[3]):
#        raise ValueError
#except ValueError:
#    print("Valores incorretos, numeros devem serem compostos exclusivamente de 0 e 1")
#    sys.exit(1)
  
#num1 = int(sys.argv[1])
#num2 = int(sys.argv[2])
#num3 = int(sys.argv[3])
#salao(num1,num2,num3)

salao(3,2,2)

#print_salao()
print(len(set_saloes))

#Current time afters
end_time = time.time()

elapsed_time = end_time - start_time

print("Time: {r:1.3f}".format(r=elapsed_time))