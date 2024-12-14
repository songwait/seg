import fld
import hough
import lsd


def main(fileNames):
    f = open(fileNames, encoding="utf-8")
    lines = f.readlines()
    for i in range(len(lines)):
        fileName = lines[i].strip("\n")
        print(fileName)
        fld.fld(fileName)
        # lsd.lsd(fileName)
        # hough.hough(fileName)
    f.close()    

if __name__ == "__main__":
    main("data/frame.txt")