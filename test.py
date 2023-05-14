import cv2
import numpy as np

img1 = cv2.imread("out/heatmap.jpg")
img2 = cv2.imread("out/out2/heatmap.jpg")

# Computing the pixel-wise difference between the two images
difference = cv2.subtract(img1, img2)

# Computing image similarity (in percentages)
similarity = (np.sum(difference == 0) / difference.size) * 100

print("Image similarity: ", similarity, "%")