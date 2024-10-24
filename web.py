import os, sys, time
import requests
import json
from core.webcore import *
import pywebio as web
import pywebio.output as out
import pywebio.input as input

def main():
    web.session.set_env(title="💻Staxle 面板后台🤣")
    out.put_image(open("img/stax.png","rb").read())
    out.put_html("<h1>Staxle Web Panel</h1>")
    out.put_text("基于 Staxle v1.03.6")
    pwd = input.input("输入 Staxle 面板后台密码：")
    with open(".web_passwd","r") as f:
        dui_pwd = f.read()
    if pwd == dui_pwd:
        runpanel()
    else:
        out.popup("密码错误，请重新刷新页面重试")

def runpanel():
    out.put_text("关闭面板后台需要转到面板设置点击关闭页面后台才可关闭")
    out.put_tabs([
       {"title":"服务器","content":[
          out.put_html("<h3>Nginx 服务器</h3>"),
          out.put_text("一款速度快，cpu占用小的C++开源自由服务器"),
          out.put_buttons(["安装","启动","关闭"],onclick=[nginx, ng_start, ng_close]),
          out.put_html("<h3>Apache 服务器</h3>"),
          out.put_text("全球第一的服务器"),
          out.put_button("安装",onclick=lambda: de02()),
          out.put_html("<h3>PHP</h3>"),
          out.put_text("动态页面、CMS和框架的基础"),
          out.put_button("安装",onclick=lambda: de03()),
          out.put_html("<h3>IRC 服务器</h3>"),
          out.put_text("即时聊天通讯服务器"),
          out.put_button("安装",onclick=lambda: de04()),
          out.put_html("<h3>code-server</h3>"),
          out.put_text("浏览器上的 VSCode"),
          out.put_button("安装",onclick=lambda: de05()),
       ]},
       {"title":"桌面环境","content":[
          out.put_markdown("# Shit")
       
       ]},
       {"title":"后台链接转接","content":[
          out.put_link("Apache 页面",url="http://127.0.0.1:8080")
       ]},
       {"title":"面板设置","content":[
          out.put_html("<h2>面板后台和Staxle选项</h2>"),
          out.put_button("关于 Staxle",onclick=lambda: about()),
          out.put_button("更新 Staxle",onclick=lambda: new()),
          out.put_button("关闭面板后台",onclick=lambda: close())
       ]}
    ])

def close():
    out.toast("🤣👉面板后台已关闭 请转至终端")
    time.sleep(0.3)
    os._exit(0)

if __name__ == "__main__":
    print("输入 127.0.0.1:15334 进入面板后台")
    print("关闭面板后台需要转到面板设置点击关闭页面后台才可关闭")
    web.start_server(main, host="0.0.0.0", port=15334, debug=True)
    web.session.hold()
