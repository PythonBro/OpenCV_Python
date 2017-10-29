import cv2
import numpy as np
import os

os.chdir("C:\\Users\\Kanazashi\\Documents\\PythonIntro")

def main():

    th1 = 50
    th2 = 150
    
    img = cv2.imread("sample.jpg")
    screen = cv2.imread("screen.jpg")
    
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    screen = cv2.cvtColor(screen, cv2.COLOR_RGB2GRAY)

    screen = cv2.resize(screen, (gray.shape[1], gray.shape[0]))

    edge = 255 - cv2.Canny(gray, 80, 120)

    gray[gray <= th1] = 0
    gray[gray >= th2] = 255

    gray[np.where((gray > th1) & (gray < th2))] = screen[np.where((gray > th1)&(gray < th2))]
    
    manga = cv2.bitwise_and(gray, edge)

    cv2.imwrite("output.jpg", manga)

if __name__ == '__main__':
    main()    
