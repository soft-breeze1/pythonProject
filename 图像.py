import cv2
import matplotlib.pyplot as plt
import numpy as np

# 读取图像
img = cv2.imread("D:/1.jpg")

# 显示图像
# cv2.imshow('dongman',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# matplotlib
# plt.imshow(img[:,:,::-1], cmap='gray')
# plt.show()

# 灰度图演示
# plt.imshow(img, cmap=plt.cm.gray)
# plt.show()

# 图像保存
cv2.imwrite("D:/2.jpg", img)
