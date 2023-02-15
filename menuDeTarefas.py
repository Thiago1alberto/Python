
while True:
    print("MENU DE TAREFAS")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Marcar tarefa como concluída")
    print("4. Sair")

    choice = input("Escolha uma opção: ")

    if choice == "1":
        task = input("Digite a tarefa: ")
        tasks.append(task)
        print("Tarefa adicionada com sucesso!")
    elif choice == "2":
        if len(tasks) == 0:
            print("Não há tarefas adicionadas.")
        else:
            print("Lista de tarefas:")
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task}")
    elif choice == "3":
        if len(tasks) == 0:
            print("Não há tarefas adicionadas.")
        else:
            task_index = int(input("Digite o número da tarefa concluída: "))
            if task_index < 1 or task_index > len(tasks):
                print("Índice inválido.")
            else:
                tasks.pop(task_index - 1)
                print("Tarefa marcada como concluída!")
    elif choice == "4":
        print("Obrigado por usar o menu de tarefas.")
        break
    else:
        print("Opção inválida. Tente novamente.")
