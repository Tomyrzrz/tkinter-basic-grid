from tkinter import *

ventana_raiz = Tk()

ventana_raiz.geometry("700x400")

ventana_raiz.title("Crea cuenta Mercado Libre")

ventana_raiz.config(bg="white")

ventana_raiz.resizable(0,0)

frame = Frame(ventana_raiz, width=700, height=50)
frame.config(bg="yellow", bd=1, relief="groove") #groove
frame.place(x=0,y=0)

logo_mercado = PhotoImage(file="descarga.png")
Label(frame, image=logo_mercado, width=50, height=50).place(x=0,y=0)

lbl_completa = Label(ventana_raiz,bg="white", fg="black", text="Completa tus datos", font=("Arial",18))
lbl_completa.grid(row=0, column=0, sticky="sw", padx=10, pady=70)

btn_empresas = Button(ventana_raiz, bg="white", fg="blue", bd=0, text="Crear una cuenta de empresa >", font=("Arial",9))
btn_empresas.grid(row=0, column=3, sticky="W", pady=70)

lbl_nombre = Label(ventana_raiz,bg="white", fg="gray", text="Nombre", font=("Arial",11))
lbl_nombre.grid(row=1, column=0, sticky="W", padx=10, pady=5)

nombre = StringVar()
txt_nombre = Entry(ventana_raiz, bg="white", font=("Arial",12), textvariable=nombre)
txt_nombre.grid(row=2, column=0, sticky="W", padx=10)

lbl_apellidos = Label(ventana_raiz,bg="white", fg="gray", text="Apellidos", font=("Arial",11))
lbl_apellidos.grid(row=1, column=1, sticky="W", padx=10, pady=5)

apellidos = StringVar()
txt_apellidos = Entry(ventana_raiz, bg="white", font=("Arial",12), textvariable=apellidos)
txt_apellidos.grid(row=2, column=1, sticky="W", padx=10)

lbl_email = Label(ventana_raiz,bg="white", fg="gray", text="Email", font=("Arial",11))
lbl_email.grid(row=3, column=0, sticky="w", padx=10, pady=20)

email = StringVar()
txt_email = Entry(ventana_raiz, bg="white", font=("Arial",12), textvariable=email)
txt_email.grid(row=4, column=0, sticky="W", padx=10)

lbl_clave = Label(ventana_raiz,bg="white", fg="gray", text="Clave", font=("Arial",11))
lbl_clave.grid(row=3, column=1, sticky="w", padx=10, pady=20)

clave = StringVar()
txt_clave = Entry(ventana_raiz, bg="white", font=("Arial",16), textvariable=clave)
txt_clave.grid(row=4, column=1, sticky="W", padx=10)

btn_crear = Button(ventana_raiz, bg="blue", width=18, fg="white", bd=1, text="Crear cuenta", font=("Arial",16))
btn_crear.grid(row=5, column=0, padx=10, pady=15)

lbl_terminos = Label(ventana_raiz,bg="white", fg="gray", text="Al registrarme, declaro que soy mayor de edad \ny acepto los Términos y condiciones \ny las Políticas de privacidad de \nMercado Libre y Mercado Pago.", justify="left", font=("Arial",9))
lbl_terminos.grid(row=5, column=1, padx=10, pady=20)




ventana_raiz.mainloop()


