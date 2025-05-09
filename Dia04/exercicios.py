#### List e Dict Comprehension ####
# 1. Lista com cubos (versão correta como lista)
cubos = [n * n * n for n in range(5)]
print(cubos)

# 3. Dicionário com triplo (corrigido: de 1 a 3)
triplo = {n: n * 3 for n in range(1, 4)}
print(triplo)

# 2. Lista com múltiplos de 3 de 1 a 10
multiplos = [n for n in range(1, 11) if n % 3 == 0]
print(multiplos)

# 4. Dicionário com contagem de letras da palavra "banana"
frequencia = {letra: "banana".count(letra) for letra in set("banana")}
print(frequencia)

##### Slicing Avançado #####

# Lista de frutas
frutas = ["maçã", "banana", "uva", "kiwi", "abacaxi"]

print(frutas[1:4])      # ['banana', 'uva', 'kiwi']
print(frutas[:3])       # ['maçã', 'banana', 'uva']
print(frutas[::2])      # ['maçã', 'uva', 'abacaxi']
print(frutas[::-1])     # ['abacaxi', 'kiwi', 'uva', 'banana', 'maçã']

# String com slicing
texto = "programar"
print(texto[0:7:2])     # 'pormr'
print(texto[::-1])      # 'ramargorp'

# Exercícios resolvidos

# 1. Três primeiros elementos
cores = ["vermelho", "azul", "verde", "amarelo", "roxo"]
print(cores[:3])        # ['vermelho', 'azul', 'verde']

# 2. Inverter string
mensagem = "python é divertido"
print(mensagem[::-1])   # 'oditrev id é nohtyp'

# 3. Caracteres nas posições pares
palavra = "codelandia"
print(palavra[::2])     # 'cdlnia'

# 4. Inverter lista
numeros = [1, 2, 3, 4, 5]
print(numeros[::-1])    # [5, 4, 3, 2, 1]
 

##### Sorted e Key #####

# 1. Ordem alfabética
frutas = ["banana", "uva", "abacaxi", "kiwi"]
ordenadas = sorted(frutas)
print(ordenadas)  # ['abacaxi', 'banana', 'kiwi', 'uva']

# 2. Ordem pelo tamanho
print(sorted(frutas, key=len))  # ['uva', 'kiwi', 'banana', 'abacaxi']

# 3. Ordem pelo último caractere
palavras = ["tigre", "cobra", "elefante", "boi"]
print(sorted(palavras, key=lambda x: x[-1]))  
# ['cobra', 'elefante', 'tigre', 'boi']

# 4. Ordenar dicionário pelas notas
notas = {"Lucas": 8, "Marina": 6, "João": 9}
ordenado = sorted(notas.items(), key=lambda x: x[1])
print(ordenado)  # [('Marina', 6), ('Lucas', 8), ('João', 9)]


##### Enumeração (enumerate) e empacotamento (zip) #####

#enumerate
filmes = ["Barbie", "Lupin", "Viva"]

for i, nome in enumerate(filmes, start=1):
    print(f"{i}. {nome}")

#zip
frutas = ["banana", "morango", "uva"]
cores = ["amarelo", "vermelho", "roxo"]

for fruta, cor in zip(frutas, cores):
    print(f"{fruta} é da cor {cor}")


##### Manipulação de strings complexa #####

#fatiamento slicing
frase = "Codelândia"
print(frase[4:])  # "lândia"

mensagem = "Python é massa"
print(mensagem[::-1])  # "assam é nohtyP"

palavra = "programação"
print(palavra[::2])  # "pormrço"

#métodos úteis
# 1. Transformar para minúsculo e remover espaços
saudação = " Olá Mundo ".lower().strip()
print(saudação)  # "olá mundo"

# 2. Substituir "vermelho" por "azul"
frase = "O carro vermelho passou".replace("vermelho", "azul")
print(frase)  # "O carro azul passou"

# 3. Separar a string "maçã,banana,uva" em uma lista
frutas = "maçã,banana,uva".split(",")
print(frutas)  # ['maçã', 'banana', 'uva']

# 4. Juntar itens de uma lista com "-"
n = "-".join(["um", "dois", "três"])
print(n)  # "um-dois-três"

##### Expressões Regulares #####

import re

# Exercício 1: Encontrar a primeira palavra que começa com "f"
texto = "O foguete voa rápido"
# Usando re.search() para encontrar a primeira palavra que começa com "f"
resultado = re.search(r"\bf\w*", texto, re.IGNORECASE)
if resultado:
    print("Primeira palavra que começa com 'f':", resultado.group())  # "foguete"
else:
    print("Nenhuma palavra encontrada.")

# Exercício 2: Substituir o número 123 por 999
frase = "O número é 123"
# Usando re.sub() para substituir "123" por "999"
sub = re.sub(r"123", "999", frase)
print("Frase após substituição:", sub)  # "O número é 999"

# Exercício 3: Encontrar todas as palavras com mais de 4 letras
texto = "Eu adoro Python e programação"
# Encontrando todas as palavras usando \w+ (que encontra sequências de caracteres alfanuméricos)
palavras = re.findall(r"\w+", texto)
# Filtrando palavras que têm mais de 4 letras
palavras_com_mais_de_4 = [p for p in palavras if len(p) > 4]
print("Palavras com mais de 4 letras:", palavras_com_mais_de_4)  # ['adoro', 'Python', 'programação']

