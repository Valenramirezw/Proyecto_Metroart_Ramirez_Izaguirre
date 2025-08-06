class Artist:
    def __init__(self, artist_name, artist_nationality, artist_birth, artist_death):
        self.artist_name = artist_name
        self.artist_nationality = artist_nationality
        self.artist_birth = artist_birth
        self.artist_death = artist_death

    def show_attr(self):
        return f'''Artista: {self.artist_name}
Nacionalidad: {self.artist_nationality}
Fecha de Nacimiento: {self.artist_birth} - Fecha de Muerte: {self.artist_death}
'''
    
