from djitellopy import Tello
import time
import cv2
import face_recognition
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
        PRUEBA 6 -> Activar cámara... 
""" 
def prueba_seis():
    # Conectar con el dron
    tello.connect()

    # Mostrar nivel de batería
    try:
        print(f"Batería: {tello.get_battery()}%")
    except:
        print("No se pudo obtener la batería")

    # Encender transmisión de video
    tello.streamon()

    # Guardar referencia para leer imágenes de la cámara

    frame_read = tello.get_frame_read()

    # Mostrar video durante 30 segundos o hasta presionar 'q'
    start_time = time.time()
    while time.time() - start_time < 30:
        frame = frame_read.frame
        cv2.imshow("Vista del Tello", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Apagar transmisión y cerrar ventana
    tello.streamoff()
    cv2.destroyAllWindows()

"""
        PRUEBA 7 -> detectar rostro...
""" 
def prueba_siete():
    # Conectar dron y encender cámara
    tello.connect()
    tello.streamon()

    # Cargar detector de rostros
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    )

    try:
        while True:
            # Capturar imagen
            frame = tello.get_frame_read().frame
            frame = cv2.resize(frame, (640, 480))
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Buscar rostros en la imagen
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)

            # Dibujar rectángulos en cada rostro
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

            # Mostrar cantidad de rostros detectados
            cv2.putText(frame, f"Rostros detectados: {len(faces)}",
                        (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 255, 255), 2)

            # Mostrar imagen en ventana
            cv2.imshow("Face Detection", frame)

            # Salir con 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    finally:
        # Apagar cámara y cerrar ventana
        tello.streamoff()
        cv2.destroyAllWindows()

"""
        PRUEBA 8 -> seguir rostro...
""" 

def prueba_ocho():
    # Conectar al dron y encender transmisión de video
    tello = Tello()
    tello.connect()
    tello.streamon()

    # Despegue y subir 70 cm
    tello.takeoff()
    tello.move_up(70)  # Subir 70 cm para un inicio seguro

    # Comienza el proceso de búsqueda
    searching_for_face = True
    print("Iniciando escaneo para encontrar rostros...")

    try:
        while True:
            # Capturar imagen desde la cámara del dron
            frame = tello.get_frame_read().frame
            frame = cv2.resize(frame, (640, 480))  # Redimensionar para mejorar el rendimiento
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convertir a RGB para la librería

            # Buscar rostros en la imagen y codificarlos
            face_locations = face_recognition.face_locations(rgb_frame)
            face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

            # Variable para controlar si encontramos rostros
            face_found = False

            # Revisar cada rostro detectado
            for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                # Dibujar un rectángulo en la cara detectada
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

                # Escribir el nombre debajo del rectángulo
                cv2.putText(frame, "Rostro Detectado", (left, top - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)

                # Si se detectó al menos un rostro, marcar la variable face_found
                face_found = True

                # Llamar a la función para seguir el rostro
                follow_face(tello, (top, right, bottom, left), frame)

            if not face_found:
                # Si no se encuentra el rostro, hacer que el dron gire lentamente
                print("Buscando rostros... El dron girará.")
                tello.rotate_clockwise(30)  # Girar 30 grados

            # Mostrar el video en pantalla
            cv2.imshow('Video', frame)

            # Salir con la tecla 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    finally:
        # Apagar transmisión y cerrar ventana
        tello.streamoff()
        cv2.destroyAllWindows()
        print(f"Batería: {tello.get_battery()}% de batería")


"""
        PRUEBA 9 -> detectar rostro especifico...
""" 

def prueba_nueve():
    # Conectar dron y encender transmisión de video
    tello = Tello()
    tello.connect()
    tello.streamon()
    print(f"Batería: {tello.get_battery()}% de batería")

    # Cargar foto de referencia y obtener su codificación facial
    imagen_andres = face_recognition.load_image_file("img/Andres.jpg")
    encoding_andres = face_recognition.face_encodings(imagen_andres)[0]

    # Guardar las caras conocidas y sus nombres
    known_face_encodings = [encoding_andres]
    known_face_names = ["Andres"]

    try:
        while True:
            # Capturar imagen desde la cámara del dron
            frame = tello.get_frame_read().frame
            frame = cv2.resize(frame, (640, 480))
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convertir a RGB para la librería

            # Buscar rostros en la imagen y codificarlos
            face_locations = face_recognition.face_locations(rgb_frame)
            face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

            # Revisar cada rostro detectado
            for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

                # Nombre por defecto si no hay coincidencia
                name = "Desconocido"
                if True in matches:
                    first_match_index = matches.index(True)
                    name = known_face_names[first_match_index]

                # Dibujar un rectángulo en la cara
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                # Escribir el nombre debajo del rectángulo
                cv2.putText(frame, name, (left, top - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)

            # Mostrar el video en pantalla
            cv2.imshow('Video', frame)

            # Salir con la tecla 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    finally:
        # Apagar transmisión y cerrar ventana
        tello.streamoff()
        cv2.destroyAllWindows()
        print(f"Batería: {tello.get_battery()}% de batería")   



"""
        PRUEBA 10 -> seguir rostro especifico...
""" 


def follow_face(tello, face_location, frame):
    """
    Función para seguir el rostro una vez detectado.
    El dron ajustará su posición en función de la ubicación del rostro en la imagen.
    """
    # Extraer la posición del rostro en el marco
    top, right, bottom, left = face_location
    face_center_x = (left + right) // 2
    face_center_y = (top + bottom) // 2

    frame_center_x = frame.shape[1] // 2
    frame_center_y = frame.shape[0] // 2

    # Calcular la diferencia entre el centro del rostro y el centro de la cámara
    offset_x = face_center_x - frame_center_x
    offset_y = face_center_y - frame_center_y

    # Mover el dron hacia el rostro en función de la diferencia
    if abs(offset_x) > 30:
        if offset_x > 0:
            tello.move_right(40)
        else:
            tello.move_left(40)

    if abs(offset_y) > 50:
        if offset_y > 0:
            tello.move_down(20)
        else:
            tello.move_up(20)

    # Si el rostro está centrado, avanzar
    if abs(offset_x) < 50 and abs(offset_y) < 50:
        print("Siguiendo al rostro...")
        tello.move_forward(30)  # Avanzar hacia el rostro





def prueba_diez():
    # Conectar al dron y encender transmisión de video
    tello = Tello()
    tello.connect()
    tello.streamon()

    # Cargar foto de referencia y obtener su codificación facial
    imagen_andres = face_recognition.load_image_file("img/Andres.jpg")
    encoding_andres = face_recognition.face_encodings(imagen_andres)[0]

    # Despegue y subir 100 cm
    tello.takeoff()
    tello.move_up(70)  # Subir 100 cm para un inicio seguro

    # Guardar las caras conocidas y sus nombres
    known_face_encodings = [encoding_andres]
    known_face_names = ["Andres"]

    # Comienza el proceso de búsqueda
    searching_for_face = True
    print("Iniciando escaneo para encontrar el rostro...")

    try:
        while True:
            # Capturar imagen desde la cámara del dron
            frame = tello.get_frame_read().frame
            frame = cv2.resize(frame, (640, 480))  # Redimensionar para mejorar el rendimiento
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convertir a RGB para la librería

            # Buscar rostros en la imagen y codificarlos
            face_locations = face_recognition.face_locations(rgb_frame)
            face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

            # Variable para controlar si encontramos el rostro
            face_found = False

            # Revisar cada rostro detectado
            for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

                # Nombre por defecto si no hay coincidencia
                name = "Desconocido"
                if True in matches:
                    first_match_index = matches.index(True)
                    name = known_face_names[first_match_index]
                    face_found = True  # Rostro encontrado

                # Dibujar un rectángulo en la cara detectada
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                # Escribir el nombre debajo del rectángulo
                cv2.putText(frame, name, (left, top - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)

            if face_found:
                # Si el rostro es encontrado, comenzar a seguirlo
                print("Rostro encontrado. Iniciando seguimiento...")
                follow_face(tello, face_locations[0], frame)  # Llamar a la función para seguir el rostro
            else:
                # Si no se encuentra el rostro, hacer que el dron gire lentamente
                print("Buscando rostro... El dron girará.")
                tello.rotate_clockwise(30)  # Girar 30 grados

            # Mostrar el video en pantalla
            cv2.imshow('Video', frame)

            # Salir con la tecla 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    finally:
        # Apagar transmisión y cerrar ventana
        tello.streamoff()
        cv2.destroyAllWindows()
        print(f"Batería: {tello.get_battery()}% de batería")

        
if __name__ == "__main__":
    prueba_diez()
   
    