from modelos.genero_anime import GeneroAnime

class GestorGeneros:
    """
    Servicio que gestiona géneros de anime.
    Separa la lógica del sistema de los modelos.
    """

    def __init__(self):
        self.generos = []

    def agregar_genero(self, nombre: str, descripcion: str):
        """Crea un nuevo género y lo agrega a la lista."""
        genero = GeneroAnime(nombre, descripcion)
        self.generos.append(genero)

    def listar_generos(self):
        """Muestra todos los géneros registrados."""
        for genero in self.generos:
            print(genero.mostrar_info())

    def eliminar_genero(self, nombre: str):
        """Elimina un género por nombre (simulando liberación de recursos)."""
        for genero in self.generos:
            if genero.nombre == nombre:
                self.generos.remove(genero)
                # Al removerlo, Python podrá ejecutar el destructor (__del__)
                del genero
                print(f"[SERVICIO] Género '{nombre}' eliminado del gestor.")
                return
        print(f"[SERVICIO] Género '{nombre}' no encontrado.")