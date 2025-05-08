# Dia 03 - Funções em Python: Decoradores e Recursão 🔁✨

## ✅ Assuntos estudados:

### 🔹 Decoradores – Funções que modificam outras funções
- Decoradores são usados para **"envolver"** uma função e adicionar funcionalidades extras **sem alterar o código original**.
- Usam a sintaxe `@decorador` acima da função que será decorada.

```python
def meu_decorador(func):
    def wrapper():
        print("Antes da função")
        func()
        print("Depois da função")
    return wrapper

@meu_decorador
def diga_oi():
    print("Oi!")

diga_oi()
# Saída:
# Antes da função
# Oi!
# Depois da função
```

#### 📌 Observações:
- Decoradores são muito usados com funções como `@staticmethod`, `@classmethod` e `@property`.
- Também aparecem bastante em bibliotecas como Flask e Django.

---

### 🔹 Recursão – Funções que chamam a si mesmas
- Uma função recursiva é aquela que **se chama dentro de si mesma**, geralmente para resolver um problema que pode ser dividido em partes menores.
- Toda função recursiva precisa ter um **caso base**, que impede chamadas infinitas.

```python
def contagem_regressiva(n):
    if n == 0:
        print("Pronto!")
    else:
        print(n)
        contagem_regressiva(n - 1)

contagem_regressiva(3)
# Saída:
# 3
# 2
# 1
# Pronto!
```

#### Outro exemplo: soma de 1 até `n`
```python
def soma(n):
    if n == 1:
        return 1
    else:
        return n + soma(n - 1)

print(soma(5))  # Saída: 15
```

#### 📌 Observações:
- Recursão é útil para problemas como:
  - Fatorial
  - Sequência de Fibonacci
  - Percorrer estruturas como árvores e diretórios
- Pode ser substituída por laços (`for`, `while`) em muitos casos.
- **Atenção:** recursão profunda demais pode causar `RecursionError`.

---

✨ Terceiro dia finalizado! Decoradores e recursão são superpoderes no Python – com eles, a gente começa a pensar como programador ninja! 💻⚡