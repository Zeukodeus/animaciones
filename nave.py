from tkinter import *
import random
import tkinter

# Variables globales
base = 460
altura = 320
radio = 50

# Función para modificar el arco hacia arriba
def arriba():
    c.move(ball, 0, -10)
    check_collision()

# Función para modificar el arco hacia abajo
def abajo():
    c.move(ball, 0, 10)
    check_collision()

# Función para modificar el arco hacia la izquierda
def izquierda():
    c.move(ball, -10, 0)
    check_collision()

# Función para modificar el arco hacia la derecha
def derecha():
    c.move(ball, 10, 0)
    check_collision()

# Función para verificar colisión
def check_collision():
    ball_coords = c.coords(ball)
    for circle in circles:
        circle_coords = c.coords(circle)
        if collision(ball_coords, circle_coords):
            reset_ball()
            break

ventana_principal = Tk()
ventana_principal.title("Graficador 2D - Lineas Rectas")
ventana_principal.geometry("500x800")
ventana_principal.resizable(False, False)
ventana_principal.config(bg="black")

# Frame de graficación
frame_graficacion = Frame(ventana_principal, bg="white", width=480, height=350)
frame_graficacion.place(x=10, y=10)

# Creación del lienzo (canvas)
c = Canvas(frame_graficacion, width=base, height=altura, bg="black")
c.place(x=10, y=10)

ball_image = tkinter.PhotoImage(file="img/nave.png")

# Dibujar la imagen del balón en el lienzo
initial_position = (200, 200)
ball = c.create_image(initial_position[0], initial_position[1], image=ball_image)

# Frame de controles
frame_controles = Frame(ventana_principal, bg="white", width=480, height=440)
frame_controles.place(x=10, y=350)

# Botón para mover hacia arriba
arriba_icon = PhotoImage(file="img/arriba.png")
bt_arriba = Button(frame_controles, image=arriba_icon, command=arriba)
bt_arriba.place(x=210, y=150, width=60, height=60)

# Botón para mover hacia abajo
abajo_icon = PhotoImage(file="img/abajo.png")
bt_abajo = Button(frame_controles, image=abajo_icon, command=abajo)
bt_abajo.place(x=210, y=290, width=60, height=60)

# Botón para mover hacia la izquierda
izquierda_icon = PhotoImage(file="img/izq.png")
bt_izquierda = Button(frame_controles, image=izquierda_icon, command=izquierda)
bt_izquierda.place(x=135, y=220, width=60, height=60)

# Botón para mover hacia la derecha
derecha_icon = PhotoImage(file="img/derecha.png")
bt_derecha = Button(frame_controles, image=derecha_icon, command=derecha)
bt_derecha.place(x=285, y=220, width=60, height=60)

ventana_principal.mainloop()
