# Ubicación: D:\IA_VideoBot\bot\telegram_bot.py

import os
import asyncio
import logging
import traceback
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Corrige la importación para que coincida con tu nombre de archivo real
from generator.svd_runner_real import text_to_video_workflow

# --- Configuración Segura ---
# Le decimos a dotenv que busque el archivo .env dentro de la carpeta 'config'
load_dotenv(dotenv_path='config/.env')

# Lee las variables del entorno
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

if not TELEGRAM_TOKEN:
    # Este error se mostrará si el token no se encuentra.
    # Asegúrate de haber revocado el token antiguo y de usar el nuevo.
    raise ValueError("No se encontró el TELEGRAM_TOKEN. Asegúrate de que tu archivo .env está en la carpeta 'config' y está configurado correctamente.")

# Configurar logging para ver qué está pasando en la consola
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


# --- Funciones del Bot ---

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Manda un mensaje de bienvenida cuando el usuario usa /start."""
    await update.message.reply_text(
        "¡Hola! Soy un bot que crea videos a partir de texto. "
        "Envíame una descripción (prompt) y haré mi magia. "
        "Ten en cuenta que el proceso es muy lento y puede tardar más de una hora."
    )

async def generate_video_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Maneja los mensajes de texto y comienza la generación del video."""
    prompt = update.message.text
    chat_id = update.message.chat_id
    logger.info(f"Recibido prompt del chat {chat_id}: '{prompt}'")

    await context.bot.send_message(
        chat_id=chat_id,
        text=f"🤖 Petición recibida para: '{prompt}'.\n\n"
             "El proceso de generación ha comenzado. Esto puede tardar mucho tiempo. "
             "Te notificaré cuando el video esté listo. ¡Gracias por tu paciencia!"
    )

    try:
        # Define una ruta de salida única para este video para evitar conflictos
        output_file_path = f"output/{chat_id}_{update.message.message_id}.mp4"

        # Ejecuta la función pesada en un hilo separado para no bloquear el bot
        loop = asyncio.get_running_loop()
        await loop.run_in_executor(
            None, text_to_video_workflow, prompt, output_file_path
        )

        logger.info(f"Video generado. Enviando {output_file_path} al chat {chat_id}.")
        await context.bot.send_video(
            chat_id=chat_id,
            video=open(output_file_path, 'rb'),
            caption=f"¡Tu video para '{prompt}' está listo! 🎉"
        )
        
        # Opcional: Borrar el video del servidor después de enviarlo para ahorrar espacio
        os.remove(output_file_path)

    except Exception as e:
        logger.error(f"Error al generar video para el chat {chat_id}: {e}", exc_info=True)
        await context.bot.send_message(
            chat_id=chat_id,
            text="Lo siento, ocurrió un error crítico y no pude generar tu video."
        )

def main():
    """Inicia y corre el bot."""
    print("Iniciando bot...")
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # Añadir los manejadores de comandos
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, generate_video_handler))

    print("Bot iniciado. Presiona Ctrl+C para detener.")
    application.run_polling()


if __name__ == '__main__':
    main()