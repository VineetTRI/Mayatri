from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #Title of page
        title_label = Label(self.root,text="TRAIN DATASET",font=("Times New Roman",35,"bold"),bg="green",fg="black")
        title_label.place(x=0,y=0,width=1530,height=45)

        # Top Label Image
        img_top = Image.open("C:/Users/hs/Desktop/FaceRecog/images/train.jpeg")
        img_top = img_top.resize((1530,325),Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        
        #Label for top label image
        first_label = Label(self.root,image=self.photoimg_top)
        first_label.place(x=0,y=55,width=1530,height=325)

        #button
        b1_1 = Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("Times New Roman",30,"bold"),bg="red",fg="white")
        b1_1.place(x=0,y=380,width=1530,height=60)


        # bottom Label Image
        img_bottom = Image.open("C:/Users/hs/Desktop/FaceRecog/images/tf.webp")
        img_bottom = img_bottom.resize((1530,325),Image.Resampling.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        
        #Label for top label image
        first_label = Label(self.root,image=self.photoimg_bottom)
        first_label.place(x=0,y=440,width=1530,height=325)

    def train_classifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L') # Gray scale
            imageNp = np.array(img,'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1) == 13
        ids = np.array(ids)

        # Train the classifier
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training dataset completed!!")


        
if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()