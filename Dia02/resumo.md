# Dia 02 - Funções em Python: `*args`, `**kwargs`, `lambda` e parâmetros padrão 🧠

## ✅ Assuntos estudados:

### 🔹 `*args` – Argumentos posicionais variáveis
- Permite passar vários argumentos para uma função.
- Eles são recebidos como uma **tupla**.

```python
def somar(*args):
    return sum(args)

print(somar(1, 2, 3))  # Saída: 6
```

### 🔹 `**kwargs` – Argumentos nomeados variáveis
- Permite passar vários **argumentos com nome**.
- Eles são recebidos como um **dicionário**.

```python
def exibir_info(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

exibir_info(nome="João", idade=30)
# Saída:
# nome: João
# idade: 30
```

### 🔹 Parâmetros padrão
- Uma função pode ter **valores padrão** nos parâmetros.
- Se não for passado um valor, o padrão será usado.

```python
def cumprimentar(nome="amigo"):
    print(f"Olá, {nome}!")

cumprimentar()            # Saída: Olá, amigo!
cumprimentar("Camila")    # Saída: Olá, Camila!
```

### 🔹 Funções `lambda`
- Funções **anônimas**, úteis para funções simples.
- Sintaxe curta: `lambda argumentos: expressão`

```python
quadrado = lambda x: x ** 2
print(quadrado(4))  # Saída: 16
```

Também podem ser usadas com funções como `map()`, `filter()`, etc.

```python
numeros = [1, 2, 3, 4]
dobros = list(map(lambda x: x * 2, numeros))
print(dobros)  # Saída: [2, 4, 6, 8]
```

## 📌 Observações:
- `*args` e `**kwargs` podem ser usados juntos na **ordem correta**:  
  `def funcao(padrao, *args, **kwargs):`
- `lambda` não substitui `def` para funções grandes — é ideal para expressões simples.
- Usar parâmetros padrão ajuda a evitar erros quando a função for chamada sem argumentos.

---

✨ Segundo dia finalizado! Cada função que aprendemos hoje é uma nova ferramenta na nossa caixinha. Vamos em frente! 🚀
