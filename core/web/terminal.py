import os, subprocess, sys
import pywebio.input as inp
import pywebio.output as out
import pywebio as web

def _decode_data(byte_data: bytes):
    try:
        return byte_data.decode('UTF-8')
    except UnicodeDecodeError:
        return byte_data.decode('GB18030')

def term():
    web.session.set_env(title="💻Staxle_Terminal")
    out.put_image(open("img/stax.png","rb").read())
    out.put_html("<h1>Staxle Web Terminal Runner</h1>")
    out.put_text("通过网页执行终端命令并显示在网页上")
    out.put_link("返回主页", app="index")
    out.put_warning("请不要执行循环/中间需要输入东西的命令！")
    command = inp.input("输入命令")
    
    p = subprocess.Popen(command, stdout = subprocess.PIPE, stderr=subprocess.STDOUT)
    result = []
    while p.poll() is None:
        line = p.stdout.readline().strip()
        if line:
            line = _decode_data(line)
            result.append(line)
            out.put_text(line)
        # 清空缓存
        sys.stdout.flush()
        sys.stderr.flush()
    
    out.put_info("执行完成，如需继续执行请刷新")