import tkinter as tk

class Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
    
    def show(self):
        self.lift()

class HomePage(Page):
    def __init__(self, parent, controller):
        Page.__init__(self, parent, controller)
        self.addListBtnImg = tk.PhotoImage(file='images/list_img.png')
        self.addPersonnelImg = tk.PhotoImage(file='images/add_personell_img.png')
        self.payroll_img = tk.PhotoImage(file='images/payroll_img.png')
        
        header_menu_lbl = tk.LabelFrame(self,width=1200,height=80,bg='#BEC8CF',bd=5,relief='solid')
        header_menu_txt = tk.Label(self,text='PAYROLL',font=('B Titr',23,'bold'),bg='#BEC8CF')
        
        self.btn_list = tk.Button(self,width=400,height=620,image=self.addListBtnImg,bd=0,cursor='hand2',activebackground='#191818', command=lambda: controller.show_page(AboutPage))
        self.btn_add_personnel = tk.Button(self,width=400,height=620,image=self.addPersonnelImg,bd=0,cursor='hand2',activebackground='#191818')
        self.btn_payroll = tk.Button(self,width=400,height=620,image=self.payroll_img,bd=0,cursor='hand2',activebackground='#191818')
        header_menu_txt.place(x=510,y=15)
        header_menu_lbl.place(x=0,y=0)
        self.btn_list.place(x=0,y=80)
        self.btn_add_personnel.place(x=400,y=80)
        self.btn_payroll.place(x=800,y=80)

class AboutPage(Page):
    def __init__(self, parent, controller):
        Page.__init__(self, parent, controller)
        header_menu_lbl = tk.LabelFrame(self,width=1200,height=80,bg='red',bd=5,relief='solid')
        header_menu_txt = tk.Label(self,text='PAYROLL',font=('B Titr',23,'bold'),bg='#BEC8CF')
        header_menu_txt.place(x=510,y=15)
        header_menu_lbl.place(x=0,y=0)
        label = tk.Label(self, text="درباره ما")
        label.place(x=250,y=300)
        button = tk.Button(self, text="رفتن به تماس با ما", command=lambda: controller.show_page(ContactPage))
        button.place(x=250,y=500)

class ContactPage(Page):
    def __init__(self, parent, controller):
        Page.__init__(self, parent, controller)
        label = tk.Label(self, text="تماس با ما")
        label.pack()
        button = tk.Button(self, text="رفتن به صفحه اصلی", command=lambda: controller.show_page(HomePage))
        button.pack()

class MyApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        container = tk.Frame(self)
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
