from tkinter import *
from tkinter import messagebox
import pymysql
from tkinter import ttk

# ================================= class =================================
class Student:
    def __init__(self, root):
        # ================================= colors =================================
        bg_color_fr_1 = "#8e44ad"
        bg_color_fr_2 = "#8e44ad"
        bg_color_fr_1_btn = "#7d3c98"
        bg_btn_frame = "#bb8fce"
        # ================================= color end =================================
        self.root = root
        self.root.title('Student Management System')
        self.root.geometry('1280x680+10+10')

        # ================================= header =================================
        title = Label(
            self.root, text='Student Management System',
            font=('Helvetica', 30), bg='#6c3483', fg='#FFFFFF',
            pady=10
        )
        title.place(x=0, y=0, relwidth=1) # text in center and adjustable width
        # ================================= header end =================================

        # ================================= variables =================================

        self.rollNoData = StringVar()
        self.usernameData = StringVar()
        self.emailData = StringVar()
        self.contactData = StringVar()
        self.genderData = StringVar()
        self.dobData = StringVar()

        self.searchBarData = StringVar()
        self.searchTextData = StringVar()

        # ================================= end variables =================================

        # ================================= frame one =================================
        m_frame = Frame(self.root, bd=4, relief=RIDGE, bg=bg_color_fr_1)
        m_frame.place(x=20, y=80, width=450, height=560)

        header_frame_1 = Label(
            m_frame, text='Manage Students',
            font=('times new roman', 15, 'bold'), bg=bg_color_fr_1, fg='#FFFFFF'
        )
        header_frame_1.grid(row=0, pady=8, padx=20, columnspan=2, sticky=W)

        # ================================= roll number entry =================================
        rn_label = Label(
            m_frame, text='Roll No.', font=('Helvetica', 15), bg=bg_color_fr_1,
            fg='#FFFFFF'
        )
        rn_label.grid(row=1, column=0, pady=15, padx=10)
        rn_entry = Entry(
            m_frame, width=25, bd=2, font=('Helvetica', 15),
            textvariable=self.rollNoData
        )
        rn_entry.grid(row=1, column=1, pady=15, padx=10)

        # ================================= name entry =================================
        name_label = Label(
            m_frame, text='Name.', font=('Helvetica', 15), bg=bg_color_fr_1,
            fg='#FFFFFF'
        )
        name_label.grid(row=2, column=0, pady=15, padx=10)
        name_entry = Entry(
            m_frame, width=25, bd=2, font=('Helvetica', 15),
            textvariable=self.usernameData
        )
        name_entry.grid(row=2, column=1, pady=15, padx=10)

        # ================================= email entry =================================
        email_label = Label(
            m_frame, text='Email.', font=('Helvetica', 15), bg=bg_color_fr_1,
            fg='#FFFFFF'
        )
        email_label.grid(row=3, column=0, pady=15, padx=10)
        email_entry = Entry(
            m_frame, width=25, bd=2, font=('Helvetica', 15),
            textvariable=self.emailData
        )
        email_entry.grid(row=3, column=1, pady=15, padx=10)

        # ================================= contact entry =================================
        contact_label = Label(
            m_frame, text='Contact.', font=('Helvetica', 15), bg=bg_color_fr_1,
            fg='#FFFFFF'
        )
        contact_label.grid(row=4, column=0, pady=15, padx=10)
        contact_entry = Entry(
            m_frame, width=25, bd=2, font=('Helvetica', 15),
            textvariable=self.contactData
        )
        contact_entry.grid(row=4, column=1, pady=15, padx=10)

        # ================================= DOB entry =================================
        dob_label = Label(
            m_frame, text='DOB.', font=('Helvetica', 15), bg=bg_color_fr_1,
            fg='#FFFFFF'
        )
        dob_label.grid(row=5, column=0, pady=15, padx=10)
        dob_entry = Entry(
            m_frame, width=25, bd=2, font=('Helvetica', 15),
            textvariable=self.dobData
        )
        dob_entry.grid(row=5, column=1, pady=15, padx=10)

        # ================================= gender entry =================================
        gender_label = Label(
            m_frame, text='Gender.', font=('Helvetica', 15), bg=bg_color_fr_1,
            fg='#FFFFFF'
        )
        gender_label.grid(row=6, column=0, pady=15, padx=10)
        # import ttk for combo box (dropDown)
        # state='readonly' i.e user can't write anything
        gender_combobox = ttk.Combobox(
            m_frame, font=('times new roman', 15),
            width=26, state='readonly', textvariable=self.genderData
        )
        gender_combobox['values'] = ('Male', 'Female', 'Others')
        gender_combobox.grid(row=6, column=1, pady=15, padx=10)

        # ================================= address entry =================================
        address_label = Label(
            m_frame, text='Address.', font=('Helvetica', 15), bg=bg_color_fr_1,
            fg='#FFFFFF'
        )
        address_label.grid(row=7, column=0, pady=15, padx=10)
        self.address_entry = Text(m_frame, width=35, height=3, bd=2)
        self.address_entry.grid(row=7, column=1, pady=15, padx=10)

        # ================================= button frame =================================
        b_frame = Frame(m_frame, bd=2, relief=RIDGE, bg=bg_btn_frame, padx=5, pady=5)
        b_frame.grid(row=8, columnspan=4, padx=15)

        # ================================= add
        add_user = Button(
            b_frame, text='Add', width=10, padx=5, pady=5,
            font=('Helvetica', 9), bg=bg_color_fr_1_btn, fg='#FFFFFF',
            bd=2, relief=GROOVE, command=self.add_students
        )
        add_user.grid(row=0, column=0, padx=5)

        # ================================= update
        update_user = Button(
            b_frame, text='Update', width=10, padx=5, pady=5,
            font=('Helvetica', 9), bg=bg_color_fr_1_btn, fg='#FFFFFF',
            bd=2, relief=GROOVE, command=self.update_data
        )
        update_user.grid(row=0, column=1, padx=5)

        # ================================= delete
        delete_user = Button(
            b_frame, text='Delete', width=10, padx=5, pady=5,
            font=('Helvetica', 9), bg=bg_color_fr_1_btn, fg='#FFFFFF',
            bd=2, relief=GROOVE, command=self.delete_data
        )
        delete_user.grid(row=0, column=2, padx=5)

        # ================================= clear
        clear_user = Button(
            b_frame, text='Clear', width=10, padx=5, pady=5,
            font=('Helvetica', 9), bg=bg_color_fr_1_btn, fg='#FFFFFF',
            bd=2, relief=GROOVE, command=self.clear
        )
        clear_user.grid(row=0, column=3, padx=5)
        # ================================= button frame end =================================
        # ================================= frame one =================================



        # ================================= frame two =================================
        d_frame = Frame(self.root, bd=4, relief=RIDGE, bg=bg_color_fr_2)
        d_frame.place(x=510, y=80, width=750, height=560)

        # ================================= header =================================
        header_frame_2 =  Label(
            d_frame, text='Database',
            font=('times new roman', 15, 'bold'), bg=bg_color_fr_2, fg='#FFFFFF'
        )
        header_frame_2.grid(row=0, columnspan=4, sticky=W, padx=20, pady=8)
        # ================================= header end =================================

        # ================================= top =================================
        Label(
            d_frame, text='Search By: ',
            font=('times new roman', 15, 'bold'), bg=bg_color_fr_2, fg='#FFFFFF'
        ).grid(row=1, column=0, pady=15, padx=10)
        search_combobox = ttk.Combobox(
            d_frame, font=('times new roman', 15),
            width=10, state='readonly', textvariable=self.searchBarData
        )
        search_combobox['values'] = ('RollNo', 'Name', 'Contact')
        search_combobox.grid(row=1, column=1, pady=15, padx=10)

        search_entry = Entry(
            d_frame, width=15, bd=2, font=('Helvetica', 15), textvariable=self.searchTextData
        )
        search_entry.grid(row=1, column=2, pady=15, padx=10)

        search_user = Button(
            d_frame, text='search', width=10, padx=5, pady=5,
            font=('Helvetica', 9), bg='#FFFFFF', fg='#000000',
            bd=2, relief=GROOVE, command=self.search_data
        )
        search_user.grid(row=1, column=3, padx=5)
        show_user = Button(
            d_frame, text='Show All', width=10, padx=5, pady=5,
            font=('Helvetica', 9), bg='#FFFFFF', fg='#000000',
            bd=2, relief=GROOVE, command=self.get_data
        )
        show_user.grid(row=1, column=4, padx=5)
        # ================================= top end =================================

        # ================================= table frame =================================
        t_frame = Frame(d_frame, bd=4, relief=RIDGE, bg=bg_color_fr_2)
        t_frame.place(x=10, y=95, width=725, height=450)

        # ================================= scroll bar x_axis
        scroll_x = Scrollbar(t_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(t_frame, orient=VERTICAL)
        # self.student table to make it globally accessibly
        self.student_table = ttk.Treeview(
            t_frame, xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set,
            columns=("RollNo", "Name", "Email", "Gender", "Contact", "DOB", "Address")
        )
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        # helps in scrolling the page accordingly
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        # ================================= to show all columns along with scrolls
        self.student_table.heading("RollNo", text='RollNo')
        self.student_table.heading("Name", text='Name')
        self.student_table.heading("Email", text='Email')
        self.student_table.heading("Gender", text='Gender')
        self.student_table.heading("Contact", text='Contact')
        self.student_table.heading("DOB", text='DOB')
        self.student_table.heading("Address", text='Address')
        # otherwise index column will show, to remove use ['show'] = 'headings'
        self.student_table['show']='headings'
        # width of all columns
        self.student_table.column("RollNo", width=50)
        self.student_table.column("Name", width=120)
        self.student_table.column("Email", width=120)
        self.student_table.column("Gender", width=120)
        self.student_table.column("Contact", width=120)
        self.student_table.column("DOB", width=120)
        self.student_table.column("Address", width=150)
        self.student_table.pack(fill=BOTH, expand=1) # to apply use, expand=1

        # binding, on click option binding
        self.student_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.get_data()
        # ================================= table frame end =================================

    # ================================= add button function
    def add_students(self):
        if self.rollNoData.get()=="" \
                or self.usernameData.get()=="" \
                or self.contactData=="" \
                or self.emailData.get()==""\
                or self.genderData.get()=="":
            messagebox.showerror('Error', 'All Fields are Required')
        else:
            # create connection
            conn = pymysql.connect(
                host='localhost', user='root',
                password="", database="StudentManagementSys"
            )
            # create cursor use to execute query
            cur = conn.cursor()
            # create query
            cur.execute(
                "insert into studentTable values(%s,%s,%s,%s,%s,%s,%s)",
                (self.rollNoData.get(), self.usernameData.get(), self.emailData.get(),
                 self.genderData.get(), self.contactData.get(), self.dobData.get(),
                 self.address_entry.get('1.0', END))  # get('from', to)
            )
            # fire
            conn.commit()
            # call function when data added
            self.get_data()
            # clear after adding
            self.clear()
            # close
            conn.close()
            messagebox.showinfo('Success', 'Record has been added successfully')
    # ================================ retrieve data function =================================
    def get_data(self):
        # create connection
        conn = pymysql.connect(
            host='localhost', user='root',
            password="", database="StudentManagementSys"
        )
        # create cursor use to execute query
        cur = conn.cursor()
        # create query
        cur.execute("select * from studentTable")
        rows = cur.fetchall()
        if len(rows) != 0:
            # to delete previous data and show all
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('', END, values=row)
            # fire
            conn.commit()
        # close
        conn.close()
    # ================================= clear function =================================
    def clear(self):
        self.rollNoData.set("")
        self.usernameData.set("")
        self.emailData.set("")
        self.contactData.set("")
        self.genderData.set("")
        self.dobData.set("")
        self.address_entry.delete("1.0", END)

    # ================================= on click function =================================
    def get_cursor(self, vr):
        cursor_row = self.student_table.focus()
        contents = self.student_table.item(cursor_row)
        row = contents['values']
        self.rollNoData.set(row[0])
        self.usernameData.set(row[1])
        self.emailData.set(row[2])
        self.genderData.set(row[3])
        self.contactData.set(row[4])
        self.dobData.set(row[5])
        self.address_entry.delete("1.0", END)
        self.address_entry.insert(END, row[6])
    # ================================= update data =================================
    def update_data(self):
        # create connection
        conn = pymysql.connect(
            host='localhost', user='root',
            password="", database="StudentManagementSys"
        )
        # create cursor use to execute query
        cur = conn.cursor()
        # create query
        cur.execute(
            "update studentTable set Name=%s,Email=%s,Gender=%s,Contact=%s,DOB=%s,Address=%s where RollNo=%s",
            (self.usernameData.get(), self.emailData.get(),
             self.genderData.get(), self.contactData.get(), self.dobData.get(),
             self.address_entry.get('1.0', END),self.rollNoData.get())  # get('from', to)
        )
        # fire
        conn.commit()
        # call function when data added
        self.get_data()
        # clear after adding
        self.clear()
        # close
        conn.close()
    # ================================= delete data =================================
    def delete_data(self):
        # create connection
        conn = pymysql.connect(
            host='localhost', user='root',
            password="", database="StudentManagementSys"
        )
        # create cursor use to execute query
        cur = conn.cursor()
        # create query
        cur.execute("delete from studentTable where RollNo=%s",self.rollNoData.get())
        # fire
        conn.commit()
        # call function when data added
        self.get_data()
        # clear after adding
        self.clear()
        # close
        conn.close()

    def search_data(self):
        # create connection
        conn = pymysql.connect(
            host='localhost', user='root',
            password="", database="StudentManagementSys"
        )
        # create cursor use to execute query
        cur = conn.cursor()
        # create query
        cur.execute("select * from studentTable where "+str(self.searchBarData.get())+" LIKE '%"+str(self.searchTextData.get())+"%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            # to delete previous data and
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('', END, values=row)
            # fire
            conn.commit()
        # close
        conn.close()


root = Tk()
obj = Student(root)
root.mainloop()
# ================================= end =================================
