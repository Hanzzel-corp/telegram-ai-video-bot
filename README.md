# 🤖 Bot de Telegram para Generación de Video con IA

Genera **videos animados a partir de texto** e imágenes usando inteligencia artificial.

Este bot de Telegram utiliza modelos de IA como Stable Diffusion y Stable Video Diffusion para convertir un prompt de texto en un video animado, o para transformar tus fotos a estilo anime.

---
## 🧠 Características

- 🎨 **Texto a Video:** Envía un prompt y recibe un video animado.
- 🖼️ **Foto a Anime:** Envía una foto y el bot la transformará a estilo anime.
- 🤖 **Interfaz vía Telegram:** Control total a través de comandos y mensajes simples.
- 📂 **Código Abierto:** Libre para usar, modificar y aprender.

---
## 📦 Requisitos

- Python 3.10 o superior
- Git
- Una cantidad considerable de RAM (8GB como mínimo, 16GB+ recomendado)
- GPU con soporte CUDA (opcional, pero **altamente recomendado** para velocidad)

---
## ⚙️ Instalación

1.  **Clona el repositorio:**
    ```bash
    git clone https://github.com/Hanzzel-corp/telegram-ai-video-bot.git
    cd telegram-ai-video-bot
    ```

2.  **Crea y activa un entorno virtual:**
    ```bash
    # Crear el entorno
    python -m venv env
    # Activar en Windows
    .\env\Scripts\activate
    # Activar en Linux/Mac
    # source env/bin/activate
    ```

3.  **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configura tu Token de Telegram:**
    - Habla con `@BotFather` en Telegram para crear un bot y obtener tu token.
    - Crea una carpeta llamada `config` en la raíz del proyecto.
    - Dentro de `config`, crea un archivo llamado `.env`.
    - Añade tu token al archivo `.env` de esta forma:
      ```
      TELEGRAM_TOKEN="AQUÍ_VA_TU_TOKEN_SECRETO"
      ```

---
## 🚀 Uso

Una vez instalado, ejecuta el bot desde la carpeta raíz del proyecto con el siguiente comando:

```bash
python -m bot.telegram_bot
```

El bot se iniciará y estará esperando mensajes. Ahora puedes ir a Telegram y hablar con él.

Para generar un video: Simplemente envíale un mensaje de texto con tu prompt (ej. Un colibrí de cristal volando entre rayos de luz).

Para crear un anime: Envíale una foto directamente.

📸 Ejemplo
(Próximamente: un GIF mostrando el bot en acción)

🧪 Créditos
Este proyecto fue desarrollado por Hanzzel Corp. NCT se menciona únicamente como una línea conceptual de investigación. Este bot no declara integrar NCT ni demostrar comportamiento cuántico.

⭐ Licencia
MIT License - Libre para usar, modificar y mejorar.

---

## Dirección de investigación y autoría

**José Zamora — Investigador principal independiente (Independent Principal Investigator), Hanzzel Corp.**

Este repositorio es un proyecto individual del ecosistema Hanzzel Corp. La relación técnica de este proyecto con NCT, cuando existe, se limita al alcance descrito en esta documentación; la pertenencia institucional no implica integración adicional ni valida resultados más allá de la evidencia documentada aquí.
