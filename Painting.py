class Painting:
     def __init__(self, painting_id, painting_title, painting_artist, painting_classification, painting_date, painting_image, painting_dpto):
        self.painting_id = painting_id
        self.painting_title = painting_title
        self.painting_artist = painting_artist
        self.painting_classification = painting_classification
        self.painting_date = painting_date
        self.painting_image = painting_image
        self.painting_dpto = painting_dpto

     def show_attr(self):
        return f'''Obra: {self.painting_title} (ID: {self.painting_id})
Artista: {self.painting_artist.artist_name}
'''
    
     def show_details(self):
        return f'''Obra: {self.painting_title} (ID: {self.painting_id})
Clasificación: {self.painting_classification} - Fecha de Creación: {self.painting_date}
Información del artista:
{self.painting_artist.show_attr()}'''