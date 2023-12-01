import tkinter as tk
from tkinter import ttk
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime



class SistemaAsistencia:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Sistema de Asistencia")
        self.ventana.geometry("600x400")

        self.usuario_actual = None

        # Crear marco de inicio de sesión
        self.frame_login = ttk.Frame(ventana)
        self.frame_login.pack()

        self.label_usuario = ttk.Label(self.frame_login, text="Usuario:")
        self.label_usuario.grid(row=0, column=0, padx=10, pady=10)

        self.entry_usuario = ttk.Entry(self.frame_login)
        self.entry_usuario.grid(row=0, column=1, padx=10, pady=10)

        self.label_contrasena = ttk.Label(self.frame_login, text="Contraseña:")
        self.label_contrasena.grid(row=1, column=0, padx=10, pady=10)

        self.entry_contrasena = ttk.Entry(self.frame_login, show="*")
        self.entry_contrasena.grid(row=1, column=1, padx=10, pady=10)

        self.boton_login = ttk.Button(self.frame_login, text="Iniciar Sesión", command=self.verificar_login)
        self.boton_login.grid(row=2, column=0, columnspan=2, pady=10)

        self.label_mensaje = ttk.Label(self.frame_login, text="")
        self.label_mensaje.grid(row=3, column=0, columnspan=2, pady=10)

        # Crear marco principal
        self.frame_principal = ttk.Frame(ventana)

        # Crear pestañas
        self.pestanas = ttk.Notebook(self.frame_principal)

        for i in range(1, 7):
            pagina = ttk.Frame(self.pestanas)
            boton_asistencia = ttk.Button(pagina, text="Asistencia", command=lambda: self.registrar_asistencia(i))
            boton_asistencia.pack(pady=10)
            boton_falta = ttk.Button(pagina, text="Falta", command=lambda: self.registrar_falta(i))
            boton_falta.pack(pady=10)
            label_maestro = ttk.Label(pagina, text="Maestro")
            label_maestro.pack()

            self.pestanas.add(pagina, text=f"Pestaña {i}")

        self.pestanas.pack()

        # Mostrar la ventana
        self.ventana.mainloop()

    def verificar_login(self):
        usuario = self.entry_usuario.get()
        contrasena = self.entry_contrasena.get()

        if usuario in usuarios and usuarios[usuario] == contrasena:
            self.usuario_actual = usuario
            self.frame_login.pack_forget()
            self.frame_principal.pack()
        else:
            self.label_mensaje["text"] = "Usuario o contraseña incorrectos"

    def registrar_asistencia(self, pestaña):
        mensaje = f"El docente en la Pestaña {pestaña} no ha faltado."
        self.enviar_correo("Asistencia", mensaje)

    def registrar_falta(self, pestaña):
        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        mensaje = f"El docente en la Pestaña {pestaña} ha faltado. Fecha y hora: {fecha_actual}."
        self.enviar_correo("Falta", mensaje)

    def enviar_correo(self, asunto, mensaje):
        destinatario = "leoluna609@gmail.com"

        servidor_correo = smtplib.SMTP("smtp.gmail.com", 587)
        servidor_correo.starttls()
        servidor_correo.login("raysaidas12@gmail.com", "contraseña")

        mensaje_correo = MIMEMultipart()
        mensaje_correo["From"] = "raysaidas12@gmail.com"
        mensaje_correo["To"] = destinatario
        mensaje_correo["Subject"] = asunto
        mensaje_correo.attach(MIMEText(mensaje, "plain"))

        servidor_correo.send_message(mensaje_correo)

        servidor_correo.quit()

if __name__ == "__main__":
    ventana = tk.Tk()
    app = SistemaAsistencia(ventana)
