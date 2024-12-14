import copy
import math

import cv2
from matplotlib import pyplot as plt
import numpy as np

def mergeLines(lines,minTheta,minDistance,img,show):
    arr = []
    for i in range(len(lines)):
        x0 = int(round(lines[i][0][0]))
        y0 = int(round(lines[i][0][1]))
        x1 = int(round(lines[i][0][2]))
        y1 = int(round(lines[i][0][3]))
        d = math.dist((x0,y0),(x1,y1))
        theta = math.degrees(math.atan2(y1-y0,x1-x0))%180
        arr.append([theta,d,(x0,y0),(x1,y1),i])
    delete = []
    for i in range(len(arr)-1):
        j = 0
        while(j<=len(arr)-1 and i not in delete):    
            if(checkSameLine(arr[j ][2],arr[j][3],arr[i][2],arr[i][3])<minDistance and j!=i and abs((arr[j][0]-arr[i][0])%180)<minTheta ):
                before = []
                after = []
                before.append((arr[j ][2][0],arr[j][2][1],arr[j ][3][0],arr[j][3][1]))
                before.append((arr[i ][2][0],arr[i][2][1],arr[i ][3][0],arr[i][3][1]))
                newLine = mergeTwoLine(arr[j][2],arr[j][3],arr[i][2],arr[i][3])
                lines[i][0][0] = newLine[0][0]
                lines[i][0][1] = newLine[0][1]
                lines[i][0][2] = newLine[1][0]
                lines[i][0][3] = newLine[1][1]
                arr[i][2] = newLine[0]
                arr[i][3] = newLine[1]
                after.append((arr[i ][2][0],arr[i][2][1],arr[i ][3][0],arr[i][3][1]))
                cal = tupleCal(newLine[1],newLine[0])
                arr[i][1]  = math.dist(newLine[0],newLine[1])
                arr[i][0]  = math.degrees(math.atan2(cal[1],cal[0]))%180
                delete.append(j)
                if show:
                    drawLinesForTest(img,before,True,i,j)
                    drawLinesForTest(img,after,True,j,j)                
            j = j + 1
    return deleteArr(delete,lines)



def mergeLines(lines,minTheta,minDistance,img,show):
    arr = []
    for i in range(len(lines)):
        x0 = int(round(lines[i][0][0]))
        y0 = int(round(lines[i][0][1]))
        x1 = int(round(lines[i][0][2]))
        y1 = int(round(lines[i][0][3]))
        d = math.dist((x0,y0),(x1,y1))
        theta = math.degrees(math.atan2(y1-y0,x1-x0))%180
        arr.append([theta,d,(x0,y0),(x1,y1),i])
    delete = []
    for i in range(len(arr)-1):
        j = 0
        while(j<=len(arr)-1 and i not in delete):    
            if(lineToLineDist(arr[j ][2],arr[j][3],arr[i][2],arr[i][3])<minDistance and j!=i and abs((arr[j][0]-arr[i][0])%180)<minTheta ):
                before = []
                after = []
                before.append((arr[j ][2][0],arr[j][2][1],arr[j ][3][0],arr[j][3][1]))
                before.append((arr[i ][2][0],arr[i][2][1],arr[i ][3][0],arr[i][3][1]))
                newLine = mergeTwoLine(arr[j][2],arr[j][3],arr[i][2],arr[i][3])
                lines[i][0][0] = newLine[0][0]
                lines[i][0][1] = newLine[0][1]
                lines[i][0][2] = newLine[1][0]
                lines[i][0][3] = newLine[1][1]
                arr[i][2] = newLine[0]
                arr[i][3] = newLine[1]
                after.append((arr[i ][2][0],arr[i][2][1],arr[i ][3][0],arr[i][3][1]))
                cal = tupleCal(newLine[1],newLine[0])
                arr[i][1]  = math.dist(newLine[0],newLine[1])
                arr[i][0]  = math.degrees(math.atan2(cal[1],cal[0]))%180
                delete.append(j)
                if show:
                    drawLinesForTest(img,before,True,i,j)
                    drawLinesForTest(img,after,True,j,j)                
            j = j + 1
    return deleteArr(delete,lines)

def markEdges(lines,img):
    for i in range(len(lines)):
        x0 = int(round(lines[i][0][0]))
        y0 = int(round(lines[i][0][1]))
        x1 = int(round(lines[i][0][2]))
        y1 = int(round(lines[i][0][3]))
        d = math.dist((x0,y0),(x1,y1))
        
#定义形状检测函数
def ShapeDetection(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)  #寻找轮廓点
    for obj in contours:
        area = cv2.contourArea(obj)  #计算轮廓内区域的面积
        cv2.drawContours(img, obj, -1, (255, 0, 0), 4)  #绘制轮廓线
        perimeter = cv2.arcLength(obj,True)  #计算轮廓周长
        approx = cv2.approxPolyDP(obj,0.02*perimeter,True)  #获取轮廓角点坐标
        CornerNum = len(approx)   #轮廓角点的数量
        x, y, w, h = cv2.boundingRect(approx)  #获取坐标值和宽度、高度

        #轮廓对象分类
        if CornerNum ==3: objType ="triangle"
        elif CornerNum == 4:
            if w==h: objType= "Square"
            else:objType="Rectangle"
        elif CornerNum>4: objType= "Circle"
        else:objType="N"

        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)  #绘制边界框
        cv2.putText(img,objType,(x+(w//2),y+(h//2)),cv2.FONT_HERSHEY_COMPLEX,0.6,(0,0,0),1)  #绘制文字
        
def filterDistance(lines,min,max):
    delete = []
    for i in range(len(lines)):
        x0 = int(round(lines[i][0][0]))
        y0 = int(round(lines[i][0][1]))
        x1 = int(round(lines[i][0][2]))
        y1 = int(round(lines[i][0][3]))
        d = math.dist((x0,y0),(x1,y1))
        if d > max or d < min:
            delete.append(i)
    return deleteArr(delete,lines)
        
def calDistance(x0,y0,x1,y1,max,min):
    d = math.dist((x0,y0),(x1,y1))
    if d > max or d <min:
        return False
    return True
import numpy as np

# def pointTolinedist(point, line_start, line_end):
#     """计算点到线段的最短距离"""
#     lineVecX = line_end[0] - line_start[0]
#     lineVecY = line_end[1] - line_start[1]
#     pointVecX = point[0] - line_start[0]
#     pointVecY = point[1] - line_start[1]
#     lineLen = np.linalg.norm((lineVecX,lineVecY))
#     lineUnitVecX = lineVecX / lineLen
#     lineUnitVecY = lineVecY / lineLen
#     pointVecScaledX = pointVecX / lineLen
#     pointVecScaledY = pointVecY / lineLen
#     t = np.dot((lineUnitVecX,lineUnitVecY), (pointVecScaledX,pointVecScaledY))    
#     if t < 0.0:
#         t = 0.0
#     elif t > 1.0:
#         t = 1.0
#     nearestX = lineVecX * t
#     nearestY = lineVecY * t
#     dist = np.linalg.norm((pointVecX-nearestX,pointVecY-nearestY) )
#     return dist

def checkSameLine(start1, end1, start2, end2):
    return
def pointToLineDist(point, start, end):
    cross = (end[0]-start[0])*(point[0]-start[0])+(end[1]-start[1])*(point[1]-start[1])
    if cross <= 0:
        return math.dist(point,start)
    d2 = (end[0]-start[0])*(end[0]-start[0])+(end[1]-start[1])*(end[1]-start[1])
    if cross >= d2:
        return math.dist(point,end)
    r = cross / d2
    px = start[0] + (end[0]-start[0])*r
    py = start[1] + (end[1]-start[1])*r
    return math.dist(point,(px,py))

def lineToLineDist(start1, end1, start2, end2):
    dist1 = pointToLineDist(start1, start2, end2)
    dist2 = pointToLineDist(end1, start2, end2)
    dist3 = pointToLineDist(start2, start1, end1)
    dist4 = pointToLineDist(end2, start1, end1)
    return min(dist1, dist2, dist3, dist4)

def mergeTwoLine(start1, end1, start2, end2):
    distances = []
    distances.append((math.dist(start1,end1),(start1,end1)))
    distances.append((math.dist(start1,start2),(start1,start2)))
    distances.append((math.dist(start1,end2),(start1,end2)))
    distances.append((math.dist(end1,start2),(end1,start2)))
    distances.append((math.dist(end1,end2),(end1,end2)))
    distances.append((math.dist(start2,end2),(start2,end2)))
    maxValue = max(distances,key = takeFirst)
    return maxValue[1]
    
def deleteArr(delete,arr):
    return np.delete(arr,delete,0)

def tupleCal(a,b):
    return b[0]-a[0],b[1]-a[1]

def show(img,img0):
    plt.figure(figsize=(20,10))
    plt.subplot(1,2,1)
    plt.imshow(img,cmap="gray")
    plt.title("source",fontsize=12)
    plt.axis("off")
    plt.subplot(1,2,2)
    plt.imshow(img0,cmap="gray")
    plt.title("result",fontsize=12)
    plt.axis("off")
    plt.show()

def drawLines(img0,lines,show):
    for dline in lines:
        x0 = int(round(dline[0][0]))
        y0 = int(round(dline[0][1]))
        x1 = int(round(dline[0][2]))
        y1 = int(round(dline[0][3]))
        cv2.line(img0, (x0, y0), (x1,y1), (0,255,0), 2, cv2.LINE_AA)
        if show:
            plt.figure(figsize=(20,10))
            plt.subplot(1,1,1)
            plt.imshow(img0,cmap="gray")
            plt.title("source",fontsize=12)
            plt.axis("off")
            plt.show()
            
def showLines(img_tmp,lines):
    for i in range(len(lines)):
        img0 = copy.copy(img_tmp)    
        x0 = int(round(lines[i][0][0]))
        y0 = int(round(lines[i][0][1]))
        x1 = int(round(lines[i][0][2]))
        y1 = int(round(lines[i][0][3]))
        cv2.line(img0, (x0, y0), (x1,y1), (0,255,0), 2, cv2.LINE_AA)
        plt.figure(figsize=(20,10))
        plt.subplot(1,1,1)
        plt.imshow(img0,cmap="gray")
        plt.title(str(i),fontsize=12)
        plt.axis("off")
        plt.show()
        
def drawLinesForTest(img_tmp,lines,show,i,j):
    img0 = copy.copy(img_tmp)
    for dline in lines:
        x0 = int(round(dline[0]))
        y0 = int(round(dline[1]))
        x1 = int(round(dline[2]))
        y1 = int(round(dline[3]))
        cv2.line(img0, (x0, y0), (x1,y1), (0,255,0), 10, cv2.LINE_AA)
    if show:
        plt.figure(figsize=(20,10))
        plt.subplot(1,1,1)
        plt.imshow(img0,cmap="gray")
        plt.title(str(i)+'__'+str(j),fontsize=12)
        plt.axis("off")
        plt.show()    

def takeFirst(elem):
    return elem[0]

if __name__ == "__main__":
    print('hello')