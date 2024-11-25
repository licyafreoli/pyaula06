# import json  # Importa o módulo JSON para manipulação de dados em formato JSON

# categorias_validas = {"Trabalho", "Pessoal", "Estudos", "Saúde"}  # Conjunto com categorias válidas para as tarefas
# prioridades_validas = {"Baixa", "Média", "Alta"}  # Conjunto com prioridades válidas para as tarefas

# tarefas = {}  # Dicionário para armazenar as tarefas

# def adicionar_tarefa(titulo, descricao, categoria, prioridade):
#     # Verifica se a categoria fornecida é válida
#     if categoria not in categorias_validas:
#         return f"Categoria inválida. Escolha entre: {', '.join(categorias_validas)}"
#     # Verifica se a prioridade fornecida é válida
#     if prioridade not in prioridades_validas:
#         return f"Prioridade inválida. Escolha entre: {', '.join(prioridades_validas)}"
    
#     # Cria um novo ID para a tarefa com base no número de tarefas existentes
#     id_tarefa = len(tarefas) + 1
#     # Adiciona a tarefa ao dicionário de tarefas
#     tarefas[id_tarefa] = {
#         "titulo": titulo,
#         "descricao": descricao,
#         "categoria": categoria,
#         "prioridade": prioridade,
#     }
#     return f"Tarefa '{titulo}' adicionada com sucesso!"  # Retorna uma mensagem de sucesso

# def listar_tarefas():
#     # Verifica se existem tarefas
#     if not tarefas:
#         return "Nenhuma tarefa encontrada."
#     # Retorna uma lista formatada de tarefas
#     return [
#         f"{id_tarefa}: {info['titulo']} - {info['categoria']} - {info['prioridade']}"
#         for id_tarefa, info in tarefas.items()
#     ]

# def remover_tarefa(id_tarefa):
#     # Verifica se o ID da tarefa existe no dicionário
#     if id_tarefa in tarefas:
#         del tarefas[id_tarefa]  # Remove a tarefa do dicionário
#         return f"Tarefa {id_tarefa} removida com sucesso."
#     return "ID da tarefa não encontrado."  # Retorna uma mensagem de erro se o ID não existir

# def salvar_tarefas():
#     # Abre o arquivo tarefas.json no modo de escrita
#     with open("tarefas.json", "w") as arquivo:
#         json.dump(tarefas, arquivo)  # Salva o dicionário de tarefas no arquivo

# def carregar_tarefas():
#     global tarefas  # Define que a variável tarefas é global
#     try:
#         # Tenta abrir o arquivo tarefas.json no modo de leitura
#         with open("tarefas.json", "r") as arquivo:
#             tarefas = json.load(arquivo)  # Carrega o conteúdo do arquivo para o dicionário tarefas
#     except FileNotFoundError:
#         tarefas = {}  # Se o arquivo não for encontrado, inicializa tarefas como um dicionário vazio

# def menu():
#     carregar_tarefas()  # Carrega as tarefas ao iniciar o menu
#     while True:
#         # Exibe o menu de opções
#         print("\nMenu de Gerenciamento de Tarefas:")
#         print("1. Adicionar Tarefa")
#         print("2. Listar Tarefas")
#         print("3. Remover Tarefa")
#         print("4. Salvar e Sair")
        
#         opcao = input("Escolha uma opção: ")  # Recebe a escolha do usuário
        
#         if opcao == "1":
#             # Pede os dados da nova tarefa
#             titulo = input("Título: ")
#             descricao = input("Descrição: ")
#             categoria = input(f"Categoria ({', '.join(categorias_validas)}): ")
#             prioridade = input(f"Prioridade ({', '.join(prioridades_validas)}): ")
#             # Adiciona a nova tarefa
#             print(adicionar_tarefa(titulo, descricao, categoria, prioridade))
        
#         elif opcao == "2":
#             # Lista todas as tarefas
#             print("\n".join(listar_tarefas()))
        
#         elif opcao == "3":
#             try:
#                 # Recebe o ID da tarefa a ser removida
#                 id_tarefa = int(input("ID da Tarefa a remover: "))
#                 # Remove a tarefa
#                 print(remover_tarefa(id_tarefa))
#             except ValueError:
#                 # Trata o erro se o ID não for um número válido
#                 print("ID inválido!")
        
#         elif opcao == "4":
#             # Salva as tarefas e encerra o programa
#             salvar_tarefas()
#             print("Tarefas salvas. Até logo!")
#             break
        
#         else:
#             print("Opção inválida!")  # Trata a escolha inválida do menu

# if __name__ == "__main__":
#     menu()  # Chama a função menu se o script for executado diretamente
