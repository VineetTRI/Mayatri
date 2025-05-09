from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Help:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System") 

        #Title of page
        title_label = Label(self.root,text="HELP DESK",font=("Times New Roman",35,"bold"),bg="black",fg="skyblue")
        title_label.place(x=0,y=0,width=1530,height=45)

        # Top Label Image
        img_top = Image.open("C:/Users/hs/Desktop/FaceRecog/images/Atten4.webp")
        img_top = img_top.resize((1530,720),Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        
        #Label for top label image
        first_label = Label(self.root,image=self.photoimg_top)
        first_label.place(x=0,y=55,width=1530,height=720)

        dev_label = Label(first_label,text="Email: vineettripathi750@gmail.com",font=("times new roman",20,"bold"),bg="white")
        dev_label.place(x=550,y=220)



if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()
