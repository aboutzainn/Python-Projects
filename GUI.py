import tkinter as tk
from tkinter import ttk

win=tk.Tk()
win.title('Project IGI')
win.geometry('300x300')
win.minsize(200,200)

#Labels
name_label=ttk.Label(win,text='Enter your Name')
name_label.grid(row=0,column=0)

age_label=ttk.Label(text='Enter your Age')
age_label.grid(row=1,column=0,sticky=tk.W)

email_label=ttk.Label(text='Enter your email')
email_label.grid(row=2, column=0)

gender_label=ttk.Label(win,text='Select Gender')
gender_label.grid(row=3,column=0,sticky=tk.W)

#Entryboxes

name_var=tk.StringVar()
name_entrybox=ttk.Entry(win,width=16,textvariable=name_var)
name_entrybox.grid(row=0 ,column=1)
name_entrybox.focus()

age_var=tk.StringVar()
age_entrybox=ttk.Entry(win,width=16,textvariable=age_var)
age_entrybox.grid(row=1 ,column=1)

email_var=tk.StringVar()
email_entrybox=ttk.Entry(win,width=16,textvariable=email_var)
email_entrybox.grid(row=2 ,column=1)

#Combobox
gender_var=tk.StringVar()
gender_combobox=ttk.Combobox(win,width=12,textvariable=gender_var,state='readonly')
gender_combobox['values']=('Male','Female','Other')
gender_combobox.current(0)
gender_combobox.grid(row=3,column=1 ,sticky=tk.W)

#RadioButton
Radio_choice=tk.StringVar()
radio1=ttk.Radiobutton(win,text='Student',value='Student',variable=Radio_choice)
radio1.grid(row=4,column=0)

radio2=ttk.Radiobutton(win,text='Teacher',value='Teacher',variable=Radio_choice)
radio2.grid(row=4,column=1)

#CheckButton
checkbutton=tk.IntVar()
check_button=ttk.Checkbutton(win,text='Mark if you subsribed my channel',variable=checkbutton)
check_button.grid(row=5,columnspan=3)

#Submit
def action():
    username=name_var.get()
    userage=age_var.get()
    user_email=email_var.get()
    gender=gender_combobox.get()
    radio=Radio_choice.get()
    if checkbutton.get()==0:
        subscribed="NOT Subscribed"
    else:subscribed="Subscribed"
    with open('file.txt','a') as f:
        f.write(f'{username},{userage},{user_email}, {gender}, {radio} , {subscribed}')
    
    #Clear inputs after submit
    name_entrybox.delete(0,tk.END)
    age_entrybox.delete(0,tk.END)
    email_entrybox.delete(0,tk.END)
    gender_combobox.delete(0,tk.END)
    # radio1.delete(0,tk.END)
    # radio2.delete(0,tk.END)
    name_label.configure(foreground="Blue")

    print(f"Username is {username}, Gender is {gender} and age is {userage} and {radio}")
    print(f"email id is {user_email} and channel is {subscribed}")
    
submit_button=ttk.Button(win,text='Submit' ,command=action)
submit_button.grid(sticky=tk.W)

#END
win.mainloop()