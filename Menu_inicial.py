
class Cadastro:
    def __init__(self):
        self.usuario = []

    def registrar_usuario(self,nome,email,senha):
        self.usuario.append({'nome':nome,'email':email,'senha':senha})
        return True 
    
    def verificar_loguin(self,email,senha):
        for usuario in self.usuario:
            if usuario['email'] == email and usuario['senha'] == senha:
                return True
        print('Senha ou Email incorreto')
        input('enter >>>')
        return False 
        
