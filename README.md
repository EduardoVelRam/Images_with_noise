# 🧪 Image Noise Simulation and Removal with OpenCV

This project demonstrates a simple image processing pipeline that simulates **salt-and-pepper noise** in a grayscale image and then removes it using a **median filtering technique**. The goal of this script is educational: to illustrate how noise affects images and how classical filtering methods can restore image quality.

Digital images frequently suffer from noise introduced during acquisition, transmission, or compression. Salt-and-pepper noise is a common form of corruption where random pixels are replaced with either very dark or very bright values. This project provides a basic example of how such noise can be artificially generated and later reduced using standard image processing tools.

---

## 🔍 Project Overview

The workflow begins by loading a color image and converting it into grayscale. Grayscale images simplify many processing tasks because they contain only intensity information rather than multiple color channels.

Next, a custom noise generation function introduces random pixel corruption. Each pixel in the image is evaluated using a probability value that determines whether it should remain unchanged, turn black, or turn white. The resulting image visually simulates the typical salt-and-pepper noise pattern often seen in damaged or poorly transmitted images.

Once the noisy image is produced, the script applies a **median filter** to reduce the noise. Median filtering works by replacing each pixel with the median value from its surrounding neighborhood. This technique is particularly effective for removing isolated noise points while preserving edges and structural details.

---

## 🎯 Applications

This example is useful for:

- Learning basic image preprocessing techniques  
- Understanding noise models in computer vision  
- Experimenting with classical denoising filters  
- Teaching introductory digital image processing concepts  

---

## 🚀 Outcome

By comparing the original image, the noisy version, and the filtered result, users can clearly observe how noise affects visual data and how median filtering helps recover a cleaner image.
