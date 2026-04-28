#  Sistema de Gestión de Biblioteca UNEMI

* Nombres: Jean Pierre Mina Quintero
           Geovanna Mailyn Gracia Quiñonez
* Carrera:Ingeniería en Software
* Semestre:4to semestre

## Descripción del Proyecto

En este proyecto desarrollamos un sistema básico para la gestión de una biblioteca universitaria utilizando Python y Programación Orientada a Objetos.

El sistema permite registrar libros y estudiantes, así como realizar préstamos y devoluciones. Además, se puede consultar qué libros tiene prestados un estudiante y validar la disponibilidad de los mismos.

Adicionalmente, se implementó el uso de datos aleatorios mediante la librería Faker, lo que permite simular un entorno más dinámico y realista.

## Estructura del Proyecto

El proyecto está organizado en carpetas para separar el código y facilitar su comprensión:

mi_biblioteca/
│
├── modelo/
│   ├── persona.py
│   ├── estudiante.py
│   ├── libro.py
│   ├── prestamo.py
│   └── biblioteca.py
│
├── diagramas/
│   └── diagrama_clases.puml
│
├── main.py
└── README.md

## Aplicación de Programación Orientada a Objetos

En el desarrollo del sistema aplicamos varios conceptos importantes de POO:

* Encapsulamiento: los atributos de las clases son privados  
* Herencia: la clase Estudiante hereda de Persona  
* Abstracción: se modelan únicamente los datos necesarios del sistema  
* Polimorfismo: uso del método `__str__` en diferentes clases  

## Uso de la Librería Faker

Para mejorar la funcionalidad del sistema, utilizamos la librería Faker de Python, la cual permite generar datos aleatorios de manera automática.

Gracias a esta herramienta, se generaron nombres de estudiantes, títulos de libros, autores e identificadores (ISBN), evitando el ingreso manual de datos y logrando una simulación más realista del sistema.

Esto permitió que el sistema sea más dinámico y representativo de un entorno real de biblioteca.

## Ejecución del Programa

Para ejecutar el programa se deben seguir los siguientes pasos:

1. Instalar la librería Faker:

pip install Faker

2. Ejecutar el programa:

python main.py

## Funcionalidades del Sistema

* Registro de libros  
* Registro de estudiantes  
* Préstamo de libros  
* Devolución de libros  
* Consulta de préstamos activos  

## Observación del Proyecto

Este proyecto nos permitió comprender de mejor manera cómo aplicar la Programación Orientada a Objetos en un caso real, desde el análisis del problema hasta la implementación en código Python.

Además, fortalecimos nuestras habilidades en la organización del código, el uso de clases y la implementación de funcionalidades que simulan situaciones del mundo real.
