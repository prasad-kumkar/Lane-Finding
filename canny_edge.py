import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2

# Read in the image and convert to grayscale
image = mpimg.imread('exit-ramp.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

# Define a kernel size for Gaussian smoothing / blurring
# Note: this step is optional as cv2.Canny() applies a 5x5 Gaussian internally
kernel_size = 3
blur_gray = cv2.GaussianBlur(gray,(kernel_size, kernel_size), 0)

# Define parameters for Canny and run it
# NOTE: if you try running this code you might want to change these!
low_threshold = 100
high_threshold = 255
edges = cv2.Canny(blur_gray, low_threshold, high_threshold)

# Display the image


plt.subplot(121),plt.imshow(blur_gray, cmap='Greys_r'),plt.title('Gaussian Blue')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges, cmap='Greys_r'),plt.title('Canny')
plt.xticks([]), plt.yticks([])
plt.show()