from tkinter.constants import BOTTOM, TOP
import qrcode
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import ttk, Toplevel, Label, PhotoImage
from tkinter.messagebox import askyesno, showerror, showwarning, showinfo

import Database as db

def retrive():
    if id.get() == '':
        showerror('ID not found', 'Please Enter a ID')
    else:
        student_info = db.Student(id.get(), name.get(), institution.get(), stream.get(), event.get(), ph_num.get())
        readProgress = student_info.csvRead(id.get())
        
        if readProgress == "ID not Found":
            showwarning("Data not Found", "Data with the given ID \n is not available.")
        else:
            str = f'Student ID: {readProgress[0]}\nName: {readProgress[1]}\nInstitution: {readProgress[2]}\nStream: {readProgress[3]}\nEvent: {readProgress[4]}\nPhone Number: {readProgress[5]}'
            showinfo("Information", f'Data Found:\n' + str)
            qr_code(str)

def qr_popup():
    top = Toplevel(form)
    top.geometry("720x720")
    top.title("QR Code")
    top['background'] = '#3d3d3d'
    title = ttk.Label(top, text="QR-Code", background = '#3d3d3d', foreground = 'white', font=("Helvetica", 26))
    title.pack(padx = 30, pady = 30)

    src = "D:\Internships\TopTrove\Project\Files\Pics\QR_Data.png"
    img = Image.open(src)
    r_img = img.resize((500, 500))
    img = ImageTk.PhotoImage(r_img)
    qr = Label(top, image = img)
    qr.photo = img
    qr.pack(padx = 25, pady = 25)

    exit_button = ttk.Button(top, text="Exit", command = top.destroy)
    exit_button.pack(padx = 15, pady = 15, expand = True)

def qr_code(str):
    img = qrcode.make(str)
    type(img)  # qrcode.image.pil.PilImage
    img.save("D:\Internships\TopTrove\Project\Files\Pics\QR_Data.png")
    qr_popup()

def confirm():
    if id.get() == '' or name.get() == '' or institution.get() == '' or stream.get() == '' or event.get() == '' or ph_num.get() == '':
        showerror('Empty fields', 'Please Enter all Information')
    else:
        str = f'Student ID: {id.get()}\nName: {name.get()}\nInstitution: {institution.get()}\nStream: {stream.get()}\nEvent: {event.get()}\nPhone Number: {ph_num.get()}'
        answer = askyesno('Confirmation', 'Is Below Information Correct:\n' + str)

        if answer:
            student_info = db.Student(id.get(), name.get(), institution.get(), stream.get(), event.get(), ph_num.get())
            writeProgress = student_info.csvWrite()
            if writeProgress == "Data already exists":
                showerror("Data already exists", "Data for with same ID \nalready exists")
            else:
                qr_code(str)

        clear_text()

def clear_text():
    id_entry.delete('0', "end")
    name_entry.delete('0', "end")
    institution_entry.delete('0', "end")
    stream_entry.delete('0', "end")
    event_entry.delete('0', "end")
    ph_num_entry.delete('0', "end")


form = tk.Tk()
form.title("Database Entry")
form['background'] = '#3d3d3d'

window_width = 500
window_height = 550

# get the screen dimension
screen_width = form.winfo_screenwidth()
screen_height = form.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
form.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
form.iconbitmap('D:\Internships\TopTrove\Project\Files\Pics\R_logo.ico')

# configure the grid
form.columnconfigure(0, weight=1)
form.columnconfigure(1, weight=1)

title = ttk.Label(form, text="Student Entry Form", background = '#3d3d3d', foreground = 'white', font=("Helvetica", 24))
title.grid(row = 0, sticky=tk.N, padx = 15, pady = 15, columnspan = 50)



# store input in variables
id = tk.StringVar()
name = tk.StringVar()
institution = tk.StringVar()
stream = tk.StringVar()
event = tk.StringVar()
ph_num = tk.StringVar()

# Studet ID
id_label = ttk.Label(form, text="Student ID:", background = '#3d3d3d', foreground = 'white', font=("Helvetica", 18))
id_label.grid(column = 0, row = 1, sticky=tk.W, padx = 15, pady = 15)

id_entry = ttk.Entry(form, textvariable = id, font = ("Helvetica", 18))
id_entry.grid(column = 1, row = 1, sticky=tk.E, padx = 15, pady = 15)
id_entry.focus()

# Name
name_label = ttk.Label(form, text="Name:", background = '#3d3d3d', foreground = 'white', font=("Helvetica", 18))
name_label.grid(column = 0, row = 2, sticky=tk.W, padx = 15, pady = 15)

name_entry = ttk.Entry(form, textvariable = name, font = ("Helvetica", 18))
name_entry.grid(column = 1, row = 2, sticky=tk.E, padx = 15, pady = 15)

# Instutution
institution_label = ttk.Label(form, text="Instutution:", background = '#3d3d3d', foreground = 'white', font=("Helvetica", 18))
institution_label.grid(column = 0, row = 3, sticky=tk.W, padx = 15, pady = 15)

institution_entry = ttk.Entry(form, textvariable = institution, font = ("Helvetica", 18))
institution_entry.grid(column = 1, row = 3, sticky=tk.E, padx = 15, pady = 15)
institution_entry.focus()

# Stream
stream_label = ttk.Label(form, text="Stream:", background = '#3d3d3d', foreground = 'white', font=("Helvetica", 18))
stream_label.grid(column = 0, row = 4, sticky=tk.W, padx = 15, pady = 15)

stream_entry = ttk.Entry(form, textvariable = stream, font = ("Helvetica", 18))
stream_entry.grid(column = 1, row = 4, sticky=tk.E, padx = 15, pady = 15)

# Event
event_label = ttk.Label(form, text="Event:", background = '#3d3d3d', foreground = 'white', font=("Helvetica", 18))
event_label.grid(column = 0, row = 5, sticky=tk.W, padx=15, pady=15)

event_entry = ttk.Entry(form, textvariable = event, font = ("Helvetica", 18))
event_entry.grid(column = 1, row = 5, sticky=tk.E, padx=15, pady=15)
event_entry.focus()

# Phone Number
ph_num_label = tk.Label(form, text="Phone Number:", background = '#3d3d3d', foreground = 'white', font=("Helvetica", 18))
ph_num_label.grid(column = 0, row = 6, sticky=tk.W, padx=15, pady=15)

ph_num_entry = ttk.Entry(form, textvariable = ph_num, font = ("Helvetica", 18))
ph_num_entry.grid(column = 1, row = 6, sticky=tk.E, padx=15, pady=15)

# QR button
confirm_button = ttk.Button(form, text="Confirm", command = confirm)
confirm_button.grid(column = 0, row = 7, sticky=tk.S, padx=15, pady=15)

# Retrivel button
retrive_button = ttk.Button(form, text="Retrieve", command = lambda : retrive())
retrive_button.grid(column = 1, row = 7, sticky=tk.S, padx=15, pady=15)

# Clear button
clear_button = ttk.Button(form, text="Clear", command = clear_text)
clear_button.grid(column = 0, row = 8, sticky=tk.S, padx=15, pady=15)

# Exit button
exit_button = ttk.Button(form, text="Exit", command = form.quit)
exit_button.grid(column = 1, row = 8, sticky=tk.S, padx=15, pady=15)


form.mainloop()
