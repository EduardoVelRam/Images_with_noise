import numpy as np
import cv2
import random

# Adding noise function 
def im_noise(image, prob):
    output = np.zeros(image.shape, np.uint8)
    thres = 1 - prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output

# opening the image
frame = cv2.imread('images/image2.jpg')

# change the image to gray scale
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# open image with noise
cv2.imshow('Original Image', gray)

# wait for a key press and get in variable
k = cv2.waitKey(0)

# building the noise image
noise_img = im_noise(gray, 0.05)

# showing the noise image
cv2.imshow('Noise Image', noise_img)

# wait for a key press and get in variable
k = cv2.waitKey(0)
cv2.destroyAllWindows()

# remove noise
# median filter
denoised = cv2.medianBlur(noise_img, 5)

cv2.imshow('Denoised Image', denoised)
cv2.waitKey(0)
cv2.destroyAllWindows()