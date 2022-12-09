import cv2
import imutils
import numpy as np
import  pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img = cv2.imread(r'C:\Users\Vlad\Desktop\masina\clio.jpg ')
#img = cv2.resize(img,(800,600))
#cv2.imshow('Imagine Redimensionala',img)
gray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray =cv2.bitateralFilter(gray,13,15,15)
edged = cv2.Canny(gray,30,200)
cv2.imshow('Imagine cu filtru gri',gray)
cv2.imshow('Canny Edge Image',edged)

contur =cv2.findContours(edged.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
contur = imutils.grab_contours(contur)
contur = sorted(contur,key = cv2.contourArea,reverse = True)[:10]
screenCnt = None
for c in contur:
    peri = cv2.arcLength(c,True)
    approx = cv2.approxPolyDP(c,0.018 * peri,True)
    if len(approx) ==4:
        screenCnt = approx
        break
  if screenCnt is None:
  detected = 0
  print("Nu a fost detectat niciun contur")
  else:
  detected = 1
  mask = np.zeros(gray.shape,np.uint8)
  new_image = cv2.drawContours(mask,[screenCnt],0,255,-1)
  ##cv2.imshow('Contur',new_image)##
  (x,y) = np.where(mask ==255)
  (topx,topy) = (np.min(x),np.min(y))
  (bottomx,bottomy) = (np.max(x),np.max(y))
  CROP = gray[topx:bottomx+1,topy:bottomy+1]
  text_numar = pytesseract.image_to_string(CROP,config='--psn 10')
  img = cv2.resize(img,(500,300))
  CROP = cv2.resize(CROP,(400,200))

cv2.imshow('DECUPAT',CROP)
cv2.waitkey(0)
cv2.destroyAllWindows()

