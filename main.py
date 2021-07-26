from tkinter import *
import tkinter as tk


class Product:
    def __init__(self, name='', specification='', info='', num=0):
        self.name = name
        self.specification = specification
        self.info = info
        self.num = num

    def setNum(self, num):
        self.num = num

    def __str__(self):
        return self.name + self.specification + self.info


class Bland:
    def __init__(self, name='', industry='', country='', bland_num='', info=''):
        self.name = name
        self.industry = industry
        self.country = country
        self.bland_num = bland_num
        self.info = info
        self.product_list = []

    def setBland(self, industry, country, bland_num, info):
        self.industry = industry
        self.country = country
        self.bland_num = bland_num
        self.info = info

    def addProduct(self, product):
        self.product_list.append(product)

    def getBlandInfo(self):
        return '<hr /><h3>产品类型</h3><p style="text-align: center;">' + self.industry + ',' + self.country + \
               '</p><hr /><h3>厂家介绍</h3><img src="http://info.aoyoumall.com/Mypicture/' + self.bland_num + \
               '.jpg" /><p>' + self.info + '</p><hr /><h3>产品介绍</h3> '

    def getProductInfo(self):
        if len(self.product_list) == 0:
            return ''
        else:
            productsinfo = ''
            i = 1
            for product in self.product_list:
                product.setNum(int(self.bland_num) + i)
                i += 1
                productsinfo = productsinfo + '<hr /><h3>' + product.name + \
                               '</h3><img src="http://info.aoyoumall.com/Mypicture/' + str(product.num) + \
                               '.jpg" /><p>规格：' + product.specification + '</p><p>' + product.info + '</p> '
            return productsinfo

    def getInfo(self):
        return self.getBlandInfo() + self.getProductInfo()


def combineInfoBland(country, industry, img_start, bland_info):
    bland.setBland(industry, country, img_start, bland_info)
    return bland.getInfo()


def combineInfoProduct(name1, spec1, info1, name2, spec2, info2, name3, spec3, info3, name4, spec4, info4, name5, spec5,
                       info5):
    if name1 != '':
        bland.addProduct(Product(name1, spec1, info1))
    if name2 != '':
        bland.addProduct(Product(name2, spec2, info2))
    if name3 != '':
        bland.addProduct(Product(name3, spec3, info3))
    if name4 != '':
        bland.addProduct(Product(name4, spec4, info4))
    if name5 != '':
        bland.addProduct(Product(name5, spec5, info5))
    return bland.getInfo()


def change_label(name, test_output):
    test_output.delete(0, END)
    test_output.insert(0, name)


def createProduct(oldwindow, industry, country, img_start, bland_info):
    bland.setBland(industry, country, img_start, bland_info)
    oldwindow.master.destroy()
    newindow = Tk()
    newindow.title("批量上传助手 Beta version")

    frame1 = Frame(newindow)
    frame1.pack(side=LEFT, fill=Y)
    Label(frame1, text="产品名字1", width=8).pack(side=TOP, padx=5, pady=5)
    name1 = Entry(frame1)
    name1.pack(side=TOP, padx=5)
    Label(frame1, text="产品规格1", width=8).pack(side=TOP, padx=5, pady=5)
    spec1 = Entry(frame1)
    spec1.pack(side=TOP, padx=5)
    Label(frame1, text="产品介绍1", width=8).pack(side=TOP, padx=5, pady=5)
    info1 = Entry(frame1, width=20)
    info1.pack(side=TOP, fill=BOTH, padx=5, pady=10, expand=True)

    frame2 = Frame(newindow)
    frame2.pack(side=LEFT, fill=Y)
    Label(frame2, text="产品名字2", width=8).pack(side=TOP, padx=5, pady=5)
    name2 = Entry(frame2)
    name2.pack(side=TOP, padx=5)
    Label(frame2, text="产品规格2", width=8).pack(side=TOP, padx=5, pady=5)
    spec2 = Entry(frame2)
    spec2.pack(side=TOP, padx=5)
    Label(frame2, text="产品介绍2", width=8).pack(side=TOP, padx=5, pady=5)
    info2 = Entry(frame2, width=20)
    info2.pack(side=TOP, fill=BOTH, padx=5, pady=10, expand=True)

    frame3 = Frame(newindow)
    frame3.pack(side=LEFT, fill=Y)
    Label(frame3, text="产品名字3", width=8).pack(side=TOP, padx=5, pady=5)
    name3 = Entry(frame3)
    name3.pack(side=TOP, padx=5)
    Label(frame3, text="产品规格3", width=8).pack(side=TOP, padx=5, pady=5)
    spec3 = Entry(frame3)
    spec3.pack(side=TOP, padx=5)
    Label(frame3, text="产品介绍3", width=8).pack(side=TOP, padx=5, pady=5)
    info3 = Entry(frame3, width=20)
    info3.pack(side=TOP, fill=BOTH, padx=5, pady=10, expand=True)

    frame4 = Frame(newindow)
    frame4.pack(side=LEFT, fill=Y)
    Label(frame4, text="产品名字4", width=8).pack(side=TOP, padx=5, pady=5)
    name4 = Entry(frame4)
    name4.pack(side=TOP, padx=5)
    Label(frame4, text="产品规格4", width=8).pack(side=TOP, padx=5, pady=5)
    spec4 = Entry(frame4)
    spec4.pack(side=TOP, padx=5)
    Label(frame4, text="产品介绍4", width=8).pack(side=TOP, padx=5, pady=5)
    info4 = Entry(frame4, width=20)
    info4.pack(side=TOP, fill=BOTH, padx=5, pady=10, expand=True)

    frame5 = Frame(newindow)
    frame5.pack(side=LEFT, fill=Y)
    Label(frame5, text="产品名字5", width=8).pack(side=TOP, padx=5, pady=5)
    name5 = Entry(frame5)
    name5.pack(side=TOP, padx=5)
    Label(frame5, text="产品规格5", width=8).pack(side=TOP, padx=5, pady=5)
    spec5 = Entry(frame5)
    spec5.pack(side=TOP, padx=5)
    Label(frame5, text="产品介绍5", width=8).pack(side=TOP, padx=5, pady=5)
    info5 = Entry(frame5, width=20)
    info5.pack(side=TOP, fill=BOTH, padx=5, pady=10, expand=True)

    frame6 = Frame(newindow)
    frame6.pack(side=LEFT, fill=Y)
    Label(frame6, text="Output", width=8).pack(side=TOP, padx=5, pady=5)
    output = Entry(frame6)
    output.pack(side=TOP, fill=BOTH, padx=5, expand=True)
    bt = Button(frame6, text='Submit', width=20, height=3,
                command=lambda: [change_label(combineInfoProduct(name1.get(), spec1.get(), info1.get(),
                                                                 name2.get(), spec2.get(), info2.get(),
                                                                 name3.get(), spec3.get(), info3.get(),
                                                                 name4.get(), spec4.get(), info4.get(),
                                                                 name5.get(), spec5.get(), info5.get()), output),
                                 name1.delete(0, END), spec1.delete(0, END), info1.delete(0, END),
                                 name2.delete(0, END), spec2.delete(0, END), info2.delete(0, END),
                                 name3.delete(0, END), spec3.delete(0, END), info3.delete(0, END),
                                 name4.delete(0, END), spec4.delete(0, END), info4.delete(0, END),
                                 name5.delete(0, END), spec5.delete(0, END), info5.delete(0, END)
                                 ])
    bt.pack(side=TOP, padx=5, pady=5)


class RootFrame(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("批量上传助手 Beta version")
        self.pack(fill=BOTH, expand=True)

        Label(self, text='国家').pack()
        text_country = tk.Entry(self, width=20)
        text_country.pack()

        Label(self, text='类型').pack()
        text_industry = tk.Entry(self, width=20)
        text_industry.pack()

        Label(self, text='厂家介绍').pack()
        text_bland_info = tk.Entry(self, width=20)
        text_bland_info.pack()

        Label(self, text='图片开始编号').pack()
        text_img_start = tk.Entry(self, width=20)
        text_img_start.insert(END, '0')
        text_img_start.pack()
        '''
        Label(self, text='Output').pack()
        test_output = tk.Entry(self, textvariable='')
        test_output.pack()
        
        bt1 = tk.Button(self, text='Submit', width=20, height=3,
                        command=lambda: change_label(combineInfoBland(text_country.get(),
                                                                      text_industry.get(), text_img_start.get(),
                                                                      text_bland_info.get()), test_output))
        bt1.pack()
        '''
        bt2 = tk.Button(self, text='添加商品', width=20, height=3,
                        command=lambda: createProduct(self, text_industry.get(), text_country.get(),
                                                      text_img_start.get(), text_bland_info.get()))
        bt2.pack(padx=5, pady=10)


bland = Bland()
root = tk.Tk()
app = RootFrame()
root.mainloop()
