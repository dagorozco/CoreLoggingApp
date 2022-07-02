from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

def askcollar():
        if messagebox.askokcancel("Saving collar", "Do you want to save collar?"):
                savedata(hole_id, eoh, zone, minesite, prop, units, h_type, date, selected_loggeo, selected_plangeo, log_type, recovery)

def savedata(hole_id, eoh, zone, minesite, prop, units, h_type, date, logged, planned, log_type, recovery):
	con = sqlite3.connect('database_name.db')
	cur = con.cursor()
	myList = [hole_id.get(), eoh.get(), zone.get(), minesite.get(), prop.get(), units.get(), h_type.get(), date.get(), selected_loggeo, selected_plangeo, log_type.get(), recovery.get()]
	cur.execute('INSERT INTO Collar(HoleID, EOH, Zone, Minesite, Property, Units, Hole_type, Date, Logger, Planned, LOGTYPE, Recovery) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)', myList)
	con.commit() 

	
def close_program():
	exit()


# lista de las opciones para radiobuttons
unit_choices = {'meters':'Meters', 'feet':'Feet'}
type_choices = {'core':'Core', 'rc':'RC'}

window = Tk()
window.title("Adding new hole")
window.geometry("400x400")

frame = Frame()
frame.grid()

# choices for list
loggeo_choices = ('Geo1', 'Geo2', 'Geo3')
plangeo_choices = ('Geo1', 'Geo2', 'Geo3')

# Defining the variables
hole_id = StringVar()
eoh = DoubleVar()
zone = IntVar()
minesite = StringVar()
prop = StringVar()
units = StringVar()
h_type = StringVar()
date = StringVar()
loggeo = StringVar(value=loggeo_choices)
plangeo = StringVar(value=plangeo_choices)
recovery = DoubleVar()
log_type = StringVar(frame, value='Exploration')

# return the planning geo and logger geo
selected_loggeo = None
def logselect(*args):
	global selected_loggeo
	idx = int(log.curselection()[0])
	selected_loggeo = loggeo_choices[idx]

selected_plangeo = None
def planselect(*args):
	global selected_plangeo
	idx = int(plan.curselection()[0])
	selected_plangeo = plangeo_choices[idx]

# Creating the labels for the variables
label_hole_id = Label(frame, text="Hole Name:").grid(row=1, column=0, sticky=W)
label_eoh = Label(frame, text="EOH:").grid(row=5, column=0, sticky=W)
label_zone = Label(frame, text="Zone:").grid(row=4, column=0, sticky=W)
label_units = Label(frame, text="Units:").grid(row=1, column=5, sticky=W)
label_minesite = Label(frame, text="Minesite:").grid(row=2, column=0, sticky=W)
label_prop = Label(frame, text="Property:").grid(row=3, column=0, sticky=W)
label_h_type = Label(frame, text="Hole Type:").grid(row=4, column=5, sticky=E)
label_date = Label(frame, text="Date:").grid(row=6, column=0, sticky=W)
label_loggeo = Label(frame, text="Logged by:").grid(row=7, column=0, sticky=W)
label_plangeo = Label(frame, text="Planned by:").grid(row=9, column=0, sticky=W)
label_recovery = Label(frame, text="Recovery:").grid(row=10, column=0, sticky=W)
label_logtype = Label(frame, text="Log Type:").grid(row=11, column=0, sticky=W)




# Setting up the entries for the variables
entry_hole = Entry(frame, width=10, textvariable=hole_id)
entry_minesite = Entry(frame, width=10, textvariable=minesite)
entry_prop = Entry(frame, width=10, textvariable=prop)
entry_zone = Entry(frame, width=10, textvariable=zone)
entry_eoh = Entry(frame, width=10, textvariable=eoh)
entry_date = Entry(frame, width=10, textvariable=date)
entry_recovery = Entry(frame, width=10, textvariable=recovery)
entry_logtype = Entry(frame, width=10, textvariable=log_type)

# Setting the loggeo and plangeo listboxes
log = Listbox(frame, listvariable=loggeo, height=1, width=12)
log.grid(row=7, column=1, rowspan=8, sticky=N)
plan = Listbox(frame, listvariable=loggeo, height=1, width=12)
plan.grid(row=9, column=1, rowspan=8, sticky=N)

# Placing the entries onto the window
entry_hole.grid(row=1, column=1, sticky=W)
entry_minesite.grid(row=2, column=1, sticky=W)
entry_prop.grid(row=3, column=1, sticky=W)
entry_zone.grid(row=4, column=1, sticky=W)
entry_eoh.grid(row=5, column=1, sticky=W)
entry_date.grid(row=6, column=1, sticky=W)
entry_recovery.grid(row=10, column=1, sticky=W)
entry_logtype.grid(row=11, column=1, sticky=W)

# Creating the radiobutton for units and hole type variables
meters_rb = Radiobutton(frame, text=unit_choices['meters'], variable=units, value='meters')
feet_rb = Radiobutton(frame, text=unit_choices['feet'], variable=units, value='feet')
core_rb = Radiobutton(frame, text=type_choices['core'], variable=h_type, value='core')
rc_rb = Radiobutton(frame, text=type_choices['rc'], variable=h_type, value='rc')

# Placing the radiobuttons onto the window
meters_rb.grid(row=2, column=5, sticky=W)
feet_rb.grid(row=3, column=5, sticky=W)
core_rb.grid(row=5, column=5, sticky=W)
rc_rb.grid(row=6, column=5, sticky=W)

# Makes the cursor to start into the Hole ID entry field
entry_hole.focus() 

log.bind('<<ListboxSelect>>', logselect)
plan.bind('<<ListboxSelect>>', planselect)

button_save = Button(frame, text="Save", command=askcollar)
button_save.grid(row=11, column=4, sticky=W)

button_back = Button(frame, text="Back", command=close_program)
button_back.grid(row=11, column=6, sticky=SE)


window.mainloop()
