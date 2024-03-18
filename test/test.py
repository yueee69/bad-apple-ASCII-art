import cv2
import pygame
import time
import os

video_path = r"C:\Users\monke\OneDrive\桌面\bad apple\【東方】Bad Apple!! ＰＶ.mp4"
cap = cv2.VideoCapture(video_path)

music_file = r"C:\Users\monke\OneDrive\桌面\bad apple\【東方】Bad Apple!! ＰＶ【影絵】.mp3"
pygame.mixer.init()
pygame.mixer.music.load(music_file)

ascii_chars = " .:-=+*#%@"
che = False

while True:
    ret, frame = cap.read()

    if che == False:
        pygame.mixer.music.play()
        che = True

    if not ret:
        break

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    resized_frame = cv2.resize(gray_frame, (80, 40))

    text_frame = ""
    for row in resized_frame:
        for pixel in row:
            char_index = int(pixel / 255 * (len(ascii_chars) - 1))
            text_frame += ascii_chars[char_index]
        text_frame += "\n"

    print(text_frame)
    time.sleep(0.024)

cap.release()
pygame.mixer.music.stop()
cv2.destroyAllWindows()
