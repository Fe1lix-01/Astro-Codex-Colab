# Astro-Codex-Colab

🚀 Guía Rápida para Colaborar

Sigue estos sencillos pasos para empezar a trabajar en este proyecto desde Google Colab.

1. Genera tu Token Personal de Acceso (PAT)

Para conectar tu entorno de Colab con este repositorio, necesitas un token de seguridad.

  - Ve a Configuración de tu perfil de GitHub.

  - En el menú lateral, selecciona Developer settings > Personal access tokens > Tokens (classic).

  - Haz clic en Generate new token (classic).

  - Asígnale un nombre (colab-access o similar) y marca el permiso de repo.

  - Haz clic en Generate token y copia el token inmediatamente. Lo necesitarás para el siguiente paso.

2. Conecta tu Notebook de Colab

Abre un nuevo notebook de Google Colab y ejecuta estas celdas de código para clonar el repositorio y subir tus cambios.
Python

```python
# CELA 1: Clona el repositorio
# Reemplaza 'nombre-del-repositorio' con el nombre de este repositorio
!git clone https://github.com/nombre-de-usuario/nombre-del-repositorio.git
```
```python
# CELA 2: Configura tus credenciales de Git
# Reemplaza con tus datos de GitHub
%cd nombre-del-repositorio
!git config --global user.email "tu-email@ejemplo.com"
!git config --global user.name "tu-nombre-de-usuario"
```

3. Sube tus Cambios al Repositorio

Cuando termines de trabajar en Colab, usa estos comandos para sincronizar tu trabajo. La primera vez que hagas un git push, se te pedirá tu nombre de usuario de GitHub y, como contraseña, debes pegar el token personal que generaste.

```python
# CELA 3: Agrega, confirma y sube tus cambios
!git add .
!git commit -m "Descripción de los cambios que realizaste"
!git push
```
