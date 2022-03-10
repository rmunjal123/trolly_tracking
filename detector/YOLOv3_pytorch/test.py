from yolo import YOLO
from PIL import Image
import os


yolo = YOLO()

dir_origin_path = "img/"

img = "001833.jpg"

image = Image.open(os.path.join(dir_origin_path, img))

label, conf, bboxes = yolo(image)

print(label, conf, bboxes)
