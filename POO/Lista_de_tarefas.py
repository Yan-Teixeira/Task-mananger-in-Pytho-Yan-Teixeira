#Importando os dados de outro arquivo tarefas
from Tarefas import Tarefa

#defindo a classe lista de taferas 
class Lista_Tarefas:
    def __init__(self):
        self.tarefas = []

#Menu da Lista de Tarefas
    def menu(self):
        print("======= 𝑳𝒊𝒔𝒕𝒂 𝒅𝒆 𝑻𝒂𝒓𝒆𝒇𝒂𝒔 =======")
        print("________________________________")
        print("║ 1. Procurar Tarefa           ║")
        print("║ 2. Concluir Tarefa           ║")
        print("║ 3. Editar Tarefa             ║")
        print("║ 4. Excluir Tarefa            ║")
        print("║ 5. Sair                      ║")
        print("────────────────────────────────")

#/////////////////////////Métodos\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ 

#Definindo para escolher as opções
    def exibir_opcoes(self):
        while True:
            try:
                self.menu()
                escolha = (int(input("Qual opção você quer: ")))
                
                if escolha == 1:
                    nome_tarefa = input("Digite o nome da tarefa que procura: ")
                    print(self.procurar_tarefas(nome_tarefa))

                elif escolha == 2:
                    self.concluir_tarefa()

                elif escolha == 3:
                    print("Editar Tarefa")
                    self.editar_tarefas()

                elif escolha == 4:
                    self.excluir_tarefa()
                    
                elif escolha == 5:
                    print("Saindo do programa...")
                    exit()
                    break
                else:
                    print("Opção invalida!")
            except ValueError:
                print(" Digite novamente!")

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
    lista = Lista_Tarefas()
    lista.exibir_opcoes()

#FIM
