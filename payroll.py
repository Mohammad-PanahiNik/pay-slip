from tkinter import *

class Page(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
    
    def show(self):
        self.lift()

class HomePage(Page):
    def __init__(self, parent, controller):
        Page.__init__(self, parent, controller)
        self.addListBtnImg = PhotoImage(file='images/list_img.png')
        self.addPersonnelImg = PhotoImage(file='images/add_personell_img.png')
        self.payroll_img = PhotoImage(file='images/payroll_img.png')
        
        header_menu_lbl = LabelFrame(self,width=1200,height=80,bg='#BEC8CF',bd=5,relief='solid')
        header_menu_txt = Label(self,text='PAYROLL',font=('B Titr',23,'bold'),bg='#BEC8CF')
        self.btn_list = Button(self,width=400,height=620,image=self.addListBtnImg,bd=0,cursor='hand2',activebackground='#191818', command=lambda: controller.show_page(AboutPage))
        self.btn_add_personnel = Button(self,width=400,height=620,image=self.addPersonnelImg,bd=0,cursor='hand2',activebackground='#191818')
        self.btn_payroll = Button(self,width=400,height=620,image=self.payroll_img,bd=0,cursor='hand2',activebackground='#191818')
        header_menu_txt.place(x=510,y=15)
        header_menu_lbl.place(x=0,y=0)
        self.btn_list.place(x=0,y=80)
        self.btn_add_personnel.place(x=400,y=80)
        self.btn_payroll.place(x=800,y=80)

class AboutPage(Page):
    def __init__(self, parent, controller):
        Page.__init__(self, parent, controller)
        self.saveInfo = PhotoImage(file='images/zakhireInfoBtn.png')
        self.bgRegisterImg = PhotoImage(file='images/bgregister.png')
        self.profileImg = PhotoImage(file='images/profile.png')
        bgRegister = Label(self,image=self.bgRegisterImg,bg='#B2B2B2')
        self.jayAks = Label(bgRegister,image=self.profileImg,bd=2)
        self.entPersonnelID = Entry(bgRegister,font=('Tahoma',13),justify='right',bd=0,bg='#B2B2B2')
        self.entNameRegister = Entry(bgRegister,font=('Tahoma',13),justify='right',bd=0,bg='#B2B2B2')
        self.entNationalCode = Entry(bgRegister,font=('Tahoma',13),justify='right',bd=0,bg='#B2B2B2')
        self.entFather = Entry(bgRegister,font=('Tahoma',13),justify='right',bd=0,bg='#B2B2B2')
        self.entBorn = Entry(bgRegister,font=('Tahoma',13),justify='right',bd=0,bg='#B2B2B2')
        self.entShenasname = Entry(bgRegister,font=('Tahoma',13),justify='right',bd=0,bg='#B2B2B2')
        self.entChildren = Entry(bgRegister,font=('Tahoma',13),justify='right',bd=0,bg='#B2B2B2')
        self.entMaritalStatus = Entry(bgRegister,font=('Tahoma',13),justify='right',bd=0,bg='#B2B2B2')
        self.entPhone = Entry(bgRegister,font=('Tahoma',13),justify='right',bd=0,bg='#B2B2B2')
        self.entSalaryBase = Entry(bgRegister,font=('Tahoma',13),justify='right',bd=0,bg='#B2B2B2')
        self.entContractType = Entry(bgRegister,font=('Tahoma',13),justify='right',bd=0,bg='#B2B2B2')
        self.entSofContract = Entry(bgRegister,font=('Tahoma',13),justify='right',bd=0,bg='#B2B2B2')
        self.entEofContract = Entry(bgRegister,font=('Tahoma',13),justify='right',bd=0,bg='#B2B2B2')
        self.btnSaveInfo = Button(bgRegister,image=self.saveInfo,bg='#EAEAEA',bd=0,activebackground='#EAEAEA',cursor='hand2',command=lambda: controller.show_page(ContactPage))
        button = Button(self, text="رفتن به تماس با ما", command=lambda: controller.show_page(ContactPage))
        
        button.place(x=250,y=500)
        bgRegister.place(x=12,y=10)
        self.jayAks.place(x=40,y=30)
        self.entPersonnelID.place(x=825,y=82)
        self.entNameRegister.place(x=655,y=183)
        self.entNationalCode.place(x=655,y=247)
        self.entFather.place(x=655,y=311)
        self.entBorn.place(x=655,y=375)
        self.entShenasname.place(x=655,y=439)
        self.entChildren.place(x=655,y=503)
        self.entMaritalStatus.place(x=135,y=183)
        self.entPhone.place(x=135,y=247)
        self.entSalaryBase.place(x=135,y=311)
        self.entContractType.place(x=135,y=375)
        self.entSofContract.place(x=135,y=439)
        self.entEofContract.place(x=135,y=503)
        self.btnSaveInfo.place(x=450,y=575)
        
        self.entPersonnelID.focus()
        self.entPersonnelID.bind('<Return>',lambda event :self.entNameRegister.focus())
        self.entNameRegister.bind('<Return>',lambda event :self.entNationalCode.focus())
        self.entNationalCode.bind('<Return>',lambda event :self.entFather.focus())
        self.entFather.bind('<Return>',lambda event :self.entBorn.focus())
        self.entBorn.bind('<Return>',lambda event :self.entShenasname.focus())
        self.entShenasname.bind('<Return>',lambda event :self.entChildren.focus())
        self.entChildren.bind('<Return>',lambda event :self.entMaritalStatus.focus())
        self.entMaritalStatus.bind('<Return>',lambda event :self.entPhone.focus())
        self.entPhone.bind('<Return>',lambda event :self.entSalaryBase.focus())
        self.entSalaryBase.bind('<Return>',lambda event :self.entContractType.focus())
        self.entContractType.bind('<Return>',lambda event :self.entSofContract.focus())
        self.entSofContract.bind('<Return>',lambda event :self.entEofContract.focus())
        self.entEofContract.bind('<Return>',lambda event :self.btnSaveInfo.focus())
        # self.btnSaveInfo.bind('<Return>',self.funcSaveInfo)
        # self.btnSaveInfo.bind('<Button-1>',self.funcSaveInfo)
        # self.jayAks.bind('<Button-1>',self.funcAks)

class ContactPage(Page):
    def __init__(self, parent, controller):
        Page.__init__(self, parent, controller)
        label = Label(self, text="تماس با ما")
        label.pack()
        button = Button(self, text="رفتن به صفحه اصلی", command=lambda: controller.show_page(HomePage))
        button.pack()

class MyApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry("1200x700+320+150")
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.pages = {}
        self.current_page = None

        for PageClass in (HomePage, AboutPage, ContactPage):
            page = PageClass(container, self)
            self.pages[PageClass] = page
            page.grid(row=0, column=0, sticky="nsew")

        self.show_page(HomePage)

    def show_page(self, PageClass):
        page = self.pages[PageClass]
        if self.current_page is not None:
            self.current_page.pack_forget()
        page.show()
        self.current_page = page

app = MyApp()
app.mainloop()
