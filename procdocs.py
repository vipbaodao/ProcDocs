# -*-coding:utf-8-*-

import numpy as np

import cv2
import time
import os
from matplotlib import pyplot as plt
# 引入文字识别OCR SDK
from aip import AipOcr

# 定义OCR常量
APP_ID = '9258746'
API_KEY = 'KFsoEDQgsnEqsO4lwNnWdLPG'
SECRET_KEY = 'Go3y4dqudxLbGaS2uYFzpFminMrLPwgy'

FILEPATH = "./files"             # 文件图像存放路径
DATAPATH = "./data"              # 数据文件存放路径
TEMPPATH = "./tmp"               # 临时文件存放路径
TEMPLATEPATH = "./templates"     # 模板文件存放路径

def getdate():                       # 获取日期
    return time.strftime("%Y-%m-%d", time.localtime(time.time()))


def getFilefromCamera():            # 从高拍仪获取文件图像

    pass

def getImagesfromPath():            # 从指定位置获取文件图像
    pass

def analyseParams():                 # 分析获得参数，日期、份数等
    pass

def splitImage(image):                     # 分割版面

    grayimg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(grayimg, 127, 255, cv2.THRESH_BINARY_INV)
    titles = ['Origin Image','Gray Image', 'BINARY',]
    images = [image[:, :, ::-1], grayimg, thresh]
    for i in range(3):
        plt.subplot(1, 3, i + 1), plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
    plt.show()
    edges = cv2.Canny(thresh, 5, 15)
    plt.imshow(edges, 'gray')
    plt.show()
    lines = cv2.HoughLinesP(thresh, 1, np.pi / 180, 20, minLineLength=5, maxLineGap=15)
    x, y, z = image.shape
    #mask = np.zeros((x, y), image.dtype)
    mask = image.copy()
    imagecopy = image.copy()
    for loop in range(lines.shape[0]):
        x1, y1, x2, y2 = lines[loop, 0]
        print("points coordinates:", x1, y1, x2, y2)
        if loop == 0:
            cv2.line(imagecopy, (x1, y1), (x2, y2), (0, 255, 0), 20)
        else:
            cv2.line(mask, (x1, y1), (x2, y2), (255, 0, 0), 20)
    invimg = imagecopy[:, :, ::-1]
    plt.imshow(invimg)
    plt.show()
    invimg = mask[:, :, ::-1]
    plt.imshow(invimg)
    plt.show()

# OCR读取图片
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def getItemfromOCR(image):                 # 识别条目内容
    # 初始化ApiOcr对象
    aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)

    # 调用通用文字识别接口
    result = aipOcr.general(get_file_content(image))
    return result




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
    im = cv2.imread("note.jpg", cv2.IMREAD_COLOR)
    # splitImage(im)
    ocroutput = getItemfromOCR("note.jpg")
    print(ocroutput)

