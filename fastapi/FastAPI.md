# 🚀 Guía básica de instalación y ejecución de FastAPI con Uvicorn

## 📦 Paso 1: Crear un entorno virtual (opcional pero recomendado)

```bash
python -m venv env
source env/bin/activate     # Linux/macOS
env\Scripts\activate        # Windows
````

---

## 🧪 Paso 2: Instalar FastAPI y Uvicorn

```bash
pip install fastapi uvicorn pydantic
```

---

## 📝 Paso 3: Crear un archivo Python con tu API

Crea un archivo llamado `main.py` con este contenido básico:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensaje": "¡Hola desde FastAPI!"}

@app.get("/saludo/{nombre}")
def saludar(nombre: str):
    return {"saludo": f"Hola, {nombre} 👋"}
```

---

## 🚦 Paso 4: Ejecutar el servidor con Uvicorn

```bash
uvicorn main:app --reload
```

* `main`: es el nombre del archivo (sin `.py`)
* `app`: es el nombre de la instancia de FastAPI
* `--reload`: reinicia el servidor automáticamente al editar el código (modo desarrollo)

---

## 🌐 Paso 5: Acceder a tu API

Una vez ejecutado, abre en tu navegador:

* Documentación interactiva: [http://localhost:8000/docs](http://localhost:8000/docs)
* Documentación alternativa: [http://localhost:8000/redoc](http://localhost:8000/redoc)
* Ruta base: [http://localhost:8000/](http://localhost:8000/)
* Ruta personalizada: [http://localhost:8000/saludo/TuNombre](http://localhost:8000/saludo/TuNombre)

---
