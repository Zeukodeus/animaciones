import tkinter as tk

# Configuración inicial
window = tk.Tk()
window.title("Animación de una cancha de fútbol")
window.geometry("1000x600")
canvas = tk.Canvas(window, width=1000, height=600, bg="green")
canvas.pack()

# Dibujo de la cancha
canvas.create_rectangle(50, 180, 200, 440, outline="white", width=2)
canvas.create_rectangle(50, 50, 950, 550, outline="white", width=2)
canvas.create_line(500, 550, 500, 50, fill="white", width=2)
canvas.create_rectangle(800, 180, 950, 440, outline="white", width=2)
canvas.create_arc(375, 200, 625, 450, start=0, extent=359, style="arc", outline="white", width=2)
canvas.create_arc(750, 230, 850, 390, start=90, extent=180, style="arc", outline="white", width=2)
canvas.create_arc(150, 230, 250, 390, start=-90, extent=180, style="arc", outline="white", width=2)
canvas.create_rectangle(50, 220, 130, 400, outline="white", width=2)
canvas.create_rectangle(870, 220, 950, 400, outline="white", width=2)
canvas.create_oval(510, 335, 490, 315, fill="white", outline="white")

# Dibujo del balón
ball = canvas.create_oval(390, 290, 410, 310, fill="black")

# Movimiento del balón
ball_speed_x = 5
ball_speed_y = 5

def animate_ball():
    global ball_speed_x, ball_speed_y

    # Actualizar posición del balón
    canvas.move(ball, ball_speed_x, ball_speed_y)

    # Obtener coordenadas actuales del balón
    ball_coords = canvas.coords(ball)

    # Rebotar en los bordes
    if ball_coords[3] >= 550 or ball_coords[1] <= 50:
        ball_speed_y *= -1
    if ball_coords[2] >= 950 or ball_coords[0] <= 50:
        ball_speed_x *= -1

    # Llamar a la función nuevamente después de un intervalo de tiempo
    window.after(10, animate_ball)

# Iniciar animación
animate_ball()

# Ejecutar la interfaz gráfica
window.mainloop()
