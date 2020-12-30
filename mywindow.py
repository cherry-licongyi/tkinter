#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter as tk  # 使用Tkinter前需要先导入

def mywindow(local,current):
    if local == current:
        exit()

    window = tk.Tk()# 第1步，实例化object，建立窗口window
    window.title('openEuler update reminder')# 第2步，给窗口的可视化起名字
    window.geometry('520x300')  # 第3步，设定窗口的大小(长 * 宽)这里的乘是小x

    # 在图形界面上创建一个标签label用以显示并放置
    l = tk.Label(window, bg='green', fg='white',font=('微软雅黑', 40), width=16, text='openEuler')
    l.grid(row=0,rowspan=2,columnspan=2)
    
    m = tk.Label(window,  fg='black',font=('微软雅黑', 11))
    m.grid(row=2,rowspan=2,columnspan=2)
    m.config(text=' 当前版本为：'+local+'\n检测到最新版本为：'+current+'\n是否更新？\n\n')

    k = tk.Label(window,  fg='black',font=('微软雅黑', 11))
    k.grid(row=5,columnspan=2)

    def run_start():
        k.config(text='\n正在更新,请稍候...')
        #这里接下载安装包的程序

    b = tk.Button(window, text=' 立即更新 ',command=run_start)
    b.grid(row=4,column=0)
    c = tk.Button(window, text=' 稍后更新 ',command=quit)
    c.grid(row=4,column=1)

    window.mainloop() #主窗口循环显示


if __name__ == "__main__":    
    #这里接爬虫程序

    local = 'openeuler-4.09.1234'
    current = 'openeuler-4.19.1234'
    mywindow(local,current)