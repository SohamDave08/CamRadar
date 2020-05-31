import cv2
import os

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)

id = input('enter Name:   ')




def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
        
        
createFolder('./'+str(id)+'/')


FaceCount=1

while(True):
    ret,img = cam.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5 , minNeighbors=5)
    for(x,y,w,h) in faces:
        FaceCount = FaceCount+1
        print(FaceCount)
        path = './'+str(id)+'/'
        cv2.imwrite(os.path.join(path , str(id)+"."+str(FaceCount)+".jpg"),gray[y:y+h,x:x+w])
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),10)
        #cv2.waitKey(100000)
    cv2.imshow("Face",img)
    #cv2.destroyAllWindows()
    if(FaceCount>500):
        break
    else:
        continue
    
    
cam.release()
cv2.destroyAllWindows()
