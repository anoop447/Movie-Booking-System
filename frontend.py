from tkinter import *
import tkinter.messagebox


class Movie:

    def __init__(self, root):
        self.root=root
        self.root.title('Movie Booking System')
        self.root.geometry('1350x750')
        self.root.config(bg="black")

        #Fraames
        MainFrame = Frame(self.root,bg='black')
        MainFrame.grid()

        HeadFrame = Frame(MainFrame,bd=1,bg='black',relief=RIDGE,padx=50,pady=10)
        HeadFrame.pack(side=TOP)

        self.TFrame=Label(HeadFrame, font=('Arial', 50, 'bold'), text="MOVIE BOOKING SYSTEM", bg="black", fg="red")
        self.TFrame.grid() 

        BottomFrame=Frame(MainFrame, bd=2, width=1350, height=70, padx=18, pady=10, bg="black", relief=RIDGE)
        BottomFrame.pack(side=BOTTOM)

        BodyFrame=Frame(MainFrame, bd=2, width=1300, height=500, padx=20, pady=20, bg="black", relief=RIDGE)
        BodyFrame.pack(side=BOTTOM)

        LeftBody=LabelFrame(BodyFrame, bd=2, width=700, height=480, padx=20, bg="black", relief=RIDGE, font=('Arial', 15, 'bold'),text='Movie info:\n',fg='white')
        LeftBody.pack(side=LEFT)

        RightBody=LabelFrame(BodyFrame, bd=2, width=350, height=480, padx=31, pady=3, bg="black", relief=RIDGE, font=('Arial', 15, 'bold'),text='Movie Details:\n',fg='white')
        RightBody.pack(side=RIGHT)



if __name__=='__main__':
	root=Tk()
	database = Movie(root)
	root.mainloop()