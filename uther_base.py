# U.T.H.E.R.
# Unit Troubleshooting Help Easy Reference
# By S.Clark 2022
# version 2022-0-alpha

import csv
import sqlite3
from tkinter import *
import tkinter as tk
from tkinter import ttk
from subprocess import call
from PIL import ImageTk, Image



global con
con = sqlite3.connect('repair.db')

# splash screen------------------------------------------------------------------------------------------------
splash_root = Tk()
splash_root.title("U.T.H.E.R.")


app_width = 256
app_height = 256

screen_width = splash_root.winfo_screenwidth()
screen_height = splash_root.winfo_screenheight()

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)

splash_root.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

#splash_root.config(background='blue')
splash_root.iconbitmap('./assets/uther.png')
#splash_root.attributes('-alpha', 0.7)

splash_root.wm_attributes('-transparentcolor', splash_root['bg'])

my_image = ImageTk.PhotoImage(Image.open("./assets/uther.png"))

# hide title bar
splash_root.overrideredirect(True)

splash_label = Label(image=my_image)
splash_label.grid(row=0, column=0)




# instruction page function---------------------------------------------------------------------------------------------------------------

def doc():
	
	
	doc = Tk()
	doc.title("Unit Troubleshooting Help Easy Reference")



	app_width = 610
	app_height = 790

	screen_width = doc.winfo_screenwidth()
	screen_height = doc.winfo_screenheight()

	x = (screen_width / 2) - (app_width / 2)
	y = (screen_height / 2) - (app_height / 2)

	doc.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

	doc.config(bg='#66b2ff')
	doc.iconbitmap('spec4.ico')

	# search button
	doc_label = Label(doc, text="""                      Unit Troubleshooting Help Easy Reference
                                                */*/*/*/}0{\*\*\*\*


                                             INSTUCTION FOR USE
                                -------------------------------------

                                                       MAIN PAGE:
                                                           *************

 SELECT WHICH UNIT IS TO BE WORKED ON, A NEW WINDOW 
       WILL OPEN WITH THE FAULT LIST FOR THAT UNIT TYPE.

   USER MAY THEN SELECT FROM THE LIST WHAT THE PROBLEM
   IS AND A WINDOW WILL OPEN WITH THE INSTRUCTIONS FOR 
                                           CORRECTING THE ISSUE.

     MULTIPLE UNIT FAULT WINDOWS MAY BE OPEN AT ONE TIME.

                              PRESS EXIT BUTTON TO END PROGRAM.

             ADMINISTRATORS MAY SELECT THE ADMIN BUTTON 
                                     FOR FURTHER FUNCTIONS.


                                                          ADMIN PAGE:
                                                               *****************
    THE ADMIN PAGE HAS FIELDS TO ADD FAULT RECORDS TO THE
   DATABASE,   SIMPLY INPUT THE INFORMATION INTO EACH FIELD 
         AND HIT SUBMIT RECORD AND THE FAULT AND FIX WILL BE 
                                       AVAILABLE IN THE UNITS LIST.

            TO EDIT OR DELETE A RECORD,  THE ROCORD # MUST BE USED, 
IF NOT KNOWN, THEN USE THE SHOW RECORDS BUTTON TO VIEW ALL RECORDS .
    THE RECORD NUMBER WILL BE TO THE RIGHT OF THE FAULT REPAIR LISTING .

      YOU MAY SEARCH FOR A UNITS FAULTS BY HITTING THE SEARCH BUTTON.""", font="Algerian", justify= LEFT)
	doc_label.grid(row=0, column=0)

	button_quit = Button(doc, text="EXIT", command=doc.destroy, fg="white", bg="red", font="Algerian")
	button_quit.grid(row=1, column=0)

	
	


# unit 1 search function --------------------------------------------------------------------------------------------------------------------

def problem_input1():
	global problem_inputtad

    # create or connect to database
	con = sqlite3.connect('./assets/repair.db')
	# create curser
	c = con.cursor()

	query = c.execute('SELECT problem FROM repairs where unit = "UNIT 1"')# unit to search databas problems for

	data = []
	for row in c.fetchall():
		data.append(row[0])
	return data

	
	
    

	c.close()
	con.close()




def unit1_search():# name of unit to search in database, command for unit button
	global unit1_search

	search_records = Tk()
	search_records.title("Search")
	search_records.geometry()
	search_records.config(bg='#66b2ff')
	search_records.iconbitmap('./assets/spec4.ico')
# entry box search records
	
	drop2 = ttk.Combobox(search_records, values=problem_input1(), width=50, height=20)
	drop2.current(0)
	drop2.grid(row=0, column=2)
	

	
	
	def search_now():
		global search_now


		sql = ""
		selected = drop2.get()
		
		sql = "SELECT repair_pro FROM repairs WHERE problem = ?"

		
		search_now = Toplevel()
		search_now.title("Search Results")
		search_now.geometry("600x600")
		search_now.config(bg='#66b2ff')
		search_now.iconbitmap('./assets/spec4.ico')

		con = sqlite3.connect("./assets/repair.db")

		c = con.cursor()

		searched = drop2.get()
		#sql = "SELECT problem FROM repairs WHERE unit = '{drop1_val}'"

		name = (searched, )
		result = c.execute(sql, name)
		result = c.fetchall()
		

		if not result:
			result = "Record Not Found"

			main_frame = Frame(search_now)
			main_frame.pack(fill=BOTH, expand=False)

			my_canvas = Canvas(main_frame)
			my_canvas.pack(side=LEFT, fill=BOTH, expand=False)

			my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
			my_scrollbar.pack(side=RIGHT, fill=Y)

			my_canvas.configure(yscrollcommand=my_scrollbar.set)
			my_canvas.bind('<Configure>', lambda e:my_canvas.configure(scrollregion = my_canvas.bbox("all")))

			second_frame = Frame(my_canvas)

			my_canvas.create_window((0,0), window=second_frame, anchor="nw")




			button_quit = Button(second_frame, text="EXIT", command=search_now.destroy, fg="white", bg="blue")
			button_quit.grid(row=0, column=1)

			searched_label = Label(second_frame, text=result, bg="blue", fg="white", justify= LEFT)
			searched_label.grid(row=2, column=1)

		else:

			main_frame = Frame(search_now)
			main_frame.pack(fill=BOTH, expand=True)

			my_canvas = Canvas(main_frame)
			my_canvas.pack(side=LEFT, fill=BOTH, expand=True)

			my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
			my_scrollbar.pack(side=RIGHT, fill=Y)

			my_canvas.configure(yscrollcommand=my_scrollbar.set)
			my_canvas.bind('<Configure>', lambda e:my_canvas.configure(scrollregion = my_canvas.bbox("all")))

			second_frame = Frame(my_canvas)

			my_canvas.create_window((0,0), window=second_frame, anchor="nw")

			for index, x in enumerate(result):
				num = 0
				index += 2
				
				for y in x:


					num +=1


					button_quit = Button(second_frame, text="EXIT", command=search_now.destroy, fg="white", bg="blue")
					button_quit.grid(row=0, column=1)

					searched_label = Label(second_frame, text=y, justify= LEFT)
					searched_label.grid(row=2, column=1)


			
			con.commit()
			con.close()

	# search buttons

	
	search_btn = Button(search_records, text="List Repair", command=search_now, bg="blue", fg="white")
	search_btn.grid(row=1, column=1, columnspan=2, padx=10, pady=10)

	button_quit = Button(search_records, text="EXIT", command=search_records.destroy, fg="white", bg="red")
	button_quit.grid(row=99, column=1, columnspan=2)






# search type function-- used in admin search----------------------------------------------------------------------------------------------------------------

def search_type():
	
	def close():
		search_type.destroy()

	search_type = Tk()
	search_type.title("Repair Quick Reference Tool")



	app_width = 470
	app_height = 350

	screen_width = search_type.winfo_screenwidth()
	screen_height = search_type.winfo_screenheight()

	x = (screen_width / 2) - (app_width / 2)
	y = (screen_height / 2) - (app_height / 2)

	search_type.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

	search_type.config(bg='black')
	search_type.iconbitmap('./assets/spec4.ico')

		# search button
	HG200_btn = Button(search_type, text="UNIT 1", command = unit1_search, fg="white", bg="blue", font="Algerian")
	HG200_btn.grid(row=1, column=0,padx=10, pady=10, ipadx=10)

	

	# quit button
	button_quit = Button(search_type, text="EXIT", command=search_type.destroy, fg="white", bg="red", font="Algerian")
	button_quit.grid(row=7,column=1)

# update function--------------------------------------------------------------------------------------------------
def update():

	# create or connect to database
	con = sqlite3.connect('./assets/repair.db')
	# create curser
	c = con.cursor()



	record_id = select_box.get()

	c.execute("""UPDATE repairs SET
	unit = :unit,
	problem = :problem,
	repair_pro = :repair_pro

	WHERE oid = :oid""",

	{
	"unit": unit_edit.get(),
	"problem": fault_edit.get(),
	"repair_pro": fix_edit.get(),

	"oid": record_id

	}


	)


	# commit changes
	con.commit()


	# close connection
	con.close()

	editor.destroy()

# create edit function to update a record--------------------------------------------------------------------------
def edit():

	global editor
	# create new window for edit
	editor = Tk()
	editor.title("Edit Record")
	editor.geometry("700x200")
	editor.config(bg='#66b2ff')
	editor.iconbitmap('./assets/spec4.ico')


	# create or connect to database
	con = sqlite3.connect('./assets/repair.db')
	# create curser
	c = con.cursor()

	record_id = select_box.get()
	# query the database
	c.execute("SELECT * FROM repairs WHERE oid = " + record_id)
	records = c.fetchall()

	# create global variable for text box names
	global unit_edit
	global fault_edit
	global fix_edit

	# entry fields
	unit_edit = Entry(editor, width=40, bg="light grey", font="Algerian")
	unit_edit.grid(row=0, column=1, sticky=W, padx=20, pady=10)

	fault_edit = Entry(editor, width=40, bg="light grey", font="Algerian")
	fault_edit.grid(row=1, column=1, sticky=W, padx=20, pady=10)

	fix_edit = Entry(editor, width=100, bg="light grey", font="Algerian")
	fix_edit.grid(row=2, column=1, padx=20)

	# create field labels
	unit_label_edit = Label(editor, text="Unit Type", bg='#66b2ff', font="Algerian")
	unit_label_edit.grid(row=0, column=0, sticky=E, pady=10)
	fault_label_edit = Label(editor, text="Fault", bg='#66b2ff', font="Algerian")

	fault_label_edit.grid(row=1, column=0, sticky=E, pady=10)

	fix_label_edit = Label(editor, text="Repair", bg='#66b2ff', font="Algerian")
	fix_label_edit.grid(row=2, column=0, sticky=E)

	# loop through results
	for record in records:
		unit_edit.insert(0, record[0])
		fault_edit.insert(0, record[1])
		fix_edit.insert(0, record[2])

	# create a Save button
	save_btn = Button(editor, text="Save Record", command=update, bg="green", font="Algerian")
	save_btn.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# create query function-----------------------------------------------------------------------------------------------
def query():
	global query
# create new window for edit
	query = Toplevel()
	query.title("show Record")
	query.geometry("1140x600")
	query.config(bg='#66b2ff')
	query.iconbitmap('./assets/spec4.ico')

		# create or connect to database
	con = sqlite3.connect('./assets/repair.db')
		# create curser
	c = con.cursor()
		# query the database
	c.execute('SELECT *, oid FROM repairs')
	records = c.fetchall()
		#print(records)

		# loop through results
		#print_records =""
	main_frame = Frame(query)
	main_frame.pack(fill=BOTH, expand=1)

	my_canvas = Canvas(main_frame)
	my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

	my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
	my_scrollbar.pack(side=RIGHT, fill=Y)

	my_canvas.configure(yscrollcommand=my_scrollbar.set)
	my_canvas.bind('<Configure>', lambda e:my_canvas.configure(scrollregion = my_canvas.bbox("all")))

	second_frame = Frame(my_canvas, bg="#66b2ff")

	my_canvas.create_window((0,0), window=second_frame, anchor="nw")

	for index, record in enumerate(records):
		num = 0
		for y in record:
				query_label = Label(second_frame, text=y, bg='#66b2ff', font="Algerian")
				query_label.grid(row=index+1, column=num, sticky=W)

				num +=1
		# export to excel button
	csv_button = Button(second_frame, text = "Save to Excel", command=lambda: write_to_csv(records), bg="gold", font="Algerian")
	csv_button.grid(row=0, column=0, pady=20)

	button_quit = Button(second_frame, text="EXIT", command=query.destroy, fg="white", bg="red", font="Algerian")
	button_quit.grid(row=0, column=1, pady=20)
		# commit changes
	con.commit()
		# close connection
	con.close()




# delete function----------------------------------------------------------------------------------------------------
def delete():
# create or connect to database
	con = sqlite3.connect('./assets/repair.db')
	# create curser
	c = con.cursor()

	# delete record
	c.execute("DELETE from repairs WHERE oid = " + select_box.get())


	# commit changes
	con.commit()


	# close connection
	con.close()



# submit function----------------------------------------------------------------------------------------------------
def submit():


	# create or connect to database
	con = sqlite3.connect('./assets/repair.db')
	# create curser
	c = con.cursor()
	# insert into table
	c.execute("INSERT INTO repairs VALUES (:unit, :fault, :fix)",
					{
					"unit": unit.get(),
					"fault": fault.get(),
					"fix": fix.get()
					})


	# commit changes
	con.commit()


	# close connection
	con.close()
	# clear text boxes
	unit.delete(0, END)
	fault.delete(0, END)
	fix.delete(0, END)

# write to csv Excel function
def write_to_csv(records):
	with open("Repairs.csv","a", newline="") as f:
		w = csv.writer(f, dialect="excel")
		header = ["Unit Type", "Fault Type", "Possible Repairs", "Record #"]
		w.writerow(header)
		for record in records:

			w.writerow(record)


#### Admin Functions ####-------------------------------------------------------------------------------------------
def admin():

	main.destroy()
	global admin
	admin = Tk()
	admin.title("Admin ")
	app_width = 800
	app_height = 700


	x = (screen_width / 2) - (app_width / 2)
	y = (screen_height / 2) - (app_height / 2)

	admin.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

	admin.wm_attributes('-transparentcolor', admin['bg'])
	
	admin.iconbitmap('./assets/spec4.ico')

	# hide title bar
	admin.overrideredirect(True)

	# create or connect to database
	con = sqlite3.connect('./assets/repair.db')

	# create curser
	c = con.cursor()

	# create table , only used for first run
	'''c.execute("""CREATE TABLE repairs (
		unit text,
		problem text,
		repair_pro text
		)""")'''

	global select_box

	select_box = Entry(admin, width=10)
	select_box.grid(row=7, column=1)
	# create update function
# Admin fields
	# entry fields
	global unit
	global fault
	global fix

	unit = Entry(admin, width=60, bg="light grey", font="Algerian")
	unit.grid(row=0, column=1, sticky=W, padx=20, pady=10)

	fault = Entry(admin, width=60, bg="light grey", font="Algerian")
	fault.grid(row=1, column=1, sticky=W, padx=20, pady=10)

	fix = Entry(admin, width=60, bg="light grey", font="Algerian")
	fix.grid(row=2, column=1, padx=20, columnspan=3,sticky=W)

	select_box = Entry(admin, width=10, bg="light grey", font="Algerian")
	select_box.grid(row=6, column=1)

# create field labels
	unit_label = Label(admin, text="Unit Type", fg="black", font="Algerian")
	unit_label.grid(row=0, column=0, sticky=E)

	fault_label = Label(admin, text="Fault", font="Algerian")
	fault_label.grid(row=1, column=0, sticky=E)

	fix_label = Label(admin, text="Repair", font="Algerian")
	fix_label.grid(row=2, column=0, sticky=E)

	select_label = Label(admin, text="Select Record Number", font="Algerian")
	select_label.grid(row=5, column=1)

	


	div_label2 = Label(admin, text="                            * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * ")
	div_label2.grid(row=9, column=0,columnspan=3)
	div_label1 = Label(admin, text="                            * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * ")
	div_label1.grid(row=4, column=0,columnspan=3)
	# create submit button
	submit_btn = Button(admin, text="Submit Record", command=submit, fg="blue", bd="5", font="Algerian")
	submit_btn.grid(row=3, column=1, pady=10, padx=10, ipadx=30)

	# create a query button
	query_btn = Button(admin, text="Show Records", command=query, fg="blue", bd="5", font="Algerian")
	query_btn.grid(row=10, column=1, pady=10, padx=10, ipadx=30)

	# create a delete button
	delete_btn = Button(admin, text="Delete Record", command=delete, fg="blue", bd="5", font="Algerian")
	delete_btn.grid(row=8, column=1, pady=10, padx=10, ipadx=30)

	# create a Update button
	update_btn = Button(admin, text="Edit Record", command=edit, fg="blue", bd="5", font="Algerian")
	update_btn.grid(row=7, column=1, pady=10, padx=10, ipadx=30)

	# create search button
	search_btn = Button(admin, text="Search", command=search_type, fg="blue", bd="5", font="Algerian")
	search_btn.grid(row=11, column=1, padx=10, pady=10, ipadx=30)

	button_quit = Button(admin, text="EXIT", command=admin.destroy, fg="Red", bd="5", font="Algerian")
	button_quit.grid(row=12, column=1)
	#### Buttons for main window ####


	doc_btn = Button(admin, text="Instructions", command=doc, fg="white", bd="5", font="Algerian")
	doc_btn.grid(row=13, column=1)

	




# main window----------------------------------------------------------------------------------------------------

def main_window():
	global main_window
	splash_root.destroy()
	

	global main
	main = Tk()
	main.title("UTHER - Unit Troubleshooting Help Easy Reference")



	app_width = 600
	app_height = 600



	x = (screen_width / 2) - (app_width / 2)
	y = (screen_height / 2) - (app_height / 2)

	main.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

	#main.wm_attributes('-transparentcolor', main['bg'])
	
	main.iconbitmap('./assets/spec4.ico')

	# hide title bar
	main.overrideredirect(True)

	

	title_label = Label(main, text="§ § Reference Database For Unit Repair § §", fg="#277c31", borderwidth="5", font="Algerian")
	title_label.grid(row=0, column=0, columnspan=4, pady=10)

	# search button
	unit1_btn = Button(main, text="UNIT 1", command = unit1_search, fg="#277c31", borderwidth="5", font="Algerian")
	unit1_btn.grid(row=1, column=0,padx=10, pady=10, ipadx=10)

	
	sep_label = Label(main, text="/ / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /", fg="#277c31", font="Algerian")
	sep_label.grid(row=7, column=0, columnspan=4, pady=10)

	admin_btn = Button(main, text="§",command = admin,fg="green", font="Algerian")
	admin_btn.grid(row=10, column=2)


	button_quit = Button(main, text="EXIT", command=main.quit, fg="red", borderwidth="5", font="Algerian")
	button_quit.grid(row=10, column=1)


# close splash screen after 3 secs----------------------------------------------------------------------------------

splash_root.after(3000, main_window)
# main loop---------------------------------------------------------------------------------------------------------
mainloop()
