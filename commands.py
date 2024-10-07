from config import TOKEN, chat, obtener_chat
from telegram.ext import Application, CommandHandler, MessageHandler, filters
import speedtest
import qrcode
import os
import random

application = Application.builder().token(TOKEN).build()

async def gemini(update, context):
    try:
        pregunta = update.message.text.split(" ", 1)[1]
        mensaje_generando = await update.message.reply_text("Generando respuesta...")

        response = chat.send_message(pregunta)
        response_nuevo = response.text.replace("**", "")

        await mensaje_generando.edit_text(response_nuevo)

    except IndexError:
        await update.message.reply_text("Por favor, proporciona una pregunta después del comando.")
application.add_handler(CommandHandler("ai", gemini))

async def gemini_private(update, context):
    user_message = update.message.text
    mensaje_generando = await update.message.reply_text("Generando respuesta...")

    response = chat.send_message(user_message)
    response_nuevo = response.text.replace("**", "")

    await mensaje_generando.edit_text(response_nuevo)
application.add_handler(MessageHandler(filters.TEXT & filters.ChatType.PRIVATE & ~filters.COMMAND, gemini_private))

async def gemini_r(update, context):
    try:
        if update.message.reply_to_message:
            pregunta = update.message.reply_to_message.text
            message_id = update.message.reply_to_message.id
        else:
            pregunta = update.message.text.split(" ", 1)[1]
            message_id = None

        mensaje_generando = await update.message.reply_text("Generando respuesta...", reply_to_message_id=message_id)

        response = chat.send_message(pregunta)
        response_nuevo = response.text.replace("**", "")

        await mensaje_generando.edit_text(response_nuevo)

    except IndexError:
        await update.message.reply_text("Por favor, proporciona una pregunta después del comando.")
application.add_handler(CommandHandler("air", gemini_r))

async def help(update, context):
    await update.message.reply_text("""
Hola personita del internet.
                                    
Soy un bot creado con Python y potenciado por Inteligencia Artificial Gemini by Google. Estoy aquí para ayudarte a responder tus preguntas, ofrecerte información y hacer que tu experiencia en Telegram sea más fácil y divertida. ¡Pregúntame lo que quieras!.
                                    
Para cualquier otra consulta preguntale @kirby_limon
""")
application.add_handler(CommandHandler("ayuda", help))

async def start(update, context):
    oraciones = [
    "El sol brilla intensamente en el cielo.",
    "Hoy es un buen día para aprender algo nuevo.",
    "El gato duerme plácidamente.",
    "La tecnología avanza a pasos agigantados.",
    "Las montañas están cubiertas de nieve.",
    "¡Soy la mejor tocando la guitarra!",
    "Estoy para ayudarte en lo que necesites",
    "¿Alguna vez te dijeron lo guapo/a que eres?"
    ]

    def oracion_aleatoria(oraciones):
        return random.choice(oraciones)

    await update.message.reply_text(f"""
¡Hola!, soy Bocchis Bot.

{oracion_aleatoria(oraciones)}
""")
application.add_handler(CommandHandler("start", start))

async def speedtest_command(update, context):
    mensaje_inicial = await update.message.reply_text("Realizando test de velocidad...")

    try:
        st = speedtest.Speedtest()
        st.download()
        st.upload()
        st.get_best_server()
        resultados = st.results.dict()

        mensaje_resultados = f"""
Resultados del test de velocidad Speedtest by Ookla:

Servidor: {resultados['client']['isp']}
Ping: {resultados['ping']} ms
Descarga: {resultados['download'] / 1000000:.2f} Mbps
Subida: {resultados['upload'] / 1000000:.2f} Mbps
"""

        await mensaje_inicial.edit_text(mensaje_resultados)

    except Exception as e:
        await update.message.reply_text(f"Error al realizar el test de velocidad: {e}")
application.add_handler(CommandHandler("speedtest", speedtest_command))

async def reiniciar_conversacion(update, context):
    global chat

    PASSWORD_CORRECTA = "quesitoconpan"
    try:
        user_message = update.message.text.split(" ", 1)[1]
        if user_message == PASSWORD_CORRECTA:
            chat = obtener_chat() 
            await update.message.reply_text("Bot reiniciado.")
        else:
            await update.message.reply_text("Lo siento la contraseña es incorrecta.")
    except IndexError:
        await update.message.reply_text("Esta función requiere de una contraseña.")
application.add_handler(CommandHandler("reiniciar", reiniciar_conversacion))

async def sticker_handler(update, context):
    await update.message.reply_text("Ese es un sticker divertido xD")
application.add_handler(MessageHandler(filters.Sticker.ALL & filters.ChatType.PRIVATE, sticker_handler))

async def sticker_handler(update, context):
    await update.message.reply_text("Humm... Interesante foto, aunque es una lastima que actualmente no puedo verla pero puedes darme detalles sobre ella y con gusto te ayudaré.")
application.add_handler(MessageHandler(filters.PHOTO & filters.ChatType.PRIVATE, sticker_handler))

async def qr_command(update, context):
    try:
        if update.message.reply_to_message:
            texto = update.message.reply_to_message.text
        else:
            texto = update.message.text.split(" ", 1)[1]

        img = qrcode.make(texto)
        img.save("qrcode.png")

        await update.message.reply_photo("qrcode.png")

        os.remove("qrcode.png")

    except IndexError:
        await update.message.reply_text("Por favor, proporciona el texto para generar el código QR. Ejemplo: /qrcode Hola mundo")
application.add_handler(CommandHandler("qrcode", qr_command))
