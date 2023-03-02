import cv2

import numpy as np


# Функция вычисления хэша
def CalcImageHash(FileName):
    image = cv2.imread('elements_img/' + FileName)  # Прочитаем картинку
    resized = cv2.resize(image, (8, 8), interpolation=cv2.INTER_AREA)  # Уменьшим картинку
    gray_image = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)  # Переведем в черно-белый формат
    avg = gray_image.mean()  # Среднее значение пикселя
    ret, threshold_image = cv2.threshold(gray_image, avg, 255, 0)  # Бинаризация по порогу

    # Рассчитаем хэш
    _hash = ""
    for x in range(8):
        for y in range(8):
            val = threshold_image[x, y]
            if val == 255:
                _hash = _hash + "1"
            else:
                _hash = _hash + "0"

    return _hash


def CompareHash(hash1, hash2):
    l = len(hash1)
    i = 0
    count = 0
    while i < l:
        if hash1[i] != hash2[i]:
            count = count + 1
        i = i + 1
    return count


# hash1 = CalcImageHash("elem_230301_142236.png")
# hash2 = CalcImageHash("elem_230301_142320.png")
# print(hash1)
# print(hash2)
# print(CompareHash(hash1, hash2))



# load the input images
img1 = cv2.imread('elements_img/' + 'elem_230301_155606.png')
img2 = cv2.imread('elements_img/' + 'elem_230301_155609.png')

resized1 = cv2.resize(img1, (64, 64), interpolation=cv2.INTER_AREA)  # Уменьшим картинку
resized2 = cv2.resize(img2, (64, 64), interpolation=cv2.INTER_AREA)  # Уменьшим картинку

# convert the images to grayscale
img1 = cv2.cvtColor(resized1, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(resized2, cv2.COLOR_BGR2GRAY)

# define the function to compute MSE between two images
def mse(img1, img2):
   h, w = img1.shape
   diff = cv2.subtract(img1, img2)
   err = np.sum(diff**2)
   mse = err/(float(h*w))
   return mse, diff

error, diff = mse(img1, img2)
print("Image matching Error between the two images:", error)

cv2.imshow("difference", diff)
cv2.waitKey(0)
cv2.destroyAllWindows()