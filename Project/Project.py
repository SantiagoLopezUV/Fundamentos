# Project Restaurant
import tkinter

def log_out():
    print("Estas en Registro")


def signin():
    print("Inicio de Sesion")


def ventana_1tkinter():
    #   Primera Ventana | Inicio
    ventana_main = tkinter.Tk()
    ventana_main.title("Restaurant SLP")
    ventana_main.geometry("370x330")
    inicio = tkinter.Label(ventana_main, text = "Mi Restaurante",\
        font = "Helvetica 14")
    #logo
    intro = tkinter.Label(ventana_main, text = \
        """
        Nuestro restaurante es un lugar donde ofrecemos
        una variedad de platos deliciosos y recursos
        culinarios para el público para satisfacer tus
        necesidades culinarias y hacewrte disfrutar d una
        experiencia gastronómica excepcional.
        """)
    button_signin = tkinter.Button(ventana_main, text = "Registrarse",\
        font = "Helvetica 11", command = lambda: log_out)
    button_logout = tkinter.Button(ventana_main, text = "Iniciar Sesion",\
        font = "Helvetica 11", command = lambda: signin)
    inicio.pack()
    intro.pack()
    button_signin.pack()
    button_logout.pack()
    ventana_main.mainloop()


def logger():
    new_e = nemail.get()
    new_p = npassw.get()
    print(new_p + "+" + new_e)

def ventana_2tkinter():   
    #   Segunda  Ventana | Registro
    ventana_1 = tkinter.Tk()
    ventana_1.title("Registro")
    ventana_1.geometry("370x330")
    inicio = tkinter.Label(ventana_1, text = "Mi Restaurante",\
        font = "Helvetica 14")
    # logo
    lbl1 = tkinter.Label(ventana_1, text = "Registrarse",\
        font = "Helvetica 11")
    lbl2 = tkinter.Label(ventana_1, text = "Email")
    lbl3 = tkinter.Label(ventana_1, text = "Contraseña")
    lbl4 = tkinter.Label(ventana_1, text = "Confirmar Contraseña")
    nemail = tkinter.Entry(ventana_1, )
    npassw = tkinter.Entry(ventana_1)
    npassw1 = tkinter.Entry(ventana_1)
    button_loged = tkinter.Button(ventana_1, text = "Registrar",\
        font = "Helvetica 10", command = lambda: logger)
    inicio.pack()
    lbl1.pack()
    lbl2.pack()
    nemail.pack()
    lbl3.pack()
    npassw.pack()
    lbl4.pack()
    npassw1.pack()
    button_loged.pack()
    ventana_1.mainloop()

if __name__ == '__main__':
    ventana_1tkinter()