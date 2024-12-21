import os, sys, time
import json
import urllib.request
import requests
import getpass
import socket
import platform as plat
from subprocess import check_output as inputstream
import core.i18n.i18n as lang
from core.staxapps import *

# stax_global 类
class stax():
    version = "v1.05.2"
    version_num = 173

work_path = os.getcwd()

# 自定义异常类：
# 配置空/值错误
class StaxleConfigLackOrValueError(Exception):
     def __init__(self, msg):
         self.msg = msg
    
     def __str__(self):
         return self.msg

def output(type,msg):
    result = ""
    if type == "e":
        result = '\033[31m' + '[ERR] ' + '\033[0m'
    if type == "d":
        result = '\033[32m' + '[DONE] ' + '\033[0m'
    if type == "w":
        result = '\033[33m' + '[WRN] ' + '\033[0m'
    if type == "i":
        result = '\033[34m' + '[INFO] ' + '\033[0m'
    result = result + time.strftime("%H:%M:%S") + " " + msg
    return result

script_path = os.path.realpath(__file__)
staxcore_path = os.path.dirname(script_path)
stax_path = staxcore_path+"/.."

stax_banner = """
   \033[31m____\033[34m__  \033[33m    \033[32m    \033[31m   _\033[34m_
  \033[32m/ __\033[31m/ /_\033[34m___ \033[33m___ \033[32m__ /\033[31m /__
 \033[33m_\ \\\033[32m/ __\033[31m/ _ \033[34m`/\ \033[33m\ //\033[32m / -_)
\033[34m/___\033[33m/\__\033[32m/\_,\033[31m_//_\033[34m\_\/\033[33m_/\__/\033[0m
"""
#   \033[0mAll-in-One \033[32mtermux\033[0m Tool-panel
#            By Toad114514

stax_banner2 = "          \033[0m" + str(lang.get("stax.banner.1")) + " \033[32m" + str(lang.get("stax.banner.2")) + " \033[0m" + str(lang.get("stax.banner.3"))

stax_web_about = """
    ___  __                        __
  / __/ / /_  ___   ___  __  / /__
 _\ \  / __/ /_ `/\ \ // / -_)
/___/ \__/  \_,_//_\_\/_/\__/
   All-in-One termux Tool-panel
       By Toad114514
"""
backtomenu_banner = """
99) 回到主页面
00) 退出 Staxle
"""

whoami = os.popen("whoami").read()
kenrel = os.popen("uname -s").read()
osys = os.popen("uname -o").read()

prefix = os.getenv("PREFIX")
cache_1 = prefix+"/tmp/staxle"
configFile = "../stax.conf"
configBase = "[HOME] = ~"
user = getpass.getuser()
# ip
soc_var=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip_socket_temp = soc_var.connect(("8.8.8.8",80))
ip = soc_var.getsockname()[0]

# 不知道干什么用的，还是写了罢
def writeStatus(statusId):
	open(cache_1,"w").write(str(statusId))

def readStatus():
	try:
		statusId = open(cache_1,"r").read()
		if statusId == "1":
			return True
		return False
	except IOError:
		return False

def restart_program():
	python = sys.executable
	os.execl(python, python, * sys.argv)
	curdir = os.getcwd()

def backtomenu_option():
	if not readStatus():
		print(backtomenu_banner)
		backtomenu = input("stax/done: ")
		
		if backtomenu == "99":
			restart_program()
		elif backtomenu == "0" or backtomenu == "00":
			sys.exit()
		else:
			print("\n无效输入。")
			time.sleep(2)
			restart_program()

def err():
    print("无效输入。")
    input("")

def done(desc):
    print("------------------------")
    print("      操作完成        ")
    print("------------------------")
    print(desc)
    print("------------------------")
    backtomenu_option()

# Home 位置
def checkConfigFile():
	if os.path.exists(configFile):
		if os.path.isdir(configFile):
			os.system(f"rm -rf {configFile}")
			open(configFile,"w").write(configBase)
	else:
		open(configFile,"w").write(configBase)

# 这里知道干什么用的，但是此处注释被奶龙偷走了
# 你得 “今夜星光闪闪...” 才能获得此处注释
def loadConfigFile():
	checkConfigFile()
	lfile = ""
	try:
		lfile = [x.split("=")[-1].strip() for x in open(configFile,"r").splitlines() if x.split("=")[0].strip() == "[HOME]"][0]
	except Exception as e:
		lfile = "~"
	return lfile

homeDir = loadConfigFile()

# staxconf 配置类
class staxconf():
    user=""
    git_clone_mirror=""
    skip_aug=""

# 获取配置
def config_get():
    config_path="./core/config"
    want = ["gitmirror", "user", "skip_aug"]
    # search what is not exists
    for w in want:
        if os.path.exists(os.path.join(config_path, w)) == False:
            strss="是不是没有运行 setup.sh！！！！！我造密码币的配置项缺斤少两没有一个我要的"
            raise StaxleConfigLackOrValueError(strss)
    # set value
    if os.popen(f"cat {config_path}/user").read() == "":
        staxconf.user=str(plat.system())
    else:
        staxconf.user=os.popen(f"cat {config_path}/user").read().strip()
    # gitmirror
    staxconf.git_clone_mirror=os.popen(f"cat {config_path}/gitmirror").read().strip()
    if staxconf.git_clone_mirror != "github" and staxconf.git_clone_mirror != "kkgithub":
        raise StaxleConfigLackOrValueError("✓8玩意，gitmirror 项只能写 github 和 kkgithub，你写了个 "+staxconf.git_clone_mirror+" 进去喂猪啊番薯")
    
    # skip_aug
    staxconf.skip_aug=os.popen(f"cat {config_path}/skip_aug").read().strip()
    if staxconf.skip_aug != "y" and staxconf.skip_aug != "n":
        raise StaxleConfigLackOrValueError("✓8玩意，skip_aug 项只能写 y 和 n，你写了个 "+staxconf.skip_aug+" 进去喂猪啊番薯")

# 标题
def banner():
	print(stax_banner)
	print(stax_banner2)
	print("       By Toad114514")
	print(stax.version+"("+str(stax.version_num)+")"+"    欢迎 "+staxconf.user+"/localhost")

# 升级 
def update():
    update_json = requests.get("https://api.github.com/repos/toad114514/staxle/releases/latest")
    print("目前 Staxle 版本："+stax.version)
    print("请等待获取最新的 Releases...")
    # 解析数据
    if update_json.status_code == 200:
        update_info=json.loads(update_json.text)
        print("\n")
        print("最近的 Releases 版本："+update_info["tag_name"])
        if update_info["prerelease"] == True:
            print("\033[33m预发行版本！十分甚至九分不稳定！\033[0m")
        print("提交时间："+update_info["published_at"].replace("T"," ").replace("Z",""))
        print("===============================")
        print("c(hanglog) 查看本次更新日志    u(pdate) 更新    b(ack) 退出")
        inp=input("输入：")
        if inp.strip() == "c" or inp.strip() == "changlog":
            ud_body=update_info["body"]
            print(update_info["name"]+" ("+update_info["tag_name"]+") 更新日志：")
            print("===============================")
            print(ud_body)
            print("===============================")
            print("u(pdate) 更新    b(ack) 退出")
            inp=input("输入：")
            if inp.strip() == "u" or inp.strip() == "update":
                os.system("git pull && cd")
                print("更新完成，重新输入 stax或staxle 可体验新版本")
                exit()
            elif inp.strip() == "b" or inp.strip() == "back":
                restart_program()
            else: print("无效输入"); time.sleep(0.7); restart_program()
        elif inp.strip() == "u" or inp.strip() == "update":
            os.system("git pull && cd")
            print("更新完成，重新输入 stax 或 staxle 可体验新版本")
            exit()
        elif inp.strip() == "b" or inp.strip() == "back":
            restart_program()
        else: print("无效输入"); time.sleep(0.7); restart_program()

# 关于
def about():
    print(stax_banner)
    print("Staxle "+stax.version+" ("+str(stax.version_num)+")")
    print(whoami+"@"+kenrel+"/"+osys)
    print("Python "+str(plat.python_version())+"("+str(plat.python_implementation())+")")
    print("work_path:"+stax_path)
    print("ip:",ip)
    input("按下回车键回到菜单")
    restart_program()

# 关于（web.py）
def about_web():
    about01 = "Staxle "+stax.version+" ("+str(stax.version_num)+")"
    about02 = str(plat.system())+"("+str(plat.processor())+"/"+str(plat.architecture())+")"
    about03 = "Python "+str(plat.python_version())+"("+str(plat.python_implementation())+")"
    about04 = "ip:"+ip
    return stax_web_about + "\n终端设备：\n" + about01 + "\n" + about02 + "\m" + about03 + "\n" + about04

