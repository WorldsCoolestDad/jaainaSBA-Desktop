from tkinter import *
# from typing import Sized


#mycursor.execute("CREATE TABLE CompletedJobs (jobid int PRIMARY KEY AUTO_INCREMENT, jobdate DATE, client VARCHAR(50),"
#                "buyer VARCHAR(50), platform VARCHAR(25), pay DECIMAL(6,2))")#mycursor.execute("DESCRIBE CompletedJobs")
# for x in mycursor:
#     print(x)
# income = Income("7/12/2021", "Iberia Bank", "Core Tech", "WM", "234.00")
# income.save_records()
# income.get_records()

#Define window dimensions and calculate center of screen position
ja = Tk()
ja.geometry("800x150+300+200")
width_of_screen= ja.winfo_screenwidth()
height_of_screen= ja.winfo_screenheight()
window_width = 800
window_height = 500
x_coor = (width_of_screen/2) - (window_width/2)
y_coor = (height_of_screen/2) - (window_height/2)
ja.title("Ja'Aina-SBA")

#Display section title
input_title_frame = Frame(ja, height=20,  bg="grey")
input_title_label=Label(input_title_frame, text="Record Input", fg="white",font="Times 10", bg="grey")
title_length= len(input_title_label['text'])
pad_length = (window_width/2) - (title_length * 3)
input_title_label.grid(row=0, column=0, padx=pad_length)
input_title_frame.grid(row=0, column=0)

#Display input fields headers
input_headers_frame = Frame(ja)
date_header = Label(input_headers_frame, text="Date",fg="blue")
date_header.grid(row=0, column=0, padx=(50,100))
client_header = Label(input_headers_frame, text="Client",fg="blue")
client_header.grid(row=0, column=1, padx=(0,0))
buyer_header = Label(input_headers_frame, text="Buyer", fg="blue")
buyer_header.grid(row=0, column=2, padx=(110,0))
platform_header = Label(input_headers_frame, text="Platform", fg="blue")
platform_header.grid(row=0, column=3, padx=(100,100))
pay_header = Label(input_headers_frame, text="Pay",fg="blue")
pay_header.grid(row=0, column=4, padx=(20,80))
input_headers_frame.grid(row=1, column=0)

#display entry boxes
entry_boxes_frame= Frame(ja, height=30, width=window_width- 10, relief=SOLID)
date_entry = Entry(entry_boxes_frame)
date_entry.grid(row=0, column=0)
client_entry = Entry(entry_boxes_frame)
client_entry.grid(row=0, column=1, padx=(20,0))
buyer_entry = Entry(entry_boxes_frame)
buyer_entry.grid(row=0, column=2, padx=(20,0))
platform_entry = Entry(entry_boxes_frame)
platform_entry.grid(row=0, column=3, padx=(25,0))
pay_entry = Entry(entry_boxes_frame)
pay_entry.grid(row=0, column=4, padx=(25,25))
entry_boxes_frame.grid(row=2,column=0)

#display buttons
button_frame = Frame(ja)
clear_button = Button(button_frame, text="Clear All", font="12", relief=RAISED)
clear_button.grid(row=0, column=0, padx=(0,20), pady=(20,0))
save_button = Button(button_frame, text="Save Record", font="12", relief=RAISED)
save_button.grid(row=0, column=1, pady=(20,0))
button_frame.grid(row=3, column=0)

ja.mainloop()
