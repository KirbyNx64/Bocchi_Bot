from commands import application
import platform
import sys
import os

def reboot():
    if platform.system() == "Windows":
        os.execv(sys.executable, ['python'] + sys.argv)
    else:
        os.execv(sys.executable, ['python3'] + sys.argv)

if __name__ == "__main__":
    while True:
        try:
            print("\n- Bot Iniciado.")
            application.run_polling()
        except Exception as e:
            print(f"Error detectado: {e}")
            reboot()