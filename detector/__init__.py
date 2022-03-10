from .YOLOv3 import YOLOv3
from .YOLOv3_pytorch import YOLO

__all__ = ['build_detector']


# return bbox.numpy(), cls_conf.numpy(), cls_ids.numpy()
# detector will return numpy format bbox(x,y,w,h), class confidence, and class id (after NMS)
def build_detector(cfg, use_cuda):
    # use the YOLOv3_pytorch model to detect trolly
    choice = 1
    if choice == 0:
        return YOLOv3(cfg.YOLOV3.CFG, cfg.YOLOV3.WEIGHT, cfg.YOLOV3.CLASS_NAMES,
                      score_thresh=cfg.YOLOV3.SCORE_THRESH, nms_thresh=cfg.YOLOV3.NMS_THRESH,
                      is_xywh=True, use_cuda=use_cuda)

    else:
        return YOLO()
