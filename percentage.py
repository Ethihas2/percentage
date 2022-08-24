from tkinter import *

root = Tk()
root.geometry('600x600')
root.title("Percentage")

label_3 = Label(root)
label_5 = Label(root)
label_10 = Label(root)

class Grade_3:
    def __init__(self,language_arts,maths):
        self.maths = maths
        self.language_arts = language_arts
    def percentage(self):
        self.total_marks = self.language_arts+self.maths
        self.total_marks_with100 = self.total_marks*100
        self.percent = self.total_marks_with100/200
        label_3["text"]=str(self.percent)

class Grade_5:
    def __init__(self,language_arts,maths,social):
        self.maths = maths
        self.language_arts = language_arts
        self.social = social
    def percentage(self):
        self.total_marks = self.language_arts+self.maths+self.social
        self.total_marks_with100 = self.total_marks*100
        self.percent = self.total_marks_with100/300
        label_5["text"]=str(self.percent)

class Grade_10:
    def __init__(self,language_arts,maths,social,french):
        self.maths = maths
        self.language_arts = language_arts
        self.social = social
        self.french = french
    def percentage(self):
        self.total_marks = self.language_arts+self.maths+self.social+self.french
        self.total_marks_with100 = self.total_marks*100
        self.percent = self.total_marks_with100/400
        label_10["text"]=str(self.percent)

obj_3 = Grade_3(90, 90)
obj_5 = Grade_5(90, 90,53)
obj_10 = Grade_10(90, 23,76,43)

btn3 = Button(root,text="Grade 3",command=obj_3.percentage)
btn3.place(relx=0.5,rely=0.2,anchor=CENTER)
label_3.place(relx=0.5,rely=0.3,anchor=CENTER)

btn5 = Button(root,text="Grade 5",command=obj_5.percentage)
btn5.place(relx=0.5,rely=0.4,anchor=CENTER)
label_5.place(relx=0.5,rely=0.5,anchor=CENTER)

btn10 = Button(root,text="Grade 10",command=obj_10.percentage)
btn10.place(relx=0.5,rely=0.6,anchor=CENTER)
label_10.place(relx=0.5,rely=0.7,anchor=CENTER)

root.mainloop()