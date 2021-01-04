import tkinter
import tkinter.messagebox
from tkinter import scrolledtext
from tkinter import ttk 

import packeg_info
#导入包管理信息

class mywindow:
    #界面布局方法
    def __init__(self):
        #创建主界面，并且保存到成员属性中
        self.window = tkinter.Tk()# 第1步，实例化object，建立窗口window
        self.window.title('openEuler Update Reminder')# 第2步，给窗口的可视化起名字
        self.window.geometry('600x400')  # 第3步，设定窗口的大小(长 * 宽)这里的乘是小x

        self.num = 24
        self.param = packeg_info.info
        # print(param)
        # 界面布局
        self.menus()
        self.layout()
        self.window.mainloop()
    
     
    #菜单界面摆放
    def menus(self):
        # 添加菜单
        # 创建总菜单
        allmenu = tkinter.Menu(self.window)

        # 添加子菜单
        filemenu = tkinter.Menu(allmenu, tearoff=0)
        # 添加选项卡
        filemenu.add_command(label='偏好设置(A)  ', command=self.mypreference)
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
    def layout(self):
        # 在图形界面上创建一个标签label用以显示商标并放置
        l = tkinter.Label(self.window, bg='green', fg='white',font=('微软雅黑', 30),text='*openEuler*')
        l.place(x=0, y=0, width=600, height=70)
        
        # 显示屏
        result = tkinter.StringVar()

        show_text1 = tkinter.Label(self.window, bd=2, font=('微软雅黑', 12),anchor='nw', text='openEuler更新提醒:')
        show_text1.place(x=10, y=100, width=580, height=50)
        show_result = tkinter.Label(self.window, bd=2, font=('微软雅黑', 12),anchor='nw', textvariable=result)
        show_result.place(x=10, y=150, width=580, height=50)
        show_text2 = tkinter.Label(self.window, bd=2, font=('微软雅黑', 12),anchor='sw', text='\t是否进行更新？')
        show_text2.place(x=10, y=200, width=500, height=50)

        update_info = '\t检测到'+str(self.num)+'个软件发布新的更新包'
        result.set(update_info)
     
        # 功能按钮"查看详情"
        button_info = tkinter.Button(self.window, text='  查看详情  ',font=('微软雅黑', 10),command=self.show_detail)
        button_info.place(x=300,y=320)
    
        # 功能按钮"一键更新"
        button_updateall = tkinter.Button(self.window, text='  一键更新  ',font=('微软雅黑', 10),command=self.run_update_all)
        button_updateall.place(x=400,y=320)

        # 功能按钮"下次提醒"
        button_nexttime = tkinter.Button(self.window, text='  下次提醒  ',font=('微软雅黑', 10),command=quit)
        button_nexttime.place(x=500,y=320)



        

     #菜单功能
    
    def myfunc(self):
        tkinter.messagebox.showinfo('','程序员懒死在电脑前，打死也做不出的功能，只是装饰而已～')



    def run_update_all(self):
        tkinter.messagebox.showinfo('','正在更新,请稍候...')
        ######
        #这里接下载安装包的程序
        #######




    def show_detail(self):
        self.detail_info = tkinter.Tk()
        self.detail_info.title('openEuler Update Reminder 升级详情')
        self.detail_info.geometry('920x560')
        
        #创建表格
        mat = " %(name)-24s \t%(c_v)s\t\t%(n_v)s\t\t%(size)s\t\t%(date)s\t"
        ll = mat%{'name':'名称','c_v':'当前版本','n_v':'最新版本','size':'大小','date':'发布日期'}
        mate = " %(name)-24s \t%(c_v)s\t\t%(n_v)s\t\t%(size)s\t\t%(date)s\t"
        table_label = tkinter.Label(self.detail_info, bd=2, font=('微软雅黑', 12),anchor='nw', text=ll)
        table_label.place(x=60,y=10,width=800,height=40)

        table_text = scrolledtext.ScrolledText(self.detail_info,width=880,height=400)
        table_text.place(x=10,y=50,width=900,height=400)

        # table_text = tkinter.Text(self.detail_info,width=880,height=400)
        # table_text.place(x=10,y=50,width=880,height=400)

        # scroll = tkinter.Scrollbar(self.detail_info)
        # scroll.place(x=900,y=50,height=400)
        # scroll.config(command=table_text.yview)
        # table_text.config(yscrollcommand=scroll.set)

        var = []
        i = 0
        for package in self.param:
            # print(package)
            tt = mate%{'name':package['name'],'c_v':package['current_version'],'n_v':package['new_version'],'size':package['size'],'date':package['date']}
           
            v = tkinter.IntVar() # 定义v整型变量用来存放选择行为返回值
            c = tkinter.Checkbutton(table_text,bg='white',text=tt,font=('微软雅黑', 12), anchor='nw',variable=v, onvalue=1, offvalue=0, command=self.package_select)    
            table_text.window_create("insert", window=c)

            # 传值原理类似于radiobutton部件
            i = i +1
        
        chosen_info = '已选择'+str(i)+'个软件包，是否更新？\n'
        table_label = tkinter.Label(self.detail_info, bd=2, font=('微软雅黑', 12),anchor='nw', text=chosen_info)
        table_label.place(x=30,y=460,width=880,height=40)

        # 功能按钮"全选"
        button_all = tkinter.Button(self.detail_info, text='  全选  ',font=('微软雅黑', 12),command=self.show_detail)
        button_all.place(x=600,y=500)
    
        # 功能按钮"更新"
        button_update = tkinter.Button(self.detail_info, text='  更新  ',font=('微软雅黑', 12),command=self.run_update_all)
        button_update.place(x=700,y=500)

        # 功能按钮"取消"
        button_no = tkinter.Button(self.detail_info, text='  取消  ',font=('微软雅黑', 12),command=quit)
        button_no.place(x=800,y=500)

        self.detail_info.mainloop()
       


    def package_select(self):
        print('select')


    #暂未开发说明
    def wait(self):
        tkinter.messagebox.showinfo('','功能在努力的实现，请期待2.0版本的更新')

    def mypreference(self):
        prefernece = tkinter.Tk()
        prefernece.title('openEuler Update Reminder 偏好设置')
        prefernece.geometry('600x400')
        

        ddb_default_L = tkinter.Label(prefernece, text='  轮询时间：',font=('微软雅黑', 12))
        ddb_default_L.place(x=80,y=20)
        ddb_default = ttk.Combobox(prefernece,font=('微软雅黑', 12))
        ddb_default.place(x=180,y=20)
        ddb_default['value'] = ('每次开机', '每 周', '每 15 天','每 30 天')
        ddb_default.current(0)

        prefernece.mainloop()

    #暂未开发说明
    def wait(self):
        tkinter.messagebox.showinfo('','功能在努力的实现，请期待2.0版本的更新')






#实例化对象
mywindow = mywindow()