import os, sys, time
import json
import urllib.request
import requests
import getpass
import socket
import platform as plat
from subprocess import check_output as inputstream

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

   \033[0mAll-in-One \033[32mtermux\033[0m Tool-panel
            By Toad114514
"""

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

# 自动更新源和软件包
def aug():
    if staxconf.skip_aug == False:
        os.system("apt update -y && apt upgrade -y")

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
                os.system("cd "+stax_path+" && git pull && cd")
                print("更新完成，重新输入 stax/staxle 可体验新版本")
            elif inp.strip() == "b" or inp.strip() == "back":
                restart_program()
            else: print("无效输入"); time.sleep(0.7); restart_program()
        elif inp.strip() == "u" or inp.strip() == "update":
            os.system("cd "+stax_path+" && git pull && cd")
            print("更新完成，重新输入 stax 或 staxle 可体验新版本")
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

def gitc(repo):
    if staxconf.git_clone_mirror == "kkgithub":
        os.system("git clone https://kkgithub.com/"+repo)
    else:
        os.system("git clone https://github.com/"+repo)

# 服务器命令
def nginxins():
    aug()
    os.system("pkg install nginx")
    done("安装已完成。您的 nginx 文件夹已存放于 /usr/local/nginx")

def apacheins():
    aug()
    os.system("apt install httpd -y")
    done("apache已安装，配置文件在 /etc/httpd/conf，网站目录在 /var/www/html")

def phpins():
    aug()
    os.system("apt install php -y")
    sel = input("输入你目前使用的服务器\n1) Nginx\n2) Apache\n输入：")
    if sel == "1":
        os.system("apt install php-fpm -y")
    elif sel == "2":
        os.system("apt install apache-php -y")
    done("PHP 安装成功，如果要配置 php 请启动 Server2me")

def ircins():
    aug()
    os.system("apt install ngircd -y")
    done("ngircd 安装成功，配置文件在 /etc/ngircd/ 里")

def sshd():
    aug()
    os.system("apt install sshd -y")
    done("sshd 安装完成\n输入 sshd 启动")

def lighttpd():
    aug()
    os.system("apt install lighttpd -y")
    done("lighttpd 安装完成\n可进入 Server2me 配置")

def mysql():
    aug()
    os.system("apt install mariadb -y")
    done("mysql 安装完成！\n输入 mysqld 启动服务器")

def proot_distro():
    proot_distro_ins = os.popen("pkg list-installed|grep proot-distro")
    if "proot-distro" not in proot_distro_ins.read():
        os.system("apt install proot-distro -y")
        done("proot-distro 安装完成")
    else:
        print("Proot-distro 帮助：")
        print("proot-distro ls 查看可安装的proot")
        print("proot-distro install <alisa> 安装proot")
        print("proot-distro sh <alisa> 启动linux")
        input("回车继续")
        restart_program()
###########
# 桌面环境
###########
def openbox():
    openbox_ins = os.popen("pkg list-installed|grep openbox")
    if "openbox" not in openbox_ins.read():
        aug()
        os.system("apt install x11-repo -y")
        os.system("apt install openbox tint2 aterm -y")
        tigervnc_ins = os.popen("pkg list-installed|grep tigervnc")
        if "tigervnc" not in tigervnc_ins.read():
            print("接下来需要配置 vnc 设置，三个输入框依次是：\n输入vnc密码\n再次输入vnc密码\n启用查看模式（不可操控）\n前两个框输入你的vnc密码，后面输入n关闭\n按下回车进行配置")
            os.system("vncserver -localhost")
        else:
            print(output("d","已安装 tigervnc，跳过 vnc 配置..."))
        print("写入 vnc 启动脚本...")
        startvnc = "openbox &\ntint2 &\naterm &"
        os.system("rm -rf ~/.vncxstartup")
        os.system(f"echo {startvnc} > ~/.vnc/xstartup")
        done("openbox 和 vnc 安装成功\n输入 vncserver 启动桌面环境")
    else:
        print("已经安装了 openbox 窗口管理器，您要...\n1) 卸载 openbox（保留vnc服务）\n2) 卸载 openbox（不保留vnc服务）\n3) 启动该桌面环境\n4) 返回主菜单")
        sel = input("Staxle/installed $:")
        if sel == "1":
            os.system("apt remove openbox aterm tint2 -y")
            os.system("apt autoremove")
            done("openbox 删除成功\n但是vnc服务没有删除")
        elif sel == "2":
            os.system("apt remove openbox aterm tint2 tigervnc -y")
            os.system("apt autoremove")
            print(output("i","正在删除 vnc 配置文件"))
            os.system("rm -rf ~/.vnc")
            done("openbox 和 vnc 服务卸载完成")
        elif sel == "3":
            os.system("vncserver")
            restart_program()
        elif sel == "4":
            restart_program()
        else:
            restart_program()

def fvwm():
    x_ins = os.popen("pkg list-installed|grep fvwm")
    if "fvwm" not in x_ins.read():
        aug()
        os.system("apt install x11-repo -y")
        os.system("apt install fvwm tint2 aterm -y")
        tigervnc_ins = os.popen("pkg list-installed|grep tigervnc")
        if "tigervnc" not in tigervnc_ins.read():
            print("接下来需要配置 vnc 设置，三个输入框依次是：\n输入vnc密码\n再次输入vnc密码\n启用查看模式（不可操控）\n前两个框输入你的vnc密码，后面输入n关闭\n按下回车进行配置")
            os.system("vncserver -localhost")
        else:
            print(output("d","已安装 tigervnc，跳过 vnc 配置..."))
        print("写入 vnc 启动脚本...")
        startvnc = "fvwm &\ntint2 &\naterm &"
        os.system("rm -rf ~/.vnc/xstartup")
        os.system(f"echo {startvnc} > ~/.vnc/xstartup")
        done("fvwm 和 vnc 安装成功\n输入 vncserver 启动桌面环境")
    else:
        print("已经安装了 fvwm 窗口管理器，您要...\n1) 卸载 openbox（保留vnc服务）\n2) 卸载 openbox（不保留vnc服务）\n3) 启动该桌面环境\n4) 返回主菜单")
        sel = input("Staxle/installed $:")
        if sel == "1":
            os.system("apt remove fvwm aterm tint2 -y")
            os.system("apt autoremove")
            done("fvwm 删除成功\n但是vnc服务没有删除")
        elif sel == "2":
            os.system("apt remove openbox aterm tint2 tigervnc -y")
            os.system("apt autoremove")
            print(output("i","正在删除 vnc 配置文件"))
            os.system("rm -rf ~/.vnc")
            done("fvwm 和 vnc 服务卸载完成")
        elif sel == "3":
            os.system("vncserver")
            restart_program()
        elif sel == "4":
            restart_program()
        else:
            restart_program()

#############
# Xfce4-DesktopEnvironment Code
#############
def xfce4():
    print("你想要在使用什么方式输出图形？\n[1] VNC \n[2] termux-x11 (图形加速，建议）")
    sel = input("选择：")
    if sel.strip() == "1":
        disp = "vnc"
        print("设置 vnc 密码，这个密码在连接时需要用到（长度必须是 5-8 位）")
        vnc_passwd = input("输入密码：")
    elif sel.strip() == "2":
        disp = "tx11"
        print("\n请在你的手机上面安装好 termux-x11\n还未安装的请移到 https://pan.huang1111.cn/s/m78eS1?path=%2F%E5%AE%89%E5%8D%93APK%2Ftermux-x11 下载并安装")
        input("如果已经安装好 termux-x11 的按下回车键继续")
        is_legacy = input("\n你的设备是不是为老手机/战神机？（例如oppoa5）\n因为termux-x11默认使用新的绘画方式，但老手机/战神机只会显示一个鼠标就没有了，解决方法就是使用传统绘画模式\n要启用传统绘画模式吗？[y/n]：")
        if is_legacy != "y" and is_legacy != "n":
            print("无效输入")
            time.sleep(0.5)
            restart_program()
    else:
        print("无效输入")
        time.sleep(0.7)
        restart_program()
    # vnc_config
    if disp == "vnc":
        output("i","开始安装 xfce4...")
        aug()
        os.system("pkg install x11-repo")
        os.system("pkg install xfce4 tigervnc -y")
        output("i","设置 vnc 服务器...")
        os.system("mkdit ~/.vnc")
        os.system(f"echo {vnc_passwd} > ~/.vnc/passwd")
        with open("~/.vnc/xstartup","w") as f:
            f.write("startxfce4")
        os.system("chmod +x ~/.vnc/xstartup")
        os.system("touch $PREFIX/bin/xfce4")
        with open(os.path.join(prefix, "bin", "xfce4"),"w") as f:
            bash_setup = "#type-bash vnc\n# 请不要删除上方注释！\necho xfce4的图形输出在 localhost:5902，请使用任意 vnc 客户端访问 localhost:5902\nvncserver :2 -geometry 1920x1080"
            f.write(bash_setup)
        os.system("chmod +x $PREFIX/bin/xfce4")
        print("xfce4 安装完成\n以后只需输入 xfce4 便可启动\n你现在要：")
        sel = input("[1] 现在启动\n[2] 返回 Staxle")
        if sel == "1":
            os.system("xfce4")
            restart_program()
        else:
            restart_program()
    # termux x11
    elif disp == "tx11":
        output("i","开始安装 xfce4...")
        aug()
        os.system("pkg install x11-repo")
        os.system("pkg install xfce4 tigervnc xwayland termux-x11-nightly -y")
        output("i","设置 termux-x11...")
        os.system("touch $PREFIX/bin/xfce4")
        if is_legacy == "y":
            with open(os.path.join(prefix, "bin", "xfce4"),"w") as f:
                bash_setup = "# vnc\ntermux-x11 :0 -legacy-drawing &\nenv DISPLAY=:0 startxfce4 &\necho xfce4的图形输出在 termux-x11 服务器上，请打开 termux-x11 应用"
                f.write(bash_setup)
        if is_legacy == "n":
            with open(os.path.join(prefix, "bin", "xfce4"),"w") as f:
                bash_setup = "#type-bash tx11\n#请不要删除上方注释！\ntermux-x11 :0 &\nenv DISPLAY=:0 startxfce4 &\necho xfce4的图形输出在 termux-x11 服务器上，请打开 termux-x11 应用"
                f.write(bash_setup)
        os.system("chmod +x $PREFIX/bin/xfce4")
        print("xfce4 安装完成\n以后只需输入 xfce4 便可启动\n你现在要：")
        sel = input("[1] 现在启动\n[2] 返回 Staxle")
        if sel == "1":
            os.system("xfce4")
            restart_program()
        else:
            restart_program()

def xfce4_main():
    if "xfce4" in os.popen("pkg list-installed|grep xfce4").read():
        sel = input("检测到已安装 xfce4，你要\n[1] 启动\n[2] 卸载\n[3] 重装\n[4] 设置\n[5] 退出")
        if sel == "2":
            sel = input("确定卸载xfce4？[y/n]：")
            if sel == "y":
                os.system("pkg remove xfce4 -y")
                print("卸载完成。")
                time.sleep(0.7)
                restart_program()
            else:
                restart_program()
        elif sel == "1":
            os.system("xfce4")
            restart_program()
        elif sel == "3":
            xfce4()
        elif sel == "4":
            with open(os.path.join(prefix, "bin", "xfce4"),"r") as f:
                type = f.read()
            type = os.popen("cat $PREFIX/bin/xfce4|grep type-bash").read()
            if type in "tx11":
                sel = input("使用传统绘画模式？（老设备/战神机需要使用 否则黑屏只有鼠标显示 例如oppoa5）\n[y/n](任意内容取消修改): ")
                if sel == "y":
                    os.system("sed -i '3s/.*/termux-x11 :0 -legacy-drawing &' $PREFIX/bin/xfce4")
                    restart_program()
                elif sel == "n":
                    os.system("sed -i '3s/.*/termux-x11 :0 &' $PREFIX/bin/xfce4")
                    restart_program()
                else:
                    restart_program()
            elif type in "vnc":
                sel = input("修改显示分辨率（长x宽，中间的x是必须是字母小写x，例如 1920x1080、800x600 等）：")
                temp = "vncserver :2 -geometry "+sel
                os.system(f"sed -i '3s/.*/{temp}' $PREFIX/bin/xfce4")
                restart_program()
            else:
                print("程序不知道你的 xfce4 使用了什么方式显示（你是不是删掉那行注释了！），自动返回")
                time.sleep(1)
                restart_program()
        elif sel == "5":
            restart_program()
        else:
            print("无效输入")
            time.sleep(0.7)
            restart_program()
    else:
        xfce4()

########
# Termux
#########
def termux_repo():
    os.system("termux-change-repo")
    restart_program()

def termux_storage():
    print("请在弹出来的窗口中点击允许")
    time.sleep(0.8)
    os.system("termux-setup-storage")
    restart_program()

def qurxin():
    aug()
    os.system("apt install git mpv figlet -y")
    os.system("pip install lolcat")
    gitc("fikrado/qurxin")
    os.system('mv qurxin {}'.format(homeDir))
    os.system("cd ./qurxin")
    os.system("chmod +x *")
    os.system("sh ./install.sh")
    done("qurxin 安装完成\n重启 termux 便可查看")

def termux_desktop():
    print("你可能需要去查询向导，详细请访问 https://github.com/adi1090x/termux-desktop")
    time.sleep(1.5)
    aug()
    os.system("apt install git -y")
    os.system("git clone --depth=1 https://github.com/adi1090x/termux-desktop.git")
    os.system('mv termux-desktop {}'.format(homeDir))
    os.system("cd ~/termux-desktop")
    os.system("chmod +x ./setup.sh")
    os.system("./setup.sh --install")
    done("termux-desktop 安装完成\n您的设备拥有了一个桌面环境\n您可输入 cd ~/termux-desktop && ./setup.sh --uninstall 卸载它")

def toolx():
    aug()
    os.system("pkg install python3 git -y")
    gitc("vaginessa/Tool-X")
    os.system('mv Tool-X {}'.format(homeDir))
    os.system("cd ~/Tool-X")
    os.system("chmod +x ./install.axe")
    os.system("./install.axe")

def lazymux():
    aug()
    os.system("pkg install python3 git -y")
    gitc("Gameye98/Lazymux")
    os.system("mv Lazymux {}".format(homeDir))
    done("Lazymux 安装完成！\n输入 cd Lazymux && python lazymux.py 启动")

#def tmoe():

def neofetch():
    neofetch_ins = os.popen("pkg list-installed|grep neofetch")
    if "neofetch" not in neofetch_ins.read():
        aug()
        os.system("apt install neofetch -y")
        os.system("neofetch")
        done("neofetch 安装完成\n输入 neofetch 查询信息\n或者在本工具的 termux 菜单里再次选择 neofetch 即可查询")
    else:
        os.system("neofetch")
        input("回车键继续")
        restart_program()

# hacker
def nmap():
    aug()
    os.system("apt install nmap -y")
    done("Nmap 安装完成\n输入 nmap 启动")

def sqlmap():
    aug()
    os.system("apt install git python2 -y")
    gitc("sqlmapproject/sqlmap")
    os.system('mv sqlmap {}'.format(homeDir))
    done("Sqlmap 安装完成")

def evilurl():
    aug()
    os.system("apt install git python2 python3 -y")
    gitc("UndeadSec/EvilURL")
    os.system('mv sqlmap {}'.format(homeDir))
    done("EvilUrl 安装完成")

def wifite2():
    if int(inputstream("id -u".split()).decode("utf8")) != 0: print("\n你设备都没Root还想黑别人家WiFi？食懵你啊！"); restart_program()
    else:
        aug()
        os.system("apt install git python2 python3 -y")
        gitc("derv82/wifite2")
        os.system('mv wifite2 {}'.format(homeDir))
        done("wifite2 安装完成")

def wifiphisher():
    if int(inputstream("id -u".split()).decode("utf8")) != 0: print("\n你设备都没Root还想黑别人家WiFi？食懵你啊！"); restart_program()
    else:
        aug()
        os.system("apt install git python3 -y")
        gitc("wifiphisher/wifiphisher")
        os.system('mv wifiphisher {}'.format(HomeDir))
        done("wifiphisher 安装完成")

def apktool():
    aug()
    os.system('apt install nodejs apktool -y')
    os.system('npm i -g apk-mitm')
    open(os.getenv("HOME")+"/.bashrc","a").write("\nalias apk-mitm=\"apk-mitm --apktool $PREFIX/share/java/apktool.jar\"\n")
    done("apktool 安装完成\n输入 apk-mitm 使用")

def eagleeye():
    aug()
    os.system("apt install python3 -y")
    gitc("ThoughtfulDev/EagleEye")
    os.system('mv EagleEye {}'.format(homeDir))
    os.system("cd ~/EagleEye")
    os.system("pip install -r requirements.txt")
    os.system("pip install --update beautifulsoup4 html5lib spry")
    done("EagleEye 安装完成")

def emailall():
    aug()
    os.system("apt install git -y")
    gitc("Taonn/EmailAll.git")
    os.system('mv EmailAll {}'.format(homeDir))
    os.system("pip3 install -r requirements.txt")
    done("EmailAll 安装完成")

def arl():
    aug()
    os.system("apt install wget -y")
    os.system("wget https://raw.githubusercontent.com/Aabyss-Team/ARL/master/misc/setup-arl.sh")
    os.system('mv setup-arl.sh {}'.format(homeDir))
    os.system("cd ~")
    os.system("chmod +x ./setup-arl.sh")
    os.system("./setup-arl.sh")
    done("ARL 安装完成\n使用浏览器输入 http://本设备IP:5003/ 登录后台\n账号：admin 密码：arlpass")

def mapeye():
    aug()
    os.system("apt install git -y")
    gitc("bhikandeshmukh/MapEye.git")
    os.system('mv MapEye {}'.format(homeDir))
    os.system("apt install python php -y")
    os.system("pip3 install requests")
    done("MapEye 安装完成")

def sqlscan():
    aug()
    os.system("apt install php curl -y")
    os.system("curl https://raw.githubusercontent.com/Cvar1984/sqlscan/dev/build/main.phar --output $PREFIX/bin/sqlscan")
    os.system("chmod +x $PREFIX/bin/sqlscan")
    done("Sqlscan 安装完成\n输入 sqlscan 使用")

def sqlmate():
    aug()
    os.system("apt install git -y")
    gitc("UltimateHackers/sqlmate")
    os.system('mv sqlmate {}'.format(homeDir))
    os.system("cd ~/sqlmate")
    os.system("pip install -r requirements.txt")
    done("sqlmate 安装完成")

def xsstrike():
    aug()
    os.system('apt install git python2 -y')
    os.system('python2 -m pip install fuzzywuzzy prettytable mechanize HTMLParser')
    gitc("s0md3v/XSStrike")
    os.system('mv XSStrike {}'.format(homeDir))
    done("XSStrike 安装完成")

def metasploit():
    aug()
    print(output("i","安装 Metasploit-framework 6（依靠脚本 gushmazuko/metasploit_in_termux）"))
    gitc("gushmazuko/metasploit_in_termux")
    os.system('mv metasploit_in_termux {}'.format(homeDir))
    os.system("cd {}/metasploit_in_termux && bash metasploit.sh".format(homeDir))
    done("Metasploit 安装完成\n执行 msfconsole 启动")

def easysploit():
    aug()
    os.system("pkg install git -y")
    gitc("KALILINUXTRICKSYT/easysploit")
    os.system('mv easysploit {}'.format(homeDir))
    os.system("cd easysploit")
    print(output("i","启动 Easysploit 安装脚本..."))
    os.system("bash ./installer.sh")
    done("Easysploit 安装完成！输入 easysploit 启动工具")

def phonesploit():
    aug()
    os.system("pkg install git python -y")
    gitc("AzeemIdrisi/PhoneSploit-Pro.git")
    os.system('mv PhoneSploit-Pro {}'.format(homeDir))
    os.system("cd $HOME/PhoneSploit-Pro")
    os.system("python install -r requirements.txt")
    done("PhoneSploit 安装完成！\n输入 'cd ~/PhoneSploit-Pro && python3 phonesploitpro.py' 启动")

def cmseek():
    aug()
    os.system("pkg install git python -y")
    gitc("Tuhinshubhra/CMSeeK")
    os.system('mv CMSeeK {}'.format(homeDir))
    os.system("cd $HOME/CMSeeK")
    os.system("python install -r requirements.txt")
    done("CMSeek 安装成功\n输入'cd ~/CMSeek && python3 cmseek.py' 启动")

# 软件中心
## IDE
def vim():
    aug()
    os.system("pkg install vim -y")
    done("vim 安装完成\n输入 vim 进入编辑器")

def emacs():
    aug()
    os.system("pkg install emacs -y")
    done("Emacs 安装完成\n输入 Emacs 进入编辑器")

def code_server():
    aug()
    os.system("pkg install tur-repo -y")
    os.system("apt install code-server -y")
    done("Code-Server 安装完成\ncode-server 配置文件路径位于 ~/.config/code-server/config.yaml\n启动：code-server")

def clang():
    aug()
    os.system("pkg install clang -y")
    done("clang 安装成功")

def lazygit():
    os.system("pkg install lazygit -y")
    done("Lazygit 安装成功\n在git文件夹中输入 lazygit 启动")
## 网络/互联网
def w3m():
    aug()
    os.system("pkg install w3m -y")
    done("w3m 安装完成\n用法：w3m <链接>")

def weechat():
    aug()
    os.system("pkg install weechat -y")
    done("weechat 安装完成\n启动：weechat")

def lynx():
    aug()
    os.system("pkg install lynx -y")
    done("lynx 安装完成\n启动：lynx <url>")

def firefox():
    aug()
    os.system("pkg install x11-repo -y")
    os.system("pkg install firefox -y")
    done("Firefox 安装成功\n在桌面环境中输入 firefox 启动浏览器")

##########
## 多媒体
##########
def timg():
    aug()
    os.system("pkg install timg -y")
    done("timg 安装成功！\n查看图片和视频：timg <图片/视频路径>")

def mpd():
    aug()
    os.system("pkg install mpd -y")
    done("mpd 安装成功！")

def mpv():
    aug()
    os.system("pkg install mpv -y")
    done("mpd 安装成功！\n播放音频（其实视频也可以 但在终端运行下只有声）：mpv <音频/视频路径>")

def musicfox():
    aug()
    os.system("pkg install musicfox -y")
    done("musicfox 安装成功！\ntermux 播放音乐时可能会卡，可以去仓库查看解决办法\n仓库地址：https://github.com/go-musicfox/go-musicfox\n启动命令：musicfox")