from djitellopy import Tello
import time
"""
        PRUEBA 1 -> Despegue, mantener posición y aterrizaje...
"""
def main():
    # Acceder a la bibliotca de "TELLO"
    tello = Tello()
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

if __name__ == "__main__":
    main() # Ejecución del código