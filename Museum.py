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


    def get_object_id(self):
        pass

    def search_painting_department(self):
        pass


    def search_painting_nationality(self):
        pass

    def search_painting_name(self):
        pass


    def show_details(self):
        pass


    def show_image(self):
        pass

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


