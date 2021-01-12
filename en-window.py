import tkinter
import tkinter.messagebox
from tkinter import scrolledtext
from tkinter import ttk 

import packeg_info
#导入包管理信息

config = {'cycle':0,'my_font':6}
font_conf = ('Arial','Consolas', 'Comic Sans MS','Times New Roman', 'system','MS Serif', 'Verdana')
cycle_conf = ('each time', 'every week', 'each 15 days','each month')

# print(font_conf)
# print(cycle_conf[config['cycle']])

class mywindow:
    #界面布局方法
    def __init__(self,type_preferrence,type_show_package_info):
        #创建主界面，并且保存到成员属性中
        self.window = tkinter.Tk()# 第1步，实例化object，建立窗口window
        self.window.title('openEuler Update Reminder')# 第2步，给窗口的可视化起名字
        self.window.geometry('540x360')  # 第3步，设定窗口的大小(长 * 宽)这里的乘是小x

        self.myfont = font_conf[config['my_font']]
        self.num = 24
        
        self.aaa = type_show_package_info
        # print(param)
        # 界面布局
        self.menus(type_preferrence)
        self.layout(type_show_package_info)
        self.window.mainloop()
    
     
    #菜单界面摆放
    def menus(self,type_preferrence):
        # 添加菜单
        # 创建总菜单
        allmenu = tkinter.Menu(self.window)

        # 添加子菜单
        filemenu = tkinter.Menu(allmenu, tearoff=0)
        # 添加选项卡
        filemenu.add_command(label='偏好设置(A)  ', command=type_preferrence)
        allmenu.add_cascade(label='设置(V)', menu=filemenu)

        # 添加子菜单2
        editmenu = tkinter.Menu(allmenu, tearoff=0)
        # 添加选项卡
        editmenu.add_command(label='查看历史记录(L)', command=self.myfunc)
        editmenu.add_command(label='清除历史记录(I)', command=self.myfunc)
        # 添加分割线
        editmenu.add_separator()
        editmenu.add_command(label='查看当前版本信息(H)', command=self.myfunc)
        allmenu.add_cascade(label='日志(E)', menu=editmenu)

        # 添加子菜单3
        helpmenu = tkinter.Menu(allmenu, tearoff=0)
        # 添加选项卡
        helpmenu.add_command(label='查看帮助(V)       F1', command=self.myfunc)
        # 添加分割线
        helpmenu.add_separator()
        # 添加选项卡
        helpmenu.add_command(label='关于此软件(A)', command=self.myfunc)
        allmenu.add_cascade(label='帮助(H)', menu=helpmenu)

        self.window.config(menu=allmenu)

    #主界面摆放
    def layout(self,type_show_package_info):
        # 在图形界面上创建一个标签label用以显示商标并放置
        l = tkinter.Label(self.window, bg='green', fg='white',font=(self.myfont, 30),text='*openEuler*')
        l.place(x=0, y=0, relwidth=1, relheight=0.25)
        
        # 显示屏
        result = tkinter.StringVar()

        show_text1 = tkinter.Label(self.window, bd=2, font=(self.myfont, 12),anchor='nw', text='openEuler更新提醒:')
        show_text1.place(relx=0.1, rely=0.3)
        show_result = tkinter.Label(self.window, bd=2, font=(self.myfont, 12),anchor='nw', textvariable=result)
        show_result.place(relx=0.15, rely=0.4)
        show_text2 = tkinter.Label(self.window, bd=2, font=(self.myfont, 12),anchor='sw', text='\t是否进行更新？')
        show_text2.place(relx=0.15, rely=0.5)

        update_info = '\t检测到'+str(self.num)+'个软件发布新的更新包'
        result.set(update_info)
     
        # 功能按钮"查看详情"
        button_info = tkinter.Button(self.window, text='查看详情',font=(self.myfont, 11),command=self.show__info)
        button_info.place(relx=0.5, rely=0.8)
    
        # 功能按钮"一键更新"
        button_updateall = tkinter.Button(self.window, text='一键更新',font=(self.myfont, 11),command=self.run_update_all)
        button_updateall.place(relx=0.65, rely=0.8)

        # 功能按钮"下次提醒"
        button_nexttime = tkinter.Button(self.window, text='下次提醒',font=(self.myfont, 11),command=quit)
        button_nexttime.place(relx=0.8, rely=0.8)

    
    def show__info(self):
        self.window.destroy()
        my_info = self.aaa()
   

     #菜单功能
    
    def myfunc(self):
        tkinter.messagebox.showinfo('','程序员懒死在电脑前，打死也做不出的功能，只是装饰而已～')



    def run_update_all(self):
        tkinter.messagebox.showinfo('','正在更新,请稍候...')
        ######
        #这里接下载安装包的程序
        #######



class show_package_info:
    """docstring for show_detail"""
    def __init__(self):

        self.detail_info = tkinter.Tk()
        self.detail_info.title('openEuler Update Reminder 升级详情')
        self.detail_info.geometry('920x560')
        
        self.myfont = font_conf[config['my_font']]
        self.param = packeg_info.info
        self.nmm = {}

        self.package_num = 0
        self.package_size = 0
        self.chosen_info = '已选择 '+str(self.package_num)+' 个软件包,大小为 '+str(self.package_size)+' KB,是否更新？\n'

        self.detail_layout()

        self.detail_info.mainloop()
        # self.detail_info.bind('<Configure>',self.update_w_h)
        


    def detail_layout(self):
        
        #创建表格
        mat = " %(name)-32s %(c_v)10s \t%(n_v)10s \t%(size)6s\t"
        mate = " %(name)-32s %(c_v)10s \t%(n_v)10s \t%(size)8s\t"
        # mat = " %(name)-16s \t%(c_v)s\t%(n_v)s\t%(size)s\t%(date)s\t"
        # ll = mat%{'name':'名称','c_v':'当前版本','n_v':'最新版本','size':'大小','date':'发布日期'}
        # ll = mat%{'name':'名称','c_v':'当前版本','n_v':'最新版本','size':'大小'}
        ll = mat%{'name':'Name','c_v':'Current Ver','n_v':'Latest Ver','size':'Size'}
        # mate = " %(name)-16s \t%(c_v)s\t%(n_v)s\t%(size)s\t%(date)s\t"
        table_label = tkinter.Label(self.detail_info, bd=2, font=(self.myfont, 12),anchor='nw', text=ll)
        table_label.place(x=50,y=0)

        self.table_text = scrolledtext.ScrolledText(self.detail_info,width=880,height=400)
        # self.table_text.place(x=10,y=30,width=900,height=400)
        self.table_text.place(x=10,y=30,relwidth=0.98,relheight=0.8)

        # var = []
        
        i = 0
        for package in self.param:
            
            # tt = mate%{'name':package['name'],'c_v':package['current_version'],'n_v':package['new_version'],'size':package['size'],'date':package['date']}
            tt = mate%{'name':package['name'],'c_v':package['current_version'],'n_v':package['new_version'],'size':package['size']}    
            name = 'check'+str(i)
            self.nmm[name] = tkinter.IntVar() # 定义v整型变量用来存放选择行为返回值
            self.name = tkinter.Checkbutton(self.table_text,bg='white',text=tt,font=(self.myfont, 12), anchor='nw',variable=self.nmm[name], onvalue=1, offvalue=0, command=self.package_select)    
            self.table_text.window_create("insert", window=self.name)
  
            i = i +1
        
        self.table_label = tkinter.Label(self.detail_info, bd=2, font=(self.myfont, 12),anchor='nw', text=self.chosen_info)
        self.table_label.place(relx=0.1,rely=0.86,width=880,height=40)
 
        # 功能按钮"全选"
        button_all = tkinter.Button(self.detail_info, text=' 全选 ',font=(self.myfont, 12),command=self.choose_all)
        button_all.place(relx=0.7,rely=0.9)
    
        # 功能按钮"更新"
        button_update = tkinter.Button(self.detail_info, text=' 更新 ',font=(self.myfont, 12),command=self.update_chosen)
        button_update.place(relx=0.8,rely=0.9)

        # 功能按钮"取消"
        button_no = tkinter.Button(self.detail_info, text=' 取消 ',font=(self.myfont, 12),command=self.detail_info.destroy)
        button_no.place(relx=0.9,rely=0.9)

        # self.detail_info.bind('<Configure>',self.update_w_h)

       
    def get_package_num_and_show(self):
        print('get_package_num_and_show')
        all = 0
        for i in range(len(self.nmm)):
            name = 'check'+str(i)
            # print(self.nmm[name].get())
            all = all + self.nmm[name].get()

        self.chosen_info = '已选择 '+str(all)+' 个软件包,大小为 ,是否更新？\n'
        self.table_label.config(text=self.chosen_info)
        
    

    def package_select(self):
        print('select')
        self.get_package_num_and_show()
        



    def choose_all(self):
        print('choose_all')
        for i in range(len(self.nmm)):
            name = 'check'+str(i)
            self.nmm[name].set(1)

        self.get_package_num_and_show()

        # self.chosen_info = '已选择 '+str(all)+' 个软件包,大小为 ,是否更新？\n'
        # self.table_label.config(text=self.chosen_info)
        
        


    def update_chosen(self):
    
        print('update_chosen')
        # all = 0
        # for i in range(len(self.nmm)):
        #   name = 'check'+str(i)
        #   all = all + self.nmm[name].get()
        # print(all)
        """
        ######################
        ##
        ######################
        """


class mypreference:
    """docstring for mypreference"""
    def __init__(self):
        #创建主界面，并且保存到成员属性中
        self.prefernece = tkinter.Tk()# 第1步，实例化object，建立窗口window
        self.prefernece.title('openEuler Update Reminder Prefernece Config')# 第2步，给窗口的可视化起名字
        self.prefernece.geometry('540x360')  # 第3步，设定窗口的大小(长 * 宽)这里的乘是小x

        self.myfont = font_conf[config['my_font']]
        self.my_font_ = config['my_font']
        
        # 'Consolas'
        
        self.cycle = config['cycle']
      
        # 界面布局
        self.preference_layout()
        self.prefernece.mainloop()

        
    def preference_layout(self):
        
        self.poll_default_L = tkinter.Label(self.prefernece, text='Polling Cycle：',font=(self.myfont, 12))
        self.poll_default_L.place(relx=0.15,rely=0.15)
        self.poll_default = ttk.Combobox(self.prefernece,font=(self.myfont, 12))
        self.poll_default.place(relx=0.45,rely=0.15)
        self.poll_default['value'] = ('each time', 'every week', 'each 15 days','each month')
        self.poll_default.current(self.cycle)

        self.font_default_L = tkinter.Label(self.prefernece, text='         font：',font=(self.myfont, 12))
        self.font_default_L.place(relx=0.15,rely=0.3)
        self.font_default = ttk.Combobox(self.prefernece,font=(self.myfont, 12))
        self.font_default.place(relx=0.45,rely=0.3)
        self.font_default['value'] = ('Consolas', 'Times', '微软雅黑')
        self.font_default.current(self.my_font_)

        self.langu_default_L = tkinter.Label(self.prefernece, text='     language：',font=(self.myfont, 12))
        self.langu_default_L.place(relx=0.15,rely=0.45)
        self.langu_default = ttk.Combobox(self.prefernece,font=(self.myfont, 12))
        self.langu_default.place(relx=0.45,rely=0.45)
        self.langu_default['value'] = ('English', '中文')
        self.langu_default.current(0)



        # 功能按钮"保存"
        button_update = tkinter.Button(self.prefernece, text=' Save ',font=(self.myfont, 11),command=self.save_config)
        button_update.place(relx=0.6,rely=0.8)

        # 功能按钮"取消"
        button_exc = tkinter.Button(self.prefernece, text=' Exc ',font=(self.myfont, 11),command=self.prefernece.destroy)
        button_exc.place(relx=0.8,rely=0.8)
        

    def save_config(self):
        print('save')
        poll_n = self.poll_default.current()
        font_n = self.font_default.current()
        langu_n = self.langu_default.current()
        print(poll_n,font_n,langu_n)
        # self.myfont = 'Times'
   
# # config = {'cycle':0}
# test = show_package_info()
# test = mypreference()
#实例化对象
mywindow = mywindow(type_preferrence=mypreference,type_show_package_info=show_package_info)

