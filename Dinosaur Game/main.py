import pyautogui
import time
from PIL import ImageGrab

def detect_collision(data):
    for i in range(746, 820):
        for j in range(411, 611):
            if data[i, j] == (83, 83, 83):
                pyautogui.keyDown('down')
                return True 
    return False 
 
def jump():
    pyautogui.keyUp('down')
    pyautogui.keyDown('space')
    time.sleep(0.15)
    pyautogui.keyUp('space')
    pyautogui.keyDown('down')

if __name__ == "__main__":
    print("To stop move mouse to the corner of the screen or use Ctrl+C.")
    time.sleep(3) 
    pyautogui.keyDown('down')
    while True: 
        screenshot = ImageGrab.grab().convert('RGB')  
        data = screenshot.load()

        if detect_collision(data):
            jump()
