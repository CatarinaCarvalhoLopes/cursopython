Dia 04 - Manipulação Avançada de Estruturas de Dados 🧠📊
✅ Assuntos estudados:
🔹 List Comprehension e Dict Comprehension – Compreensão de listas e dicionários
List comprehension permite criar listas de forma compacta e eficiente, usando uma única linha de código.

Dict comprehension é uma maneira de criar dicionários de maneira similar ao list comprehension.

python
Copiar
Editar
# Exemplo de List Comprehension
quadrados = [n * n for n in range(5)]
print(quadrados)  # Saída: [0, 1, 4, 9, 16]

# Exemplo de Dict Comprehension
cubos = {n: n * n * n for n in range(5)}
print(cubos)  # Saída: {0: 0, 1: 1, 2: 8, 3: 27, 4: 64}
📌 Observações:
Ambos são poderosos para criar novas estruturas de dados de forma compacta e eficiente.

Útil em contextos como filtrar e transformar dados em uma única linha.

🔹 Slicing Avançado – Cortes e manipulação de sequências
Slicing avançado permite manipular listas e strings de forma detalhada.

A sintaxe básica é sequencia[início:fim:passo], permitindo pegar partes das sequências de maneira flexível.

python
Copiar
Editar
# Exemplo de Slicing
cores = ["vermelho", "azul", "verde", "amarelo", "roxo"]
print(cores[:3])  # Saída: ['vermelho', 'azul', 'verde']

mensagem = "python é divertido"
print(mensagem[::-1])  # Saída: "odivridê é nohtyp"
📌 Observações:
Slicing permite reverter sequências, pegar partes específicas ou até pular elementos.

A sintaxe pode ser ajustada com o passo para otimizar operações.

🔹 Ordenação com Funções Personalizadas (key, sorted) – Organizando dados
sorted() e key são usados para ordenar listas e outras coleções de maneira personalizada.

A função key permite que você defina um critério de ordenação.

python
Copiar
Editar
# Exemplo de ordenação usando key
frutas = ["banana", "uva", "abacaxi", "kiwi"]
ordenadas = sorted(frutas, key=len)
print(ordenadas)  # Saída: ['kiwi', 'uva', 'banana', 'abacaxi']
📌 Observações:
Você pode ordenar usando critérios como tamanho, alfabético, ou ordem crescente/decrescente.

Utilizado também com dicionários e outras coleções.

🔹 Enumeração (enumerate) e Empacotamento (zip) – Trabalhando com índices e múltiplos iteráveis
enumerate() facilita obter o índice e o valor de elementos de uma lista ou sequência.

zip() combina dois ou mais iteráveis, criando pares de elementos correspondentes.

python
Copiar
Editar
# Exemplo de enumerate
frutas = ["banana", "uva", "abacaxi"]
for i, fruta in enumerate(frutas, start=1):
    print(i, fruta)
# Saída:
# 1 banana
# 2 uva
# 3 abacaxi

# Exemplo de zip
cores = ["amarelo", "vermelho", "roxo"]
for fruta, cor in zip(frutas, cores):
    print(f"{fruta} é da cor {cor}")
# Saída:
# banana é da cor amarelo
# uva é da cor vermelho
# abacaxi é da cor roxo
📌 Observações:
enumerate() é útil para iterar sobre sequências quando você precisa do índice.

zip() é ótimo para combinar várias listas em uma única iteração.

🔹 Manipulação de Strings Complexa (Fatiamento, Métodos Úteis, Expressões Regulares) – Trabalhando de forma avançada com texto
O fatiamento de strings é um recurso muito poderoso para acessar partes de strings.

Métodos úteis como lower(), strip(), replace(), split() e join() são usados frequentemente para manipular strings de forma eficiente.

Expressões regulares são usadas para buscar padrões complexos em strings.

python
Copiar
Editar
# Exemplo de fatiamento e manipulação de strings
frase = " Olá Mundo ".lower().strip()
print(f"Saudação manipulada: {frase}")  # Saída: "olá mundo"

# Exemplo de expressão regular para substituir texto
import re
texto = "O número é 123"
sub = re.sub(r"123", "999", texto)
print(sub)  # Saída: "O número é 999"
📌 Observações:
Fatiamento pode ser feito de várias maneiras, incluindo reversão de strings e seleção de caracteres específicos.

Expressões regulares são ferramentas poderosas para buscar e manipular texto conforme padrões.

✨ Quarto dia finalizado! Hoje, exploramos técnicas poderosas de manipulação de dados e strings. Agora estamos prontos para trabalhar com listas, dicionários e strings de maneira ainda mais avançada no Python! 🚀