import cv2
import numpy as np
from PIL import Image

image = cv2.imread('image.png')

edges = cv2.Canny(image, 50, 100)

contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for c in contours:
    approx = cv2.approxPolyDP(c, 0.02 * cv2.arcLength(c, True), True)
    if len(approx) == 4:
        x, y, w, h = cv2.boundingRect(c)

        if w > 200 and h > 150 and w < 1000 and h < 500:
            roi = image[y:y+h, x:x+w]
            roi = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
            roi = Image.fromarray(roi)
            roi.save('border_{}_{}_{}_{}.png'.format(x, y, w, h))
