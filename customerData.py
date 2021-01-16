from tkinter import *
import tkinter.messagebox
import database
import tickets

class Custm:

    def __init__(self, root):
        self.root=root
        self.root.title('Movie Booking System')
        self.root.geometry('1350x750')
        self.root.config(bg="black")


        def clcdata():
            self.txtCustom_id.delete(0,END)
            self.txtCustom_name.delete(0,END)
            self.txtCustom_email.delete(0,END)
            self.txtCustom_phno.delete(0,END)
           

        

        Custom_id = StringVar()
        Custom_name = StringVar()
        Custom_email = StringVar()
        Custom_phno = StringVar()

        MainFrame = Frame(self.root,bg='black')
        MainFrame.grid()


        HeadFrame = Frame(MainFrame,bd=1,bg='black',relief=RIDGE,padx=50,pady=10)
        HeadFrame.pack(side=TOP)

        self.TFrame=Label(HeadFrame, font=('Arial', 50, 'bold'), text="MOVIE TICKET BOOKING SYSTEM", bg="black", fg="red")
        self.TFrame.grid()

        BottomFrame=Frame(MainFrame, bd=2, width=1350, height=70, padx=18, pady=10, bg="black", relief=RIDGE)
        BottomFrame.pack(side=BOTTOM)

        BodyFrame=Frame(MainFrame, bd=2, width=1300, height=500, padx=20, pady=20, bg="black", relief=RIDGE)
        BodyFrame.pack(side=BOTTOM)

        LeftBody=LabelFrame(BodyFrame, bd=2, width=1000, height=480, padx=20, bg="black", relief=RIDGE, font=('Arial', 15, 'bold'),text='Customer info:\n',fg='white')
        LeftBody.pack()


        self.lblCustom_id=Label(LeftBody, font=('Arial', 18, 'bold'), text="Customer ID:", padx=2, pady=2, bg="black", fg="orange")
        self.lblCustom_id.grid(row=0, column=0, sticky=W)
        self.txtCustom_id=Entry(LeftBody, font=('Arial', 18, 'bold'), textvariable=Custom_id, width=39, bg="black", fg="white")
        self.txtCustom_id.grid(row=0, column=1)

        self.lblCustom_name=Label(LeftBody, font=('Arial', 18, 'bold'), text="Customer Name:", padx=2, pady=2, bg="black", fg="orange")
        self.lblCustom_name.grid(row=1, column=0, sticky=W) 
        self.txtCustom_name=Entry(LeftBody, font=('Arial', 18, 'bold'), textvariable=Custom_name, width=39, bg="black", fg="white")
        self.txtCustom_name.grid(row=1, column=1)

        self.lblCustom_email=Label(LeftBody, font=('Arial', 18, 'bold'), text="Customer Email:", padx=2, pady=2, bg="black", fg="orange")
        self.lblCustom_email.grid(row=2, column=0, sticky=W) 
        self.txtCustom_email=Entry(LeftBody, font=('Arial', 18, 'bold'), textvariable=Custom_email, width=39, bg="black", fg="white")
        self.txtCustom_email.grid(row=2, column=1)

        self.lblCustom_phno=Label(LeftBody, font=('Arial', 18, 'bold'), text="Customer Phno:", padx=2, pady=2, bg="black", fg="orange")
        self.lblCustom_phno.grid(row=3, column=0, sticky=W) 
        self.txtCustom_phno=Entry(LeftBody, font=('Arial', 18, 'bold'), textvariable=Custom_phno, width=39, bg="black", fg="white")
        self.txtCustom_phno.grid(row=3, column=1)

        self.btnadd=Button(BottomFrame, text="Add", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="orange")
        self.btnadd.grid(row=0, column=0)

        self.btnclear=Button(BottomFrame, text="Clear", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="orange",command=clcdata)
        self.btnclear.grid(row=0, column=1)

        self.btnnext=Button(BottomFrame, text="Next", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="orange",command=lambda:self.openTicketsInfo()) # if wanted (Mainframe) as args
        self.btnnext.grid(row=0, column=2)

    def openTicketsInfo(self):
        
        #frame.grid_forget()
        top = Toplevel()
        tickets.Ticket(top)



if __name__=='__main__':
	root=Tk()
	database = Custm(root)
	root.mainloop()