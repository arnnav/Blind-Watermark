
import cv2
import numpy as np
import random


ori_path='d.png'
img_path='res1.png'
res_path='ex1.png'
alpha=5
ori = cv2.imread(ori_path)
img = cv2.imread(img_path)
ori_f = np.fft.fft2(ori)
img_f = np.fft.fft2(img)
height, width = ori.shape[0], ori.shape[1]
watermark = (ori_f - img_f) / alpha
watermark = np.real(watermark)
res = np.zeros(watermark.shape)
random.seed(height + width)
x = range(height / 2)
y = range(width)
random.shuffle(x)
random.shuffle(y)
for i in range(height / 2):
	for j in range(width):
		res[x[i]][y[j]] = watermark[i][j]
cv2.imwrite(res_path, res, [int(cv2.IMWRITE_JPEG_QUALITY), 100])

