🚀 README.md mejorado
markdown
Copiar
Editar
# 🤖 Telegram AI Video Bot

Genera **videos animados a partir de texto** usando inteligencia artificial.

Este bot de Telegram utiliza modelos de IA como Stable Diffusion y Stable Video Diffusion para convertir un prompt de texto en un video realista y animado.

---

## 🧠 Características

- 🎨 **Texto a Imagen** con `Stable Diffusion`
- 🎞️ **Imagen a Video** con `Stable Video Diffusion`
- 🤖 **Interfaz vía Telegram**
- 💬 Comandos simples para generar contenido visual

---

## 📦 Requisitos

- Python 3.10 o superior
- GPU con soporte CUDA (opcional, recomendado)
- Dependencias (instalables con `pip install -r requirements.txt`)
- Cuenta de HuggingFace para acceder a los modelos

---

## ⚙️ Instalación

```bash
git clone https://github.com/Hanzzel-corp/telegram-ai-video-bot.git
cd telegram-ai-video-bot
python -m venv env
env\Scripts\activate  # En Windows
pip install -r requirements.txt
🚀 Uso
Configura tu bot de Telegram con el token en bot/telegram_bot.py.

Ejecuta el bot:

bash
Copiar
Editar
python test_run.py
Envía un mensaje a tu bot con el prompt:

nginx
Copiar
Editar
Un colibrí de cristal volando entre rayos de luz
Recibirás un video generado por IA.

📂 Estructura del Proyecto
bash
Copiar
Editar
.
├── bot/
│   └── telegram_bot.py       # Controla la interacción con Telegram
├── generator/
│   └── svd_runner_real.py    # Genera el video usando SVD
├── output/
│   └── final_video.mp4       # Resultado generado
├── requirements.txt
└── README.md
📸 Ejemplo


🧪 Créditos
Este proyecto fue desarrollado por Hanzzel Corp usando la lógica de los NCT (Números Cuánticos Tridimensionales) como base para futura integración semántica.

⭐ Licencia
MIT - Libre para usar, modificar y mejorar.

yaml
Copiar
Editar

---

¿Te lo subo directamente como nuevo `README.md` o querés editarlo vos y luego hacer commit?
