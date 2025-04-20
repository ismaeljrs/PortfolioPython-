class Acesso_ao_sistema:
    def __init__(self):
        self.add_tarefa = []
    
    def adicionar_tarefa(self,objetivo,prioridade,data):
        self.add_tarefa.append({'[]':objetivo,'Prioridade':prioridade,'Prazo':data})
        return True
       
    def ver_tarefa(self):
        if len(self.add_tarefa) == 0:
            print('Ainda não tenhuma tarefa adicionada')
        for i,tarefa in enumerate(self.add_tarefa):
            print( f'{i+1}.[ ] {tarefa["[]"]} - Prioridade: {tarefa['Prioridade']} - Prazo: {tarefa['Prazo']}')
            

