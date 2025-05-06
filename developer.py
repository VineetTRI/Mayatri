from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Developer:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System") 

        #Title of page
        title_label = Label(self.root,text="DEVELOPER",font=("Times New Roman",35,"bold"),bg="white",fg="blue")
        title_label.place(x=0,y=0,width=1530,height=45)

        # Top Label Image
        img_top = Image.open("C:/Users/hs/Desktop/FaceRecog/images/Atten5.webp")
        img_top = img_top.resize((1530,720),Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        
        #Label for top label image
        first_label = Label(self.root,image=self.photoimg_top)
        first_label.place(x=0,y=55,width=1530,height=720)

        #Frame
        main_frame = Frame(first_label,bd=2,bg="white")
        main_frame.place(x=1000,y=55,width=500,height=600)

        # Top Label Image
        img_top1 = Image.open("C:/Users/hs/Desktop/FaceRecog/images/dev.png")
        img_top1 = img_top1.resize((200,200),Image.Resampling.LANCZOS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)
        
        #Label for top label image
        first_label = Label(main_frame,image=self.photoimg_top1)
        first_label.place(x=300,y=0,width=200,height=200)

        #Developer info
        dev_label = Label(main_frame,text="Hello!!",font=("times new roman",20,"bold"),bg="white")
        dev_label.place(x=0,y=5)
        dev_label = Label(main_frame,text="Welcome to Developers\n Area",font=("times new roman",20,"bold"),bg="white")
        dev_label.place(x=0,y=40)

        #Third image
        img3 = Image.open("C:/Users/hs/Desktop/FaceRecog/images/Student3.webp")
        img3 = img3.resize((500,400),Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        #Label for third image
        first_label = Label(main_frame,image=self.photoimg3)
        first_label.place(x=0,y=230,width=500,height=400)

if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()