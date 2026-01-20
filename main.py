from servicios.gestor_generos import GestorGeneros

def main():
    print("=== Sistema de Géneros de Anime ===")

    gestor = GestorGeneros()

    # Crear géneros (uso de __init__)
    gestor.agregar_genero("Shonen", "Acción y aventura, dirigido a jóvenes.")
    gestor.agregar_genero("Shojo", "Romance y drama, dirigido a chicas adolescentes.")
    gestor.agregar_genero("Seinen", "Historias más maduras y complejas.")

    print("\n--- Lista de géneros registrados ---")
    gestor.listar_generos()

    # Eliminar un género (uso de __del__)
    print("\n--- Eliminando un género ---")
    gestor.eliminar_genero("Shojo")

    print("\n--- Lista actualizada ---")
    gestor.listar_generos()

if __name__ == "__main__":
    main()