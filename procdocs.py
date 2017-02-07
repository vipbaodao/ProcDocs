#coding:utf-8

import numpy as np

import cv2
import time
import os

FILEPATH = "./files"             #文件图像存放路径
DATAPATH = "./data"              #数据文件存放路径
TEMPPATH = "./tmp"               #临时文件存放路径
TEMPLATEPATH = "./templates"     #模板文件存放路径

def getdate():                       #获取日期
    return time.strftime("%Y-%m-%d", time.localtime(time.time()))


def getFilefromCamera():            #从高拍仪获取文件图像
    pass

def getImagesfromPath():            #从指定位置获取文件图像
    pass

def analyseParams():                 #分析获得参数，日期、份数等
    pass

def splitImage(image):                     #分割版面
    cvimg = image
    cv2.imshow("splitimgs", cvimg)
    pass

def getItemfromOCR():                 #识别条目内容
    pass

def initDirectory(datestr):            #创建相应的工作目录
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
