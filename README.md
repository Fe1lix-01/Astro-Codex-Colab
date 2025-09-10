# Astro-Codex-Colab

🔒 Guía para Colaboradores: Conectar Google Colab a este Repositorio

Para que puedas trabajar en este proyecto usando Google Colab y sincronizar tus cambios con este repositorio, necesitas generar un Token de Acceso Personal (PAT) en tu cuenta de GitHub. Este token actuará como una contraseña única y segura para tus operaciones con Git.

Sigue estos pasos:

1. Generar tu Token de Acceso Personal (PAT) en GitHub

    Inicia sesión en tu cuenta de GitHub.

    Ve a tu foto de perfil en la esquina superior derecha y haz clic en Settings (Configuración).

    En el menú lateral izquierdo, haz clic en Developer settings (Configuración de desarrollador).

    Selecciona Personal access tokens (Tokens de acceso personal) y luego Tokens (classic).

    Haz clic en el botón verde Generate new token (classic).

    Configura tu token:

        Note: Dale un nombre descriptivo a tu token, como colab-access o nombre-del-proyecto.

        Expiration: Elige una fecha de vencimiento que te resulte conveniente. Una duración limitada es más segura.

        Select scopes: Marca la casilla de repo. Esto le dará a tu token los permisos necesarios para leer y escribir en los repositorios.

    Haz clic en Generate token.

    ¡IMPORTANTE! Copia el token que aparece en pantalla. Es la única vez que lo verás. Guárdalo en un lugar seguro (por ejemplo, en un gestor de contraseñas) o pégalo directamente en Colab.

2. Conectar tu Notebook de Colab con el Repositorio

Una vez que tengas tu token, abre un nuevo notebook de Colab y ejecuta las siguientes celdas de código.

    Clonar el repositorio:
    Python

!git clone https://github.com/usuario-del-repositorio/nombre-del-repositorio.git

Configurar tus credenciales de Git:
Python

%cd nombre-del-repositorio
!git config --global user.email "tu-email@ejemplo.com"
!git config --global user.name "tu-nombre-de-usuario-de-github"

Subir tus cambios (push): La primera vez que hagas un git push, se te pedirá tu nombre de usuario de GitHub y tu contraseña. Para la contraseña, pega el token de acceso personal que generaste.
Python

!git add .
!git commit -m "Mi primer commit desde Colab"
!git push
