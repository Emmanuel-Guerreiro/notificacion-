from win10toast import ToastNotifier
from datetime import datetime, timedelta
from time import sleep

tiempo_inicio = datetime.now()
mas_veinte_minutos = tiempo_inicio + timedelta(minutes = 20)
mas_cuarenta_minutos = tiempo_inicio + timedelta(minutes = 40)
mas_sesenta_minutos = tiempo_inicio + timedelta(minutes= 60)


class notificaciones:
    
    def __init__(self, nombre, mensaje, icono, duracion):
        self.nombre = nombre
        self.mensaje = mensaje
        self.icono = icono
        self.duracion = duracion
        
    
    def mostrar_notificacion(self):
        toaster = ToastNotifier()
        toaster.show_toast(self.nombre, self.mensaje, icon_path = self.icono, duration = self.duracion)


notificacion_ojos = notificaciones('Cuidado de ojos', 'Descansa la vista durante 20 segundos', 'ojo.ico', 7)
notificacion_movimiento = notificaciones('Moverse', 'Levantate y mueve un poco las piernas', 'ojo.ico', 7)
notificacion_agua = notificaciones('Tomar agua', 'Toma agua para mantenerte hidratado', 'ojo.ico', 7)



def corroborar_hora():

    global tiempo_inicio, mas_veinte_minutos, mas_sesenta_minutos, mas_cuarenta_minutos

    while True:
        if tiempo_inicio >= mas_veinte_minutos:
            notificacion_ojos.mostrar_notificacion()
            tiempo_inicio = datetime.now()
            mas_veinte_minutos = tiempo_inicio + timedelta(seconds = 20)
        elif tiempo_inicio >= mas_sesenta_minutos:
            notificacion_movimiento.mostrar_notificacion()
            tiempo_inicio = datetime.now()
            mas_sesenta_minutos = tiempo_inicio + timedelta(seconds = 20)
        elif tiempo_inicio >= mas_cuarenta_minutos:
            notificacion_agua.mostrar_notificacion()
            tiempo_inicio = datetime.now()
            mas_cuarenta_minutos = tiempo_inicio + timedelta(seconds = 20)
        else:
            sleep(10)
            tiempo_inicio = datetime.now()
            corroborar_hora()

corroborar_hora()
