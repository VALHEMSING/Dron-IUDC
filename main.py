from djitellopy import Tello
import time
import cv2
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

    # Derecha e izquierda
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
        
"""
        PRUEBA 5 -> Primer recorrido... 
"""          
        
def prueba_cinco():
       # Conexión al DRON
    tello.connect()

    # Despegar
    tello.takeoff()
    time.sleep(1)  # Esperar a que se estabilice

    # Se mueve hacia arriba  y abajo
    print(" adelante y atras ")
    # Se mueve hacia arriba
    tello.move_up(80)
    # Se mueve hacia adelante
    tello.move_forward(110)
    time.sleep(1)  # Esperar a que se estabilice
    #gira 90° a la derecha 
    tello.rotate_clockwise(-90)
     # Se mueve hacia adelante
    tello.move_forward(110)
    time.sleep(1)  # Esperar a que se estabilice
    #gira 90° a la derecha 
    tello.rotate_clockwise(-90)
     # Se mueve hacia adelante
    tello.move_forward(100)
    time.sleep(1)  # Esperar a que se estabilice
    #gira 90° a la derecha 
    tello.rotate_clockwise(-90)
     # Se mueve hacia adelante
    tello.move_forward(100)
 
    time.sleep(1)

    # Aterrizar
    tello.land()
   # Visualización en consola de la batería
    print(f"Batería: {tello.get_battery()}%")   

"""
        PRUEBA 6 -> Activar camara... 
""" 

def prueba_seis():
    tello.connect()
    # Ahora obtener la batería
    try:
        print(f"Batería: {tello.get_battery()}%")
    except Exception as e:
        print("No se pudo obtener la batería:", e)

    # Iniciar transmisión de video
    tello.streamon()

    # Obtener el lector de frames
    frame_read = tello.get_frame_read()

    # Mostrar el video durante 30 segundos o hasta que se presione 'q'
    start_time = time.time()
    while time.time() - start_time < 30:
        frame = frame_read.frame

        # Mostrar el video
        cv2.imshow("Vista del Tello", frame)

        # Salir si se presiona 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Detener transmisión
    tello.streamoff()
    cv2.destroyAllWindows()

"""
        PRUEBA 7 -> Activar camara... 
""" 
def prueba_siete():
     # Inicializar dron
    tello = Tello()
    tello.connect()
    tello.streamon()

    # Cargar clasificador de rostro
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    )

    # Despegar
    tello.takeoff()
    time.sleep(1)
    tello.send_rc_control(0, 0, 0, 0)

    try:
        while True:
            # Obtener frame
            frame = tello.get_frame_read().frame
            frame = cv2.resize(frame, (640, 480))
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Detectar rostros
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)

            if len(faces) > 0:
                (x, y, w, h) = faces[0]
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

                # Centro del rostro
                face_center_x = x + w // 2
                face_center_y = y + h // 2

                # Errores
                error_x = face_center_x - 320
                error_y = face_center_y - 240

                # Velocidades
                yaw_speed = int(error_x / 20)       # giro izquierda/derecha
                up_down_speed = int(-error_y / 20)  # subir/bajar

                # Mover dron
                tello.send_rc_control(0, 0, up_down_speed, yaw_speed)
            else:
                # Si no ve rostro, se queda quieto
                tello.send_rc_control(0, 0, 0, 0)

            # Mostrar video
            cv2.imshow("Face Tracking", frame)

            # Salir con 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    finally:
        tello.send_rc_control(0, 0, 0, 0)
        tello.land()
        tello.streamoff()
        cv2.destroyAllWindows()
if __name__ == "__main__":
    prueba_siete()
   
    