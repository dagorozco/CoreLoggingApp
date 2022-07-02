from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3


# Message button to save litho
def asklitho():
	if messagebox.askokcancel("Saving litho", "Do you want to save litho?"):
		saverockdata(hole_id, from_litho, to_litho, selected_rock, selected_color, modifier, rock_desc, litho_unit)

def askstructure():
	if messagebox.askokcancel("Saving Structure", "Do you want to save structure?"):
		savestructure(hole_id, s_depth, angle, s_type)

def asksample1():
	if messagebox.askokcancel("Sampling", "Do you want to save Sample?"):
		s1(hole_id, sample1, from1, to1)

def asksample2():
	if messagebox.askokcancel("Sampling", "Do you want to save Sample?"):
		s2(hole_id, sample2, from2, to2)

def asksample3():
	if messagebox.askokcancel("Sampling", "Do you want to save Sample?"):
		s3(hole_id, sample3, from3, to3)

def asksample4():
	if messagebox.askokcancel("Sampling", "Do you want to save Sample?"):
		s4(hole_id, sample4, from4, to4)

def askqc():
	if messagebox.askokcancel("Sampling", "Do you want to save Duplicate?"):
		quality(hole_id, orig_sample, qc_sample)
def askstd():
        if messagebox.askokcancel("Sampling", "Do you want to save Standard?"):
                std(hole_id, std_sample_id, std_code)
		
def saverockdata(hole_id, from_litho, to_litho, rock, color_sel, modifier, rock_desc, litho_unit):
	con = sqlite3.connect('database_name.db', timeout=3)
	cur = con.cursor()
	myrock = [hole_id.get(), from_litho.get(), to_litho.get(), selected_rock, selected_color, modifier.get(), rock_desc.get(), litho_unit.get()]
	cur.execute('INSERT INTO Lithology(HoleID, From_l, To_l, Rock_code, Color, Modifier, Description, Litho_Unit) VALUES (?,?,?,?,?,?,?,?)', myrock)
	con.commit()

def savestructure(hole_id, s_depth, angle, s_type):
	con = sqlite3.connect('database_name.db')
	cur = con.cursor()
	mystructure = [hole_id.get(), s_depth.get(), angle.get(), s_type.get()]
	cur.execute('INSERT INTO Structures(HoleID, Depth, Angle, Type) VALUES (?,?,?,?)', mystructure)
	con.commit()	

def s1(hole_id, sample1, from1, to1):
	con = sqlite3.connect('database_name.db')
	cur = con.cursor()
	samp1 = [hole_id.get(), sample1.get(), from1.get(), to1.get()]
	cur.execute('INSERT INTO Sampling(HoleID, Sample_ID, Sample_From, Sample_To) Values (?,?,?,?)', samp1)
	con.commit()

def s2(hole_id, sample2, from2, to2):
	con = sqlite3.connect('database_name.db')
	cur = con.cursor()
	samp2 = [hole_id.get(), sample2.get(), from2.get(), to2.get()]
	cur.execute('INSERT INTO Sampling(HoleID, Sample_ID, Sample_From, Sample_To) Values (?,?,?,?)', samp2)
	con.commit()

def s3(hole_id, sample3, from3, to3):
	con = sqlite3.connect('database_name.db')
	cur = con.cursor()
	samp3 = [hole_id.get(), sample3.get(), from3.get(), to3.get()]
	cur.execute('INSERT INTO Sampling(HoleID, Sample_ID, Sample_From, Sample_To) Values (?,?,?,?)', samp3)
	con.commit()

def s4(hole_id, sample4, from4, to4):
	con = sqlite3.connect('database_name.db')
	cur = con.cursor()
	samp4 = [hole_id.get(), sample4.get(), from4.get(), to4.get()]
	cur.execute('INSERT INTO Sampling(HoleID, Sample_ID, Sample_From, Sample_To) Values (?,?,?,?)', samp4)
	con.commit()

def quality(hole_id, original_sample, duplicate_sample):
	con = sqlite3.connect('database_name.db')
	cur = con.cursor()
	quality = [hole_id.get(), orig_sample.get(), qc_sample.get()]
	cur.execute('INSERT INTO QAQC(HoleID, Original_sample, Duplicate) Values (?,?,?)', quality)
	con.commit()

def std(hole_id, std_sample, std_code):
        con = sqlite3.connect('database_name.db')
        cur = con.cursor()
        std = [hole_id.get(), std_sample_id.get(), std_code.get()]
        cur.execute('INSERT INTO Standards(HoleID, Sample_ID, Std_type) Values (?,?,?)', std)
        con.commit()

def calclenght():
	from_r = from_entry.get()
	to_r = to_entry.get()
	try:
		final_lenght = float(to_r) - float(from_r) 
		final_lenght = round(final_lenght, 2)
		lenght_calc.config(text=final_lenght)
	except:
		lenght_calc.config(text="Invalid")

def clear_structure():
	s_type_entry.delete(0, 'end')
	s_depth_entry.delete(0, 'end')
	s_angle_entry.delete(0, 'end')

def clear_litho():
	from_entry.delete(0, 'end')
	from_entry.insert(0, to_entry.get())
	to_entry.delete(0, 'end')
	modifier_entry.delete(0, 'end')
	rock_desc_entry.delete(0, 'end')
	unit_entry.delete(0, 'end')



def close_program():
	exit()

window = Tk()
window.geometry("1100x400")
window.title("Add lithology...(dev. by D. Orozco)")
root = Frame()
root.grid()

#rock types for the listbox
rock_codes = ('rock1', 'rock2', 'rock3', 'rock4','rock5', 'rock6', 'rock7', 'rock8')
color_codes = (' ', 'white', 'beige', 'red')


# Variables
hole_id = StringVar()
from_litho = DoubleVar()
to_litho = DoubleVar()
litho = StringVar(value=rock_codes)
color = StringVar(value=color_codes)
modifier = StringVar()
rock_desc = StringVar()
sample1 = StringVar()
sample2 =StringVar()
sample3 = StringVar()
sample4 = StringVar()
from1 = DoubleVar()
from2 = DoubleVar()
from3 = DoubleVar()
from4 = DoubleVar()
to1 = DoubleVar()
to2 = DoubleVar()
to3 = DoubleVar()
to4 = DoubleVar()
s_depth = DoubleVar()
s_type = StringVar()
angle = IntVar()
qc_sample = StringVar()
orig_sample = StringVar()
lenght = DoubleVar()
litho_unit = StringVar()
std_sample_id = StringVar()
std_code = StringVar(root, value='AG17')

#return the litho selected from listbox
selected_rock = None
def onselect(*args):
	global selected_rock
	idx = int(listbox.curselection()[0])
	selected_rock = rock_codes[idx]

# Return the selected color from listbox
selected_color = None
def colorselect (*args):
	global selected_color
	idx = int(l.curselection()[0])
	selected_color = color_codes[idx]

save_rock_press = None
def save (hole_id, from_litho, to_litho, rock, color_sel, modifier, rock_desc):
	con = sqlite3.connect('database_name.db', timeout=3)
	cur = con.cursor()
	myrock = [hole_id.get(), from_litho.get(), to_litho.get(), selected_rock, selected_color, modifier.get(), rock_desc.get()]
	cur.execute('INSERT INTO Lithology(HoleID, From_l, To_l, Rock_code, Color, Modifier, Description) VALUES (?,?,?,?,?,?,?)', myrock)
	con.commit()

# Window is divided in 2 sections, first section is as follow
hole_id_label = Label(root, text="Hole ID:").grid(row=0, column=0, sticky=W)
from_litho_label = Label(root, text="From:").grid(row=1, column=0, sticky=W)
to_litho_label = Label(root, text="To:").grid(row=1, column=3, sticky=W)
litho_label = Label(root, text="Lithology:").grid(row=2, column=0, sticky=W)
color_label = Label(root, text="Color:").grid(row=2, column=3)
modifier_label = Label(root, text="Modifier:").grid(row=14, column=0, sticky=W)
description_label = Label(root, text="Description:").grid(row=15, column=0, sticky=W)
unit_label = Label(root, text="Litho Unit:").grid(row=16, column=0, sticky=W)
lenght_label = Label(root, text="Lenght:").grid(row=0, column=3, sticky=W)
lenght_calc = Label(root)
lenght_calc.grid(row=0, column=4)

# Buttons to calculate lenght
lenght_button = Button(root, text="Calculate", command=calclenght)
lenght_button.grid(row=0, column=5)

# Adding the entries
hole_entry = Entry(root, width=10, textvariable=hole_id)
hole_entry.grid(row=0, column=1, sticky=W)
from_entry = Entry(root, width=5, textvariable=from_litho)
from_entry.grid(row=1, column=1, sticky=W)
to_entry = Entry(root, width=5, textvariable=to_litho)
to_entry.grid(row=1, column=4, sticky=W)
# Preparing the litho and color listboxes
listbox = Listbox(root, listvariable=litho, height=6, width=12)
listbox.grid(row=2, column=1, rowspan=8, sticky=W)
litho_scroll = Scrollbar(root, command=listbox.yview, orient=VERTICAL)
listbox.configure(yscrollcommand=litho_scroll.set)
litho_scroll.config(command=listbox.yview)
litho_scroll.grid(row=2, column=2, sticky=N+S, rowspan=10)
l = Listbox(root, listvariable=color, height=6, width=7)
l.grid(row=2, column=4, rowspan=8)
l_scroll = Scrollbar(root, command=listbox.yview, orient=VERTICAL)
l.configure(yscrollcommand=l_scroll.set)
l_scroll.config(command=l.yview)
l_scroll.grid(row=2, column=5, sticky=N+S+W, rowspan=10)
modifier_entry = Entry(root, width=5, textvariable=modifier)
modifier_entry.grid(row=14, column=1, sticky=W)
rock_desc_entry = Entry(root, width=10, textvariable=rock_desc)
rock_desc_entry.grid(row=15, column=1, sticky=W)
unit_entry = Entry(root, width=5, textvariable=litho_unit)
unit_entry.grid(row=16, column=1, sticky=W)


# Buttons to save data
sr_button = Button(root, text='Save litho', command=asklitho)
sr_button.grid(row=15, column=5)
add_litho = Button(root, text="Add new", command=clear_litho)
add_litho.grid(row=17, column=5)
exit_button = Button(root, text="Exit", command=close_program)
exit_button.grid(row=36, column=12)

hole_entry.focus()

listbox.bind('<<ListboxSelect>>', onselect)
l.bind('<<ListboxSelect>>', colorselect)



# labels for the sampling section
sample_id = Label(root, text="Sample Number").grid(row=1, column=10)
from_sample = Label(root, text="From:").grid(row=1, column=11)
to_sample = Label(root, text="To:").grid(row=1, column=12)

# Preparing the space for samples
sampleid1 = Entry(root, width=15, textvariable=sample1)
sampleid1.grid(row=2, column=10)
from1 = Entry(root, width=5, textvariable=from1)
from1.grid(row=2, column=11)
to1 = Entry(root, width=5, textvariable=to1)
to1.grid(row=2, column=12)
save_sample1 = Button(root, text="Save Sample", command=asksample1)
save_sample1.grid(row=2, column=13)
sampleid2 = Entry(root, width=15, textvariable=sample2)
sampleid2.grid(row=4, column=10)
from2 = Entry(root, width=5, textvariable=from2)
from2.grid(row=4, column=11)
to2 = Entry(root, width=5, textvariable=to2)
to2.grid(row=4, column=12)
save_sample2 = Button(root, text="Save Sample", command=asksample2)
save_sample2.grid(row=4, column=13)
sampleid3 = Entry(root, width=15, textvariable=sample3)
sampleid3.grid(row=6, column=10)
from3 = Entry(root, width=5, textvariable=from3)
from3.grid(row=6, column=11)
to3 = Entry(root, width=5, textvariable=to3)
to3.grid(row=6, column=12)
save_sample3 = Button(root, text="Save Sample", command=asksample3)
save_sample3.grid(row=6, column=13)
sampleid4 = Entry(root, width=15, textvariable=sample4)
sampleid4.grid(row=8, column=10)
from4 = Entry(root, width=5, textvariable=from4)
from4.grid(row=8, column=11)
to4 = Entry(root, width=5, textvariable=to4)
to4.grid(row=8, column=12)
save_sample4 = Button(root, text="Save Sample", command=asksample4)
save_sample4.grid(row=8, column=13)

# Structure side of lithology
s_type_label = Label(root, text="Structure type:").grid(row=33, column=0, sticky=W)
s_depth_label = Label(root, text="Depth:").grid(row=34, column=0, sticky=W)
s_angle_label = Label(root, text="Angle:").grid(row=35, column=0, sticky=W)

# Entries for the structures
s_type_entry = Entry(root, width=10, textvariable=s_type)
s_type_entry.grid(row=33, column=1, sticky=W)
s_depth_entry = Entry(root, width=5, textvariable=s_depth)
s_depth_entry.grid(row=34, column=1, sticky=W)
s_angle_entry = Entry(root, width=5, textvariable=angle)
s_angle_entry.grid(row=35, column=1, sticky=W)

# Buttons to save structural data
save_s = Button(root, text="Save Structure", command=askstructure)
save_s.grid(row=36, column=0, sticky=W)
add_s = Button(root, text="Add new", command=clear_structure)
add_s.grid(row=37, column=0, sticky=W)

# QA QC section
qc_title = Label(root, text="QA/QC").grid(row=16, column=10, sticky=E)
qc_sample_id = Label(root, text="Dup Sample ID").grid(row=17, column=10)
orig_sample_id = Label(root, text="Original Sample ID").grid(row=17, column=11)
qc_entry = Entry(root, width=15, textvariable=qc_sample)
qc_entry.grid(row=18, column=10)
qc_orig_entry = Entry(root, width=15, textvariable=orig_sample)
qc_orig_entry.grid(row=18, column=11)
qc_save = Button(root, text="Save QC", command=askqc)
qc_save.grid(row=18, column=12)

# Standard section in QA QC
std_smp_id = Label(root, text="STD Sample ID").grid(row=19, column=10)
std_type = Label(root, text="STD Code").grid(row=19, column=11)
std_smp_id_entry = Entry(root, width=15, textvariable=std_sample_id)
std_smp_id_entry.grid(row=20, column=10)
std_type_entry = Entry(root, width=15, textvariable=std_code)
std_type_entry.grid(row=20, column=11)
std_save = Button(root, text="Save STD", command=askstd)
std_save.grid(row=20, column=12)

# Button to save samples


window.mainloop()
