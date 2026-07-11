import keyboard
import time

print("Aperte ESC para testar...")
while True:
    if keyboard.is_pressed("esc"):
        print("ESC detectado!")
        break
    time.sleep(0.1)