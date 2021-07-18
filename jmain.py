import tkinter as tk
from jpacks.income import Income
from jpacks.dbconnect import *


#db = connect_to_db()
#mycursor = db.cursor()
#mycursor.execute("CREATE TABLE CompletedJobs (jobid int PRIMARY KEY AUTO_INCREMENT, jobdate DATE, client VARCHAR(50),"
#                "buyer VARCHAR(50), platform VARCHAR(25), pay DECIMAL(6,2))")#mycursor.execute("DESCRIBE CompletedJobs")
#for x in mycursor:
#    print(x)


income = Income("7/12/2021", "Iberia Bank", "Core Tech", "WM", "234.00")
window = tk.Tk()
window.title('JaAinaSBA')
window.geometry("600x400")

label1 = tk.Label(text=income.display_records(), fg='blue')
label1.pack()
window.mainloop()
