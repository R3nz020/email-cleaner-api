# Email cleaner API

API REST para validar, limpiar y extraer dominios de correos electrónicos, construida con Flask. Pensada para integrarse en flujos de registro, marketing y análisis de datos.

---

## Requisitos

- **Python 3.10+:** Verificar con `python --version`.
- **PowerShell:** Usar la Terminal de Windows 11 o PowerShell clásico.
- **Dependencias:** `flask`, `email-validator` (se instalan más abajo).

---

## Configuración local paso a paso en PowerShell

1. **Abrir PowerShell y navegar al proyecto**
   ```powershell
   cd C:\Users\dellr\Documents\email_cleaner_api

- Crear el entorno virtual en powershell
python -m venv .venv

- Activar el entorno virtual
.\.venv\Scripts\Activate.ps1

- Instalar dependencias
pip install flask email-validator

- Ejecutar la aplicación
python run.py


- Servidor local: http://127.0.0.1:5000/

Nota: Si PowerShell bloquea scripts, habilitar con:
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser



Endpoints
|  |  |  | 
| /validate-emails | POST |  | 
| /clean-emails |  | POST | 
| /extract-domains | POST |  | 

Payload común
{
  "emails": [
    " usuario@example.com ",
    "test@valid.com",
    "admin@empresa.org"
  ]
}

Pruebas paso a paso
Postman
- Crear request POST a http://127.0.0.1:5000/validate-emails
- Headers:
- Content-Type: application/json
- Body (raw, JSON):
{
  "emails": [
    "usuario@example.com",
    "correo@dominio",
    "test@valid.com"
  ]
}
- 
- Repetir para /clean-emails con:
{
  "emails": [
    "  usuario@example.com ",
    "correo@dominio.com",
    "test@valid.com  "
  ]
}
- Repetir para /extract-domains con:
{
  "emails": [
    "usuario@example.com",
    "test@valid.com",
    "admin@empresa.org"
  ]
}

curl (Windows PowerShell)
- Validación
curl -X POST http://127.0.0.1:5000/validate-emails ^
-H "Content-Type: application/json" ^
-d "{\"emails\": [\"usuario@example.com\", \"correo@dominio\", \"test@valid.com\"]}"
- Limpieza
curl -X POST http://127.0.0.1:5000/clean-emails ^
-H "Content-Type: application/json" ^
-d "{\"emails\": [\"  usuario@example.com \", \"correo@dominio.com\", \"test@valid.com  \"]}"
- Extracción de dominios
curl -X POST http://127.0.0.1:5000/extract-domains ^
-H "Content-Type: application/json" ^
-d "{\"emails\": [\"usuario@example.com\", \"test@valid.com\", \"admin@empresa.org\"]}"



Respuestas esperadas

- /validate-emails
{
  "valid_emails": ["usuario@example.com", "test@valid.com"],
  "invalid_emails": ["correo@dominio"]
}

- /clean-emails
{
  "cleaned_emails": [
    "usuario@example.com",
    "correo@dominio.com",
    "test@valid.com"
  ]
}

- /extract-domains
{
  "domains": [
    "example.com",
    "valid.com",
    "empresa.org"
  ]
}



Troubleshooting rápido
- No encuentra Activate.ps1: Confirmar que existe .venv\Scripts\Activate.ps1 con dir .venv\Scripts.
- Error “No module named flask”: Instalar dependencias dentro del entorno activo con pip install flask email-validator.
- app.py no encontrado: Ejecutar python run.py si el entrypoint del proyecto es run.py.
- Scripts bloqueados: Set-ExecutionPolicy RemoteSigned -Scope CurrentUser.


---

## Despliegue en Render (Producción)

La API está desplegada en [Render](https://render.com), lo que permite acceder a los endpoints desde cualquier cliente HTTP (Postman, navegador, etc.).

### Paso a paso para desplegar

1. **Crear cuenta en Render**
   - Ir a [render.com](https://render.com) y registrarse.

2. **Subir el proyecto a GitHub**
   - Asegurarse de tener el código en un repositorio público o privado.

3. **Crear nuevo servicio web en Render**
   - Tipo: **Web Service**
   - Fuente: **GitHub**
   - Rama: `main` (o la que uses)
   - Build Command:
     ```bash
     pip install -r requirements.txt
     ```
   - Start Command:
     ```bash
     python run.py
     ```

4. **Configurar entorno**
   - Python version: `3.10`
   - Agregar variables de entorno si las usás (ej. `FLASK_ENV=production`)

5. **Deploy**
   - Render instalará dependencias y levantará el servidor.
   - Verás una URL pública como:
     ```
     https://email-cleaner-api.onrender.com
     ```

6. **Probar en Postman**
   - Cambiar `http://127.0.0.1:5000/...` por la URL pública de Render.
   - Ejemplo:
     ```
     https://email-cleaner-api.onrender.com/validate-emails
     ```

---

## Logs y monitoreo

- Render muestra logs en tiempo real.
- Podés ver errores, prints y confirmaciones de cada request.
- Útil para depurar y verificar que los endpoints estén activos.

---

## Recomendaciones

- Usar `requirements.txt` para mantener dependencias claras.
- Confirmar que `run.py` es el entrypoint correcto.
- Probar cada endpoint en producción antes de escalar.

---