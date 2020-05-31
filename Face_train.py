import os
from PIL import Image
import numpy as np
import cv2
import pymysql



#Linking DB
mydb = pymysql.connect(host="localhost", user="root", passwd="", db="Criminals")
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM Records")
result = mycursor.fetchall()
p=0
for i in result:
    p=1

if p == 1:
    mycursor.execute("DELETE FROM Records")
else:
    pass



face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

recognizer = cv2.face.LBPHFaceRecognizer_create()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, "Criminals")

current_id = 0
label_ids = {}
y_labels = []
x_train = []
ids=[]
for root, dirs, files in os.walk(image_dir):
    New=0    
    for file in files:
        if file.endswith("png") or file.endswith("JPEG") or file.endswith("JPG") or file.endswith("jpeg") or file.endswith("jpg") or file.endswith("PNG"):
            path = os.path.join(root, file)
            label = os.path.basename(os.path.dirname(path)).replace(" ","-").lower()
            
            #Give ID:
            if label in label_ids:
                pass
            else:
                label_ids[label] = current_id
                current_id += 1
            
            id_ = label_ids[label]
            print(id_)
            print(label)
            
            if New == 0:
                sql_insert_query = "INSERT INTO Records (Name, ID, Detects) VALUES (%s,%s,%s)"
                insert_tuple = (label, id_, 0)
                mycursor.execute(sql_insert_query, insert_tuple)
                mydb.commit()
                New=1
                print ("Record inserted successfully into RECORDS table")
            else:
                pass
            
            ids.append(id_)

                
            pil_image = Image.open(path).convert("L")
            size = (550,550)
            final_image = pil_image.resize(size, Image.ANTIALIAS)
            image_array = np.array(final_image, "uint8")  #Every pixels into numpy array


            faces = face_cascade.detectMultiScale(image_array, scaleFactor=1.5 , minNeighbors=5)

            for (x,y,w,h) in faces:
                roi = image_array[y:y+h, x:x+w]
                x_train.append(roi)
                y_labels.append(id_)
                

recognizer.train(x_train, np.array(y_labels))
recognizer.save("trainer.yml")

print("All criminals are trainned")
