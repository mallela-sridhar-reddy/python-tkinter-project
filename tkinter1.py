from tkinter import *
import pymysql

window = Tk()
#database connection
connection = pymysql.connect(host="localhost", user="root", passwd="", database="tkinterdb")
cursor = connection.cursor()

window.title("Besant Technologies")
window.geometry("700x500")
window.config(bg="light blue")
varReg = IntVar()
varEnqui = IntVar()
f = open("newstudentdetails.txt", "w")
f.write("Date \t")
f.write("Name \t")
f.write("Mobile No \t")
f.write("Alternate No \t")
f.write("Email Id \t")
f.write("Address \t")
f.write("Course Intended \t")
f.write("Batch Preffered \t")
f.write("HYCKAU \t")
f.write("EorF \t")
f.write("Contact \t")
f.write("Counselor \t")
f.write("Fees \t")
f.write("Comment \n")
f.close()
def messageshow():
    f = open("newstudentdetails.txt", "a")
    f.write(first.get() + "\t")
    f.write(second.get() + "\t")
    f.write(third.get() + "\t")
    f.write(fourth.get() + "\t")
    f.write(fifth.get() + "\t")
    f.write(sixth.get() + "\t")
    f.write(seventh.get() + "\t")
    f.write(eighth.get() + "\t")
    f.write(ninth.get() + "\t")
    f.write(tenth.get() + "\t")
    f.write(eleventh.get() + "\t")
    f.write(twelfth.get() + "\t")
    f.write(thirteenth.get() + "\t")
    f.write(fourteenth.get() + "\n")
    f.close()
    record1 = "INSERT INTO StudentsTable(Date,Name,Mobile_No,Alternate_No,Email_Id,Address,Course_Intended,Batch_Preffered,How_You_Come_To_Know_Us,Are_You_Experienced_Or_Fresher,Contact_Person_From_Besant,Counselor,Fees,Comment) VALUES('"+first.get()+"','"+second.get()+"','"+third.get()+"','"+fourth.get()+"','"+fifth.get()+"','"+sixth.get()+"','"+seventh.get()+"','"+eighth.get()+"','"+ninth.get()+"','"+tenth.get()+"','"+eleventh.get()+"','"+twelfth.get()+"','"+thirteenth.get()+"','"+fourteenth.get()+"');"
    cursor.execute(record1)
    connection.commit()
    print("Data Inserted Successfully")
    connection.close()

def clicked(value):
    """myLabel = Label(window, text=value)
    myLabel.grid()"""
user_text = Text(window,height=2,foreground="red",bg="snow",width=17,border=0,font="Arial 9")
user_text.grid(row=1,column=1)
user_text.insert(END, 'Besant Technologies  Enquiry Form')
Label(window, text='Date:',bg="light blue").grid(row=2,column=0,sticky="w")
Label(window, text='Name:',bg="light blue").grid(row=3,column=0,sticky="w")
Label(window, text='Mobile No:',bg="light blue").grid(row=4,column=0,sticky="w")
Label(window, text='Alternate No:',bg="light blue").grid(row=5,column=0,sticky="w")
Label(window, text='Email Id:',bg="light blue").grid(row=6,column=0,sticky="w")
Label(window, text='Address:',bg="light blue").grid(row=7,column=0,sticky="w")
Label(window, text='Course Intended:',bg="light blue").grid(row=8,column=0,sticky="w")
Label(window, text='Batch Preffered:',bg="light blue").grid(row=9,column=0,sticky="w")
Label(window, text='How You Come To Know Us:',bg="light blue").grid(row=10,column=0,sticky="w")
Label(window, text='Are You Experienced Or Fresher:',bg="light blue").grid(row=11,column=0,sticky="w")
Label(window, text='Contact Person From Besant Technologies:',bg="light blue").grid(row=12,column=0,sticky="w")
Label(window, text='Counselor:',bg="light blue").grid(row=13,column=0,sticky="w")
Label(window, text='Fees:',bg="light blue").grid(row=14,column=0,sticky="w")
Label(window, text='Comment:',bg="light blue").grid(row=15,column=0,sticky="w")
first = Entry(window,width=50)
second = Entry(window,width=50)
third = Entry(window,width=50)
fourth = Entry(window,width=50)
fifth = Entry(window,width=50)
sixth = Entry(window,width=50)
seventh = Entry(window,width=50)
eighth = Entry(window,width=50)
ninth = Entry(window,width=50)
tenth = Entry(window,width=50)
eleventh = Entry(window,width=50)
twelfth = Entry(window,width=50)
thirteenth = Entry(window,width=50)
fourteenth = Entry(window,width=50)
first.grid(row=2,column=1)
second.grid(row=3,column=1)
third.grid(row=4,column=1)
fourth.grid(row=5,column=1)
fifth.grid(row=6,column=1)
sixth.grid(row=7,column=1)
seventh.grid(row=8,column=1)
eighth.grid(row=9,column=1)
ninth.grid(row=10,column=1)
tenth.grid(row=11,column=1)
eleventh.grid(row=12,column=1)
twelfth.grid(row=13,column=1)
thirteenth.grid(row=14,column=1)
fourteenth.grid(row=15,column=1)
Checkbutton(window, text='Enquiry', variable=varEnqui,command=lambda:clicked(varEnqui.get())).grid(row=16,column=1,sticky="w")
Checkbutton(window, text='Registration', variable=varReg,command=lambda:clicked(varReg.get())).grid(row=16,column=1)
button = Button(window, text='Submit', width=5,bg="green", command=messageshow)
button.grid(row=17,column=1,sticky="w")
button = Button(window, text='Quit', width=5,bg="red", command=window.quit)
button.grid(row=17,column=1)
window.mainloop()
