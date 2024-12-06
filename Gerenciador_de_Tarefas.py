tarefas = []
print("Bem vindo(a) ao Gerenciador de Tarefas")

def menu():
    print("\n=== Lista de Tarefas ===")
    print("1. Adicionar Tarefa")
    print("2. Exibir tarefa")
    print("3. Concluir tarefa")
    print("4. Remover tarefa")
    print("5. Sair")
    return int(input("Escola uma opção: "))

while True:
    opcao = menu()

    if opcao == 1:
        tarefa = input("Digite a tarefa: ")
        tarefas.append(tarefa)
        print(f"Tarefa {tarefa} adicionada".title())

    elif opcao == 2:
        print("\n=== Lista de Tarefas ===")
        if not tarefas:
            print("Nenhuma tarefa para exibir")
        else:
            for i, tarefa in enumerate (tarefas, start=1):
                print(f"{i}. {tarefa}".title())

    elif opcao == 3:
        if not tarefas:
            print("Nenhuma tarefa concluiada")
        else:
            print("\n=== Concluir tarefa ===")
            for i, tarefa in enumerate (tarefas, start=1):
                print(f"{i}. {tarefa}")
            num = int(input("Digite o número da tarefa: "))
            if 1 <= num <= len(tarefas):
                tarefa_concluiada = tarefas.pop(num - 1)
                print(f"Tarefa '{tarefa_concluiada}' concluida! ")
            else:
                print("Codigo invalido")

    elif opcao == 4:
        if not tarefas:
            print("Nenhuma tarefa para remover")
        else:
            print("\n=== Remover tarefa ===")
            for i, tarefa in enumerate (tarefas, start=1):
                print(f"{i}. {tarefa}")
            num = int(input("Digite o número da tarefa: "))
            if 1 <= num <= len(tarefas):
                tarefa_removida = tarefas.pop(num -1)
                print(f"Tarefa '{tarefa_removida}' removida! ")
            else:
                print("Codigo invalido")

    elif opcao == 5:
        print("Saindo do Gerenciador de tarefas.")
        break
    else:
        print("Codigo invalido")
