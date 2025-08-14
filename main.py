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
    
    
"""
        PRUEBA 2 -> Giro a la derecha de 360°...
"""   
def prueba_dos():
    # Conexión al DRON
    tello.connect()
    # Visualización en consola de la batería
    print(f"Batería: {tello.get_battery()}%")

    # Despegar
    tello.takeoff()
    time.sleep(3)  # Esperar a que se estabilice

    # Giro a la derecha 360°
    print("Girando 360° a la derecha...")
    #gira 360° a la derecha 
    tello.rotate_clockwise(360)

    # Pausa para estabilizar
    time.sleep(2)

    # Aterrizar
    tello.land()

"""
        PRUEBA 3 -> Movimiento derecha e izquierda...
"""  
def prueba_tres():
    # Conexión al DRON
    tello.connect()
    # Visualización en consola de la batería
    print(f"Batería: {tello.get_battery()}%")

    # Despegar
    tello.takeoff()
    time.sleep(3)  # Esperar a que se estabilice

    # Giro a la derecha 180°
    print(" derecha e izquierda")
    # Se mueve a la derecha
    tello.move_right(20)
    # Se mueve a la izquierda
    tello.move_left(40)
    # Se mueve a la derecha 
    tello.move_right(20)

    # Pausa para estabilizar
    time.sleep(1)

    # Aterrizar
    tello.land()
    
"""
        PRUEBA 4 -> Movimiento adelante y atras... 
"""     
def prueba_cuatro():
   # Conexión al DRON
    tello.connect()
    # Visualización en consola de la batería
    print(f"Batería: {tello.get_battery()}%")

    # Despegar
    tello.takeoff()
    time.sleep(1)  # Esperar a que se estabilice

    # Se mueve hacia adelante y atras
    print(" adelante y atras ")
    # Se mueve hacia adelante
    tello.move_forward(40)
    # Se mueve hacia atras
    tello.move_back(40)
    # Se mueve hacia adelante
    tello.move_forward(20)

    # Pausa para estabilizar
    time.sleep(1)

    # Aterrizar
    tello.land()
    
    
def prueba_seis():
       # Conexión al DRON
    tello.connect()
    # Visualización en consola de la batería
    print(f"Batería: {tello.get_battery()}%")

    # Despegar
    tello.takeoff()
    time.sleep(1)  # Esperar a que se estabilice

    # Se mueve hacia arriba  y abajo
    print(" adelante y atras ")
    # Se mueve hacia arriba
    tello.move_up(40)
    # Se mueve hacia abajo
    tello.move_down(40)
   
    # Pausa para estabilizar
    time.sleep(1)

    # Aterrizar
    tello.land()
         
        
        
if __name__ == "__main__":
    prueba_cuatro()
   
    