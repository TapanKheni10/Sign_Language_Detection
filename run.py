import os

os.system("python -m yolov5.detect --weights artifacts/best.pt --img 416 --conf 0.6 --source 0")