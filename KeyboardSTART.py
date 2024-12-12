from pynput.keyboard import Key, Controller, Listener
import time
import random

keyboard = Controller()
stop = False

def press_key():
    global stop
    save_time = time.time()

    while not stop:
        number = random.randint(0, 16)
        if number in [0, 7, 13]:
            key = 'w'
        elif number in [1, 8, 14]:
            key = 'a'
        elif number in [2, 9, 15]:
            key = 's'
        elif number in [3, 10, 16]:
            key = 'd'
        elif number in [4, 11]:
            key = 'z'
        elif number in [5, 12]:
            key = 'x'
        elif number in [6]:
            key = 'e'
        print(f'Generated number: {key}={number}')
        keyboard.press(key)
        time.sleep(0.25)
        keyboard.release(key)
        time.sleep(1)

        if time.time() - save_time >= 3600:
            keyboard.press('c')
            keyboard.release('c')
            save_time = time.time()

def on_press(key):
    global stop
    if key == Key.esc:
        stop = True
        return False

from threading import Thread
thread = Thread(target=press_key)
thread.start()

with Listener(on_press=on_press) as listener:
    listener.join()
