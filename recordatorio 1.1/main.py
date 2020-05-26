from win10toast import ToastNotifier
from datetime import datetime, timedelta
from time import sleep

tiempo_inicio = datetime.now()
masVeinteMinutos = tiempo_inicio + timedelta(minutes = 20)

def notificacion():
    toaster = ToastNotifier()
    toaster.show_toast("Cuidado de ojos", "Aflojar la vista durante 20 segundos", icon_path = "ojo.ico", duration = 20)

def corroborar_hora():

    global tiempo_inicio, masVeinteMinutos

    while True:
        if tiempo_inicio >= masVeinteMinutos:
            notificacion()
            tiempo_inicio = datetime.now()
            masVeinteMinutos = tiempo_inicio + timedelta(minutes = 20)
        else:
            sleep(600)
            tiempo_inicio = datetime.now()
            corroborar_hora()

corroborar_hora()

notificacion()