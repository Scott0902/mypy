import pyautogui
import time
while True:
    x, y = pyautogui.position()
    print(f"X: {str(x).rjust(4)} Y: {str(y).rjust(4)}",end='\r',flush=True)
    time.sleep(0.1)