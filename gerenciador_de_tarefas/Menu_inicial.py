
class Cadastro:
    def __init__(self):
        self.usuario = []
    
    def registra_usuario(self,nome,email,senha):
        self.usuario.append(
           {'nome' : nome,
            'email' : email,
            'senha' : senha,
            'tarefa' : []}
        )
    def verificar_loguin(self,email,senha):
        for usuario in self.usuario:
            if usuario['email'] == email and usuario['senha'] == senha:
                return
        print('Senha ou Email incorreto')
        input('enter >>>')
        return False 

    def titulo(self,email):
        for usuario in self.usuario:
            if ['email'] == email and ['nome'] == usuario:
                return ['nome']

# acessar ao sistema 
class Acesso_ao_sistema(Cadastro):
    def __init__(self):
        super().__init__()

    def adicionar_tarefa(self,usuario,objetivo,prioridade,data):
        for usuario in self.usuario:
            usuario['email'] == email
        self.add_tarefa.append({'[]':objetivo,'Prioridade':prioridade,'Prazo':data})
        return True
       

        



# class Cadastro:
#     def __init__(self):
#         self.usuario = []

#     def registrar_usuario(self,nome,email,senha):
#         self.usuario.append(
#             {'nome':nome,
#              'email':email,
#              'senha':senha,
#              'tarefa': []}
#         )
#         return True 
    
    # def verificar_loguin(self,email,senha):
    #     for usuario in self.usuario:
    #         if usuario['email'] == email and usuario['senha'] == senha:
    #             return
    #     print('Senha ou Email incorreto')
    #     input('enter >>>')
    #     return False 
    
    # def titulo(self,email):
    #     for usuario in self.usuario:
    #         if ['email'] == email and ['nome'] == usuario:
    #             return ['nome']


# acessar ao sistema 
# class Acesso_ao_sistema(Cadastro):
#     def __init__(self):
#         self.add_tarefa = []
    
#     def adicionar_tarefa(self,objetivo,prioridade,data):
#         for usuario in self.usuario:
#             usuario['email'] == email
#         # self.add_tarefa.append({'[]':objetivo,'Prioridade':prioridade,'Prazo':data})
#         # return True
       
#     def ver_tarefa(self):
#         if len(self.add_tarefa) == 0:
#             print('Ainda não tenhuma tarefa adicionada')
#         for i,tarefa in enumerate(self.add_tarefa):
#             print( f'{i+1}.[ ] {tarefa["[]"]} - Prioridade: {tarefa['Prioridade']} - Prazo: {tarefa['Prazo']}')
