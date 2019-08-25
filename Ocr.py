mport imutils
import pytesseract
import numpy as np
import cv2

image = cv2.imread('sample94.jpg')
#image = imutils.resize(image, width=500)
cv2.imshow('rawimage', image)
cv2.waitKey(0)
#thre = filters.threshold_otsu(image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('grayscaleimage', gray)
cv2.waitKey(0)
gray = cv2.bilateralFilter(gray, 11, 17, 17)
cv2.imshow('bilateral Filter', gray)
cv2.waitKey(0)

edged = cv2.Canny(gray, 100, 200)
cv2.imshow('edgedetectionimage', edged)
cv2.waitKey(0)
cnts, new = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
img1 = image.copy()
cv2.drawContours(image, cnts, 3, (0, 255, 0), 3)
#cv2.imshow('all contours', img1)
cv2.waitKey(0)
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:30]
numberplateCnt = None
img2 = image.copy()
cv2.drawContours(img2, cnts, -1, (0, 255, 0), 3)
cv2.imshow('contourimage', img2)
cv2.waitKey(0)
count = 0
idx = 7
for c in cnts:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 *peri, True)
    if len(approx) == 4:
        NumberPlateCnt = approx
        x, y, w, h = cv2.boundingRect(c)
        new_img = image[y:y + h, x:x + w]
        cv2.imwrite('croppedImage' + str(idx) + '.png', new_img)
        idx+=1
        break
image = cv2.drawContours(image, [NumberPlateCnt], -1, (0, 255, 0), 3)
cv2.imshow('croppednumplate', image)
cv2.waitKey(0)
cropped_img_loc = 'croppedImage7.png'
cv2.imshow('a', cv2.imread(cropped_img_loc))
text = pytesseract.image_to_string(image, lang='eng')
print('number is=', text)
cv2.waitKey(0)