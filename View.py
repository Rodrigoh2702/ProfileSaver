from tkinter import *
from tkinter import messagebox
import SheetWriter



def run():
    if candidateLinkText.get() == '' or userNameText.get() == '' or  userAccountText.get() == '' or userPasswordText.get() == '':
        messagebox.showerror('Campos requeridos', 'Por favor llena todos los campos')
        return
    SheetWriter.addRow(candidateLinkText.get(), userNameText.get(), userAccountText.get(), userPasswordText.get())

app = Tk()

# Link del perfil
candidateLinkText = StringVar()
candidateLinkLabel = Label(app, text='Link del perfil:', font=('bold', 14), pady=20)
candidateLinkLabel.grid(row=0, column=0, sticky=W)
candidateLinkEntry = Entry(app, textvariable=candidateLinkText)
candidateLinkEntry.grid(row=0, column=1)

# Quien lo añadio
userNameText = StringVar()
userNameLabel = Label(app, text='Lo añade:', font=('bold', 14), pady=20)
userNameLabel.grid(row=1, column=0, sticky=W)
userNameEntry = Entry(app, textvariable=userNameText)
userNameEntry.grid(row=1, column=1)

# Cuenta que lo añadio
userAccountText = StringVar()
userAccountLabel = Label(app, text='Correo electronico: ', font=('bold', 14), pady=20)
userAccountLabel.grid(row=2, column=0, sticky=W)
userAccountEntry = Entry(app, textvariable=userAccountText)
userAccountEntry.grid(row=2, column=1)

# Contraseña de la cuenta
userPasswordText = StringVar()
userPasswordLabel = Label(app, text='Contraseña: ', font=('bold', 14), pady=20)
userPasswordLabel.grid(row=3, column=0, sticky=W)
userPasswordEntry = Entry(app, textvariable=userPasswordText, show='*')
userPasswordEntry.grid(row=3, column=1)

# Boton para usar el programa
runButton = Button(app, text='Añadir perfil', width=12, command=run, activebackground='cyan')
runButton.grid(row=4, column=0, pady=20)

app.title('LinkedIn Profile Saver')
# app.geometry('700x400')

app.mainloop()
