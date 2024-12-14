# coding=utf-8
import math
import re
import cv2
from matplotlib import pyplot as plt
import numpy as np

from utils import drawLines, show, showLines
import utils
def lsd(filePath):
    # 读取输入图片
    img0  = cv2.imdecode(np.fromfile(filePath, dtype=np.uint8), cv2.IMREAD_COLOR)
    # 将彩色图片转换为灰度图片
    img = cv2.cvtColor(img0,cv2.COLOR_BGR2GRAY)

    # 创建一个LSD对象
    lsd = cv2.createLineSegmentDetector(0)
    # 执行检测结果
    dlines = lsd.detect(img)
    lines = dlines[0]
    lines = utils.filterDistance(lines,0,9999)
    drawLines(img0,lines,False)
    # showLines(img0,lines)
    lines = utils.mergeLines(lines,2,0,img0,False)
    # drawLines(img0,lines,False)

    # showLines(img0,lines)
    lines = utils.filterDistance(lines,100,9999)
    # drawLines(img0,lines,False)

    lines = utils.mergeLines(lines,5,10,img0,False)
    # showLines(img0,lines)
    
    print(len(lines))
    # drawLines(img0,lines,False)
    show(img,img0)
    
    
    
        
if __name__ == "__main__":
    lsd("./data/tennis/frame/【网球黄金视角】观看比赛最佳视角，感受世界顶尖球员的技巧！.15.png")