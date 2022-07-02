from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

# Messagebutton to save coordinates
def askcoord():
        if messagebox.askokcancel("Save coordinates", "Do you want to save litho?"):
                savecord(hole_id, coordinate_system, easting, northing, elevation, surveyor, Year, Drill_comp, wgs84_zone, other_system)



def savecord(hole_id, coordinate_system, easting, northing, elevation, surveyor, Year, Drill_comp, wgs84_zone, other_system):
	con = sqlite3.connect('database_name.db')
	cur = con.cursor()
	mycord = [hole_id.get(), coordinate_system.get(), easting.get(), northing.get(), elevation.get(), surveyor.get(), Year.get(), Drill_comp.get(), wgs84_zone.get(), other_system.get()]
	cur.execute('INSERT INTO Coordinates(HoleID, Coordinates_system, LocationX, LocationY, LocationZ, LOCCOMP, YEARDRILL, Driller, WGS84_Zone, Other_system) VALUES (?,?,?,?,?,?,?,?,?,?)', mycord)
	con.commit() 

	
def close_coord():
	exit()

coor_choices = {'local':'Local', 'wgs84':'WGS84', 'other':'Other'}

window =Tk()
window.title("Final coordinates")
window.geometry("500x400")

root = Frame()
root.grid()

# Need to add hole Id to create a link to the main table

# Setting up the variables for this window
hole_id = StringVar()
coordinate_system = StringVar()
easting = DoubleVar()
northing = DoubleVar()
elevation = DoubleVar()
surveyor = StringVar()
Year = IntVar()
Drill_comp = StringVar()
wgs84_zone = StringVar() # There is an entry associated with this variable
other_system = StringVar() # There is an entry associated with this variable

# Creating the labels for the variables
hole_label = Label(root, text="Hole Id")
coord_label = Label(root, text="Grid type:")
east_label = Label(root, text="Easting:")
north_label = Label(root, text="Northing")
z_label = Label(root, text="Elevation:")
surveyor_label = Label(root, text="Surveyor")
year_label = Label(root, text="Year drilled:")
wgs84_zone_label = Label(root, text="Zone:")
other_system_label = Label(root, text="Specify:") 
drill_comp_label = Label(root, text="Driller")

# Placing the labels onto the window
hole_label.grid(row=0, column=1, sticky=W)
coord_label.grid(row=1, column=1, sticky=W)
wgs84_zone_label.grid(row=4, column=1, sticky=W)
other_system_label.grid(row=6, column=1, sticky=W)
east_label.grid(row=2, column=14, sticky=E)
north_label.grid(row=3, column=14, sticky=E)
z_label.grid(row=4, column=14, sticky=E)
surveyor_label.grid(row=5, column=14, sticky=E)
year_label.grid(row=6, column=14, sticky=E)
drill_comp_label.grid(row=7, column=14, sticky=E)

# Defining the entries field
hole_entry = Entry(root, width=10, textvariable=hole_id)
wgs84_zone_entry = Entry(root, width=10, textvariable=wgs84_zone, state='disabled')
other_system_entry = Entry(root, width=10, textvariable=other_system, state='disabled')
east_entry = Entry(root, width=10, textvariable=easting)
north_entry = Entry(root, width=10, textvariable=northing)
elevation_entry = Entry(root, width=10, textvariable=elevation)
surveyor_entry = Entry(root, width=10, textvariable=surveyor)
surveyor_entry.insert(0, "CompanyName")
surveyor_entry.config(state='readonly')
year_entry = Entry(root, width=10, textvariable=Year)
drill_comp_entry = Entry(root, width=10, textvariable=Drill_comp)
drill_comp_entry.insert(0, "CompanyName")
drill_comp_entry.config(state='readonly')

# Placing the entries onto the window
hole_entry.grid(row=0, column=2, sticky=W)
wgs84_zone_entry.grid(row=4, column=2, sticky=W)
other_system_entry.grid(row=6, column=2, sticky=W)
east_entry.grid(row=2, column=15, sticky=E)
north_entry.grid(row=3, column=15, sticky=E)
elevation_entry.grid(row=4, column=15, sticky=E)
surveyor_entry.grid(row=5, column=15, sticky=E)
year_entry.grid(row=6, column=15, sticky=E)
drill_comp_entry.grid(row=7, column=15, sticky=E)

# Radiobuttons for grid choices
loc_choice = Radiobutton(root, text=coor_choices['local'], variable=coordinate_system, value='local')
wgs84_choice = Radiobutton(root, text=coor_choices['wgs84'], variable=coordinate_system, value='wgs84')
other_choice = Radiobutton(root, text=coor_choices['other'], variable=coordinate_system, value='other')

# Placing the radiobuttons on the screen
loc_choice.grid(row=2, column=1, sticky=W)
wgs84_choice.grid(row=3, column=1, sticky=W)
other_choice.grid(row=5, column=1, sticky=W)

hole_entry.focus()

saving = Button(root, text="Save", command=askcoord)
closing = Button(root, text="Back", command=close_coord)

saving.grid(row=16, column=4, sticky=W)
closing.grid(row=16, column=10)

window.mainloop()





