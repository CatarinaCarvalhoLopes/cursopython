#### abrindo a lista de tarefas ####
tarefas = []

#### fazendo a função "adicionar tarefas"
def adicionar_tarefa(titulo):
    nova_tarefa = {
        "Id": len(tarefas) + 1,
        "Titulo": titulo,
        "Status": "Pendente"
    }
    tarefas.append(nova_tarefa)

#### fazendo a função "listar tarefas"
def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
    else:
        for tarefa in tarefas:
            print(f"[{tarefa['Id']}] {tarefa['Titulo']} - {tarefa['Status']}")

#### fazendo a função "remover tarefas"
def remover_tarefa(id):
    for i, tarefa in enumerate(tarefas):
        if tarefa["Id"] == id:
            del tarefas[i]
            print(f"Tarefa com ID {id} removida com sucesso.")
            return
    print(f"Tarefa com ID {id} não encontrada.")


#### fazendo a função "concluir tarefas"
def concluir_tarefa(id):
    for tarefa in tarefas:
        if tarefa["Id"] == id:
            tarefa["Status"] = "Concluída"
            print(f"Tarefa com ID {id} concluída.")
            return
    print(f"Tarefa com ID {id} não encontrada.")


#### fazendo a função "filtrar tarefas"
def filtrar_tarefas(status):
    encontrou = False
    for tarefa in tarefas:
        if tarefa["Status"].lower() == status.lower():
            print(f"[{tarefa['Id']}] {tarefa['Titulo']} - {tarefa['Status']}")
            encontrou = True
    if not encontrou:
        print("Nenhuma tarefa encontrada.")


#### fazendo a função "gerar estatisticas"
def gerar_estatisticas():
    total = len(tarefas)
    pendentes = sum(1 for t in tarefas if t["Status"] == "Pendente")
    concluidas = sum(1 for t in tarefas if t["Status"] == "Concluída")

    print(f"Total de tarefas: {total}")
    print(f"Tarefas pendentes: {pendentes}")
    print(f"Tarefas concluídas: {concluidas}")


#### fazendo a função "Menú"
def menu():
    print("\n📋 MENU DE OPÇÕES")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Remover tarefa")
    print("4. Concluir tarefa")
    print("5. Filtrar por status")
    print("6. Ver estatísticas")
    print("7. Sair")
    escolha = input("Escolha uma opção: ")


### Escolhas
    if escolha == "1":
        while True:
            titulo = input("Digite o título da tarefa (ou 0 para voltar): ")
            if titulo == "0":
                break
            adicionar_tarefa(titulo)

    elif escolha == "2":
        listar_tarefas()

    elif escolha == "3":
        while True:
            entrada = input("Digite o ID da tarefa para remover (ou 0 para voltar): ")
            if entrada == "0":
                break
            if entrada.isdigit():
                remover_tarefa(int(entrada))
            else:
                print("Digite um número válido.")

    elif escolha == "4":
        while True:
            entrada = input("Digite o ID da tarefa para concluir (ou 0 para voltar): ")
            if entrada == "0":
                break
            if entrada.isdigit():
                concluir_tarefa(int(entrada))
            else:
                print("Digite um número válido.")

    elif escolha == "5":
        while True:
            status = input("Digite o status (Pendente ou Concluída) ou 0 para voltar: ")
            if status == "0":
                break
            filtrar_tarefas(status)

    elif escolha == "6":
        gerar_estatisticas()

    elif escolha == "7":
        print("Saindo... até logo!")
        exit()

    else:
        print("Opção inválida.")
#chamando o menu
menu()
