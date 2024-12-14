import cv2
def videoToFrame(filename,savePath):
    cap = cv2.VideoCapture(filename)
    i = 0
    if(cap.isOpened()):
        while True:
            ret,img = cap.read()
            if(i%(10*60) == 0):
                savePathAll = str(savePath+ str(int(i/(30*30))) +".png")
                cv2.imencode('.jpg', img)[1].tofile(savePathAll)
            i = i+1
            if not ret: break


def main(fileName):
    f = open(fileName, encoding="utf-8")
    lines = f.readlines()
    for i in range(len(lines)):
        print(lines[i].strip("\n"))
        videoToFrame(lines[i].strip("\n"),lines[i].replace("video","frame").strip("\n").strip(" ").strip("mp4"))
    f.close()    

if __name__ == "__main__":
    main("data/video.txt")