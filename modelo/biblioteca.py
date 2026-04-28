from modelo.libro import Libro
from modelo.estudiante import Estudiante
from modelo.prestamo import Prestamo

class Biblioteca:
    def __init__(self, nombre):
        self._nombre = nombre
        self._libros = []
        self._estudiantes = []
        self._prestamos = []

    def registrar_libro(self, libro):
        self._libros.append(libro)
        print(f"Libro registrado: {libro.titulo}")

    def registrar_estudiante(self, estudiante):
        self._estudiantes.append(estudiante)
        print(f"Estudiante registrado: {estudiante.nombre}")

    def prestar_libro(self, isbn, cedula, fecha_prestamo, fecha_devolucion):
        libro = next((l for l in self._libros if l.isbn == isbn), None)
        estudiante = next((e for e in self._estudiantes if e.cedula == cedula), None)

        if libro is None:
            return "Libro no encontrado"

        if estudiante is None:
            return "Estudiante no encontrado"

        if not libro.disponible:
            return "Libro no disponible"

        libro.prestar()
        prestamo = Prestamo(libro, estudiante, fecha_prestamo, fecha_devolucion)
        self._prestamos.append(prestamo)

        return f"Préstamo realizado: {libro.titulo}"

    def devolver_libro(self, isbn, cedula):
        for p in self._prestamos:
            if p.libro.isbn == isbn and p.estudiante.cedula == cedula and p.activo:
                p.registrar_devolucion()
                return "Libro devuelto"

        return "No se encontró préstamo"

    def consultar_prestamos_activos(self, cedula):
        return [p for p in self._prestamos if p.estudiante.cedula == cedula and p.activo]

    
    def __str__(self):
        return (f"Biblioteca '{self._nombre}' | "
                f"Libros: {len(self._libros)} | "
                f"Estudiantes: {len(self._estudiantes)} | "
                f"Préstamos: {len(self._prestamos)}")