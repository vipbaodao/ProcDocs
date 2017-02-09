# -*-coding:utf-8-*-

import numpy as np

import cv2
import time
import os
from matplotlib import pyplot as plt

FILEPATH = "./files"             # 文件图像存放路径
DATAPATH = "./data"              # 数据文件存放路径
TEMPPATH = "./tmp"               # 临时文件存放路径
TEMPLATEPATH = "./templates"     # 模板文件存放路径


LINESPACE = 5                    # 行距
REGIONHEIGHT = 50                # 区块高度
REGIONWIDTH = 50                 # 区块宽度

def getdate():                       # 获取日期
    return time.strftime("%Y-%m-%d", time.localtime(time.time()))


def getFilefromCamera():            # 从高拍仪获取文件图像
    pass

def getImagesfromPath():            # 从指定位置获取文件图像
    pass

def analyseParams():                 # 分析获得参数，日期、份数等
    pass

def splitImage(image):                     # 分割版面
    grayimage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, bwimg = cv2.threshold(grayimage, 127, 255, cv2.THRESH_BINARY_INV)
    # ret, thresh = cv2.threshold(grayimage, 127, 255, cv2.THRESH_TOZERO_INV)
    edges = cv2.Canny(bwimg, 5, 15)
    titles = ['ORIGINAL IMAGE', 'BINARY', 'EDGES']
    curimages = [grayimage, bwimg, edges]
    for i in range(3):
        plt.subplot(1, 3, i + 1), plt.imshow(curimages[i], 'gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
    # plt.show()
    # lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 20, minLineLength=5, maxLineGap=15)
    lines = cv2.HoughLinesP(bwimg, 1, np.pi / 180, 20, minLineLength=5, maxLineGap=15)
    for loop in range(lines.shape[0]):
        x1, y1, x2, y2 = lines[loop, 0]
        print("points coordinates:", x1, y1, x2, y2)
        cv2.line(image, (x1, y1), (x2, y2), (255, 0, 0), 2)        # 蓝色
    invimg = image[:, :, ::-1]
    # plt.figure(1)
    # plt.imshow(invimg)
    # plt.show()
    contentlines = confirmContentLines(bwimg)
    print(contentlines)
    print(len(contentlines))
    rects = confirmContentRegion(bwimg, contentlines)

    # return rects

def confirmContentRegion(image, contentlines):
    for x in contentlines:
        line = image[x, :]
        startindex, endindex = findEndsofNonzerovalue(line)
        # findEndsofNonzerovalue(line)
        print(x, startindex, endindex)
    pass

def findEndsofNonzerovalue(line):      # 确定内容所在行中，内容的起止位置
    index = range(line.shape[0])

    for x in index:
        if line[x] != 0:
            startindex = x
            break
    for x in index[::-1]:
        if line[x] != 0:
            endindex = x
            break
    return (startindex, endindex)



def confirmContentLines(image):        # 确定有内容的行，返回内容所在行的坐标
    hhist = image.sum(axis = 1)
    coords = list()
    for i in range(hhist.shape[0]):
        if hhist[i] > 0:
            coords.append(i)
    return coords



def projectionAnalysis(image):

    pass

def getItemfromOCR():                 # 识别条目内容
    pass

def initDirectory(datestr):            # 创建相应的工作目录
    if not os.path.isdir(DATAPATH):
        os.mkdir(DATAPATH)
    if not os.path.isdir(TEMPLATEPATH):
        os.mkdir(TEMPLATEPATH)
    if not os.path.isdir(TEMPPATH):
        os.mkdir(TEMPPATH)
    if not os.path.isdir(FILEPATH):
        os.mkdir(FILEPATH)
    ten_path = "/10"
    one_path = "/1"
    dirname = FILEPATH + '/' + datestr
    if not os.path.isdir(dirname):
        os.makedirs(dirname + ten_path)
        os.makedirs(dirname + one_path)






if __name__ == '__main__':
    date = getdate()
    initDirectory(date)
    im = cv2.imread("test.jpg")
    splitImage(im)

