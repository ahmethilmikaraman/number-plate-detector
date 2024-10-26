########## Kütüphaneler ############
import cv2
####################################
########## Parametreler ############
frameWidth = 640
frameHeight = 480
nPlateCascade = cv2.CascadeClassifier("Resources/haarcascades/haarcascade_russian_plate_number.xml")
minArea = 500
color = (255, 0, 255)
##################################

"""
--------------Webcam üzerinden göstereceğiniz görüntü üzerinde plaka tespit yapımı------------------

Tam çalışması için parametreler kısmındaki değişkenleri şu şekilde güncelleyin:

frameWidth = 640
frameHeight = 480
----------------------------------------------------------------------------------------------------------
"""

cap = cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,frameHeight)
cap.set(10,150)

while True:
    succes, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    numberPlates = nPlateCascade.detectMultiScale(imgGray, 1.1, 4)

    for (x, y, w, h) in numberPlates:
        area = x * y        
        if area > minArea:
            cv2.rectangle(img, (x, y), (x+w, y+h), color, 3)
            cv2.putText(img, "Number Plate", (x, y-5),
                        cv2.FONT_HERSHEY_COMPLEX, 1, color, 2)
            imgCap = img[y:y+h, x:x+w]
            cv2.imshow("Number Plate", imgCap)
            

    cv2.imshow("Output", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


"""
--------------Resources dosyasındaki number_plate.png resmi üzerinde plaka tespit yapımı------------------

Tam çalışması için parametreler kısmındaki değişkenleri şu şekilde güncelleyin:

frameWidth = 1024
frameHeight = 720
----------------------------------------------------------------------------------------------------------
"""
# img = cv2.imread("Resources/number_plate.png")
# img = cv2.resize(img,(frameWidth,frameHeight))
# print(img.shape)
# imgGray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
# numberPlates = nPlateCascade.detectMultiScale(imgGray, 1.1, 4)

# for (x, y, w, h) in numberPlates:
#         area = x * y        
#         if area > minArea:
#             cv2.rectangle(img, (x, y), (x+w, y+h), color, 3)
#             cv2.putText(img, "Number Plate", (x, y-5),
#                         cv2.FONT_HERSHEY_COMPLEX, 1, color, 2)
#             imgCap = img[y:y+h, x:x+w]
#             cv2.imshow("Number Plate", imgCap)

# cv2.imshow("Output", img)
# cv2.waitKey(0)
