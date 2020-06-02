from tkinter import *
from tkinter import messagebox
import random
import os

class BillApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1280x680+10+10')
        self.root.title('Billing system')

        bg_color = '#074463'
        fg_color = '#FFFFFF'

        # ==================================== variables ====================================
        # ==================================== variables cosmetics
        self.bath_soap_data = IntVar()
        self.face_cream_data = IntVar()
        self.face_wash_data = IntVar()
        self.hair_spray_data = IntVar()
        self.hair_gel_data = IntVar()
        self.body_lotion_data = IntVar()
        # ==================================== variables groceries
        self.rice_data = IntVar()
        self.food_oil_data = IntVar()
        self.daal_data = IntVar()
        self.wheat_data = IntVar()
        self.sugar_data = IntVar()
        self.tea_data = IntVar()
        # ==================================== variables drinks
        self.maza_data = IntVar()
        self.coca_cola_data = IntVar()
        self.frooti_data = IntVar()
        self.thumps_up_data = IntVar()
        self.limca_data = IntVar()
        self.sprite_data = IntVar()
        # ==================================== variables price & tax
        self.cosmetic_price_data = StringVar()
        self.groceries_price_data = StringVar()
        self.drinks_price_data = StringVar()
        self.cosmetic_tax_data = StringVar()
        self.groceries_tax_data = StringVar()
        self.drinks_tax_data = StringVar()
        # ==================================== customer details
        self.customer_name_data = StringVar()
        self.contact_number_data = StringVar()
        self.bill_number_data = StringVar()
        # ==================================== variables end ====================================

        # ==================================== header ====================================
        header = Label(
            self.root, text='Billing System', bd=10, relief=RAISED,
            bg=bg_color, fg='#FFFFFF', font=('times new roman', 30, 'bold'),
            pady=5
        )
        header.place(x=0, y=0, relwidth=1)
        # ==================================== header end ====================================

        # ==================================== customer detail frame ====================================
        cd_frame = LabelFrame(
            self.root, text='Customer Details', font=('courier new',15), bg=bg_color, fg='gold',
            bd=10, relief=RIDGE
        )
        cd_frame.place(x=0, y=76, relwidth=1)
        # ==================================== top input fields
        Label(
            cd_frame, text='Customer Name:', font=('courier new', 16), bg=bg_color,
            fg=fg_color
        ).grid(row=0, column=0, pady=10, padx=2)
        c_frame_customer_entry = Entry(
            cd_frame, width=16, font=('courier new', 16), bd=5, relief=SUNKEN,
            textvariable=self.customer_name_data
        )
        c_frame_customer_entry.grid(row=0, column=1, pady=10)
        Label(
            cd_frame, text='Contact No:', font=('courier new', 16), bg=bg_color,
            fg=fg_color
        ).grid(row=0, column=2, pady=10, padx=2)
        c_frame_contact_entry = Entry(
            cd_frame, width=16, font=('courier new', 16), bd=5, relief=SUNKEN,
            textvariable=self.contact_number_data
        )
        c_frame_contact_entry.grid(row=0, column=3, pady=10)
        Label(
            cd_frame, text='Bill No:', font=('courier new', 16), bg=bg_color,
            fg=fg_color
        ).grid(row=0, column=4, pady=10, padx=2)
        c_frame_bill_entry = Entry(
            cd_frame, width=16, font=('courier new', 16), bd=5, relief=SUNKEN,
            textvariable=self.bill_number_data
        )
        c_frame_bill_entry.grid(row=0, column=5, pady=10)
        c_frame_contact_entry = Button(
            cd_frame, width=8, text='search', font=('courier new', 16), bd=0, relief=GROOVE,
            fg=bg_color, command=self.retrieve
        )
        c_frame_contact_entry.grid(row=0, column=6, padx=10, sticky=E)
        # ==================================== top input fields end ====================================
        # ==================================== customer detail frame end ====================================

        # ==================================== cosmetics frame ====================================
        co_frame = LabelFrame(
            self.root, text='Cosmetics', font=('courier new', 15), bg=bg_color, fg='gold',
            bd=10, relief=RIDGE
        )
        co_frame.place(x=2, y=166, width=300, height=330)
        # ==================================== fields and inputs
        Label(
            co_frame, text='Bath soap', font=('courier new', 16), bg=bg_color, fg=fg_color
        ).grid(row=0, column=0, padx=5, pady=10)
        co_frame_bath_soap_entry = Entry(
            co_frame, width=8, font=('courier new', 16), bd=5, relief=SUNKEN,
            textvariable=self.bath_soap_data
        )
        co_frame_bath_soap_entry.grid(row=0, column=1)
        Label(
            co_frame, text='Face Cream', font=('courier new', 16), bg=bg_color, fg=fg_color
        ).grid(row=1, column=0, padx=5, pady=10)
        co_frame_face_cream_entry = Entry(
            co_frame, width=8, font=('courier new', 16), bd=5, relief=SUNKEN,
            textvariable=self.face_cream_data
        )
        co_frame_face_cream_entry.grid(row=1, column=1)
        Label(
            co_frame, text='Face Wash', font=('courier new', 16), bg=bg_color, fg=fg_color
        ).grid(row=2, column=0, padx=5, pady=10)
        co_frame_face_wash_entry = Entry(
            co_frame, width=8, font=('courier new', 16), bd=5, relief=SUNKEN,
            textvariable=self.face_wash_data
        )
        co_frame_face_wash_entry.grid(row=2, column=1)
        Label(
            co_frame, text='Hair Spray', font=('courier new', 16), bg=bg_color, fg=fg_color
        ).grid(row=3, column=0, padx=5, pady=10)
        co_frame_hair_spray_entry = Entry(
            co_frame, width=8, font=('courier new', 16), bd=5, relief=SUNKEN,
            textvariable=self.hair_spray_data
        )
        co_frame_hair_spray_entry.grid(row=3, column=1)
        Label(
            co_frame, text='Hair Gel', font=('courier new', 16), bg=bg_color, fg=fg_color
        ).grid(row=4, column=0, padx=5, pady=10)
        co_frame_hair_gel_entry = Entry(
            co_frame, width=8, font=('courier new', 16), bd=5, relief=SUNKEN,
            textvariable=self.hair_gel_data
        )
        co_frame_hair_gel_entry.grid(row=4, column=1)
        Label(
            co_frame, text='Body Lotion', font=('courier new', 16), bg=bg_color, fg=fg_color
        ).grid(row=5, column=0, padx=5, pady=10)
        co_frame_body_lotion_entry = Entry(
            co_frame, width=8, font=('courier new', 16), bd=5, relief=SUNKEN,
            textvariable=self.body_lotion_data
        )
        co_frame_body_lotion_entry.grid(row=5, column=1)
        # ==================================== cosmetics frame end ====================================

        # ==================================== groceries frame ====================================
        gr_frame = LabelFrame(
            self.root, text='Groceries', font=('courier new', 15), bg=bg_color, fg='gold',
            bd=10, relief=RIDGE
        )
        gr_frame.place(x=303, y=166, width=300, height=330)
        # ==================================== fields and inputs
        Label(
            gr_frame, text='Rice', font=('courier new', 16), bg=bg_color, fg=fg_color
        ).grid(row=0, column=0, padx=5, pady=10)
        gr_frame_rice_entry = Entry(
            gr_frame, width=8, font=('courier new', 16), bd=5, relief=SUNKEN,
            textvariable=self.rice_data
        )
        gr_frame_rice_entry.grid(row=0, column=1, padx=38)
        Label(
            gr_frame, text='Food Oil', font=('courier new', 16), bg=bg_color, fg=fg_color
        ).grid(row=1, column=0, padx=5, pady=10)
        gr_frame_food_oil_entry = Entry(
            gr_frame, width=8, font=('courier new', 16), bd=5, relief=SUNKEN,
            textvariable=self.food_oil_data
        )
        gr_frame_food_oil_entry.grid(row=1, column=1, padx=38)
        Label(
            gr_frame, text='Daal', font=('courier new', 16), bg=bg_color, fg=fg_color
        ).grid(row=2, column=0, padx=5, pady=10)
        gr_frame_daal_entry = Entry(
            gr_frame, width=8, font=('courier new', 16), bd=5, relief=SUNKEN,
            textvariable=self.daal_data
        )
        gr_frame_daal_entry.grid(row=2, column=1, padx=38)
        Label(
            gr_frame, text='Wheat', font=('courier new', 16), bg=bg_color, fg=fg_color
        ).grid(row=3, column=0, padx=5, pady=10)
        gr_frame_wheat_entry = Entry(
            gr_frame, width=8, font=('courier new', 16), bd=5, relief=SUNKEN,
            textvariable=self.wheat_data
        )
        gr_frame_wheat_entry.grid(row=3, column=1, padx=38)
        Label(
            gr_frame, text='Sugar', font=('courier new', 16), bg=bg_color, fg=fg_color
        ).grid(row=4, column=0, padx=5, pady=10)
        gr_frame_sugar_entry = Entry(
            gr_frame, width=8, font=('courier new', 16), bd=5, relief=SUNKEN,
            textvariable=self.sugar_data
        )
        gr_frame_sugar_entry.grid(row=4, column=1, padx=38)
        Label(
            gr_frame, text='Tea', font=('courier new', 16), bg=bg_color, fg=fg_color
        ).grid(row=5, column=0, padx=5, pady=10)
        gr_frame_tea_entry = Entry(
            gr_frame, width=8, font=('courier new', 16), bd=5, relief=SUNKEN,
            textvariable=self.tea_data
        )
        gr_frame_tea_entry.grid(row=5, column=1, padx=38)
        # ==================================== groceries frame end ====================================

        # ==================================== cold drink frame ====================================
        cd_frame = LabelFrame(
            self.root, text='Cold Drinks', font=('courier new', 15), bg=bg_color, fg='gold',
            bd=10, relief=RIDGE
        )
        cd_frame.place(x=604, y=166, width=300, height=330)
        # ==================================== fields and inputs
        Label(
            cd_frame, text='Maza', font=('courier new', 16), bg=bg_color, fg=fg_color
        ).grid(row=0, column=0, padx=5, pady=10)
        cd_frame_maza_entry = Entry(
            cd_frame, width=8, font=('courier new', 16), bd=5, relief=SUNKEN,
            textvariable=self.maza_data
        )
        cd_frame_maza_entry.grid(row=0, column=1, padx=26)
        Label(
            cd_frame, text='Coca Cola', font=('courier new', 16), bg=bg_color, fg=fg_color
        ).grid(row=1, column=0, padx=5, pady=10)
        cd_frame_coka_cola_entry = Entry(
            cd_frame, width=8, font=('courier new', 16), bd=5, relief=SUNKEN,
            textvariable=self.coca_cola_data
        )
        cd_frame_coka_cola_entry.grid(row=1, column=1, padx=26)
        Label(
            cd_frame, text='Frooti', font=('courier new', 16), bg=bg_color, fg=fg_color
        ).grid(row=2, column=0, padx=5, pady=10)
        cd_frame_frooti_entry = Entry(
            cd_frame, width=8, font=('courier new', 16), bd=5, relief=SUNKEN,
            textvariable=self.frooti_data
        )
        cd_frame_frooti_entry.grid(row=2, column=1, padx=26)
        Label(
            cd_frame, text='Thumps Up', font=('courier new', 16), bg=bg_color, fg=fg_color
        ).grid(row=3, column=0, padx=5, pady=10)
        cd_frame_thumps_up_entry = Entry(
            cd_frame, width=8, font=('courier new', 16), bd=5, relief=SUNKEN,
            textvariable=self.thumps_up_data
        )
        cd_frame_thumps_up_entry.grid(row=3, column=1, padx=26)
        Label(
            cd_frame, text='Limca', font=('courier new', 16), bg=bg_color, fg=fg_color
        ).grid(row=4, column=0, padx=5, pady=10)
        cd_frame_limca_entry = Entry(
            cd_frame, width=8, font=('courier new', 16), bd=5, relief=SUNKEN,
            textvariable=self.limca_data
        )
        cd_frame_limca_entry.grid(row=4, column=1, padx=26)
        Label(
            cd_frame, text='Sprite', font=('courier new', 16), bg=bg_color, fg=fg_color
        ).grid(row=5, column=0, padx=5, pady=10)
        cd_frame_sprite_entry = Entry(
            cd_frame, width=8, font=('courier new', 16), bd=5, relief=SUNKEN,
            textvariable=self.sprite_data
        )
        cd_frame_sprite_entry.grid(row=5, column=1, padx=26)
        # ==================================== cold drink frame end ====================================

        # ==================================== bill frame ====================================
        bl_frame = Frame(
            self.root, bd=10, relief=RIDGE, bg='#FFFFFF'
        )
        bl_frame.place(x=910, y=166, height=330, width=367)
        bl_frame_title = Label(
            bl_frame, text='Bill', font=('courier new', 15, 'bold'), bd=0, relief=SUNKEN,
            bg='#FFFFFF'
        )
        bl_frame_title.pack(fill=X)
        scroll_y = Scrollbar(bl_frame, orient=VERTICAL)
        scroll_y.pack(side=RIGHT, fill=Y)
        self.textArea = Text(bl_frame, yscrollcommand=scroll_y.set)
        scroll_y.config(command=self.textArea.yview)
        self.textArea.pack(fill=BOTH, expand=1)
        # ==================================== bill frame end ====================================

        # ==================================== button/menu frame ====================================
        bm_frame = LabelFrame(
            self.root, text='Billing Menu', font=('courier new',15), bg=bg_color, fg='gold',
            bd=10, relief=RIDGE
        )
        bm_frame.place(x=0, y=497, relwidth=1)
        # ==================================== calculation field
        Label(
            bm_frame, text='Total Cosmetic Price:', font=('courier new', 12),
            bg=bg_color, fg=fg_color
        ).grid(row=0, column=0, padx=5, pady=8)
        bm_frame_total_cosmetic_entry = Entry(
            bm_frame, width=10, font=('courier new', 12), bd=5, relief=SUNKEN,
            textvariable=self.cosmetic_price_data
        )
        bm_frame_total_cosmetic_entry.grid(row=0, column=1, padx=5, pady=10)
        Label(
            bm_frame, text='Cosmetic Tax:', font=('courier new', 12),
            bg=bg_color, fg=fg_color
        ).grid(row=0, column=2, padx=5, pady=8)
        bm_frame_cosmetic_tax_entry = Entry(
            bm_frame, width=10, font=('courier new', 12), bd=5, relief=SUNKEN,
            textvariable=self.cosmetic_tax_data
        )
        bm_frame_cosmetic_tax_entry.grid(row=0, column=3, padx=5, pady=10)
        Label(
            bm_frame, text='Total Groceries Price:', font=('courier new', 12),
            bg=bg_color, fg=fg_color
        ).grid(row=1, column=0, padx=5, pady=8)
        bm_frame_total_groceries_entry = Entry(
            bm_frame, width=10, font=('courier new', 12), bd=5, relief=SUNKEN,
            textvariable=self.groceries_price_data
        )
        bm_frame_total_groceries_entry.grid(row=1, column=1, padx=5, pady=10)
        Label(
            bm_frame, text='Groceries Tax:', font=('courier new', 12),
            bg=bg_color, fg=fg_color
        ).grid(row=1, column=2, padx=5, pady=8)
        bm_frame_groceries_tax_entry = Entry(
            bm_frame, width=10, font=('courier new', 12), bd=5, relief=SUNKEN,
            textvariable=self.groceries_tax_data
        )
        bm_frame_groceries_tax_entry.grid(row=1, column=3, padx=5, pady=10)
        Label(
            bm_frame, text='Total Drinks Price:', font=('courier new', 12),
            bg=bg_color, fg=fg_color
        ).grid(row=2, column=0, padx=5, pady=8)
        bm_frame_total_drinks_entry = Entry(
            bm_frame, width=10, font=('courier new', 12), bd=5, relief=SUNKEN,
            textvariable=self.drinks_price_data
        )
        bm_frame_total_drinks_entry.grid(row=2, column=1, padx=5, pady=10)
        Label(
            bm_frame, text='Drinks Tax:', font=('courier new', 12),
            bg=bg_color, fg=fg_color
        ).grid(row=2, column=2, padx=5, pady=8)
        bm_frame_drinks_tax_entry = Entry(
            bm_frame, width=10, font=('courier new', 12), bd=5, relief=SUNKEN,
            textvariable=self.drinks_tax_data
        )
        bm_frame_drinks_tax_entry.grid(row=2, column=3, padx=5, pady=10)

        # ==================================== buttons ====================================
        # ==================================== button frame
        b_frame = LabelFrame(
            bm_frame, text='Options', font=('courier new', 16), bd=5, relief=SUNKEN,
            bg=bg_color, fg='gold'
        )
        b_frame.place(x=660, y=10)
        # ==================================== total
        b_frame_total_button = Button(
            b_frame, text='Total', font=('courier new', 16), bg=bg_color, fg='#FFFFFF',
            bd=5, relief=GROOVE, width=8, command=self.total
        )
        b_frame_total_button.grid(row=0, column=0, padx=10, pady=20)
        # ==================================== bill
        b_frame_bill_button = Button(
            b_frame, text='Bill', font=('courier new', 16), bg=bg_color, fg='#FFFFFF',
            bd=5, relief=GROOVE, width=8, command=self.bill_area
        )
        b_frame_bill_button.grid(row=0, column=1, padx=10, pady=20)
        # ==================================== clear
        b_frame_clear_button = Button(
            b_frame, text='Clear', font=('courier new', 16), bg=bg_color, fg='#FFFFFF',
            bd=5, relief=GROOVE, width=8, command=self.clear
        )
        b_frame_clear_button.grid(row=0, column=2, padx=10, pady=20)
        # ==================================== exit
        b_frame_exit_button = Button(
            b_frame, text='Exit', font=('courier new', 16), bg=bg_color, fg='#FFFFFF',
            bd=5, relief=GROOVE, width=8, command=self.exit
        )
        b_frame_exit_button.grid(row=0, column=3, padx=10, pady=20)
        # ==================================== button/menu frame end ====================================

    # ==================================== function ====================================
    # ==================================== total function
    def total(self):
        if self.customer_name_data.get() != "":
            # set bill number randomly
            val = random.randint(1, 9999)
            self.bill_number_data.set(val)

            # ========= cosmetics
            self.cosmetic_bath_soap_v = self.bath_soap_data.get() * 40
            self.cosmetic_face_cream_v = self.face_cream_data.get() * 120
            self.cosmetic_face_wash_v = self.face_wash_data.get() * 60
            self.cosmetic_hair_spray_v = self.hair_spray_data.get() * 180
            self.cosmetic_hair_gel_v = self.hair_gel_data.get() * 140
            self.cosmetic_body_lotion_v = self.body_lotion_data.get() * 180
            self.total_cosmetics_price = float(
                self.cosmetic_bath_soap_v + self.cosmetic_face_cream_v +
                self.cosmetic_face_wash_v + self.cosmetic_hair_spray_v +
                self.cosmetic_hair_gel_v + self.cosmetic_body_lotion_v
            )

            self.cosmetic_price_data.set(str('Rs.') + str(self.total_cosmetics_price))
            self.cosmetic_tax_data.set(str('Rs.') + str((self.total_cosmetics_price*0.05)))
            # ========= groceries
            self.groceries_rice_v = self.rice_data.get() * 80
            self.groceries_food_oil_v = self.food_oil_data.get() * 180
            self.groceries_daal_v = self.daal_data.get() * 60
            self.groceries_wheat_v = self.wheat_data.get() * 240
            self.groceries_sugar_v = self.sugar_data.get() * 45
            self.groceries_tea_v = self.tea_data.get() * 150
            self.total_groceries_price = float(
                self.groceries_rice_v + self.groceries_food_oil_v +
                self.groceries_daal_v + self.groceries_wheat_v +
                self.groceries_sugar_v + self.groceries_tea_v
            )
            self.groceries_price_data.set(str('Rs.') + str(self.total_groceries_price))
            self.groceries_tax_data.set(str('Rs.') + str((self.total_groceries_price*0.1)))
            # ========= drinks
            self.drink_maza_v = self.maza_data.get() * 60
            self.drnik_coca_cola_v = self.coca_cola_data.get() * 60
            self.drink_frooti_v = self.frooti_data.get() * 50
            self.drink_thumbs_up_v = self.thumps_up_data.get() * 45
            self.drink_limca_v = self.limca_data.get() * 40
            self.drink_sprite_v = self.sprite_data.get() * 60
            self.total_drinks_price = float(
                self.drink_maza_v + self.drnik_coca_cola_v +
                self.drink_frooti_v + self.drink_thumbs_up_v +
                self.drink_limca_v + self.drink_sprite_v
            )
            self.drinks_price_data.set(str('Rs.') + str(self.total_drinks_price))
            self.drinks_tax_data.set(str('Rs.') + str((self.total_drinks_price*0.05)))
        else:
            messagebox.showerror('TK Retail Store', 'Customer name required!')
    # ==================================== bill function
    def welcome_bill(self):
        self.textArea.delete('1.0',END)
        self.textArea.insert(END, '\tWelcome To Alpha Retail Shop\n')
        self.textArea.insert(END, '\nBill Number   : {bn}'.format(bn=self.bill_number_data.get()))
        self.textArea.insert(END, '\nCustomer Name : {cn}'.format(cn=self.customer_name_data.get()))
        self.textArea.insert(END, '\nPhone Number  : {pn}'.format(pn=self.contact_number_data.get()))
        self.textArea.insert(END, '\n======== **** ======== **** ======== ***')
        self.textArea.insert(END, '\nProduct:\t\tQTY: Price')
        self.textArea.insert(END, '\n======== **** ======== **** ======== ***')
    def bill_area(self):
        if self.customer_name_data.get() == "":
            messagebox.showerror('TK Retail Store', 'Consumer name Required!')
        elif self.cosmetic_tax_data.get() in ('Rs.0.0','0.0')\
                and self.groceries_tax_data.get() in ('Rs.0.0','0.0')\
                and self.drinks_tax_data.get() in ('Rs.0.0','0.0'):
            messagebox.showerror('TK Retail Store', 'No item selected')
        else:
            self.welcome_bill()
            # ========= cosmetics
            if self.bath_soap_data.get() != 0:
                self.textArea.insert(
                    END, '\nBath Soap \t\t{qty}\tRs. {pr}'.format(
                        qty=str(self.bath_soap_data.get()), pr=str(self.cosmetic_bath_soap_v)
                    )
                )
            if self.face_cream_data.get() != 0:
                self.textArea.insert(
                    END, '\nFace Cream \t\t{qty}\tRs. {pr}'.format(
                        qty=str(self.face_cream_data.get()), pr=str(self.cosmetic_face_cream_v)
                    )
                )
            if self.face_wash_data.get() != 0:
                self.textArea.insert(
                    END, '\nFace Wash\t \t{qty}\tRs. {pr}'.format(
                        qty=str(self.face_wash_data.get()), pr=str(self.cosmetic_face_wash_v)
                    )
                )
            if self.hair_spray_data.get() != 0:
                self.textArea.insert(
                    END, '\nHair Spray\t \t{qty}\tRs. {pr}'.format(
                        qty=str(self.hair_spray_data.get()), pr=str(self.cosmetic_hair_spray_v)
                    )
                )
            if self.hair_gel_data.get() != 0:
                self.textArea.insert(
                    END, '\nHair Gel\t \t{qty}\tRs. {pr}'.format(
                        qty=str(self.hair_gel_data.get()), pr=str(self.cosmetic_hair_gel_v)
                    )
                )
            if self.body_lotion_data.get() != 0:
                self.textArea.insert(
                    END, '\nBody Lotion\t \t{qty}\tRs. {pr}'.format(
                        qty=str(self.body_lotion_data.get()), pr=str(self.cosmetic_body_lotion_v)
                    )
                )
            # ========= groceries
            if self.rice_data.get() != 0:
                self.textArea.insert(
                    END, '\nRice    \t\t{qty}\tRs. {pr}'.format(
                        qty=str(self.rice_data.get()), pr=str(self.groceries_rice_v)
                    )
                )
            if self.food_oil_data.get() != 0:
                self.textArea.insert(
                    END, '\nFood Oil\t\t{qty}\tRs. {pr}'.format(
                        qty=str(self.food_oil_data.get()), pr=str(self.groceries_food_oil_v)
                    )
                )
            if self.daal_data.get() != 0:
                self.textArea.insert(
                    END, '\nDaal    \t\t{qty}\tRs. {pr}'.format(
                        qty=str(self.daal_data.get()), pr=str(self.groceries_daal_v)
                    )
                )
            if self.wheat_data.get() != 0:
                self.textArea.insert(
                    END, '\nWheat    \t\t{qty}\tRs. {pr}'.format(
                        qty=str(self.wheat_data.get()), pr=str(self.groceries_wheat_v)
                    )
                )
            if self.sugar_data.get() != 0:
                self.textArea.insert(
                    END, '\nSugar    \t\t{qty}\tRs. {pr}'.format(
                        qty=str(self.sugar_data.get()), pr=str(self.groceries_sugar_v)
                    )
                )
            if self.tea_data.get() != 0:
                self.textArea.insert(
                    END, '\nTea      \t\t{qty}\tRs. {pr}'.format(
                        qty=str(self.tea_data.get()), pr=str(self.groceries_tea_v)
                    )
                )
            # ========= groceries
            if self.maza_data.get() != 0:
                self.textArea.insert(
                    END, '\nMaza     \t\t{qty}\tRs. {pr}'.format(
                        qty=str(self.maza_data.get()), pr=str(self.drink_maza_v)
                    )
                )
            if self.coca_cola_data.get() != 0:
                self.textArea.insert(
                    END, '\nCoca Cola\t\t{qty}\tRs. {pr}'.format(
                        qty=str(self.coca_cola_data.get()), pr=str(self.drnik_coca_cola_v)
                    )
                )
            if self.frooti_data.get() != 0:
                self.textArea.insert(
                    END, '\nFrooti   \t\t{qty}\tRs. {pr}'.format(
                        qty=str(self.frooti_data.get()), pr=str(self.drink_frooti_v)
                    )
                )
            if self.thumps_up_data.get() != 0:
                self.textArea.insert(
                    END, '\nThumps Up\t\t{qty}\tRs. {pr}'.format(
                        qty=str(self.thumps_up_data.get()), pr=str(self.drink_thumbs_up_v)
                    )
                )
            if self.limca_data.get() != 0:
                self.textArea.insert(
                    END, '\nLimca    \t\t{qty}\tRs. {pr}'.format(
                        qty=str(self.limca_data.get()), pr=str(self.drink_limca_v)
                    )
                )
            if self.sprite_data.get() != 0:
                self.textArea.insert(
                    END, '\nSprite   \t\t{qty}\tRs. {pr}'.format(
                        qty=str(self.sprite_data.get()), pr=str(self.drink_sprite_v)
                    )
                )

            if self.cosmetic_tax_data.get() != 'Rs.0.0':
                self.textArea.insert(END, '\n----------------------------------------')
                self.textArea.insert(
                    END, '\nCosmetic 5% tax: \t{tx}   \nTotal: Rs.{tp}'.format(
                        tx=str('Rs.') + str(round((self.total_cosmetics_price) * 0.05, 2)),
                        tp=str(self.total_cosmetics_price)
                    )
                )
            if self.groceries_tax_data.get() != 'Rs.0.0':
                self.textArea.insert(END, '\n----------------------------------------')
                self.textArea.insert(
                    END, '\nGroceries 10% tax:\t{tx} \n{tp}'.format(
                        tx=str('Rs.') + str(round((self.total_groceries_price) * 0.1, 2)),
                        tp=str(str('Total: Rs.') + str(self.total_groceries_price))
                    )
                )
            if self.drinks_tax_data.get() != 'Rs.0.0':
                self.textArea.insert(END, '\n----------------------------------------')
                self.textArea.insert(
                    END, '\nDrinks 5% tax:\t    {tx} \n{tp}'.format(
                        tx=str('Rs.') + str(round((self.total_drinks_price) * 0.1, 2)),
                        tp=str(str('Total: Rs.') + str(self.total_drinks_price))
                    )
                )
            self.textArea.insert(END, '\n----------------------------------------')
            best_price = ((self.total_cosmetics_price) + (round((self.total_cosmetics_price) * 0.05, 2))) + \
                         ((self.total_groceries_price) + (round((self.total_groceries_price) * 0.1, 2))) + \
                         ((self.total_drinks_price) + (round((self.total_drinks_price) * 0.05, 2)))
            self.textArea.insert(
                END, '\nBest Price     \t\tRs.{tp}'.format(
                    tp=str(best_price)
                )
            )
            self.save_bill()
    def save_bill(self):
        response = messagebox.askyesno('TK Retail Store', 'want to save the bill?')
        if response == True:
            self.save_data = self.textArea.get('1.0',END)
            print(self.save_data)
            file = open('Files/'+str(self.bill_number_data.get())+'.txt','w')
            if str(self.bill_number_data.get()+'.txt') in os.listdir('Files'):
                messagebox.showerror('TK Retail Store', 'Bill already exists!')
            else:
                file.write(self.save_data)
                file.close()
                messagebox.showinfo('TK Retail Store', 'saved successfully')
    # ==================================== exit function
    def exit(self):
        response = messagebox.askyesno('TK Retail Store', 'Do you want to exit?')
        if response == True:
            self.root.destroy()
    # ==================================== clear function
    def clear(self):
        self.textArea.delete('1.0', END)
        self.bath_soap_data.set(0)
        self.face_cream_data.set(0)
        self.face_wash_data.set(0)
        self.hair_spray_data.set(0)
        self.hair_gel_data.set(0)
        self.body_lotion_data.set(0)
        self.rice_data.set(0)
        self.food_oil_data.set(0)
        self.daal_data.set(0)
        self.wheat_data.set(0)
        self.sugar_data.set(0)
        self.tea_data.set(0)
        self.maza_data.set(0)
        self.coca_cola_data.set(0)
        self.frooti_data.set(0)
        self.thumps_up_data.set(0)
        self.limca_data.set(0)
        self.sprite_data.set(0)
        self.cosmetic_tax_data.set(0.0)
        self.groceries_tax_data.set(0.0)
        self.drinks_tax_data.set(0.0)
        self.cosmetic_price_data.set(0.0)
        self.groceries_price_data.set(0.0)
        self.drinks_price_data.set(0.0)
        self.customer_name_data.set("")
        self.bill_number_data.set("")
        self.contact_number_data.set("")
    # ==================================== retrieve bill function
    def retrieve(self):
        if (str(self.bill_number_data.get()+'.txt') in os.listdir('Files')):
            file = open('Files/{n}'.format(n=self.bill_number_data.get()) + '.txt', 'r')
            self.textArea.delete('1.0', END)
            for data in file:
                self.textArea.insert(END, data)
            file.close()
        else:
            messagebox.showerror('TK Retail Store', 'Bill: {b}, not found'.format(b=self.bill_number_data.get()))

root = Tk()
obj = BillApp(root)
root.mainloop()
