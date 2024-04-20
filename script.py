import json  # importa el modulo para manejar archivos JSON
import os  # importa el modulo para trabajar con funcionalidades del sistema operativo
from datetime import datetime  # importa la clase datetime del modulo datetime
from usuario import Usuario  # importa la clase 'Usuario' del modulo usuario


def cargar_usuarios_desde_archivo(archivo: str) -> list:
    """
    Carga usuarios desde un archivo y los devuelve como una lista de objetos 'Usuario'.

    Args:
        archivo (str): La ruta del archivo de usuarios.

    Returns:
        list: Una lista de objetos 'Usuario'.
    """
    lista_usuarios = []  # se inicializa una lista vacia para almacenar los usuarios cargados

    try:
        with open('usuarios.txt') as usuarios:  # se abre el archivo de usuarios
            for linea in usuarios:  # se recorre cada linea del archivo
                try:
                    # se carga el usuario desde la linea en formato JSON
                    usuario = json.loads(linea)
                    # se crea un nuevo objeto 'Usuario' y se agrega a la lista
                    nuevo_usuario = Usuario(usuario["nombre"], usuario["apellido"], usuario["email"], usuario["genero"])
                    lista_usuarios.append(nuevo_usuario)  # se ingresa el nuevo usuario en una lista
                except Exception as e:  # se captura cualquier excepción que ocurra al procesar la linea
                    registrar_error(e)  # se registra el error en el archivo de registro de errores
    except FileNotFoundError:  # se maneja la excepcion cuando el archivo no se encuentra
        print("No se ha encontrado el archivo de usuarios.")

    return lista_usuarios  # se devuelve la lista de usuarios cargados


def registrar_error(error: Exception) -> None:
    """
    Registra un error en el archivo de registro de errores.

    Args:
        error (Exception): El error que se va a registrar.
    """
    fecha_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")  # se obtiene la fecha y hora actual 
    texto_error = str(error)  # se convierte el error a una cadena de texto
    linea_error = f"{fecha_hora} - Error detectado: {texto_error}\n"  # se crea una linea de registro de error 
    with open("error.log", "a+") as log:  # se abre el archivo de registro de errores en modo de escritura (append)
        log.write(linea_error)  # se escribe la linea de registro de error en el archivo
            
#Extra para la revision/evaluacion del codigo
def limpiar_pantalla() -> None:
    """
    Limpia la pantalla de la consola.
    """
    os.system("cls") if os.name == "nt" else os.system("clear")  # Se utiliza el comando del sistema para limpiar la pantalla segunn el sistema operativo


def main() -> None:
    """
    Funcion principal del programa.
    """
    lista_usuarios = cargar_usuarios_desde_archivo("usuarios.txt")  # Se carga la lista de usuarios desde el archivo
    limpiar_pantalla()  # Se limpia la pantalla de la consola
    for usuario in lista_usuarios:  # Se recorre la lista de usuarios
        print(usuario)  # Se imprime cada usuario en la consola
        
if __name__ == "__main__":
    main()  # Se llama a la funcion principal si el script se ejecuta directamente
