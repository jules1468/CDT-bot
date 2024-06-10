import pyautogui
import os
import keyboard
import time
import threading
import random
from image_detector.detector import check_image_in_image

race = False
running = False
race_stopped = False

def press_z():
    while running:
        if not race:
            pyautogui.keyDown('w')
        else:
            pyautogui.keyUp('w')
            time.sleep(0.1)

def press_d():
    while running:
        if not race:
            time.sleep(random.randint(1, 3))
            pyautogui.keyDown('d')
            time.sleep(random.uniform(0.5, 1.5))
            pyautogui.keyUp('d')
        else:
            pyautogui.keyUp('d')
            time.sleep(0.1)

def perform_click_sequence():
    x1, y1 = 25, 417
    x2, y2 = 833, 590

    pyautogui.moveTo(x1, y1)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.moveTo(x2, y2)
    pyautogui.click()

def inracefunc():
    global race, race_stopped

    reference = r'D:\tkt\bot cdt\referance.png'
    screen = pyautogui.screenshot()
    screen_path = r'D:\tkt\bot cdt\screen.png'
    screen.save(screen_path)

    new_race = check_image_in_image(screen_path, reference)

    if not new_race and race and not race_stopped:
        perform_click_sequence()
        race_stopped = True

    if new_race:
        race_stopped = False

    race = new_race

    if not race:
        pyautogui.keyUp('w')
        pyautogui.keyUp('d')

    print(race)
    os.remove(screen_path)

def check_race_status():
    while running:
        inracefunc()
        time.sleep(1)

def start_program():
    global running
    if not running:
        running = True
        thread_z = threading.Thread(target=press_z)
        thread_d = threading.Thread(target=press_d)
        thread_race = threading.Thread(target=check_race_status)
        thread_z.start()
        thread_d.start()
        thread_race.start()
        print("Programme démarré")

def stop_program():
    global running
    if running:
        running = False
        pyautogui.keyUp('w')
        pyautogui.keyUp('d')
        print("Programme arrêté")

def toggle_program():
    if running:
        stop_program()
    else:
        start_program()

keyboard.add_hotkey('f5', toggle_program)

print("Appuyez sur F5 pour démarrer/arrêter le programme.")
keyboard.wait('esc')