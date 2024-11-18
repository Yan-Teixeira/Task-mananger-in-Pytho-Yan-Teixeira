#Importando os dados de outro arquivo tarefas
from tarefa import Tarefa

#defindo a classe lista de taferas 
class lista_Tarefas:
    def __init__(self):
        self.tarefas = []

#Adiciona novas tarefas
    def adicionar_tarefa(self):
        titulo = input("Digite o título da tarefa: ")
        data = input("Digite a data (DIA-MÊS-ANO): ")
        descricao = input("Digite uma descrição (opcional): ")
        prioridade = input("Digite a prioridade (Baixa, Média, Alta): ") or "Baixa"
        nova_tarefa = Tarefa(titulo, data, descricao, prioridade=prioridade)
        self.tarefas.append(nova_tarefa)
        print(f"Tarefa '{titulo}' adicionada com sucesso!")
    
#Procurar as taferas se está adcionada na lista ou não
    def procurar_tarefas (self, nome_tarefa):
        for tarefa in self.tarefas:
            if tarefa.titulo.lower() == nome_tarefa.lower():
                return f" A tarefa '{nome_tarefa}' foi encontrada." #True
            else:
                return f"A tarefa'{nome_tarefa}' não existe na lista." #False

#Concluindo tarefas
#nesta função será para concluir a tarefa que voce deseja
    def concluir_tarefa(self):
        print("======== Concluir Tarefas ========")
        print("──────────────────────────────────")
        nome_tarefa = input("Digite o nome da tarefa que deseja ser concluida: ")
        for tarefa in self.tarefas:
            if tarefa.titulo.lower() == nome_tarefa.lower(): #vai procurar pelo titulo da tarefa
                self.tarefas.remove(tarefa)
                print(f"Tarefa '{nome_tarefa}' removida da lista.")
                return
        print(f"Tarefa '{nome_tarefa}' não foi encontrada.")

#Editando as tarefas
    def editar_tarefas(self, Tarefas):
        print("======= Editar Tarefas =======")
        print("──────────────────────────────")
        nome_tarefa = input("Digite o nome da tarefa que deseja ser alterada:")
        for tarefa in self.tarefas:
            if tarefa.título.lower() == nome_tarefa.lower():
                novo_titulo = input (f"Novo título (anterior: {tarefa.titulo}): ") or tarefa.titulo
                nova_data = input(f"Nova data (anterior: {tarefa.data}): ") or tarefa.data
                nova_descricao = input(f"Nova descrição (anterior: {tarefa.descricao}): ") or tarefa.descricao
                nova_prioridade =  input(f"Nova prioridade (anterior: {tarefa.prioridade}): ") or tarefa.prioridade

                #Atualizando os atributos
                tarefa.titulo = novo_titulo
                tarefa.data = nova_data
                tarefa.descricao = nova_descricao
                tarefa.prioridade = nova_prioridade
                print(f"Tarefa '{nome_tarefa}' atualizada com sucesso!")
                return
        print(f"A tarefa '{nome_tarefa}' não foi encontrada.")
         
#Excluindo Tarefas
    def excluindo_tarefas(self, Tarefa):
        nome_tarefa = input("Digite o nome da terefa que deseja excluir: ")
        for tarefa in self.tarefas:
            if tarefa.titulo.lower() == nome_tarefa.lower():
                self.tarefas.remove(Tarefa)
                print(f"Tarefa {nome_tarefa}' excluida com sucesso!")
                return
            print(f"A tarefa '{nome_tarefa}' não foi encontrada.")

#Exibir todas as tarefas
    def exibir_tarefas(self):
        if not self.tarefas:
            print("nenhuma tarefas cadastrada.")
        else:
            print("======== Lista de Tarefas ========")
            print("──────────────────────────────────")

            for i, tarefa in enumerate(self.tarefas, start=1):
                print(f"{i}.\n{tarefa.info()}")

#Rodando o programa
if __name__ == "__main__":
    lista = lista_Tarefas()

#FIM