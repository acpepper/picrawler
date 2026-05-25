#!/usr/bin/env python3
from vilib import Vilib
from time import sleep, time, strftime, localtime
import threading
from os import getlogin
import readchar
import cv2

USERNAME = getlogin()
PICTURE_PATH = f"/home/{USERNAME}/Pictures/"

flag_face = False
flag_color = False
qr_code_flag = False

MANUAL = '''
Press a key to call the function:
    q: Take photo
    1: Color detect : red
    2: Color detect : orange
    3: Color detect : yellow
    4: Color detect : green
    5: Color detect : blue
    6: Color detect : purple
    0: Switch off Color detect
    r: Scan the QR code (toggle)
    f: Switch ON/OFF face detect
    s: Display detected object information
    ESC: Quit
'''

color_list = ['close', 'red', 'orange', 'yellow', 'green', 'blue', 'purple']

def face_detect(flag):
    print("Face Detect:", flag)
    Vilib.face_detect_switch(flag)

def qrcode_detect():
    global qr_code_flag
    Vilib.qrcode_detect_switch(True)
    print("Waiting for QR code...")

    text = None
    while qr_code_flag:
        temp = Vilib.detect_obj_parameter.get('qr_data', "None")
        if temp != "None" and temp != text:
            text = temp
            print("QR code:", text)
        sleep(0.2)

    Vilib.qrcode_detect_switch(False)

def take_photo():
    _time = strftime('%Y-%m-%d-%H-%M-%S', localtime(time()))
    name = f'photo_{_time}'
    Vilib.take_photo(name, PICTURE_PATH)
    print(f'Photo saved as {PICTURE_PATH}{name}.jpg')

def object_show():
    global flag_color, flag_face

    if flag_color:
        if Vilib.detect_obj_parameter.get('color_n', 0) == 0:
            print('Color Detect: None')
        else:
            x = Vilib.detect_obj_parameter.get('color_x')
            y = Vilib.detect_obj_parameter.get('color_y')
            w = Vilib.detect_obj_parameter.get('color_w')
            h = Vilib.detect_obj_parameter.get('color_h')
            print("[Color Detect] Coordinate:", (x, y), "Size:", (w, h))

    if flag_face:
        if Vilib.detect_obj_parameter.get('human_n', 0) == 0:
            print('Face Detect: None')
        else:
            x = Vilib.detect_obj_parameter.get('human_x')
            y = Vilib.detect_obj_parameter.get('human_y')
            w = Vilib.detect_obj_parameter.get('human_w')
            h = Vilib.detect_obj_parameter.get('human_h')
            print("[Face Detect] Coordinate:", (x, y), "Size:", (w, h))

def has_display():
    """Check if an X11/Wayland display is available."""
    import os
    return bool(os.environ.get('DISPLAY') or os.environ.get('WAYLAND_DISPLAY'))


def open_local_preview():
    """
    OpenCV local preview via Vilib MJPG web stream.
    Returns None when running headless (no display).
    """
    if not has_display():
        print("[INFO] No display detected — headless mode. Web preview only.")
        return None

    url = "http://127.0.0.1:9000/mjpg"
    cap = cv2.VideoCapture(url)
    for _ in range(30):
        if cap.isOpened():
            break
        sleep(0.1)
        cap.release()
        cap = cv2.VideoCapture(url)

    if not cap.isOpened():
        print("[WARN] Cannot open MJPG stream for local preview:", url)
        print("       Web preview should still work.")
        return None

    cv2.namedWindow("Vilib Preview (MJPG)", cv2.WINDOW_NORMAL)
    return cap

def _display_refresh(cap, running):
    """Refresh OpenCV preview window (only when display is available)."""
    while running[0]:
        if cap is not None:
            ret, frame = cap.read()
            if ret and frame is not None:
                cv2.imshow("Vilib Preview (MJPG)", frame)
                cv2.waitKey(1)
        sleep(0.03)


def main():
    global flag_face, flag_color, qr_code_flag
    qrcode_thread = None

    Vilib.camera_start(vflip=False, hflip=False)
    Vilib.display(local=False, web=True)
    print(MANUAL)

    use_display = has_display()
    cap = open_local_preview()

    running = [True]
    if use_display and cap is not None:
        display_thread = threading.Thread(target=_display_refresh, args=(cap, running), daemon=True)
        display_thread.start()

    try:
        while True:
            if use_display and cap is not None:
                k = cv2.waitKey(1) & 0xFF
                if k == 27:  # ESC
                    break
                key = chr(k).lower() if k not in (255, 0) else None
            else:
                try:
                    key = readchar.readkey().lower()
                except Exception:
                    continue

            if key is None:
                continue

            if key == 'q':
                take_photo()

            elif key == '\x1b':  # ESC
                break

            elif key in ['0','1','2','3','4','5','6']:
                index = int(key)
                if index == 0:
                    flag_color = False
                    Vilib.color_detect('close')
                else:
                    flag_color = True
                    Vilib.color_detect(color_list[index])
                print('Color detect:', color_list[index])

            elif key == 'f':
                flag_face = not flag_face
                face_detect(flag_face)

            elif key == 'r':
                qr_code_flag = not qr_code_flag
                if qr_code_flag:
                    if qrcode_thread is None or not qrcode_thread.is_alive():
                        qrcode_thread = threading.Thread(target=qrcode_detect, daemon=True)
                        qrcode_thread.start()
                else:
                    print('QRcode Detect: close')

            elif key == 's':
                object_show()

    except KeyboardInterrupt:
        print("\nQuit.")

    finally:
        running[0] = False
        qr_code_flag = False

        try:
            Vilib.qrcode_detect_switch(False)
        except Exception:
            pass
        try:
            Vilib.color_detect('close')
        except Exception:
            pass
        try:
            Vilib.face_detect_switch(False)
        except Exception:
            pass
        try:
            Vilib.camera_close()
        except Exception:
            pass

        if cap is not None:
            try:
                cap.release()
            except Exception:
                pass
        try:
            cv2.destroyAllWindows()
        except Exception:
            pass

if __name__ == "__main__":
    main()