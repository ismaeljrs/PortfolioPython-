import customtkinter as ctk

# Configurações da aparência
ctk.set_appearance_mode('dark')

# Função funcional
def validar_login():
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()

    if usuario == 'ismael' and senha == '1234':
        resultado_login.configure(text='Login feito com sucesso!', text_color='green')
    else:
        resultado_login.configure(text='Usuário ou senha incorretos!', text_color='red')

# Criação da janela principal
app = ctk.CTk()
app.title('Sistema de login')
app.geometry('300x300')

# Label e campo do usuário
label_usuario = ctk.CTkLabel(app, text='Usuário')
label_usuario.pack(pady=10)

entrada_usuario = ctk.CTkEntry(app, placeholder_text='Digite seu usuário')
entrada_usuario.pack(pady=10)

# Label e campo da senha
label_senha = ctk.CTkLabel(app, text='Senha')
label_senha.pack(pady=10)

entrada_senha = ctk.CTkEntry(app, placeholder_text='Digite sua senha', show='*')
entrada_senha.pack(pady=10)

# Botão de login
botao_login = ctk.CTkButton(app, text='Login', command=validar_login)
botao_login.pack(pady=10)

# Campo de feedback do login
resultado_login = ctk.CTkLabel(app, text='')
resultado_login.pack(pady=10)

# Iniciar o app
app.mainloop()
