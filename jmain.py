from tkinter import *
from typing import Sized
from jpacks.income import Income
from jpacks.dbconnect import *


#db = connect_to_db()
#mycursor = db.cursor()
#mycursor.execute("CREATE TABLE CompletedJobs (jobid int PRIMARY KEY AUTO_INCREMENT, jobdate DATE, client VARCHAR(50),"
#                "buyer VARCHAR(50), platform VARCHAR(25), pay DECIMAL(6,2))")#mycursor.execute("DESCRIBE CompletedJobs")
#for x in mycursor:
#    print(x)
#income = Income("7/12/2021", "Iberia Bank", "Core Tech", "WM", "234.00")
def min_screen():
    ja.overrideredirect(0)
    ja.iconify()
   


ja = Tk()
#print(ja.keys())
width_of_window= 800
height_of_window = 400
screen_width = ja.winfo_screenwidth()
screen_height = ja.winfo_screenheight()
x_coor = (screen_width/2) - (width_of_window/2)
y_coor = (screen_height/2) - (height_of_window/2)
ja.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window, x_coor, y_coor))
ja.title("Ja'Aina-SBA")

input_title_frame = Frame(ja)
input_title_label=Label(input_title_frame, text="Record Input", padx=365, fg="white",font="Times 10", bg="grey")
input_title_label.pack()
input_title_frame.grid(row=0, column=0)

input_headers_frame = Frame(ja)
date_header = Label(input_headers_frame, text="Date", padx=50,fg="blue")
date_header.grid(row=0, column=0)
client_header = Label(input_headers_frame, text="Client", padx=50,fg="blue")
client_header.grid(row=0, column=1)
buyer_header = Label(input_headers_frame, text="Buyer", padx=50, fg="blue")
buyer_header.grid(row=0, column=2)
platform_header = Label(input_headers_frame, text="Platform", padx=50, fg="blue")
platform_header.grid(row=0, column=3)
pay_header = Label(input_headers_frame, text="Pay", padx=50,fg="blue")
pay_header.grid(row=0, column=4)
input_headers_frame.grid(row=1, column=0)

ja.mainloop()
