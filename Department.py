class Department:
   def __init__(self, department_id, department_name):
      self.department_id = department_id
      self.department_name = department_name
   
   def show_attr(self):
      return f'Departamento {self.department_name} (ID: {self.department_id})'
      