import tkinter as tk
from tkinter import ttk,messagebox

win=tk.Tk()
win.title("Exception")
win.geometry("300x200")

# Label Frame
label_frame=ttk.LabelFrame(win,text="Exception Handling")
label_frame.grid(row=0,column=0,padx=40,pady=10)

# labels
label_name=ttk.Label(label_frame,text='Enter Your name',font=('italic',10,'bold'))
label_age=ttk.Label(label_frame,text='Enter Your age',font=('italic',10,'bold'))


# Enterbox
name_var=tk.StringVar()
age_var=tk.StringVar()

entry_name=ttk.Entry(label_frame,width=36,textvariable=name_var)
entry_age=ttk.Entry(label_frame,width=36,textvariable=age_var)

# Grid

label_name.grid(row=0,column=0,padx=5,pady=5,sticky=tk.W)
label_age.grid(row=0,column=1,padx=5,pady=5,sticky=tk.W)
entry_name.grid(row=1,column=0,padx=5,pady=5,sticky=tk.W)
entry_age.grid(row=1,column=1,padx=5,pady=5,sticky=tk.W)

#Submit

def Submit():
    name=name_var.get()
    age=age_var.get()
    if name=='' and age=='':messagebox.showwarning('Error','Enter Both the  Inputs')
    elif name=='' and age!='':messagebox.showwarning('Error','Enter Name')
    elif name!='' and age=='':messagebox.showwarning('Error','Enter Age')
    else:
        try:
            age=int(age)
            print(f"User's name is {name},and age is {age}")
        except ValueError:
                messagebox.showerror("Error",'Enter Valid Age')

submit=ttk.Button(win,text='Submit',command=Submit)
submit.grid(row=2,columnspan=2,padx=40)





win.mainloop()