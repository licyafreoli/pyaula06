import json

categorias_validas = {"Trabalho", "Pessoal", "Estudos", "Saúde"}
prioridades_validas = {"Baixa", "Média", "Alta"}

tarefas = {}

def adicionar_tarefa(titulo, descricao, categoria, prioridade):
    if categoria not in categorias_validas:
        return f"Categoria inválida. Escolha entre: {', '.join(categorias_validas)}"
    if prioridade not in prioridades_validas:
        return f"Prioridade inválida. Escolha entre: {', '.join(prioridades_validas)}"
    
    id_tarefa = len(tarefas) + 1
    tarefas[id_tarefa] = {
        "titulo": titulo,
        "descricao": descricao,
        "categoria": categoria,
        "prioridade": prioridade,
    }
    return f"Tarefa '{titulo}' adicionada com sucesso!"

def listar_tarefas():
    if not tarefas:
        return "Nenhuma tarefa encontrada."
    return [
        f"{id_tarefa}: {info['titulo']} - {info['categoria']} - {info['prioridade']}"
        for id_tarefa, info in tarefas.items()
    ]

def remover_tarefa(id_tarefa):
    if id_tarefa in tarefas:
        del tarefas[id_tarefa]
        return f"Tarefa {id_tarefa} removida com sucesso."
    return "ID da tarefa não encontrado."

#JSON
def salvar_tarefas():
    with open("tarefas.json", "w") as arquivo:
        json.dump(tarefas, arquivo)

#JSON
def carregar_tarefas():
    global tarefas
    try:
        with open("tarefas.json", "r") as arquivo:
            tarefas = json.load(arquivo)
    except FileNotFoundError:
        tarefas = {}

def menu():
    carregar_tarefas()
    while True:
        print("\nMenu de Gerenciamento de Tarefas:")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Remover Tarefa")
        print("4. Salvar e Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            titulo = input("Título: ")
            descricao = input("Descrição: ")
            categoria = input(f"Categoria ({', '.join(categorias_validas)}): ")
            prioridade = input(f"Prioridade ({', '.join(prioridades_validas)}): ")
            print(adicionar_tarefa(titulo, descricao, categoria, prioridade))
        
        elif opcao == "2":
            print("\n".join(listar_tarefas()))
        
        elif opcao == "3":
            try:
                id_tarefa = int(input("ID da Tarefa a remover: "))
                print(remover_tarefa(id_tarefa))
            except ValueError:
                print("ID inválido!")
        
        elif opcao == "4":
            salvar_tarefas()
            print("Tarefas salvas. Até logo!")
            break
        
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()
