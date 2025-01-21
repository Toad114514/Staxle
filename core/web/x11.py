import os, subprocess, sys
import pywebio.input as inp
import pywebio.output as out
import pywebio as web

def insxfce4():
    out.toast("正在安装 xfce4.....(进程可在 termux 中查看)")
    os.system('pkg install xfce4 -y')
    out.popup('操作完成','你已经安装好了 xfce4')
    with open("./core/web/xfce4") as f:
        f.write("xfce4")
    
def conftx11():
    out.toast("正在安装Termux-x11...")
    os.system("apt install termux-x11-nightly")
    out.popup("操作完成","termux-x11安装好了。请在服务器上安装termux-x11，没有就去找")
    
def startde(cmd):
    os.system("termux-x11 :0 &")
    os.system(f"env DISPLAY=:0 {cmd} &")
    out.popup("启动完成！","现在可以打开termux-x11查看桌面环境了")

def x11():
    web.session.set_env(title="💻Staxle_tx11")
    out.put_image(open("img/stax.png","rb").read())
    out.put_html("<h1>Staxle Web termux-x11 config</h1>")
    out.put_text("设置你的termux-x11在你的机子上")
    out.put_link("返回主页", app="index")
    
    out.
    out.put_buttons(["安装xfce4",'配置termux-x11','启动桌面环境'], onclick=[insxfce4, conftx11, lambda: startde("startxfce4")])