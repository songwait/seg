import copy
import cv2
import numpy as np
from ultralytics import YOLO
def loadModel(modelPath):
    model = YOLO(modelPath)
    return model
def drawLines(filePath):
    model = loadModel("runs/segment/train8/weights/best.pt")
    img0  = cv2.imdecode(np.fromfile(filePath, dtype=np.uint8), cv2.IMREAD_COLOR)
    results = model(filePath)
    for result in results:
        boxes = result.boxes  # Boxes object for bounding box outputs
        masks = result.masks  # Masks object for segmentation masks outputs
        edges = masks.xy[1:]
        # result=cv2.drawContours(img0, edges,-1, (0,255,0), 3)
        # cv2.imwrite("show/"+str(i)+"result.jpg", img0)
        i = 0
        for edge in edges:
            imgt = copy.copy(img0)
            a = []
            a.append(edge.astype(np.int64))
            cv2.drawContours(imgt, a, -1, (0,255,0),4)
            cv2.imwrite("show/"+str(i)+"result.jpg", imgt)
            i = i+1
        result.save(filename="result.jpg")  # save to disk
    

if __name__ == "__main__":
    drawLines("data/tennis/labeledFrame/frame/tennis_miss_24_1.png")