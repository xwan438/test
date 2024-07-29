import cv2
import numpy as np
from pyaudio import PyAudio, paInt16
import time


# 模拟摄像头
def simulate_camera(window_name, resolution=(640, 480), fps=30):
    cap = cv2.VideoCapture(0)  # 0 表示第一个摄像头
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, resolution[0])
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, resolution[1])
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow(window_name, frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


# 模拟麦克风
def simulate_microphone(rate=44100, chunk_size=1024):
    p = PyAudio()
    stream = p.open(format=paInt16, channels=1, rate=rate, input=True, frames_per_buffer=chunk_size)
    stream.start_stream()
    while True:
        data = stream.read(chunk_size)
        # 处理麦克风数据，例如可以打印最大值来模拟有声音输入
        print(np.max(np.frombuffer(data, dtype=np.int16)))
        if np.max(np.frombuffer(data, dtype=np.int16)) > 5000:
            print("声音检测到！")
            break
    stream.stop_stream()
    stream.close()
    p.terminate()


# 调用模拟摄像头和麦克风的函数
simulate_camera("Simulated Camera", (640, 480))
simulate_microphone()
