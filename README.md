# Proyecto de Administración de Postres y Repostería

Este proyecto es una aplicación Django para gestionar y administrar productos de repostería, permitiendo la creación, actualización y visualización de postres y otros productos.

## Descripción del Proyecto

La aplicación permite a los usuarios (administradores y huéspedes) gestionar un inventario de postres y revisar información detallada de los productos de repostería.

## Prerrequisitos o Dependencias

Lista de software y herramientas necesarias para instalar y ejecutar este proyecto:

- **Sistema Operativo**: Ubuntu 20.04, Windows 10 o superior
- **Python**: 3.8 o superior
- **Django**: 5.1.2
- **Base de datos**: SQLite (configuración predeterminada) o PostgreSQL (opcional)
- **Otros módulos**:

  - asgiref==3.8.1
  - sqlparse==0.5.1
  - tzdata==2024.2

## Instalación del Proyecto

Sigue estos pasos para configurar el entorno de desarrollo y preparar todas las dependencias:

```bash
# Clona el repositorio
git clone https://github.com/bpardo02/appWeb-Postres

# Navega al directorio del proyecto
cd proyectoinforcap

# Instala las dependencias
pip install -r requirements.txt
```

## Instrucciones para Migrar Modelos y Cargar la Base de Datos

```bash
# Realiza las migraciones de base de datos
python manage.py makemigrations
python manage.py migrate
```

## Instrucciones para Ejecutar el Proyecto

Una vez instaladas las dependencias, puedes ejecutar el proyecto usando el siguiente comando:

```bash
# Ejecuta el servidor de desarrollo de Django
python manage.py runserver


Accede a la aplicación en tu navegador en http://localhost:8000.
```

**Hecho por:** [Benjamín Pardo](https://github.com/bpardo02)
