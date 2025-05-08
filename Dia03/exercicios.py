##### Decoradores #####
def fala_antes_e_depois(fala):
    def falando():
        print("🗣 Vou começar!")
        fala()
        print("🏁 Terminei!")
    return falando

@fala_antes_e_depois
def fala_algo():
    print("Olá, mundo!")

fala_algo()
 
##### Recursão ######

def soma(n):
    if n == 1:
        return 1
    else:
        return n + soma(n - 1)

print(soma(5))
