from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox

# Message button to save survey
def asksurvey():
    if messagebox.askokcancel("Saving survey", "Do you want to save survey?"):
        savedata(hole_id, depth, azimuth, dip)

def savedata(hole_id, depth, azimuth, dip):
	con = sqlite3.connect('logging_database')
	cur = con.cursor()
	myList = [hole_id.get(), depth.get(), azimuth.get(), dip.get()]
	cur.execute('INSERT INTO Survey(HoleID, Depth, Azimuth, Dip) VALUES (?,?,?,?)', myList)
	con.commit() 


def close_coord():
	exit()

window = Tk()
window.title("Downhole survey")
window.geometry("500x400")

root = Frame()
root.grid()

# Setting the variables for this window

hole_id = StringVar()
depth = DoubleVar()
azimuth = DoubleVar()
dip = DoubleVar()

# Label and placing the variables in the window
hole_id_label = Label(root, text="Hole Id").grid(row=0, column=1, sticky=W)
depth_label = Label(root, text="Depth").grid(row=1, column=1, sticky=W)
azimuth_label = Label(root, text="Azimuth").grid(row=2, column=1, sticky=W)
dip_label = Label(root, text="Dip").grid(row=3, column=1, sticky=W)

# Placing the entries for the variables

hole_id_entry = Entry(root, width=10, textvariable=hole_id)
hole_id_entry.grid(row=0, column=2)
depth_entry = Entry(root, width=10, textvariable=depth)
depth_entry.grid(row=1, column=2)
azimuth_entry = Entry(root, width=10, textvariable=azimuth)
azimuth_entry.grid(row=2, column=2)
dip_entry = Entry(root, width=10, textvariable=dip)
dip_entry.grid(row=3, column=2)

hole_id_entry.focus()

save = Button(root, text="Save", command=asksurvey)
save.grid(row=5, column=2)
closing = Button(root, text="Back", command=close_coord)
closing.grid(row=5, column=3)



window.mainloop()
