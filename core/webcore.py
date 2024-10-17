import os, sys, time, json, requests
from core.staxcore import *
import pywebio.input as input
import pywebio.output as out

def about():
    text = about_web()
    out.popup("关于",out.put_text(text))

def done(text):
    out.popup("操作完成！",text)
    
def new():
    os.system("git clone https://github.io/Toad114514/Staxle")
    os.system("mv Staxle $PREFIX/etc/staxle")
    out.toast("更新完成，请重启 Staxle")
    time.sleep(0.2)
    os._exit(0)

def nginx():
    out.toast("请等待 nginx 安装完成")
    os.system("pkg install nginx")
    done("nginx安装完成")

def ng_start():
    out.toast("Nginx 服务启动中...")
    if "nginx" not in os.popen("pkg list-installed|grep nginx"):
        out.toast("未安装 Nginx！", color="error")
    else:
        back = os.popen("nginx").read()
        done("Nginx 返回信息：\n"+back)

def ng_stop():
    out.toast("Nginx 服务关闭中...")
    if "nginx" not in os.popen("pkg list-installed|grep nginx"):
        out.toast("未安装 Nginx！", color="error")
    else:
        back = os.popen("nginx -s stop").read()
        done("Nginx 返回信息：\n"+back)

def de02():
    out.toast("请等待 apache 安装完成")
    apacheins()
    done("apache安装完成，输入 httpd 启动")

def de03():
    out.toast("请等待 php 安装完成")
    phpins()
    done("php安装完成，输入 php-fpm 启动")

def de04():
    out.toast("请等待 ngircd 安装完成")
    ircins()
    done("ngircd安装完成")

def de05():
    out.toast("请等待 code-server 安装完成")
    out.toast("安装 tur-repo...")
    os.system("pkg install tur-repo -y")
    out.toast("安装 code-server...")
    os.system("apt install code-server -y")
    done("code-server安装完成")