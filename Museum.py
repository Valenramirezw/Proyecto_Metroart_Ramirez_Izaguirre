from Department import Department
from Artist import Artist
from Painting import Painting

import requests
import csv

from PIL import Image

class Museum:
    def __init__(self):
        self.paintings = []
        self.departments = []

    def get_data_departments(self):
        try:
            departments_api = requests.get('https://collectionapi.metmuseum.org/public/collection/v1/departments').json()['departments']
            print('- Datos de departamentos obtenidos')
            return departments_api
        except:
            print('- No se ha logrado obtener datos de la API')

    def load_data_departments(self):
        print('- Cargando Datos...')
        departments_api = self.get_data_departments()

        if not departments_api:
            return
        
        for dpto in departments_api:
            new_department = Department(dpto['departmentId'], dpto['displayName'])
            self.departments.append(new_department)
        
        print('- Datos Cargados..')

    def get_object_id(self,painting_id):
        for painting in self.paintings:
            if painting.painting_id == painting_id:
                print(f'\tObjecto {painting_id} encontrado en la lista de OBRAS')
                return painting, True
        try:
            painting_api = requests.get(f'https://collectionapi.metmuseum.org/public/collection/v1/objects/{painting_id}').json()
        except:
            print('No se ha podido acceder a la API correctamente...')
            return None, False
        
        print(f'\tObjecto {painting_id} obtenido de la API')

        try:
            name = painting_api['artistDisplayName'] if painting_api['artistDisplayName'] else 'Desconocido'
            nationality = painting_api['artistNationality'] if painting_api['artistNationality'] else 'Desconocida'
            begin = painting_api['artistBeginDate'] if painting_api['artistBeginDate'] else 'Desconocido'
            end = painting_api['artistEndDate'] if painting_api['artistEndDate'] else 'Desconocido'
            artist = Artist(name, nationality, begin, end)


            new_painting = Painting(painting_api['objectID'], painting_api['title'], artist, painting_api['classification'], painting_api['objectDate'], painting_api['primaryImage'], painting_api['department'])

            return new_painting, False
    
        except:
            print(f'\t\tEl Objeto {painting_id} es inválido...')
            return None, True

    def search_painting_department(self):
        print('\nBÚSQUEDA POR DEPARTAMENTO')

        for i,dpto in enumerate(self.departments):
            print(f'{i+1}) {dpto.show_attr()}')


        opcion = input('Ingrese el número de la opción: ')
        while not opcion.isnumeric() or int(opcion) not in range(1,len(self.departments)+1):
            print('Su opción no ha sido válida...Vuelve a intentarlo...')
            opcion = input('Ingrese el número de la opción: ')

        selected_dpto = self.departments[int(opcion)-1]
        print(f'Obteniendo Obras del Departamento: {selected_dpto.department_name}')


        selected_paintings = []
        painting_ids = requests.get(f'https://collectionapi.metmuseum.org/public/collection/v1/objects?departmentIds={selected_dpto.department_id}').json()['objectIDs']
        
        start = 0

        while start < len(painting_ids):
            for painting_id in painting_ids[start:start+10]:
                painting,boolean = self.get_object_id(painting_id)
                if painting == None:
                    continue
                if not painting:
                    print('No se puede continuar accediendo a la API')
                    break

                if not boolean:
                    self.paintings.append(painting)
                
                selected_paintings.append(painting)
            start += 10

            if start >= len(painting_ids):
                print('Fin de los resultados')
                break
            
            print(f'# de Obras Obtenidas: {len(selected_paintings)}\n¿Te gustaría obtener mas obras?')
            op = input('Si (s)/No (cualquier tecla): ')
            
            if op != 's':
                break

        if len(selected_paintings) == 0:
            print(f'\n--- SE HAN ENCONTRADO {len(selected_paintings)} OBRAS EN LA OPCIÓN SELECCIONADA')
        else:
            print(f'\n--- SE HAN ENCONTRADO {len(selected_paintings)} OBRAS EN LA OPCIÓN SELECCIONADA')
            for painting in selected_paintings:
                print(painting.show_attr())
            
            print('- Para ver los detalles de alguna obra obtenida, dirígase al MENÚ PRINCIPAL')


    def search_painting_nationality(self):
         nationalities = []
         with open('nationalities.csv', encoding='utf-8') as f:
            lector = csv.DictReader(f)
            for fila in lector:
                nationalities.append(fila['Nationality'])

         for i, nationality in enumerate(nationalities):
            print(f'{i+1}) {nationality.capitalize()}')

         opcion = input('Ingrese el número de la opción: ')
         while not opcion.isnumeric() or int(opcion) not in range(1,len(nationalities)+1):
            print('Su opción no ha sido válida...Vuelve a intentarlo...')
            opcion = input('Ingrese el número de la opción: ')


         selected_nationality = nationalities[int(opcion)-1]
         print(f'NACIONALIDAD SELECCIONADA: {selected_nationality.upper()}')
         selected_paintings = []
         painting_ids = requests.get(f'https://collectionapi.metmuseum.org/public/collection/v1/search?artistOrCulture=true&q={selected_nationality}').json()['objectIDs']
         if not painting_ids:
             print('No se han encontrado resultados...')
             return
        
         start = 0

         while start < len(painting_ids):
            for painting_id in painting_ids[start:start+10]:
                painting, boolean = self.get_object_id(painting_id)

                if painting == None:
                    continue

                if not painting:
                    print('No se puede continuar accediendo a la API')
                    break

                if selected_nationality.lower() in painting.painting_artist.artist_nationality.lower():
                    selected_paintings.append(painting)
                    print(f'\t\tObra {painting_id} seleccionada.')

                    if not boolean:
                        self.paintings.append(painting)
                else:
                    print(f'\t\tObra {painting_id} descartada. La NACIONALIDAD DEL ARTISTA no coincide con la seleccionada')

            start += 10

            if start >= len(painting_ids):
                print('Fin de los resultados')
                break
            
            print(f'# de Obras Obtenidas: {len(selected_paintings)}\n¿Te gustaría obtener mas obras?')
            op = input('Si (s)/No (cualquier tecla): ')
            
            if op != 's':
                break

        
         if len(selected_paintings) == 0:
            print(f'\n--- SE HAN ENCONTRADO {len(selected_paintings)} OBRAS EN LA OPCIÓN SELECCIONADA')
         else:
            print(f'\n--- SE HAN ENCONTRADO {len(selected_paintings)} OBRAS EN LA OPCIÓN SELECCIONADA')
            for painting in selected_paintings:
                print(painting.show_attr())
            
            print('- Para ver los detalles de alguna obra obtenida, dirígase al MENÚ PRINCIPAL')

    def search_painting_name(self):
        artist_name = input('Ingrese el NOMBRE DEL ARTISTA que desee buscar: ').lower()
        print(f'CARACTERES DE BÚSQUEDA INGRESADOS: {artist_name.upper()}')

        selected_paintings = []
        painting_ids = requests.get(f'https://collectionapi.metmuseum.org/public/collection/v1/search?artistOrCulture=true&q={artist_name}').json()['objectIDs']
        if not painting_ids == 0:
             print('No se han encontrado resultados...')
             return
        
        start = 0

        while start < len(painting_ids):
            for painting_id in painting_ids[start:start+10]:
                painting, boolean = self.get_object_id(painting_id)
                if painting == None:
                    continue

                if not painting:
                    print('No se puede continuar accediendo a la API')
                    break


                if artist_name.lower() in painting.painting_artist.artist_name.lower():
                    selected_paintings.append(painting)
                    print(f'\t\tObra {painting_id} seleccionada.')
                    if not boolean:
                        self.paintings.append(painting)
                else:
                    print(f'\t\tObra {painting_id} descartada. El NOMBRE DEL ARTISTA no coincide con la búsqueda ingresada')

            start += 10

            if start >= len(painting_ids):
                print('Fin de los resultados')
                break
            
            print(f'# de Obras Obtenidas: {len(selected_paintings)}\n¿Te gustaría obtener mas obras?')
            op = input('Si (s)/No (cualquier tecla): ')
            
            if op != 's':
                break

        if len(selected_paintings) == 0:
            print(f'\n--- SE HAN ENCONTRADO {len(selected_paintings)} OBRAS EN LA OPCIÓN SELECCIONADA')
        else:
            print(f'\n--- SE HAN ENCONTRADO {len(selected_paintings)} OBRAS EN LA OPCIÓN SELECCIONADA')
            for painting in selected_paintings:
                print(painting.show_attr())
            
            print('- Para ver los detalles de alguna obra obtenida, dirígase al MENÚ PRINCIPAL')

    def show_details(self,selected_painting):
        for i,painting in enumerate(selected_painting):
            print(f'{i+1}) {painting.painting_title} (ID: {painting.painting_id})')

        opcion = input('Ingrese el número de la opción: ')
        while not opcion.isnumeric() or int(opcion) not in range(1,len(selected_painting)+1):
            print('Su opción no ha sido válida...Vuelve a intentarlo...')
            opcion = input('Ingrese el número de la opción: ')

        print('\n')

        print(selected_painting[int(opcion)-1].show_details())
        if selected_painting[int(opcion)-1].painting_image:
            print('¿Te gustaría ver la imagen de la obra?')
            op = input('Si (s)/No (cualquier tecla): ')
            if op.lower() == 's':
                self.show_image(selected_painting[int(opcion)-1])

    def show_image(self, painting):
        url = painting.painting_image
        nombre_base = "imagen_pintura"

        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()

            content_type = response.headers.get('Content-Type')
            extension = '.png'  
            if content_type:
                if 'image/png' in content_type:
                    extension = '.png'
                elif 'image/jpeg' in content_type:
                    extension = '.jpg'
                elif 'image/svg+xml' in content_type:
                    extension = '.svg'

            nombre_archivo = f"{nombre_base}{extension}"

            with open(nombre_archivo, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)

            img = Image.open(nombre_archivo)
            img.show()
        except Exception as e:
            print(f"Err: {e}")
        except IOError as e:
            print(f"Error al manejar el archivo: {e}")

    def start(self):
        self.load_data_departments()
        
        if len(self.departments) == 0:
            return

        print('\nBIENVENIDO/A')
        while True:
            print('\nTHE METROPOLITAN MUSEUM OF ART COLLECTION')
            print('--- Menú Principal ---')
            print('1. Buscar obras por DEPARTAMENTO')
            print('2. Buscar obras por NACIONALIDAD DEL AUTOR')
            print('3. Buscar obras por NOMBRE DEL AUTOR')
            print('4. Ver DETALLES DE LAS OBRAS ALMACENADAS')
            print('-------------------------------------------------')
            print('5. SALIR DEL PROGRAMA\n')

            opcion = input('Ingresa el número de la opción: ')

            if opcion == "5":
                print('Saliendo...')
                break
            elif opcion == '1':
                self.search_painting_department()
                input('Presione ENTER para CONTINUAR ')
            elif opcion == '2':
                self.search_painting_nationality()
                input('Presione ENTER para CONTINUAR ')
            elif opcion == '3':
                self.search_painting_name()
                input('Presione ENTER para CONTINUAR ')
            elif opcion =='4':
                self.show_details(self.paintings)
                input('Presione ENTER para CONTINUAR ')
            else:
                print('Su opción no ha sido válida... Vuelva a intentarlo...')


