¡Claro! Aquí te dejo la **guía unificada y con estilo limpio**, siguiendo el mismo formato que usamos para FastAPI, pero enfocada a `requests` y el uso de la **Cat API**. Está lista para copiar en un `README.md` o en un Google Doc para tu taller:

---

````markdown
# 🐾 Guía básica: Consumir una API en Python con `requests`

En esta guía aprenderás a consumir una API real (The Cat API) usando Python y el módulo `requests`.

---

## 📦 Paso 1: Crear entorno virtual (opcional pero recomendado)

```bash
python -m venv env
source env/bin/activate     # Linux/macOS
env\Scripts\activate        # Windows
````

---

## 🧪 Paso 2: Instalar el módulo `requests`

```bash
pip install requests
```

---

## 🐱 Paso 3: Usar The Cat API

📄 Documentación oficial:
[https://developers.thecatapi.com/view-account/ylX4blBYT9FaoVd6OhvR?report=bOoHBz-8t](https://developers.thecatapi.com/view-account/ylX4blBYT9FaoVd6OhvR?report=bOoHBz-8t)

🔑 API Key (de ejemplo):

```
live_4wAzpg9xQMwZfcpLPVeML5tyV1YCGBBgHPyFE7fU823zZVwaaKdu6ABT6Egv05wC
```

---

## 📥 Peticiones `GET` con `requests`

```python
import requests

url = "https://api.thecatapi.com/v1/images/search"

response = requests.get(
    url,
    params={"limit": 3, "mime_types": "gif"},         # Query Params
    headers={"x-api-key": "TU_API_KEY"},              # Headers
    cookies={"session_id": "12345"},                  # Cookies
    auth=("usuario", "password"),                     # Autenticación básica
    timeout=10                                        # Tiempo máximo en segundos
)

print(response.json())
```

---

## 📤 Peticiones `POST` con `requests`

```python
import requests

url = "https://api.thecatapi.com/v1/votes"

response = requests.post(
    url,
    json={"image_id": "abc123", "value": 1},          # Body en JSON
    data={"campo1": "valor1", "campo2": "valor2"},    # Body como formulario
    headers={"x-api-key": "TU_API_KEY"},              # Headers
    cookies={"session_id": "12345"},                  # Cookies
    files={"file": open("foto.jpg", "rb")},           # Subida de archivos
    auth=("usuario", "password"),                     # Autenticación básica
    timeout=10,                                       # Tiempo máximo en segundos
    allow_redirects=True                              # Permitir redirecciones
)

print(response.status_code)
print(response.json())
```

