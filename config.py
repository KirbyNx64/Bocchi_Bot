TOKEN = '7835243662:AAEIrLZ5QTSgF6ycJxD9wTuXaLC35nhFhmc'
API_KEY = 'AIzaSyBEq9n-_Ksm0L069hxM21fJWNN8EjFGKH8'

import google.generativeai as ai
ai.configure(api_key=API_KEY)
def obtener_chat():
    model = ai.GenerativeModel("gemini-1.5-flash")
    return model.start_chat()

chat = obtener_chat()