class Department:
   def __init__(self, department_id, department_name):
      """Inicializa una nueva instancia del departamento.

      Args:
            department_id (int): ID del departamento
            department_name (str): Nombre del departamento
      """
      self.department_id = department_id
      self.department_name = department_name
   
   def show_attr(self):
      """Muestra los atributos del departamento.

      Returns:
         str: Descripción del departamento.
      """
      return f'Departamento {self.department_name} (ID: {self.department_id})'
      