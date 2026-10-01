import cv2
import mediapipe as mp
import subprocess
import os 
import pyautogui

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands()

camera = cv2.VideoCapture(0)

resolution_x = 720
resolution_y = 460

camera.set(cv2.CAP_PROP_FRAME_WIDTH, resolution_x)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, resolution_y)

notepad_process = None
mspaint_process = None
calc_process = None
vlc_process = None
vlc_path = r'C:\Program Files (x86)\VideoLAN\VLC\vlc.exe'
music_file_path = "music/m1.mp3"

def find_coord_hand(img, side_inverted = False):
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(img_rgb)
    all_hands = []

    if result.multi_hand_landmarks:
        for hand_side, hand_landmarks in zip(result.multi_handedness , result.multi_hand_landmarks):
            hand_info = {}
            coords = []
            for mark in hand_landmarks.landmark:
                coord_x = int(mark.x * resolution_x)
                coord_y = int(mark.y * resolution_y)
                coord_z = int(mark.z * resolution_x)
                coords.append((coord_x, coord_y, coord_z))
                hand_info['coordenadas'] = coords
            if side_inverted:
                if hand_side.classification[0].label == "Left":
                    hand_info["side"] = "Right"
                else:
                    hand_info["side"] = "Left"
            else:
                hand_info["side"] = hand_side.classification[0].label        

            all_hands.append(hand_info)

            print(coord_x, coord_y, coord_z)

            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    return img, all_hands

def fingers_raised(hand):
    fingers = []
    for fingertip in [8, 12, 16, 20]:
        if hand['coordenadas'][fingertip][1] < hand['coordenadas'][fingertip-2][1]:
            fingers.append(True)
        else:
            fingers.append(False)
    return fingers

def start_program(program):
    return subprocess.Popen(program, shell=True)

def close_program(process_name):
    os.system(f"TASKKILL /IM {process_name} /F")

def send_keypress(key):
    pyautogui.press(key)


while camera.isOpened():
    ret, frame = camera.read()
    frame = cv2.flip(frame, 1)
    if not ret:
        print("Frame vazio")
        continue
    img, all_hands = find_coord_hand(frame, False)
    if len(all_hands) == 1:
        info_finger_hand = fingers_raised(all_hands[0])
        
        if info_finger_hand == [True, False, False, True]:
            break
        elif info_finger_hand == [True, False, True, True] and vlc_process is None:
            vlc_process = start_program(f'"{vlc_path}" "{music_file_path}"')
            vlc_process = 2
    
        elif info_finger_hand == [True, False, False, False] and notepad_process is None:
            notepad_process = start_program("notepad")

        elif info_finger_hand == [True, True, False, False] and calc_process is None:
            calc_process = start_program("calc")
            
        elif info_finger_hand == [True, True, True, False] and mspaint_process is None:
            mspaint_process = start_program("mspaint")

        elif info_finger_hand == [False, True, True, True] and vlc_process is not None:
            send_keypress('space')

        elif info_finger_hand == [False, False, False, False]:
            if notepad_process is not None:
                close_program("notepad.exe")
                notepad_process = None

            if calc_process is not None:
                close_program("CalculatorApp.exe")
                calc_process = None

            if mspaint_process is not None:
                close_program("mspaint.exe")
                mspaint_process = None     

            if vlc_process is not None:
                close_program("vlc.exe")
                vlc_process = None  
                                                                                    
    cv2.imshow("camera", frame)
    key = cv2.waitKey(1)

    if key == 27:
        break