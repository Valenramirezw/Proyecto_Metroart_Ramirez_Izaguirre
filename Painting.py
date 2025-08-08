class Painting:
     def __init__(self, painting_id, painting_title, painting_artist, painting_classification, painting_date, painting_image, painting_dpto):
        """
        Inicializa una nueva instancia de la pintura.

        Args:
            painting_id (int): ID de la pintura
            painting_title (str): Título de la pintura
            painting_artist (Artist): Artista de la pintura
            painting_classification (str): Clasificación de la pintura
            painting_date (str): Fecha de creación de la pintura
            painting_image (str): URL de la imagen de la pintura
            painting_dpto (Department): Departamento al que pertenece la pintura
        """
        self.painting_id = painting_id
        self.painting_title = painting_title
        self.painting_artist = painting_artist
        self.painting_classification = painting_classification
        self.painting_date = painting_date
        self.painting_image = painting_image
        self.painting_dpto = painting_dpto

     def show_attr(self):
        """
        Muestra los atributos de la pintura.

        Returns:
            str: Descripción de la pintura.
        """
        return f'''Obra: {self.painting_title} (ID: {self.painting_id})
Artista: {self.painting_artist.artist_name}
'''
    
     def show_details(self):
        """
        Muestra los detalles de la pintura, incluyendo información del artista
        Returns:
            str: Detalles completos de la pintura.
        """
        return f'''Obra: {self.painting_title} (ID: {self.painting_id})
Clasificación: {self.painting_classification if self.painting_classification != "" else "Desconocida"} 
Fecha de Creación: {self.painting_date}
Información del artista:
{self.painting_artist.show_attr()}'''