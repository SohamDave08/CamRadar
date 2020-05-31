import cv2
import pymysql

mydb = pymysql.connect(host="localhost", user="root", passwd="", db="Criminals")
mycursor = mydb.cursor()

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml")



cap = cv2.VideoCapture(0)

while True:
    ret, Criminal = cap.read()
    gray = cv2.cvtColor(Criminal, cv2.COLOR_BGR2GRAY)  
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5 , minNeighbors=5)
    for(x,y,w,h) in faces:
       
        
        roi_gray = gray[y:y+h, x:x+w]
        
        id_,conf = recognizer.predict(roi_gray)
        
        if conf>=40 and conf<=70:
            
            cv2.rectangle(Criminal, (x,y) ,(x+w, y+h), (255,0,0),2)
              
            mycursor.execute("SELECT Name FROM Records where ID='%s'" %id_)
            result = mycursor.fetchone()
            for i in result:
                a=i
                
            
            name = a
            print(name)
            font = cv2.FONT_HERSHEY_SIMPLEX
            color = (255,255,255)
            stroke = 2
            cv2.putText(Criminal, name, (x,y), font, 1, color, stroke, cv2.LINE_AA)
            
          
            mycursor.execute("SELECT Detects FROM Records where ID='%s'" %id_)
            result = mycursor.fetchone()
            for i in result:
                a=i
            a = a+1
            print(a)
            s=a
            
           
            sql_q = ("UPDATE Records SET Detects = %s WHERE ID= '%s'")
            data = (s,id_)
            mycursor.execute(sql_q,data)
            mydb.commit()
        else:
            pass

            
    cv2.imshow('Criminal', Criminal)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
       break

cap.release()
cv2.destroyAllWindows()
