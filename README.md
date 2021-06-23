# CamRadar - Criminal detection and recognition project using the LBPH algorithm

## Motivation for the project

There is an abnormal increase in the crime rate, this leads towards a great concern about the security issues. Crime preventions and criminal identification are the main hurdles
for our police force since there is a large ratio gap between the number of crimes taken place and the availability of police personnel to combat the crime. With the improved 
security measures, the government has implemented some robust security technologies, especially CCTV cameras have been installed in many public and private areas to provide 
24x7 surveillance. The footage of the CCTV can be used to identify suspects on the scene. In this project, a facial recognition system for the identification of criminals has 
been proposed. This system will be able to detect the face and recognize face automatically in real-time. Face detection classifiers are shared by open source communities,
such as OpenCV. This project demonstrates the generic framework for the face recognition system, and the variants that are frequently encountered by
the face recognizer. One of the most famous face recognition algorithms, the LBPH algorithm using Haar feature-based cascade classifier will also be explained, the most 
important applications is in the field of face detection. Face detection is a very powerful tool for face recognition, face tracking, video surveillance, autofocusing, and 
human-computer interface systems. Some other application areas of face recognition are Information security, law enforcement and surveillance, smart cards, access controls.


## Libraries Used

### openCV2 
OpenCV2 is used for providing a medium to identify frontal_face and fetch facial features using Haarcascade.
> pip install opencv-python

### Pillow
Pillow is used to manage hundreds of criminal images in an ordered manner.
> pip install Pillow

### Numpy
Numpy is used for converting the given dataset to a training model and deploying the plugin in production with ease.
> pip install numpy

### PyMySql
PyMySql is used to refer to the criminal database and ping the collection everytime a criminal is detected by the model.
> pip install PyMySQL


## Images Of Project

### datasetCreator.py:
![](https://user-images.githubusercontent.com/51802431/94796140-f9598400-03fb-11eb-804c-11e364b6226a.png)
![](https://user-images.githubusercontent.com/51802431/94796151-feb6ce80-03fb-11eb-9680-28a00ce987b3.png)

### Face_train.py:
![](https://user-images.githubusercontent.com/51802431/94796195-13936200-03fc-11eb-8bac-a9687d8bd280.png)

### Face_detect.py:
![](https://user-images.githubusercontent.com/51802431/94796259-24dc6e80-03fc-11eb-8dbe-ad40bbc55e37.png)

### Thanks For Reading
