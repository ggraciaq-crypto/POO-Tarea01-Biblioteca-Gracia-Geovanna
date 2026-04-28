from modelo.libro import Libro
from modelo.estudiante import Estudiante
from modelo.biblioteca import Biblioteca
from faker import Faker

fake = Faker()

def main():
    print("=" * 60)
    print("  SISTEMA DE GESTIÓN DE BIBLIOTECA UNEMI")
    print("=" * 60)

    biblioteca = Biblioteca("Biblioteca Central UNEMI")
    print(f"\n{biblioteca}\n")

    
    print("── Registrando libros ──")
    libro1 = Libro(fake.isbn13(), fake.sentence(nb_words=3), fake.name())
    libro2 = Libro(fake.isbn13(), fake.sentence(nb_words=3), fake.name())
    libro3 = Libro(fake.isbn13(), fake.sentence(nb_words=3), fake.name())

    biblioteca.registrar_libro(libro1)
    biblioteca.registrar_libro(libro2)
    biblioteca.registrar_libro(libro3)

    
    print("\n── Registrando estudiantes ──")
    est1 = Estudiante(str(fake.random_number(digits=10)), fake.first_name(), fake.last_name(), "Ingeniería")
    est2 = Estudiante(str(fake.random_number(digits=10)), fake.first_name(), fake.last_name(), "Derecho")

    biblioteca.registrar_estudiante(est1)
    biblioteca.registrar_estudiante(est2)

    print(f"\n{biblioteca}\n")

    
    print("── Realizando préstamos ──")
    print(biblioteca.prestar_libro(libro1.isbn, est1.cedula, "2026-04-15", "2026-04-29"))
    print(biblioteca.prestar_libro(libro2.isbn, est1.cedula, "2026-04-15", "2026-05-01"))
    print(biblioteca.prestar_libro(libro3.isbn, est2.cedula, "2026-04-15", "2026-04-22"))

    print("\n── Intentando prestar libro ya prestado ──")
    print(biblioteca.prestar_libro(libro1.isbn, est2.cedula, "2026-04-16", "2026-04-30"))

    
    print(f"\n── Préstamos activos de {est1.nombre} {est1.apellido} ──")
    prestamos = biblioteca.consultar_prestamos_activos(est1.cedula)
    for p in prestamos:
        print(f"  → {p}")

    
    print("\n── Devolviendo un libro ──")
    print(biblioteca.devolver_libro(libro1.isbn, est1.cedula))

    print("\n── Estado del libro devuelto ──")
    print(f"  {libro1}")

    print(f"\n── Préstamos activos de {est1.nombre} {est1.apellido} (después de devolución) ──")
    prestamos = biblioteca.consultar_prestamos_activos(est1.cedula)
    for p in prestamos:
        print(f"  → {p}")

    print("\n── Prestando el libro devuelto a otro estudiante ──")
    print(biblioteca.prestar_libro(libro1.isbn, est2.cedula, "2026-04-16", "2026-04-30"))

    print(f"\n{'=' * 60}")
    print(f"  {biblioteca}")
    print(f"{'=' * 60}")

if __name__ == "__main__":
    main()