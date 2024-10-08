TOKEN = '7899466183:AAGBJ0hzjsfR5xusk6b7XRFMPcELIQgDP2o'
API_KEY = 'AIzaSyBEq9n-_Ksm0L069hxM21fJWNN8EjFGKH8'

PASSWORD_REBOOT = "8e859bde48"
PASSWORD_CORRECTA = "8e859bde48"

import google.generativeai as ai
ai.configure(api_key=API_KEY)
def obtener_chat():
    model = ai.GenerativeModel("gemini-1.5-flash")
    return model.start_chat()

chat = obtener_chat()