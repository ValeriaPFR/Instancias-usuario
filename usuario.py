class Usuario:
    """
    Clase para representar un usuario.
    
    Attributes:
        nombre (str): El nombre del usuario.
        apellidos (str): Los apellidos del usuario.
        email (str): El correo electronico del usuario.
        genero (str): El genero del usuario.
    """

    def __init__(self, nombre: str, apellido: str, email: str, genero: str) -> None:
        """
        Constructor de la clase 'Usuario'.

        Args:  
            nombre (str): El nombre del usuario.
            apellidos (str): Los apellidos del usuario.
            email (str): El correo electronico del usuario.
            genero (str): El genero del usuario.
        """
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.genero = genero
    
    def __str__(self) -> str:
        """
        Devuelve una representacion de cadena del objeto 'Usuario'.

        Returns:
            str: La representacion de cadena del objeto 'Usuario'.
        """
        return f"Nombre: {self.nombre} Apellido: {self.apellido} Email: {self.email} Genero: {self.genero}"
