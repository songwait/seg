# coding=utf-8
import math
import re
import cv2
from matplotlib import pyplot as plt
import numpy as np

from utils import drawLines, show, showLines
import utils
def fld(filePath):
    # 读取输入图片
    img0  = cv2.imdecode(np.fromfile(filePath, dtype=np.uint8), cv2.IMREAD_COLOR)
    # 将彩色图片转换为灰度图片
    img = cv2.cvtColor(img0,cv2.COLOR_BGR2GRAY)

    # 创建一个LSD对象
    fld = cv2.ximgproc.createFastLineDetector()
    # 执行检测结果
    lines = fld.detect(img)
    lines = utils.filterDistance(lines,10,9999)
    # drawLines(img0,lines,False)
    # showLines(img0,lines)
    lines = utils.mergeLines(lines,1,5,img0,False)
    # drawLines(img0,lines,False)
    print(len(lines))
    # showLines(img0,lines)
    lines = utils.filterDistance(lines,30,9999)
    # drawLines(img0,lines,False)

    lines = utils.mergeLines(lines,1,10,img0,False)
    # showLines(img0,lines)
    lines = utils.filterDistance(lines,50,9999)

    print(len(lines))
    drawLines(img0,lines,False)
    show(img,img0)
    
    
    
        
if __name__ == "__main__":
    fld("./data/tennis/frame/【网球黄金视角】观看比赛最佳视角，感受世界顶尖球员的技巧！.15.png")
    
