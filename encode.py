
import cv2
import numpy as np
import random
import matplotlib.pyplot as plt
from numpy._distributor_init import NUMPY_MKL
import scipy.fftpack as fftpack
import pylab as py


img_path='d.png'
wm_path='watermark.png'
res_path='res1.png'
alpha=5
img = cv2.imread(img_path)
img_f = np.fft.fft2(img)
height, width, channel = np.shape(img)
watermark = cv2.imread(wm_path)
wm_height, wm_width = watermark.shape[0], watermark.shape[1]
x, y = range(height / 2), range(width)
random.seed(height + width)
random.shuffle(x)
random.shuffle(y)
tmp = np.zeros(img.shape)
for i in range(height / 2):
	for j in range(width):
		if x[i] < wm_height and y[j] < wm_width:
			tmp[i][j] = watermark[x[i]][y[j]]
			tmp[height - 1 - i][width - 1 - j] = tmp[i][j]
res_f = img_f + alpha * tmp
res = np.fft.ifft2(res_f)
res = np.real(res)
cv2.imwrite(res_path, res, [int(cv2.IMWRITE_JPEG_QUALITY), 100])

