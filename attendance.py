from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

myData = []
class Attendance:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #============= variables ================
        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_attendance = StringVar()

        #First image
        img = Image.open("C:/Users/hs/Desktop/FaceRecog/images/Student1.jfif")
        img = img.resize((800,200),Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        
        #Label for first image
        first_label = Label(self.root,image=self.photoimg)
        first_label.place(x=0,y=0,width=800,height=200)

        #Second image
        img2 = Image.open("C:/Users/hs/Desktop/FaceRecog/images/Student2.jpg")
        img2 = img2.resize((800,200),Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        #Label for Second image
        first_label = Label(self.root,image=self.photoimg2)
        first_label.place(x=800,y=0,width=800,height=200)

        #Background image
        img4 = Image.open("C:/Users/hs/Desktop/FaceRecog/images/bg.jpg")
        img4 = img4.resize((1530,710),Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        
        #Label for Background image
        bg_img = Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=200,width=1530,height=710)

        #Title of page
        title_label = Label(bg_img,text="Attendance Record Area",font=("Times New Roman",35,"bold"),bg="green",fg="black")
        title_label.place(x=0,y=0,width=1530,height=45)

        #Frame
        main_frame = Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=0,y=55,width=1500,height=600)

        #Left Label Frame
        Left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=0,y=10,width=730,height=580)

        # Left Label Image
        img_left = Image.open("C:/Users/hs/Desktop/FaceRecog/images/Student1.jfif")
        img_left = img_left.resize((720,130),Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        
        #Label for left label image
        first_label = Label(Left_frame,image=self.photoimg_left)
        first_label.place(x=5,y=0,width=720,height=130)

        #Left Inside Frame
        left_inside_frame = Frame(bg_img,bd=2,relief="ridge",bg="white")
        left_inside_frame.place(x=5,y=230,width=720,height=370)

        #AttendanceID
        AttendanceID_label = Label(left_inside_frame,text="AttendanceID:",font=("times new roman",13,"bold"),bg="white")
        AttendanceID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        AttendanceID_entry = ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",13,"bold"))
        AttendanceID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #Roll
        Roll_label = Label(left_inside_frame,text="Roll:",font=("times new roman",13,"bold"),bg="white")
        Roll_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        Roll_entry = ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_roll,font=("times new roman",13,"bold"))
        Roll_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #Name
        Name_label = Label(left_inside_frame,text="Name:",font=("times new roman",13,"bold"),bg="white")
        Name_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        Name_entry = ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_name,font=("times new roman",13,"bold"))
        Name_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #Dep
        Dep_label = Label(left_inside_frame,text="Department:",font=("times new roman",13,"bold"),bg="white")
        Dep_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        Dep_entry = ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_dep,font=("times new roman",13,"bold"))
        Dep_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #time
        time_label = Label(left_inside_frame,text="Time:",font=("times new roman",13,"bold"),bg="white")
        time_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        time_entry = ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_time,font=("times new roman",13,"bold"))
        time_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #Date
        Date_label = Label(left_inside_frame,text="Date:",font=("times new roman",13,"bold"),bg="white")
        Date_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        Date_entry = ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_date,font=("times new roman",13,"bold"))
        Date_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #Attendance Status
        Attendance_label = Label(left_inside_frame,text="Attendance:",font=("times new roman",13,"bold"),bg="white")
        Attendance_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        self.atten_status = ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_atten_attendance,font="comicsansns 11 bold",state="readonly")
        self.atten_status["values"] = ("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)

        #buttons Frame
        btn_frame = Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=300,width=715,height=35)

        save_btn = Button(btn_frame,text="Import csv",command=self.importCsv,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn = Button(btn_frame,text="Update",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=2)

        reset_btn = Button(btn_frame,text="Reset",width=17,command=self.reset,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        delete_btn = Button(btn_frame,text="Export csv",command=self.exportCsv,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=1)



        #Right Label Frame
        Right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=760,y=10,width=720,height=580)

        #buttons Frame
        table_frame = Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=710,height=455)

        #============== Scroll Bar ================
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"] = "headings"
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    #=============== fetch data ====================
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    # Import CSV
    def importCsv(self):
        global myData
        myData.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile,delimiter=",")
            for i in csvread:
                myData.append(i)
            self.fetchData(myData)

    # Export CSV
    def exportCsv(self):
        try:
            if len(myData)<1:
                messagebox.showerror("No Data","No data found to export",parent = self.root)
                return False
            fln = filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write = csv.writer(myfile,delimiter=",")
                for i in myData:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data is exported to "+os.path.basename(fln)+"successfully")

        except Exception as es:
            messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
    
    def get_cursor(self,event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        row = content["values"]
        self.var_atten_id.set(row[0])
        self.var_atten_roll.set(row[1])
        self.var_atten_name.set(row[2])
        self.var_atten_dep.set(row[3])
        self.var_atten_date.set(row[4])
        self.var_atten_time.set(row[5])
        self.var_atten_attendance.set(row[6])
        
    def reset(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_date.set("")
        self.var_atten_time.set("")
        self.var_atten_attendance.set("")

        


if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()