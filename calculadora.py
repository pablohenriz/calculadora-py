import customtkinter as ctk

#configurar a aparencia
ctk.set_appearance_mode("dark")

#Criação da janela principal
app = ctk.CTk()
app.title("Calculadora")
app.geometry("400x500")

#inicialização da aplicação
app.mainloop()