# import cv2
#
#
# query_img = cv2.imread('elements_img/' + 'elem_230301_230320.png')
# original_img = cv2.imread('elements_img/' + 'elem_230301_230320.png')
# query_img_bw = cv2.cvtColor(query_img, cv2.IMREAD_GRAYSCALE)
# original_img_bw = cv2.cvtColor(original_img, cv2.IMREAD_GRAYSCALE)
#
# orb = cv2.ORB_create()
# queryKP, queryDes = orb.detectAndCompute(query_img_bw, None)
# trainKP, trainDes = orb.detectAndCompute(original_img_bw, None)
#
# matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
# matches = matcher.match(queryDes, trainDes)
# matches = sorted(matches, key = lambda x:x.distance)
# print(matches)
# final_img = cv2.drawMatches(query_img, queryKP,
#                             original_img, trainKP, matches[:20], None)
# final_img = cv2.resize(final_img, (900, 400))
#
# cv2.imshow("Matches", final_img)
# cv2.waitKey()





# import cv2
#
# method = cv2.TM_SQDIFF_NORMED
#
# small_image = cv2.imread('elements_img/' + 'Снимок экрана от 2023-03-02 00-20-05.png')
# large_image = cv2.imread('elements_img/' + 'Снимок экрана от 2023-03-02 00-18-10.png')
#
# result = cv2.matchTemplate(small_image, large_image, method)
#
# mn,_,mnLoc,_ = cv2.minMaxLoc(result)
#
# MPx,MPy = mnLoc
#
# trows,tcols = small_image.shape[:2]
# h = (MPx + tcols//2)
# v = (MPy + trows//2)
#
# cv2.line(large_image, (MPx, (MPy+MPy+trows)//2), (MPx+tcols, (MPy+MPy+trows)//2), (0,255,255), thickness=20, lineType=8, shift=0)
# cv2.imshow('one', large_image)
# cv2.imwrite('elements_img/' + 'one.jpg', large_image)
#
# cv2.waitKey(0)




import cv2
import numpy as np
# Чтение основного изображения
rgb_img = cv2.imread(r'elements_img/' + r'Снимок экрана от 2023-03-02 10-08-39.png', 1)
# rgb_img = cv2.imread(r'elements_img/' + r'Снимок экрана от 2023-03-02 00-18-10.png', 1)

# Чтение шаблона
template = cv2.imread(r'elements_img/' + r'Снимок экрана от 2023-03-02 12-50-47.png', 0)

# Порог
threshold = 0.8
method = cv2.TM_CCOEFF_NORMED

# Перевод изображения в оттенки серого
gray_img = cv2.cvtColor(rgb_img, cv2.COLOR_BGR2GRAY)

# Сохранить ширину в переменной w и высоту в переменной h шаблона
# w, h = template.shape[:-1]
w, h = template.shape

# Операция сопоставления
res = cv2.matchTemplate(gray_img,template,method)



# Сохраните координаты совпадающего местоположения в массиве numpy
loc = np.where(res >= threshold)
print(loc)

# (_, _, minLoc, maxLoc) = cv2.minMaxLoc(res)
# print(minLoc, maxLoc)
# pt = maxLoc
# d = cv2.rectangle(rgb_img, pt,(pt[0] + w, pt[1] + h),(0,255,255), 2)


# Нарисуйте прямоугольник вокруг совпадающей области
for pt in zip(*loc[::-1]):
    print(pt)
    d = cv2.rectangle(rgb_img, pt,(pt[0] + w, pt[1] + h),(0,255,255), 2)

# Отобразить окончательное совпадающее изображение шаблона
cv2.imshow('Detected', d)
cv2.waitKey(0)