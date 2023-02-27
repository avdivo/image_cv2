"""
Нахождение контура


Для работы нужно установить OpenCV:
pip install opencv-python
"""

import cv2

# прочитать изображение
img = cv2.imread('images_in/chrome2.png')

# преобразовать изображение в формат оттенков серого
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# apply binary thresholding
# Применение бинарного порога к изображению
ret, thresh = cv2.threshold(img_gray, 80, 255, cv2.THRESH_BINARY)

# Нахождение контуров
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# https://stackoverflow.com/questions/55587820/how-to-get-the-only-min-area-rectangle-on-a-multiple-contours-image-with-cv2-min

# cnt = max(contours, key=cv2.contourArea) # Наибольший контур

# Показать все контуры
# for cnt in contours:
#     x,y,w,h = cv2.boundingRect(cnt)
#     cv2.rectangle(img, (x,y), (x+w+10, y+h+10), (255,255,0), 1)
#     cv2.imshow('img', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Сохранить все контуры
ROI_number = 0
for c in contours:
    x,y,w,h = cv2.boundingRect(c)
    ROI = img[y:y+h, x:x+w]
    cv2.imwrite('images_out/ROI_{}.png'.format(ROI_number), ROI)
    ROI_number += 1



