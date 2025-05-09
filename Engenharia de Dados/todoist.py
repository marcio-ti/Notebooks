"""
Classe destinada a criar a ligação com a API do App Todoist
"""
from todoist_api_python.api import TodoistAPI
from pprint import pprint

api = TodoistAPI("ce472d89115cde96ba9aab0e19bbca802982c08d")


class Todoist:
    def __init__(self):
        self.api_projetos = api.get_projects()

        # Lista para armazenar os projetos
        self.lista_projetos = []

        for element in self.api_projetos:
            # Converte o elemento para dicionário
            element_dict = element.__dict__

            # Cria um dicionário para o projeto usando o nome como chave
            project_name = element_dict['name']
            project_dict = {project_name: element_dict}

            # Adiciona o dicionário à lista de projetos
            self.lista_projetos.append(project_dict)

    def __repr__(self):
        return pprint.pformat(self.lista_projetos, indent=4)

    def listagem_projetos(self):
        self.listagem_de_projetos = []
        for elemento in self.lista_projetos:
            for chave, valor in elemento.items():
                self.listagem_de_projetos.append(chave)
        return self.listagem_de_projetos

    def selecao_projeto(self, projeto: str):
        self.projeto_selecionado = projeto

        # Encontra o dicionário do projeto selecionado
        for elemento in self.lista_projetos:
            if projeto in elemento:
                pprint(elemento[projeto])
                return elemento[projeto]

        print(f"Projeto '{projeto}' não encontrado.")
        return None


x = Todoist()
# Exemplo de seleção de projeto
x.selecao_projeto('Estudos')

