from deepface import DeepFace

import os
import cv2
import time

def verify(userName,img):
    l=[]
    os.chdir("./Users/"+userName)
    for i in userName:
        result = DeepFace.verify(f"{img}","{i}")
        l.append(result["verified"])
    if l.count("True")/len(l)*100>65 :
        print("Verified")
    else:
        print("retake")

def getImage(userName):
    cam=cv2.VideoCapture(0)
    res,image=cam.read()
    #verify(userName,image)
    
    l=[]
    os.chdir("./Users")
    cv2.imwrite("temp.png",image)

    for i in os.listdir(userName):
        print(i)
        print("Hello")
        result = DeepFace.verify("temp.png","./"+userName+"/"+i)
        l.append(result["verified"])
    res=l.count("True")/len(l)*100
    if res>=65 :
        print("Verified")
    elif res>=40 and res<65:
        print("retake")
    else:
        print("Please verify your user credentials")
    #cv2.imshow("sampleimg",image)
    #cv2.imwrite("mani.png",image)
    

def createUser(userName):
    os.mkdir("./Users/"+userName)
    print("Folder created....")
    print("Get ready for imgs for db...")
    os.chdir("./Users/"+userName)
    for i in range(3):
        cam=cv2.VideoCapture(0)
        res,image=cam.read()
        cv2.imwrite(f"{userName}{i+1}.png",image)
        print("Try another pose")
    print("User registered successfully")
    
print("1.create Acc\n2.Mark att")
choice=int(input("Enter your choice: "))

if(choice==1):
    userName=input("Enter your Name: ")
    createUser(userName)
elif(choice==2):
    userName=input("Enter  your userName to verify: ")
    getImage(userName)
#getImage(1,"Mani")


#print(os.listdir("./Users/yoga"))

