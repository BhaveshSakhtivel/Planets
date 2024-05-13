import cv2

img = cv2.imread('E:/Python Programs/PRO-104-Project-Image-main/solar-system.jpg')

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.putText(img,
            "sun",
            (20,300),
             cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255,)
            )
            
cv2.putText(img,
            "Mercury",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255,)
            )
cv2.putText(img,
            "Earth",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255,)
            )
cv2.putText(img,
            "Mars",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255,)
            )
cv2.putText(img,
            "Jupiter",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255,)
            )
cv2.putText(img,
            "Saturn",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255,)
            )
            
cv2.putText(img,
            "Uranus",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255,)
            )
cv2.putText(img,
            "Neptune",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255,)
            )

cv2.imwrite("Solar_systemBhavesh.jpg",img)
            
            
            
            
            
            