

## 📋 Contenido

- [Requisitos previos](#-requisitos-previos)
- [Instalación](#-instalación)
- [Ejecución](#-ejecución)
- [Estructura del proyecto](#-estructura-del-proyecto)
- [Contribuciones](#-contribuciones)
- [Licencia](#-licencia)

---

## 🔍 Requisitos previos

Antes de comenzar, asegúrate de tener instalados:

- Python 3.10 o superior
- pip
- virtualenv

---

## 🛠️ Instalación

Clona el repositorio y accede a la carpeta del proyecto:

```bash
git clone https://github.com/PabloC2A/Portal-Web-CCL.git
cd Portal-Web-CCL
```

Crea y activa un entorno virtual:

```bash
python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate
```

Instala las dependencias:

```bash
pip install django==5.2.4
pip install Pillow #Necesaria para que Django pueda procesar subidas de imágenes
```

---

## ▶️ Ejecución

Aplica migraciones y ejecuta el servidor:

```bash
python manage.py migrate
python manage.py runserver
```

Accede a la aplicación en tu navegador:

```
http://localhost:8000/
```

# 🤝 Contribuciones

¡Gracias por tu interés en contribuir a este proyecto!\
Sigue los pasos a continuación para colaborar de forma ordenada y efectiva.

---

## 🚀 Cómo contribuir

### 1. Haz un fork del repositorio

Haz clic en el botón **"Fork"** (arriba a la derecha en GitHub). Esto creará una copia del proyecto en tu cuenta.

### 2. Clona tu fork

```bash
git clone https://github.com/tu-usuario/Portal-Web-CCL.git
cd Portal-Web-CCL
```

> Reemplaza `tu-usuario` con tu nombre de usuario real de GitHub.

### 3. Crea una nueva rama para tu cambio

No trabajes directamente sobre la rama `main`.

```bash
git checkout -b feature/nombre-del-cambio
```

Ejemplos:

- `feature/login-usuario`
- `fix/bug-en-menu`
- `docs/actualiza-readme`

### 4. Realiza tus cambios

Haz los cambios que deseas y asegúrate de probar que todo funcione correctamente.

### 5. Haz commit de tus cambios

```bash
git add .
git commit -m "Descripción clara y concisa del cambio"
```

> Usa mensajes de commit que expliquen **qué hiciste** y **por qué**, no solo "cambios".

### 6. Sube tus cambios a tu fork

```bash
git push origin feature/nombre-del-cambio
```

### 7. Abre un Pull Request

1. Ve a tu fork en GitHub.
2. Haz clic en **"Compare & pull request"**.
3. Asegúrate de que el PR apunte a la rama `main` del repositorio original.
4. Escribe un título y descripción clara de tus cambios.
5. Haz clic en **"Create pull request"**.

---

## 🔄 Mantén tu fork actualizado

Es recomendable mantener tu fork sincronizado con el repositorio original.

### 1. Agrega el repositorio original como remoto

```bash
git remote add upstream https://github.com/PabloC2A/Portal-Web-CCL.git
```

### 2. Trae los últimos cambios

```bash
git fetch upstream
```

### 3. Mezcla los cambios en tu rama `main`

```bash
git checkout main
git merge upstream/main
```

### 4. Sube tu rama actualizada a tu fork

```bash
git push origin main
```

---

## 🧩 ¿Cómo integrar los cambios de una rama `feature/...` al `main` de tu fork?

### Opción 1: Pull Request interno en tu fork (recomendado)

1. Ve a tu fork en GitHub.
2. Haz clic en **"Pull Requests"** > **"New Pull Request"**.
3. En el comparador selecciona:
   - `base`: tu rama `main`
   - `compare`: tu rama `feature/nombre-del-cambio`
4. Revisa los cambios y haz clic en **"Create Pull Request"**.
5. Finalmente, haz clic en **"Merge pull request"**.

### Opción 2: Fusionar manualmente con Git

Si prefieres hacerlo desde la terminal:

```bash
git checkout main
git merge feature/nombre-del-cambio
git push origin main
```

Esta opción es directa y útil si no necesitas revisión de código o estás trabajando solo.

---

## ✅ Buenas prácticas

- Usa ramas para cada funcionalidad o corrección.
- Asegúrate de que tu código compila / pasa pruebas antes de hacer PR.
- Escribe descripciones claras en tus commits y pull requests.
- Si tienes dudas, abre un *issue* o comenta en el PR.

---