from djitellopy import Tello
import time
tello = Tello()

"""
        PRUEBA 1 -> Despegue, mantener posición y aterrizaje...
"""
def prueba_uno():
    
    # Conección al DRON
    tello.connect()
    # Visualización en consola de la bateria
    print(f"Batería: {tello.get_battery()}%")
    # Despegar
    tello.takeoff()

    time.sleep(3)  # Esperar a que se estabilice

    # Enviar comando de "quedarse quieto"
    tello.send_rc_control(0, 0, 0, 0)

    # Mantener quieto durante 5 segundos
    for _ in range(5):
        tello.send_rc_control(0, 0, 0, 0)
        time.sleep(1)

    # Aterrizar
    tello.land()
    
    
    
def prueba_dos():
    # Conexión al DRON
    tello.connect()
    # Visualización en consola de la batería
    print(f"Batería: {tello.get_battery()}%")

    # Despegar
    tello.takeoff()
    time.sleep(3)  # Esperar a que se estabilice

    # Giro a la derecha 180°
    print("Girando 180° a la derecha...")
    tello.rotate_clockwise(360)

    # Pausa para estabilizar
    time.sleep(2)

    # Aterrizar
    tello.land()

def prueba_cuatro():
   # Conexión al DRON
    tello.connect()
    # Visualización en consola de la batería
    print(f"Batería: {tello.get_battery()}%")

    # Despegar
    tello.takeoff()
    time.sleep(3)  # Esperar a que se estabilice
    
         
        
        
if __name__ == "__main__":
    prueba_dos()
   
    