import cv2
import numpy as np
from pyzbar.pyzbar import decode


img1 = cv2.imread('employee-id-card.png')

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

with open('myDataFile.txt') as f:
    myDataList = f.read().splitlines()
print(myDataList)

while True:
    pluggedInLogo = None
    success, img = cap.read()
    img = cv2.cvtColor(img,cv2.COLOR_BGR2BGRA)
    for barcode in decode(img):
        myData = barcode.data.decode('utf-8')
        print(myData)

        if myData in myDataList:
            myOutput  = 'Authorized'
            Security_Clearance = 'Security Clearance:  A1'
            Comment = ''
            myColor = (0,255,0)
        else:
            myOutput  = 'Un-Authorized'
            Security_Clearance = 'Security Clearance: B1'
            Comment = 'Min A1 Clearance required'
            myColor = (0,0,255)


        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape(-1,1,2)
        cv2.polylines(img,[pts],True,myColor,5)
        pts2 = barcode.rect
        cv2.putText(img,myOutput,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,0.9,myColor,2)
        cv2.putText(img, '**************Alert************', (300, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, myColor, 2)
        cv2.putText(img, Security_Clearance, (300, 55), cv2.FONT_HERSHEY_SIMPLEX, 0.7, myColor, 2)
        cv2.putText(img, Comment, (300, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, myColor, 2)
    cv2.imshow('result',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
#print(code)
