import time
import numpy
import cv2
from PIL import Image


def calculate(image1, image2):
    hist1 = cv2.calcHist([image1], [0], None, [256], [0, 256])
    hist2 = cv2.calcHist([image2], [0], None, [256], [0, 256])
    degree = 0
    for i in range(len(hist1)):
        if hist1[i] != hist2[i]:
            degree = degree + (1 - abs(hist1[i] - hist2[i]) / max(hist1[i], hist2[i]))
        else:
            degree = degree + 1
    degree = degree / len(hist1)
    return degree


def picture_similarity(image1, image2, size=(256, 256)):
    image1 = Image.open(image1)
    image2 = Image.open(image2)
    image1 = cv2.cvtColor(numpy.asarray(image1), cv2.COLOR_RGB2BGR)
    image2 = cv2.cvtColor(numpy.asarray(image2), cv2.COLOR_RGB2BGR)
    image1 = cv2.resize(image1, size)
    image2 = cv2.resize(image2, size)
    sub_image1 = cv2.split(image1)
    sub_image2 = cv2.split(image2)
    sub_data = 0
    for im1, im2 in zip(sub_image1, sub_image2):
        sub_data += calculate(im1, im2)
    sub_data = sub_data / len(sub_image1)
    return int(sub_data*100)

if __name__ == '__main__':
#设置图片路径
    img1_path = "1.png"
    img2_path = "2.png"
    result1 = picture_similarity(img1_path, img2_path)
    print(f"相似度为：{result1}%")

