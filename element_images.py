"""
Сохранение изображения кнопки/иконки (элемента)

Для работы нужно установить OpenCV:
pip install opencv-python

$ sudo apt-get install scrot
$ sudo apt-get install python-tk python-dev
$ sudo apt-get install python3-tk python3-dev
$ workon your_virtualenv
$ pip install pillow imutils
$ pip install python3_xlib python-xlib
$ pip install pyautogui
https://pyimagesearch.com/2018/01/01/taking-screenshots-with-opencv-and-python/

"""

import tempfile
# tf = tempfile.NamedTemporaryFile()
# tf.name

import numpy as np
import pyautogui
import cv2

REGION = 128  # Сторона квадрата получаемого изображения с экрана для поиска в нем элемента

def save_image(x :int, y :int) -> str:
    """ Сохранение изображения кнопки/иконки (элемента)

    Функция принимает в качестве аргументов координаты точки на экране.
    Предполагается, что эта точка расположена на элементе, изображение которого нужно сохранить.
    Точка принимается как цент квадрата. Внутри него будет искаться изображение элемента.
    Возвращает имя нового изображения.

    """

    image = pyautogui.screenshot(region=(200,200, 300, 400))
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    cv2.imwrite("in_memory_to_disk.png", image)


save_image(0, 0)