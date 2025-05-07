nome = "Ana"
idade = 30

print("Olá,", nome)
print("Você tem", idade, "anos.")
 # ///////variáveis com print////////////




a = 10
b = 3

# Operações matemáticas
soma = a + b
print("Soma:", soma)

# Comparação
comparacao = a > b
print("A é maior que B?", comparacao)
  # /////////// Exercicio de operadores /////////////




contador = 1  # Começamos no número 1
while contador <= 10:  # Enquanto contador for menor ou igual a 10
    print(contador)  # Vai imprimir o número
    contador += 1  # Vai aumentar o número em 1 a cada vez

for i in range(1, 11):  # Isso vai contar de 1 até 10
    print(i)  # Vai imprimir os números um a um
# //////////laços de repetição for e while ///////////////




def soma():
    a = int(input("Digite um número: "))
    b = int(input("Digite mais um número: "))
    resultado = a + b
    print("A soma dos dois números é:", resultado)

soma()
# /////////funções///////




def maioridade():
    a = int(input("Digite a sua idade: "))
    if a >= 18:
        print("Você é maior de idade")
    else:
        print("Você é menor de idade")

maioridade()
 # ///////////////funções com if e else///////////////




def classificar():
    n = int(input("Digite um número: "))
    if n > 0:
        print("Positivo")
    elif n < 0:
        print("Negativo")
    else:
        print("O número é 0")

classificar()
 # /////////funções com elif //////////



filmes = ["Barbie", "Aladdin", "Frozen"] 

for filme in filmes:
    print("Eu assisti", filme)

filmes.append("Lupin") 

print("Agora a lista tem:")
for filme in filmes:
    print(filme)
 # /////////// lista e adição na lista com append ////////////



numeros = [2, 4, 6, 1, 7]

# Mostra um por um
for numero in numeros:
    print("Número:", numero)

# Agora somamos tudo
soma = sum(numeros)
print("A soma de todos os números é:", soma)
 # /////////Somando numeros da lista com sum ///////////



dados = { 
    "Ana": {"idade": 14, "cidade": "Maceió"},
    "Cat": {"idade": 24, "cidade": "SP"},
    "Leo": {"idade": 27, "cidade": "NY"}
}

# Mostrar o nome e idade de 'Cat'
print("Nome: Cat, Idade:", dados["Cat"]["idade"])

# Adicionar telefone para 'Cat'
dados["Cat"]["telefone"] = "18981060051"

# Mudar cidade de 'Cat'
dados["Cat"]["cidade"] = "Guarulhos"

# Remover idade de 'Cat'
del dados["Cat"]["idade"]

# Exibir o dicionário atualizado
print(dados)
# ////////// Dicionário aprendendo como adicionar, excluir e modificar itens da chave. //////////

#//// PROJETO DE CALCULADORA SIMPLES /////
def calculadora():
    n1 = int(input("Digite um numero: "))  # Fechando os parênteses
    n2 = int(input("Digite outro numero: "))  # Fechando os parênteses
    escolha = input('Digite "a" se quiser somar, "b" se quiser subtrair, "c" se quiser multiplicar e "d" se quiser dividir: ')
    
    if escolha == "a":  # Usando "==" para comparação
        soma = n1 + n2
        print("Resultado da soma:", soma)
    elif escolha == "b":
        sub = n1 - n2
        print("Resultado da subtração:", sub)
    elif escolha == "c":
        multi = n1 * n2
        print("Resultado da multiplicação:", multi)
    elif escolha == "d":
        if n2 != 0:  # Verificando se n2 não é zero para evitar divisão por zero
            divis = n1 / n2
            print("Resultado da divisão:", divis)
        else:
            print("Não é possível dividir por zero!")
    else:
        print("Escolha inválida!")

calculadora()
