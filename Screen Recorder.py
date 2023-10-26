import cv2
import numpy as np
import pyautogui

screen_width, screen_height = pyautogui.size()
resolution = (screen_width, screen_height)


output_filename = "test.mp4"

fps = 30.0

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(output_filename, fourcc, fps, resolution)

recording_duration = 60

for _ in range(int(fps * recording_duration)):
    screen = pyautogui.screenshot()

    frame = np.array(screen)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    out.write(frame)

out.release()