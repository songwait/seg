from io import TextIOWrapper


def pointToShape(fileName,points):
    with open("data/tennis/labeledFrame/label/"+fileName,"w") as f:
        writeFile(f,"0",[1,4,5,8],points)
        writeFile(f,"1",[1,2,7,8],points)
        writeFile(f,"1",[2,3,11,9],points)
        writeFile(f,"1",[9,10,13,14],points)
        writeFile(f,"1",[10,11,12,13],points)
        writeFile(f,"1",[14,12,6,7],points)
        writeFile(f,"1",[3,4,5,6],points)
    f.close()
def writeFile(f:TextIOWrapper, clay,index, points):
    f.write(clay)
    f.write(" "+points[index[0]*2-2]+" "+points[index[0]*2-1])
    f.write(" "+points[index[1]*2-2]+" "+points[index[1]*2-1])
    f.write(" "+points[index[2]*2-2]+" "+points[index[2]*2-1])
    f.write(" "+points[index[3]*2-2]+" "+points[index[3]*2-1])
    f.write("\n")
def readLabels(fileName):
    with open(fileName,"r") as f:
        labels = f.readlines()
        for i in range(0,len(labels)):
            label = labels[i].removesuffix("\n").split(" ")
            xl,yl=label[1],label[2]
            points = label[3:]
            for i in range(0,len(points)-1):
                if(i%2):
                    points[i] = str(float(points[i])/float(yl))
                else:
                    points[i] = str(float(points[i])/float(xl))
            pointToShape(label[0].replace("png","txt"),points)
if __name__ == "__main__":
    readLabels("data/label.txt")            