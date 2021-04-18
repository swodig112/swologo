#!/usr/bin/env python3
import numpy as np
import cv2


COLOR = (0, 0, 255)
n = int(input("insert image size(in pixels): "))
OFFSET = int(input("insert offset size(in pixels): "))
img = np.zeros((n + 2 * OFFSET, n + 2 * OFFSET, 3), np.uint8)

a = n // 4
b = a * 2
c = a * 3
a += OFFSET
b += OFFSET
c += OFFSET
n += OFFSET
img = cv2.line(img, (b, OFFSET), (b, n), COLOR, n // 100)
img = cv2.line(img, (a, b), (c, b), COLOR, n // 100)
img = cv2.line(img, (OFFSET, a), (b, c), COLOR, n // 100)
img = cv2.line(img, (n, a), (b, c), COLOR, n // 100)
img = cv2.line(img, (OFFSET, a), (b, n), COLOR, n // 100)
img = cv2.line(img, (b, n), (n, a), COLOR, n // 100)
img = cv2.line(img, (a, b), (b, OFFSET), COLOR, n // 100)
img = cv2.line(img, (c, b), (b, OFFSET), COLOR, n // 100)

img = cv2.cvtColor(img, cv2.COLOR_RGB2RGBA)

# TODO: use floodfill function from opencv
neighbours = [[0, 0]]
while neighbours != []:
    x, y = neighbours.pop()
    img[x, y, 3] = 0
    for i in [-1, 1]:
        for j in [-1, 1]:
            if 0 <= x + i < img.shape[0] and 0 <= y + j < img.shape[1]:
                if img[x + i, y + j, 3] != 0 and img[x + i, y + j, 2] == 0:
                    neighbours.append([x + i, y + j])

cv2.imwrite("logo.png", img)
