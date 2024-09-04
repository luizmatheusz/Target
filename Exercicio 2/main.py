# Existência e número de ocorrências da letra 'a' ou 'A'

# Função que verifica se, dentro de {s}, há a letra {a}, e conta o número de vezes em que ela aparece
def exist_and_count(a, s):
    exist = False
    count = 0
    
    a = a.lower()
    s = s.lower()
    
    if a in s:
        exist = True
        count = s.count(a)
        
    return exist, count
    
# Define a letra desejada
letra = 'a'

# Entrada
s = input("Entre com a string: ")

# Processamento da informação de entrada
exist, count = exist_and_count(letra, s)

# Saída
if exist:
    print(f"A letra '{letra}' esta presente na string. Ela aparece {count} vez(es).")
    
else:
    print(f"A letra {letra} nao esta presente na string.")
