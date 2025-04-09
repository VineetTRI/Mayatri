from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk

class Face_Recognition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
         
        #First image
        img = Image.open("C:/Users/hs/Desktop/FaceRecog/images/Atten4.webp")
        img = img.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        
        #Label for first image
        first_label = Label(self.root,image=self.photoimg)
        first_label.place(x=0,y=0,width=500,height=130)

        #Second image
        img2 = Image.open("C:/Users/hs/Desktop/FaceRecog/images/Atten3.jpeg")
        img2 = img2.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        
        #Label for Second image
        first_label = Label(self.root,image=self.photoimg2)
        first_label.place(x=500,y=0,width=500,height=130)

        #Third image
        img3 = Image.open("C:/Users/hs/Desktop/FaceRecog/images/Atten2.webp")
        img3 = img3.resize((550,130),Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        #Label for third image
        first_label = Label(self.root,image=self.photoimg3)
        first_label.place(x=1000,y=0,width=550,height=130)

        #Background image
        img4 = Image.open("C:/Users/hs/Desktop/FaceRecog/images/bg.jpg")
        img4 = img4.resize((1530,710),Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        
        #Label for Background image
        bg_img = Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1530,height=710)
        
        #Title of page
        title_label = Label(bg_img,text="ATTENDANCE MARKING MODEL",font=("Times New Roman",35,"bold"),bg="white",fg="red")
        title_label.place(x=0,y=0,width=1530,height=45)

        #Student button
        img5 = Image.open("C:/Users/hs/Desktop/FaceRecog/images/Student.webp")
        img5= img5.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        
        #button
        b1 = Button(bg_img,image=self.photoimg5,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1 = Button(bg_img,text="Student Details",cursor="hand2",font=("Times New Roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)

        #Face Recognition button
        img6 = Image.open("C:/Users/hs/Desktop/FaceRecog/images/fr.png")
        img6= img6.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        
        #button
        b2 = Button(bg_img,image=self.photoimg6,cursor="hand2")
        b2.place(x=500,y=100,width=220,height=220)

        b2_2 = Button(bg_img,text="Face Recognition",cursor="hand2",font=("Times New Roman",15,"bold"),bg="darkblue",fg="white")
        b2_2.place(x=500,y=300,width=220,height=40)

        #Attendance button
        img7 = Image.open("C:/Users/hs/Desktop/FaceRecog/images/Atten1.jpg")
        img7= img7.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        
        #button
        b3 = Button(bg_img,image=self.photoimg7,cursor="hand2")
        b3.place(x=800,y=100,width=220,height=220)

        b3_3 = Button(bg_img,text="Attendance",cursor="hand2",font=("Times New Roman",15,"bold"),bg="darkblue",fg="white")
        b3_3.place(x=800,y=300,width=220,height=40)

        #Help Desk button
        img8 = Image.open("C:/Users/hs/Desktop/FaceRecog/images/hd.webp")
        img8= img8.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)
        
        #button
        b4 = Button(bg_img,image=self.photoimg8,cursor="hand2")
        b4.place(x=1100,y=100,width=220,height=220)

        b4_4 = Button(bg_img,text="Help Desk",cursor="hand2",font=("Times New Roman",15,"bold"),bg="darkblue",fg="white")
        b4_4.place(x=1100,y=300,width=220,height=40)

        #Train Face button
        img9 = Image.open("C:/Users/hs/Desktop/FaceRecog/images/tf.webp")
        img9= img9.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)
        
        #button
        b5 = Button(bg_img,image=self.photoimg9,cursor="hand2")
        b5.place(x=200,y=380,width=220,height=220)

        b5_5 = Button(bg_img,text="Train Face",cursor="hand2",font=("Times New Roman",15,"bold"),bg="darkblue",fg="white")
        b5_5.place(x=200,y=580,width=220,height=40)

        #photos Face button
        img10 = Image.open("C:/Users/hs/Desktop/FaceRecog/images/photos.jfif")
        img10= img10.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)
        
        #button
        b6 = Button(bg_img,image=self.photoimg10,cursor="hand2")
        b6.place(x=500,y=380,width=220,height=220)

        b6_6 = Button(bg_img,text="Photos",cursor="hand2",font=("Times New Roman",15,"bold"),bg="darkblue",fg="white")
        b6_6.place(x=500,y=580,width=220,height=40)

        #Developer button
        img11 = Image.open("C:/Users/hs/Desktop/FaceRecog/images/dev.png")
        img11= img11.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)
        
        #button
        b7 = Button(bg_img,image=self.photoimg11,cursor="hand2")
        b7.place(x=800,y=380,width=220,height=220)

        b7_7 = Button(bg_img,text="Developer",cursor="hand2",font=("Times New Roman",15,"bold"),bg="darkblue",fg="white")
        b7_7.place(x=800,y=580,width=220,height=40)

        #Exit
        img12 = Image.open("C:/Users/hs/Desktop/FaceRecog/images/exit.jpg")
        img12= img12.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg12 = ImageTk.PhotoImage(img12)
        
        #button
        b8 = Button(bg_img,image=self.photoimg12,cursor="hand2")
        b8.place(x=1100,y=380,width=220,height=220)

        b8_8 = Button(bg_img,text="Exit",cursor="hand2",font=("Times New Roman",15,"bold"),bg="darkblue",fg="white")
        b8_8.place(x=1100,y=580,width=220,height=40)


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
    
    
