import keyboard
import cv2
import pyautogui
import time

def play_video_in_obs(video_path):
    keyboard.add_hotkey('insert', lambda: play_video(video_path))

def play_video(video_path):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error opening video file!")
        return

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        cv2.imshow('Video', frame)
        cv2.waitKey(1)

    cap.release()
    cv2.destroyAllWindows()

video_path = "path/to/your/video.mp4"
play_video_in_obs(video_path)
