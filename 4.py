# 영상읽기
# 영상출력

import cv2

cap = cv2.VideoCapture(0) #첫번째 웹캠 불러옴
print(cap.isOpened())
while(cap.isOpened()): #웹캠이 열리면 true, 안 열리면 false
    ret, frame = cap.read() #항상 두가지 값(ret, frame)으로 불러옴
    if ret :
        cv2.imshow('frame',frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
        
cap.release()
cv2.destroyAllWindows()



