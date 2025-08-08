class Artist:
    def __init__(self, artist_name, artist_nationality, artist_birth, artist_death):
        """Inicializa una nueva instancia del artista.

        Args:
            artist_name (str): Nombre del artista
            artist_nationality (str): Nacionalidad del artista
            artist_birth (str): Fecha de nacimiento del artista
            artist_death (str): Fecha de muerte del artista
        """
        self.artist_name = artist_name
        self.artist_nationality = artist_nationality
        self.artist_birth = artist_birth
        self.artist_death = artist_death

    def show_attr(self):
         """
        Muestra los atributos del artista.
        Returns:
            str: Descripción del artista."""
         return f'''\tArtista: {self.artist_name}
\tNacionalidad: {self.artist_nationality}
\tFecha de Nacimiento: {self.artist_birth} 
\tFecha de Muerte: {self.artist_death}
'''
    
