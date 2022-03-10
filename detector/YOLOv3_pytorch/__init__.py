import sys

sys.path.append("detector/YOLOv3_pytorch")

from .yolo import YOLO

__all__ = ['YOLO']
