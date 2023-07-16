from tkinter import *
from tkinter import filedialog
import sqlite3 as sql
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox

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
        self.payslip_img = PhotoImage(file='images/payroll_img.png')
        
        header_menu_lbl = LabelFrame(self,width=1200,height=80,bg='#BEC8CF',bd=5,relief='solid')
        header_menu_txt = Label(self,text='Pay Slip',font=('B Titr',23,'bold'),bg='#BEC8CF')
        self.btn_list = Button(self,width=400,height=620,image=self.addListBtnImg,bd=0,cursor='hand2',activebackground='#191818',
                               command=self.open_list)
        self.btn_add_personnel = Button(self,width=400,height=620,image=self.addPersonnelImg,bd=0,cursor='hand2',activebackground='#191818',
                                        command=lambda: controller.show_page(AddPersonnel))
        self.btn_payslip = Button(self,width=400,height=620,image=self.payslip_img,bd=0,cursor='hand2',activebackground='#191818',
                                  command=lambda: controller.show_page(Payslip))
        header_menu_txt.place(x=510,y=15)
        header_menu_lbl.place(x=0,y=0)
        self.btn_list.place(x=0,y=80)
        self.btn_add_personnel.place(x=400,y=80)
        self.btn_payslip.place(x=800,y=80)

    def open_list(self):
        personnelListP = self.controller.pages[PersonnelList]
        personnelListP.data_to_list_personnel()
        self.controller.show_page(PersonnelList)

class AddPersonnel(Page):
    def __init__(self, parent, controller):
        Page.__init__(self, parent, controller)
        self.configure(bg='#B2B2B2')
        self.saveInfo = PhotoImage(file='images/zakhireInfoBtn.png')
        self.bgRegisterImg = PhotoImage(file='images/bgregister.png')
        self.homeImg=PhotoImage(file='images/homeImg.png')
        self.profileImg = PhotoImage(file='images/profile.png')

        bgRegister = Label(self,image=self.bgRegisterImg,bg='#B2B2B2')
        self.imgSelectorBg_kala = Label(bgRegister,image=self.profileImg,bd=2)
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
        self.btnSaveInfo = Button(bgRegister,image=self.saveInfo,bg='#EAEAEA',bd=0,activebackground='#EAEAEA',cursor='hand2',
                                  command=self.funcSaveInfo)
        homeBtnPs=Button(bgRegister,image=self.homeImg,bg='#EAEAEA',activebackground='#EAEAEA',bd=0,cursor='hand2',
                         command=lambda: controller.show_page(HomePage))
        
        bgRegister.place(x=12,y=10)
        self.imgSelectorBg_kala.place(x=40,y=30)
        self.entPersonnelID.place(x=825,y=82)
        self.entNameRegister.place(x=655,y=183)
        self.entNationalCode.place(x=655,y=247)
        self.entFather.place(x=655,y=311)
        self.entChildren.place(x=655,y=375)
        self.entBorn.place(x=655,y=439)
        self.entShenasname.place(x=655,y=503)
        self.entMaritalStatus.place(x=135,y=183)
        self.entPhone.place(x=135,y=247)
        self.entSalaryBase.place(x=135,y=311)
        self.entContractType.place(x=135,y=375)
        self.entSofContract.place(x=135,y=439)
        self.entEofContract.place(x=135,y=503)
        self.btnSaveInfo.place(x=450,y=575)
        homeBtnPs.place(x=1105,y=15)
        
        self.entPersonnelID.focus()
        self.entPersonnelID.bind('<Return>',lambda event :self.entNameRegister.focus())
        self.entNameRegister.bind('<Return>',lambda event :self.entNationalCode.focus())
        self.entNationalCode.bind('<Return>',lambda event :self.entFather.focus())
        self.entFather.bind('<Return>',lambda event :self.entChildren.focus())
        self.entChildren.bind('<Return>',lambda event :self.entBorn.focus())
        self.entBorn.bind('<Return>',lambda event :self.entShenasname.focus())
        self.entShenasname.bind('<Return>',lambda event :self.entMaritalStatus.focus())
        self.entMaritalStatus.bind('<Return>',lambda event :self.entPhone.focus())
        self.entPhone.bind('<Return>',lambda event :self.entSalaryBase.focus())
        self.entSalaryBase.bind('<Return>',lambda event :self.entContractType.focus())
        self.entContractType.bind('<Return>',lambda event :self.entSofContract.focus())
        self.entSofContract.bind('<Return>',lambda event :self.entEofContract.focus())
        self.entEofContract.bind('<Return>',lambda event :self.btnSaveInfo.focus())
    
        self.imgSelectorBg_kala.bind('<Button-1>', self.funcAddImg_kala)
        self.btnSaveInfo.bind('<Return>',self.funcSaveInfo)
        # self.btnSaveInfo.bind('<Button-1>',self.funcSaveInfo)

    def funcAddImg_kala(self,event=None):
        self.img_name = filedialog.askopenfilename()
        self.procuct_img = Image.open(self.img_name)
        self.procuct_image = self.procuct_img.resize((100, 100))
        self.product_photo = ImageTk.PhotoImage(self.procuct_image)
        self.imgSelectorBg_kala['image']=self.product_photo
    
    def covert_to_binary_data(self,filename):
        with open (filename , 'rb') as f:
            blobdata = f.read()
        return blobdata
       
    def funcSaveInfo(self,event=None):
        PersonnelID = self.entPersonnelID.get()
        NameRegister = self.entNameRegister.get()
        NationalCode = self.entNationalCode.get()
        Father = self.entFather.get()
        Born = self.entBorn.get()
        Shenasname = self.entShenasname.get()
        Children = self.entChildren.get()
        MaritalStatus = self.entMaritalStatus.get()
        Phone = self.entPhone.get()
        SalaryBase = self.entSalaryBase.get()
        ContractType = self.entContractType.get()
        SofContract = self.entSofContract.get()
        EofContract = self.entEofContract.get()
        photo = self.covert_to_binary_data(self.img_name)
        
        self.con=sql.connect('mydb.db')
        self.cur=self.con.cursor()
        data=(PersonnelID,NameRegister,NationalCode,Father,Born,Shenasname,Children,MaritalStatus,Phone,
                        SalaryBase,ContractType,SofContract,EofContract,photo)
        self.cur.execute('''CREATE TABLE IF NOT EXISTS personnel (id TEXT PRIMARY KEY,name TEXT,nationalId TEXT,father TEXT
                         ,born TEXT,shenasname TEXT,children TEXT,marital_status TEXT,phone TEXT,salary_base TEXT,
                         contract_type TEXT,start_of_contract TEXT,end_of_contract TEXT,photo BLOB NOT NULL)''')
        self.cur.execute('''INSERT INTO personnel(id,name,nationalId,father,born,shenasname,children,marital_status,phone
                         ,salary_base,contract_type,start_of_contract,end_of_contract,photo) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',data)
        self.con.commit()
        
        self.entPersonnelID.delete(0,END)
        self.entNameRegister.delete(0,END)
        self.entNationalCode.delete(0,END)
        self.entFather.delete(0,END)
        self.entBorn.delete(0,END)
        self.entShenasname.delete(0,END)
        self.entChildren.delete(0,END)
        self.entMaritalStatus.delete(0,END)
        self.entPhone.delete(0,END)
        self.entSalaryBase.delete(0,END)
        self.entContractType.delete(0,END)
        self.entSofContract.delete(0,END)
        self.entEofContract.delete(0,END)
        self.imgSelectorBg_kala['image']=self.profileImg
        self.entPersonnelID.focus()
        
    
class Payslip(Page):
    def __init__(self, parent, controller):
        Page.__init__(self, parent, controller)
        self.payeHoghogh=0
        self.configure(bg='#B2B2B2')
        self.PaySlipBg=PhotoImage(file='images/payslipBg1.png')
        self.searchBtn=PhotoImage(file='images/searchBtn.png')
        self.homeImg=PhotoImage(file='images/homeImg.png')
        self.issuanceImg=PhotoImage(file='images/issuanceImg.png')

        bgpayslip=Label(self,image=self.PaySlipBg,bg='#B2B2B2')
        self.entSearchId=Entry(bgpayslip,font=('tahoma',13),bg='#B2B2B2',fg='#3C4048',bd=0)
        btnSearch=Button(bgpayslip,image=self.searchBtn,bg='#EAEAEA',activebackground='#EAEAEA',bd=0,cursor='hand2',command=self.searchId)
        frmPs=LabelFrame(bgpayslip,bg='#EAEAEA',bd=0)
        self.lblNamePS=Label(frmPs,text='',fg='#3C4048',font=('tahoma',15),bg='#EAEAEA')
        self.lblnationalPS=Label(frmPs,text='',fg='#3C4048',font=('tahoma',15),bg='#EAEAEA')
        self.lblPhonePS=Label(frmPs,text='',fg='#3C4048',font=('tahoma',15),bg='#EAEAEA')
        self.lblMaritalPS=Label(frmPs,text='',fg='#3C4048',font=('tahoma',15),bg='#EAEAEA')
        self.lblChildPS=Label(frmPs,text='',fg='#3C4048',font=('tahoma',15),bg='#EAEAEA')

        self.entDays=Entry(bgpayslip,fg='#3C4048',font=('tahoma',13),bg='#B2B2B2',bd=0)
        self.entDate=Entry(bgpayslip,fg='#3C4048',font=('tahoma',13),bg='#B2B2B2',bd=0)
        self.entOvertime=Entry(bgpayslip,fg='#3C4048',font=('tahoma',13),bg='#B2B2B2',bd=0)
        self.entHClosing=Entry(bgpayslip,fg='#3C4048',font=('tahoma',13),bg='#B2B2B2',bd=0)
        self.entNightWork=Entry(bgpayslip,fg='#3C4048',font=('tahoma',13),bg='#B2B2B2',bd=0)
        btnissuance=Button(bgpayslip,image=self.issuanceImg,bg='#EAEAEA',bd=0,activebackground='#EAEAEA',cursor='hand2',
                           command=self.issuanceFunc)
        homeBtnPs=Button(bgpayslip,image=self.homeImg,bg='#EAEAEA',activebackground='#EAEAEA',bd=0,cursor='hand2',
                            command=lambda: controller.show_page(HomePage))
        
        # entSearchId.bind('<Return>',lambda event :funcSearch())
        self.entSearchId.focus()
        self.entDays.bind('<Return>',lambda event :self.entDate.focus())
        self.entDate.bind('<Return>',lambda event :self.entOvertime.focus())
        self.entOvertime.bind('<Return>',lambda event :self.entHClosing.focus())
        self.entHClosing.bind('<Return>',lambda event :self.entNightWork.focus())
        # entNightWork.bind('<Return>',lambda event :funcIssuance())

        
        bgpayslip.place(x=20,y=29)
        self.entSearchId.place(x=488,y=100)
        btnSearch.place(x=505,y=147)
        frmPs.place(x=745,y=295)
        self.lblNamePS.grid(row=1,pady=13)
        self.lblnationalPS.grid(row=2,pady=13)
        self.lblPhonePS.grid(row=3,pady=13)
        self.lblMaritalPS.grid(row=4,pady=13)
        self.lblChildPS.grid(row=5,pady=13)
        self.entDays.place(x=188,y=324)
        self.entDate.place(x=188,y=372)
        self.entOvertime.place(x=188,y=419)
        self.entHClosing.place(x=188,y=467)
        self.entNightWork.place(x=188,y=514)
        btnissuance.place(x=261,y=563)
        homeBtnPs.place(x=1090,y=15)
        
    def searchId(self):
        Id=self.entSearchId.get()
        self.con=sql.connect('mydb.db')
        self.cur=self.con.cursor()
        self.count=0
        if Id !='':
            row=self.cur.execute('SELECT * FROM personnel WHERE id="{}"'.format(Id))
            info=list(row)
            self.lblNamePS['text']=info[0][1]
            self.lblnationalPS['text']=info[0][2]
            self.lblPhonePS['text']=info[0][8]
            self.lblMaritalPS['text']=info[0][7]
            self.lblChildPS['text']=info[0][6]
            self.payeHoghogh=info[0][9]
            self.entDays.focus()

    def issuanceFunc(self):
        haghMaskan=900000
        bonRefahi=1100000
        self.days=self.entDays.get()
        self.date=self.entDate.get()
        self.overtime=self.entOvertime.get()
        self.closing=self.entHClosing.get()
        self.nightWork=self.entNightWork.get()
        self.id2=self.entSearchId.get()
        paySlip2P = self.controller.pages[Payslip2]
        
        ezafeKari=int(self.payeHoghogh)/220*0.4*int(self.overtime)
        tatilKari=int(self.payeHoghogh)/220*0.4*int(self.closing)
        shabKari=int(self.payeHoghogh)/220*0.35*int(self.nightWork)
        payeRozane=int(self.payeHoghogh)/int(self.days)
        haghOlad=530000*int(self.lblChildPS['text'])
        payeSaati=int(payeRozane)/8
        bimeKol=(int(self.payeHoghogh)+int(haghMaskan)+int(bonRefahi))*0.3
        haghKarfarma=int(self.payeHoghogh)*0.23
        haghKargar=int(self.payeHoghogh)*0.07
        daramadHa=int(self.payeHoghogh)+int(ezafeKari)+int(tatilKari)+int(shabKari)+int(haghOlad)+int(haghMaskan)+int(bonRefahi)
        kosorat=int(haghKargar)
        khalesPardakht=int(daramadHa)-int(kosorat)
        paySlip2P.lblNamePSP2['text']=self.lblNamePS['text']
        paySlip2P.lblpersonnelIdPSP2['text']=self.id2
        paySlip2P.lblbime['text']='''{:,}'''.format(int(bimeKol))
        paySlip2P.lblHaghBimeK['text']='''{:,}'''.format(int(haghKargar))
        paySlip2P.lblHaghBimeR['text']='''{:,}'''.format(int(haghKarfarma))
        paySlip2P.dailyWage['text']='''{:,}'''.format(int(payeRozane))
        paySlip2P.hourlyWage['text']='''{:,}'''.format(int(payeSaati))
        paySlip2P.lblBonRefahi['text']='''{:,}'''.format(int(bonRefahi))
        paySlip2P.lblHaghMskn['text']='''{:,}'''.format(int(haghMaskan))
        paySlip2P.lblDays['text']='''{: <15}'''.format(self.days)
        paySlip2P.lblDate['text']='''{: <15}'''.format(self.date)
        paySlip2P.lblOvertime['text']='''{: <15}'''.format(self.overtime)
        paySlip2P.lblHClosing['text']='''{: <15}'''.format(self.closing)
        paySlip2P.lblNightWork['text']='''{: <15}'''.format(self.nightWork)
        paySlip2P.lblKosorat['text']='''{:,}'''.format(int(kosorat))
        paySlip2P.lblDaramad['text']='''{:,}'''.format(int(daramadHa))
        paySlip2P.pardakhti['text']='''{:,}'''.format(int(khalesPardakht))
        paySlip2P.controller.show_page(Payslip2)
        self.entSearchId.delete(0,END)
        self.entNightWork.delete(0,END)
        self.entHClosing.delete(0,END)
        self.entHClosing.delete(0,END)
        self.entOvertime.delete(0,END)
        self.entDate.delete(0,END)
        self.entDays.delete(0,END)
        self.lblNamePS['text']=''
        self.lblMaritalPS['text']=''
        self.lblChildPS['text']=''
        self.lblPhonePS['text']=''
        self.lblnationalPS['text']=''
        self.entSearchId.focus()
        
        

class Payslip2(Page):
    def __init__(self, parent, controller):
        Page.__init__(self, parent, controller)
        self.configure(bg='#B2B2B2')
        
        self.homeImg=PhotoImage(file='images/homeImg.png')
        self.PaySlip2Bg=PhotoImage(file='images/bgpaySlip2.png')
        self.printImg=PhotoImage(file='images/printImg.png')  
        
        bgPaySlip2=Label(self,image=self.PaySlip2Bg,bg='#B2B2B2')
        self.lblNamePSP2=Label(bgPaySlip2,fg='#333333',font=('tahoma',15),bg='#EAEAEA',text='')
        self.lblpersonnelIdPSP2=Label(bgPaySlip2,fg='#333333',font=('tahoma',15),bg='#EAEAEA',text='')
        self.lblbime=Label(bgPaySlip2,fg='#333333',font=('tahoma',15),bg='#EAEAEA',text='')
        self.lblHaghBimeK=Label(bgPaySlip2,fg='#333333',font=('tahoma',15),bg='#EAEAEA',text='')
        self.lblHaghBimeR=Label(bgPaySlip2,fg='#333333',font=('tahoma',15),bg='#EAEAEA',text='')
        self.dailyWage=Label(bgPaySlip2,fg='#333333',font=('tahoma',15),bg='#EAEAEA',text='')
        self.hourlyWage=Label(bgPaySlip2,fg='#333333',font=('tahoma',15),bg='#EAEAEA',text='')
        self.lblBonRefahi=Label(bgPaySlip2,fg='#333333',font=('tahoma',15),bg='#EAEAEA',text='')
        self.lblHaghMskn=Label(bgPaySlip2,fg='#333333',font=('tahoma',15),bg='#EAEAEA',text='')
        self.btnPrint=Button(self,image=self.printImg,bg='#B2B2B2',bd=0,activebackground='#525252',cursor='hand2')
        frmPs2=LabelFrame(bgPaySlip2,bg='#EAEAEA',bd=0)
        self.lblDays=Label(frmPs2,fg='#333333',font=('tahoma',15),bg='#EAEAEA',text='')
        self.lblDate=Label(frmPs2,fg='#333333',font=('tahoma',15),bg='#EAEAEA',text='')
        self.lblOvertime=Label(frmPs2,fg='#333333',font=('tahoma',15),bg='#EAEAEA',text='')
        self.lblHClosing=Label(frmPs2,fg='#333333',font=('tahoma',15),bg='#EAEAEA',text='')
        self.lblNightWork=Label(frmPs2,fg='#333333',font=('tahoma',15),bg='#EAEAEA',text='')
        self.lblKosorat=Label(self,text='',fg='#333333',font=('tahoma',24),bg='#EAEAEA')
        self.lblDaramad=Label(self,text='',fg='#333333',font=('tahoma',24),bg='#EAEAEA')
        self.pardakhti=Label(self,text='',fg='#EAEAEA',font=('tahoma',24),bg='#3C4048')
        homeBtnPs=Button(self,image=self.homeImg,bg='#B2B2B2',activebackground='#B2B2B2',bd=0,cursor='hand2',
                            command=lambda: controller.show_page(HomePage))
        
        bgPaySlip2.place(x=20,y=10)
        homeBtnPs.place(x=650,y=642)
        self.lblNamePSP2.place(x=600,y=19)
        self.lblpersonnelIdPSP2.place(x=250,y=19)
        self.lblbime.place(x=620,y=110)
        self.lblHaghBimeK.place(x=620,y=180)
        self.lblHaghBimeR.place(x=620,y=250)
        self.dailyWage.place(x=50,y=95)
        self.hourlyWage.place(x=50,y=152)
        self.lblBonRefahi.place(x=50,y=212)
        self.lblHaghMskn.place(x=50,y=270)
        self.btnPrint.place(x=490,y=642)
        self.lblKosorat.place(x=70,y=390)
        self.lblDaramad.place(x=70,y=460)
        self.pardakhti.place(x=70,y=555)
        frmPs2.place(x=620,y=400)
        self.lblDays.grid(row=1,pady=6)
        self.lblDate.grid(row=2,pady=6)
        self.lblOvertime.grid(row=3,pady=6)
        self.lblHClosing.grid(row=4,pady=6)
        self.lblNightWork.grid(row=5,pady=6)

class PersonnelList(Page):
    def __init__(self, parent, controller):
        Page.__init__(self, parent, controller)
        self.configure(bg='#B2B2B2')
        self.style=ttk.Style()
        self.homeImg=PhotoImage(file='images/homeImg.png')
        
        homeBtnPs=Button(self,image=self.homeImg,bg='#B2B2B2',activebackground='#B2B2B2',bd=0,cursor='hand2',
                            command=lambda: controller.show_page(HomePage))
        #list
        self.list_personnel= ttk.Treeview(self,show='headings',height=15)
        self.list_personnel['columns']=('e_contract','s_contract','Phone','NationalId','Name','id','row')
        #columns
        self.list_personnel.column('e_contract',width=170,anchor=E)
        self.list_personnel.column('s_contract',width=170,anchor=E)
        self.list_personnel.column('Phone',width=200,anchor=E)
        self.list_personnel.column('NationalId',width=200,anchor=E)
        self.list_personnel.column('Name',width=200,anchor=E)
        self.list_personnel.column('id',width=120,anchor=E)
        self.list_personnel.column('row',width=100,anchor=E)
        #heading
        self.list_personnel.heading('e_contract',text=' : پایان قرارداد',anchor=E)
        self.list_personnel.heading('s_contract',text=' : شروع قرارداد',anchor=E)
        self.list_personnel.heading('Phone',text=' : شماره موبایل',anchor=E)
        self.list_personnel.heading('NationalId',text=' : کد ملی',anchor=E)
        self.list_personnel.heading('Name',text=' : نام و نام خانوادگی',anchor=E)
        self.list_personnel.heading('id',text=' : کد کارمند',anchor=E)
        self.list_personnel.heading('row',text=' : ردیف',anchor=E)
        self.style.theme_use('clam')
        self.style.configure("Treeview.Heading",font=('Lalezar', 18),
                            padding=[0, 5, 15, 5],background='#474A56',
                            foreground="white",bd=0,relief='raised'
                            )
        self.style.map("Treeview.Heading",
            background=[('active','#686A75')])
        self.style.configure("Treeview", highlightthickness=0, 
                            height=150,
                            bd=0, font=('AraFProgram', 16),
                            background="white",foreground="black",
                            rowheight = 35,fieldbackground="white"
                            )
        self.style.map("Treeview",
            background=[('selected', '#7A8BA7')],
            foreground=[('selected', 'white')])
        
        
        self.list_personnel.place(x=20,y=70)
        homeBtnPs.place(x=1120,y=15)
    
    def data_to_list_personnel(self):
        count=0        
        self.lst=[]
        for item in self.list_personnel.get_children():
            self.list_personnel.delete(item)
        self.con=sql.connect('mydb.db')
        self.cur=self.con.cursor()
        self.cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='personnel'")
        
        self.result = self.cur.fetchone()
        if self.result != None:
            
            row=self.cur.execute('SELECT * FROM personnel')
            for i in row :
                self.lst.append(i)
            
            for i in self.lst:
                self.list_personnel.insert(parent='',index='end',text='',
                                    values=(i[12],i[11],i[8],i[2],i[1],i[0],str(count+1)))
                count += 1
        

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

        for PageClass in (HomePage, AddPersonnel, Payslip, Payslip2, PersonnelList):
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
