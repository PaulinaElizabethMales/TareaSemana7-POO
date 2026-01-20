class GeneroAnime:
    """
    Clase que representa un género de anime.
    Uso de __init__ y __del__ para demostrar constructores y destructores.
    """

    def __init__(self, nombre: str, descripcion: str):
        """
        Constructor (__init__):
        - Inicializa los atributos obligatorios del género de anime.
        - Se ejecuta automáticamente al crear una instancia.
        """
        self.nombre = nombre
        self.descripcion = descripcion
        print(f"[INIT] Se creó el género de anime: {self.nombre}")

    def __del__(self):
        """
        Destructor (__del__):
        - Se ejecuta automáticamente cuando el objeto es eliminado por el recolector de basura.
        - Aquí simulamos una 'limpieza' registrando que el objeto dejó de existir.
        """
        print(f"[DEL] El género de anime '{self.nombre}' ha sido eliminado de la memoria.")

    def mostrar_info(self) -> str:
        """Devuelve información del género de anime."""
        return f"Género: {self.nombre} - Descripción: {self.descripcion}"