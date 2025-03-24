# AI Agent Tutorial

Este repositorio contiene el código desarrollado siguiendo el tutorial de YouTube ["Building AI Agents with LangChain & OpenAI"](https://www.youtube.com/watch?v=bTMPwUgLZf0&t=242s).

## Descripción

El objetivo de este proyecto es crear un agente de IA utilizando **LangChain** y **OpenAI** para interactuar con modelos de lenguaje avanzados. Se configura el entorno de desarrollo, se cargan claves de API desde un archivo `.env` y se implementa un flujo básico de interacción con un modelo de lenguaje.

## Requisitos

- Python 3.9 o superior
- pip
- Clave de API de OpenAI

## Instalación

1. **Clona el repositorio**
   ```sh
   git clone https://github.com/tu-usuario/ai-agent-tutorial.git
   cd ai-agent-tutorial
   ```

2. **Crea y activa un entorno virtual**
   ```sh
   python -m venv venv
   source venv/bin/activate  # En macOS/Linux
   venv\Scripts\activate     # En Windows
   ```

3. **Instala las dependencias**
   ```sh
   pip install -r requirements.txt
   ```

4. **Configura la clave de API de OpenAI**
   - Crea un archivo `.env` en la raíz del proyecto y agrega:
     ```env
     OPENAI_API_KEY=tu_clave_aqui
     ```

## Uso

Ejecuta el script principal:
```sh
python main.py
```

Si la configuración es correcta, el modelo responderá a la consulta programada en el código.

## Estructura del Proyecto
```
/
├── main.py              # Código principal del agente de IA
├── .env                 # Variables de entorno (no incluir en el repositorio)
├── requirements.txt     # Dependencias del proyecto
├── README.md            # Este archivo
├── venv/                # Entorno virtual (ignorar en el repositorio)
```

## Solución de Problemas

### Error: `ModuleNotFoundError: No module named 'dotenv'`
Ejecuta:
```sh
pip install python-dotenv
```

### Error: `AuthenticationError: invalid x-api-key`
Verifica que la clave de API en `.env` sea correcta y válida.

## Contribuciones
Si deseas contribuir, haz un **fork** del repositorio, crea una nueva rama con tu cambio y envía un **pull request**.

## Licencia
Este proyecto se distribuye bajo la licencia MIT.

---

📌 **Recuerda actualizar este README según evolucione el proyecto.** 🚀

