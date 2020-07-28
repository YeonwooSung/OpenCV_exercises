import cv2
import numpy as np

file_name = "../img/sudoku.jpg"
img = cv2.imread(file_name)

# generate prewitt kernel
gx_k = np.array([[-1,0,1], [-1,0,1],[-1,0,1]])
gy_k = np.array([[-1,-1,-1],[0,0,0], [1,1,1]])

# apply prewitt kernel
edge_gx = cv2.filter2D(img, -1, gx_k)
edge_gy = cv2.filter2D(img, -1, gy_k)

# show result images
merged = np.hstack((img, edge_gx, edge_gy, edge_gx+edge_gy))
cv2.imshow('prewitt', merged)
cv2.waitKey(0)
cv2.destroyAllWindows()
