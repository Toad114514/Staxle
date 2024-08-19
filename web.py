import os, sys, time
import requests
import json
from core.staxcore import *
import pywebio as web
import pywebio.output as out
import pywebio.input as input

def main():
    web.session.set_env(title="💻Staxle 面板后台🤣")
    out.put_image(open("img/stax.png","rb").read())
    out.put_html("<h1>Staxle Web Panel</h1>")
    out.put_text("基于 Staxle v1.01")
    out.put_text("关闭面板后台需要转到面板设置点击关闭页面后台才可关闭")
    done("xxx 11454")
    out.put_tabs([
       {"title":"服务器","content":[
          out.put_html("<h3>Nginx 服务器</h3>"),
          out.put_text("一款速度快，cpu占用小的C++开源自由服务器"),
          out.put_button("安装",onclick=lambda: de01()),
          out.put_html("<h3>Apache 服务器</h3>"),
          out.put_text("全球第一的服务器"),
          out.put_button("安装",onclick=lambda: de02()),
          out.put_html("<h3>PHP</h3>"),
          out.put_text("动态页面、CMS和框架的基础"),
          out.put_button("安装",onclick=lambda: de03()),
          out.put_html("<h3>IRC 服务器</h3>"),
          out.put_text("即时聊天通讯服务器端"),
          out.put_button("安装",onclick=lambda: de04()),
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
    
def about():
    text = about_web()
    out.popup("关于",out.put_text(text))

def done(text):
    out.popup("操作完成！",text)
    
def new():
    resp = requests.get('https://toad114514.github.io/staxle/version.json')
    getback = json.loads(resp.text)
    if getback["version-code"] >= stax.version_num:
        ver = getback["version"]
        vernum = getback["version-code"]
        vertype = getback["version-type"]
        verdesc = getback["version-desc"]
        out.popup("有新版本更新",out.put_text(ver+"("+vernum+") - "+vertype+"\n更新内容：\n"+verdesc))
        out.toast("正在更新 Staxle 至"+getback["version"])
        time.sleep(1)
        os.system("git pull")
        out.toast("更新完成，请重启 Staxle")
        time.sleep(0.2)
        os._exit()
    else:
        out.toast("👍你目前用的 Staxle 是最新版本！")

def de01():
    nginxins()
    done("nginx安装完成")

def de02():
    apacheins()
    done("apache安装完成，输入 httpd 启动")

def de03():
    phpins()
    done("php安装完成，输入 php-fpm 启动")

def de04():
    ircins()
    done("ngircd安装完成")

def close():
    out.toast("🤣👉面板后台已关闭 请转至终端")
    time.sleep(0.3)
    os._exit(0)

if __name__ == "__main__":
    print("输入 127.0.0.1 进入面板后台")
    print("关闭面板后台需要转到面板设置点击关闭页面后台才可关闭")
    web.start_server(main, host="127.0.0.1", port=15334, debug=True)
    web.session.hold()
