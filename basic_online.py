from pynput.keyboard import Key, Listener

def on_press(key):
    print(f'{key} فشرده شد')

def on_release(key):
    print(f'{key} رها شد')
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()