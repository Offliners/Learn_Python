from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd

window = Tk()
window.geometry("350x350")
window.title("Personal Tool")
window.configure(background='Black')

file = None
label_style = {"bg":"black","fg":"white","font":"-size 30 -weight bold"}
button_style1 = {"bg":"white","fg":"black","font":"-size 15 -weight bold"}
button_style2 = {"bg":"white","fg":"black","font":"-size 15 -weight bold"}

def browse():
    global file
    file = filedialog.askopenfilename(filetypes=(("File","*.csv"),("All Files","*.*")))

def convert():
    try:
        xlsx = file.replace(".csv",".xlsx")
        read_file = pd.read_csv(file)
        read_file.to_excel(xlsx,index=None,header=True)
        messagebox.showinfo("Success!","File converted and saved!")
    except:
        messagebox.showerror("Error!","Error!")

label = Label(window,text="Personal Tool",**label_style)
button1 = Button(window,text="Choose a CSV file",command=browse,**button_style1)
button2 = Button(window,text="Convert CSV to xlsx",command=convert,**button_style2)
label.place(x = 50,y = 50)
button1.place(x = 85,y = 130)
button2.place(x = 85,y = 190)
window.mainloop()
