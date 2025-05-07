####Função nomeada e padrão####
def boas_vindas(nome="visitante"):
    print(f"Bem-vindo(a), {nome}!")

boas_vindas()
boas_vindas("Catarina")


#### Args###
def apresentar_amigos(*amigos):
    lista_nomes = ", ".join(amigos)
    print(f"Meus amigos são: {lista_nomes}")

apresentar_amigos("Ana", "Maria", "Bete", "Samyra", "Rafa")

#### kwrags ####
def dados_pessoais(**dados):
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")

dados_pessoais(nome="Catarina", idade=23, profissão="Professora")

#### lambda #####
nomes = ["gato", "elefante", "cão", "pombo", "boi"]
nomes_ordenados = sorted(nomes, key=lambda nome: len(nome))
print(nomes_ordenados)

numeros = [1, 2, 3, 4]
dobro = lambda numero: numero * 2
resultado = list(map(dobro, numeros))
print(resultado)


multi = lambda x, y: x * y
print(multi(4, 8))


