import os
import pickle
import cv2
import face_recognition
import cvzone
import numpy as np
from pathlib import Path


cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

imgBackground = cv2.imread('resources/background-f.png')


folderModePath = 'resources/modes'
modePathList = os.listdir(folderModePath)
imgModeList = []
for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath, path)))

print("Loading Encode File ...")
file = open("EncodeFile.p", 'rb')

encodeListKnownWithIds = pickle.load(file)
file.close()
encodeListKnown, studentIds = encodeListKnownWithIds

print("Encode File Loaded")

present_prn_file= Path("present.p")

if (present_prn_file.is_file()): 
    os.remove(present_prn_file)
present_prn=[]

imgStudent = []

while True:
    
    success, img = cap.read()

    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)

    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    faceCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)

    imgBackground[162:162 + 480, 55:55 + 640] = img
    # imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[1]

    for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        

        matchIndex = np.argmin(faceDis)
        

        
        if matches[matchIndex]:
            print("Known Face Detected")
            print(studentIds[matchIndex])
            
            present_prn_list_file = open("present.p", 'wb')

            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            bbox = 55 + x1, 162 + y1, x2 - x1, y2 - y1
            imgBackground = cvzone.cornerRect(imgBackground, bbox, rt=0)
            id = studentIds[matchIndex]


            present_prn.append(int(id))
            
            pickle.dump(present_prn, present_prn_list_file)
           
            
    cv2.imshow("Face Attendance", imgBackground)
    cv2.waitKey(1)








    