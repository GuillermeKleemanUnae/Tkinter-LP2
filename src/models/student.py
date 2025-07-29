"""
Modelo de datos para representar un estudiante
"""

class Student:
    """
    Clase que representa un estudiante
    """
    
    # Contador para generar IDs únicos
    _id_counter = 1
    
    def __init__(self, name, email, age, course):
        """
        Inicializa un nuevo estudiante
        
        Args:
            name (str): Nombre del estudiante
            email (str): Email del estudiante
            age (int): Edad del estudiante
            course (str): Curso del estudiante
        """
        self.student_id = Student._id_counter
        Student._id_counter += 1
        
        self.name = name
        self.email = email
        self.age = age
        self.course = course
        
    def __str__(self):
        """
        Representación en string del estudiante
        """
        return f"ID: {self.student_id}, Nombre: {self.name}, Email: {self.email}, Edad: {self.age}, Curso: {self.course}"
        
    def __repr__(self):
        """
        Representación oficial del objeto
        """
        return f"Student(id={self.student_id}, name='{self.name}', email='{self.email}', age={self.age}, course='{self.course}')"
        
    def to_dict(self):
        """
        Convierte el estudiante a un diccionario
        
        Returns:
            dict: Diccionario con los datos del estudiante
        """
        return {
            'id': self.student_id,
            'name': self.name,
            'email': self.email,
            'age': self.age,
            'course': self.course
        }
        
    @classmethod
    def from_dict(cls, data):
        """
        Crea un estudiante desde un diccionario
        
        Args:
            data (dict): Diccionario con los datos del estudiante
            
        Returns:
            Student: Nueva instancia de Student
        """
        student = cls(data['name'], data['email'], data['age'], data['course'])
        student.student_id = data['id']
        return student
