
# 🚕 Proyecto Python: Taxímetro

![Banner Proyectos](https://github.com/user-attachments/assets/bc6e34f7-4031-43dd-8cfc-805c935ba3c4)

Este proyecto simula la implementacion de un taxímetro en Python, para que calcule las tarifa del viaje basado en el tiempo empleado del vehiculo tanto en movimiento como detenido.
La idea es facilitar un calculo rapido, preciso y eficiente, para los clientes que quieran utilizar este servicio.

## 🚀 Enlace a metodologia agile empleada en el proyecto - Jira

https://gestor-habitos-personales.atlassian.net/jira/core/projects/PKT/board?groupBy=status&atlOrigin=eyJpIjoiZjMyMTBlOWE2ZTk4NDJhMzg5NGI4MzJmNzE5YmVhNTciLCJwIjoiaiJ9

---

## 📁 Estructura del Proyecto

```
Project01_Kirutasu_Taximeter/
├── idea/
│   ├──.gitignore                     # Ignora .venv
├── taximeter/
│   ├── __init__.py
│   ├── calculatingFare.py            # Función calculating_fare
│   └── taximeter.py                  # Logica principal de la implementacion
└── tests/
    └── test_calculatingFare.py       # Pruebas unitarias del metodo calculating_fare
```

---

## 📊 Niveles de Implementación y descripcion del funcionamiento

### 🟢 Nivel Esencial

1. Se muestra un mensaje de bienvenida
2. Se muestran las diferentes opciones de comandos, solicitando al usuario que de el input del que quiere seleccionar y ejecutar
3. Se inicia el trayecto en parado, simulando un taxi.
4. Se calcula la tarifa del trayecto, teniendo en cuenta los diferentes estados:
   - 📍 Parado: 0,02 € por segundo
   - 🛣️ En movimiento: 0,05 € por segundo
5. Se permite cambiar de estado durante el trayecto
6. Se finaliza el trayecto mostrando el resumen de la tarifa total.
7. Se permite iniciar un nuevo trayecto sin que el programa se cierre

*Todo esto se muestra por consola, CLI (Interfaz de Línea de Comandos)

### 🟡 Nivel medio
- Agregados 4 tests unitarios para asegurar el correcto funcionamiento del programa, verificando la funcion de calculo de tarifa.


### *Proximas mejoras a implementar:
- Uso de diferentes branches durante el desarrollo del proyecto. 
- Implementar un sistema de logs para la trazabilidad del código.
- Crear un registro histórico de trayectos pasados en un archivo de texto plano.
- Permitir la configuración de precios para adaptarse a la demanda actual.

- Refactorizar el código utilizando un enfoque orientado a objetos (OOP).
- Implementar un sistema de autenticación con contraseñas para proteger el acceso al programa.
- Desarrollar una interfaz gráfica de usuario (GUI) para hacer el programa más amigable.

---

## Funcionalidades fuera del metodo principal

### `calculating_fare(secs_stopped, secs_moving)`
Esta función calcula la tarifa total en euros basada en el tiempo detenido y el tiempo en movimiento:
- **Tiempo detenido**: 0.02 €/s.
- **Tiempo en movimiento**: 0.05 €/s.

---

## 📌 Prácticas Git utilizadas

- `feat:`, `fix:`, `docs:`, `refactor:`, `chore:` 
- commits y comandos de control de versiones GIT (add, commit, status, push...) mediante consola en el propio IDE (InteliJ)

---

## 🛠️ Tecnologías empleadas

- Python
- Git y GitHub para control de versiones
- Jira para la gestión del proyecto
- Biblioteca adicional (Unittest)

---

## 🎯 Objetivos de este proyecto

- Iniciarse en la programación con una aplicación funcional en **Python**.
- Practicar la estructura, sintaxis y entendimiento de código.
- Uso de **Git** y **GitHub** con el objetivo de seguir familiarizandose con el workflow estandar.
- Adoptar buenas prácticas:
  - Comentar el codigo para un mejor entendimiento (propio y ajeno
  - Crear un primer README decente, para habituarse a utilizar documentacion
  - Convenciones para mensajes de `commit` (como `feat:`, `fix:`, `docs:`, `refactor:`)
  - Incorporar metodologias Agile al dia a dia.
  - Probar test unitarios si no se está habituado a ello
