import os, sys, time
import urllib.request
import getpass
import socket
import platform as plat
from subprocess import check_output as inputstream
class stax():
    version = "v1.02"
    version_num = 115

stax_banner = """
   ______             __
  / __/ /____ ___ __ / /__
 _\ \/ __/ _ `/\ \ // / -_)
/___/\__/\_,_//_\_\/_/\__/
   All-in-One termux Tool-panel
            By Toad114514
"""
backtomenu_banner = """
99) 回到主页面
00) 退出 Staxle
"""

prefix = os.getenv("PREFIX")
cache_1 = prefix+"/tmp/staxle"
configBase = "[HOME] = ~"
configFile = "../stax.conf"
user = getpass.getuser()
# ip
soc_var=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip_socket_temp = soc_var.connect(("8.8.8.8",80))
ip = soc_var.getsockname()[0]

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

def banner():
	print(stax_banner)
	print(stax.version + "    欢迎 "+user+"/"+str(plat.system()))

def err():
    print("无效输入。")
    input("")

def aug():
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

def loadConfigFile():
	checkConfigFile()
	lfile = ""
	try:
		lfile = [x.split("=")[-1].strip() for x in open(configFile,"r").splitlines() if x.split("=")[0].strip() == "[HOME]"][0]
	except Exception as e:
		lfile = "~"
	return lfile

homeDir = loadConfigFile()

def about():
    print(stax_banner)
    print("Staxle "+stax.version+" ("+str(stax.version_num)+")")
    print("终端设备：")
    print(str(plat.system())+"("+str(plat.processor())+"/"+str(plat.architecture())+")")
    print("Python "+str(plat.python_version())+"("+str(plat.python_implementation())+")")
    print("ip:",ip)
    input("按下回车键回到菜单")
    restart_program()

def about_web():
    about01 = "Staxle "+stax.version+" ("+str(stax.version_num)+")"
    about02 = str(plat.system())+"("+str(plat.processor())+"/"+str(plat.architecture())+")"
    about03 = "Python "+str(plat.python_version())+"("+str(plat.python_implementation())+")"
    about04 = "ip:"+ip
    return stax_banner + "\n终端设备：\n" + about01 + "\n" + about02 + "\m" + about03 + "\n" + about04
    
# 服务器命令
def nginxins():
    aug()
    os.system("wget http://nginx.org/download/nginx-1.14.2.tar.gz")
    os.system("apt install gcc pcre pcre-devel openssl tar -y")
    os.system("tar -xvf ./nginx-1.14.2.tar.gz -C /usr/local")
    os.system("rm -rf ./nginx-1.14.2.tar.gz")
    os.system("cd nginx-1.14.2")
    os.system("""
./configure \
--prefix=/usr/local/nginx \
--pid-path=/var/run/nginx/nginx.pid \
--lock-path=/var/lock/nginx.lock \
--error-log-path=/var/log/nginx/error.log \
--http-log-path=/var/log/nginx/access.log \
--with-http_gzip_static_module \
--http-client-body-temp-path=/var/temp/nginx/client \
--http-proxy-temp-path=/var/temp/nginx/proxy \
--http-fastcgi-temp-path=/var/temp/nginx/fastcgi \
--http-uwsgi-temp-path=/var/temp/nginx/uwsgi \
--http-scgi-temp-path=/var/temp/nginx/scgi \
--with-http_stub_status_module \
--with-http_ssl_module \
--with-file-aio \
--with-http_realip_module
    """)
    os.system("mkdir /var/temp/nginx -p")
    os.system("make")
    os.system("make install")
    done("安装已完成。您的 nginx 文件夹已存放于 /usr/local/nginx")

def nginxconfig():
    aug()
    os.system("vim /usr/local/nginx/conf/nginx.conf")
    restart_program()

def nginxstart():
    os.system("cd sbin")
    os.system("./nginx")
    done("Nginx 已启动")
    os.system("ps -aux | grep nginx")

def nginxstop():
    os.system("cd sbin")
    os.system("./nginx -s stop")
    done("Nginx 已关闭")

def nginxreload():
    os.system("cd sbin && ./nginx -s reload")
    done("Nginx 配置已重置")

def apacheins():
    aug()
    os.system("apt install httpd -y")
    done("apache已安装，配置文件在 /etc/httpd/conf，网站目录在 /var/www/html")

def apachestart():
    os.system("/etc/init.d/httpd start")
    done("Apache 已启动")

def apachestop():
    os.system("/etc/init.d/httpd stop")
    done("Apache 已关闭")

def phpins():
    aug()
    pkg("php libapache2-mod-php php-fpm")
    done("PHP 安装成功，安装后自动与 Nginx 和 Apache 配合")

def ircins():
    aug()
    os.system("apt install ngircd")
    done("ngircd 安装成功，配置文件在 /etc/ngircd/ 里")

def ircstart():
    os.system("/etc/init.d/ngircd start")
    done("Ngircd 服务器已启动")

def ircstop():
    os.system("/etc/init.d/ngircd stop")
    done("Ngircd 服务器已停止")

def sshd():
    aug()
    os.system("apt install sshd")
    done("sshd 安装完成\n输入 sshd 启动")

def proot_distro():
    os.system("apt install proot-distro")
    done("proot-distro 安装完成")

# Termux
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
    os.system("apt install mpv figlet")
    os.system("pip install lolcat")
    os.system("git clone https://github.com/fikrado/qurxin")
    os.system('mv qurxin {}'.format(homeDir))
    os.system("cd ./qurxin")
    os.system("chmod +x *")
    os.system("sh ./install.sh")
    done("qurxin 安装完成\n重启 termux 便可查看")

def termux_desktop():
    print("你可能需要去查询向导，详细看 https://github.com/adi1090x/termux-desktop")
    time.sleep(1.5)
    aug()
    os.system("git clone --depth=1 https://github.com/adi1090x/termux-desktop.git")
    os.system('mv termux-desktop {}'.format(homeDir))
    os.system("cd ~/termux-desktop")
    os.system("chmod +x ./setup.sh")
    os.system("./setup.sh --install")
    done("termux-desktop 安装完成\n您的设备拥有了一个桌面环境\n您可输入 cd ~/termux-desktop && ./setup.sh --uninstall 卸载它")

#def tool_x():

#def lazymux():

#def tmoe():

def neofetch():
    if os.path.exists("/data/data/com.termux/files/usr/bin/neofetch"):
        os.system("neofetch")
        input("回车键继续")
        restart_program()
    else:
        aug()
        os.system("apt install neofetch")
        os.system("neofetch")
        done("neofetch 安装完成\n输入 neofetch 查询信息\n或者在本工具的 termux 菜单里再次选择 neofetch 即可查询")
    
# hacker
def nmap():
    aug()
    os.system("apt install nmap -y")
    done("Nmap 安装完成\n输入 nmap 启动")

def sqlmap():
    aug()
    os.system("apt install git python2")
    os.system("git clone https://github.com/sqlmapproject/sqlmap")
    os.system('mv sqlmap {}'.format(homeDir))
    done("Sqlmap 安装完成")

def evilurl():
    aug()
    os.system("apt install git python2 python3")
    os.system("git clone https://github.com/UndeadSec/EvilURL")
    os.system('mv sqlmap {}'.format(homeDir))
    done("EvilUrl 安装完成")

def wifite2():
    if int(inputstream("id -u".split()).decode("utf8")) != 0: print("\n你设备都没Root还想黑别人家WiFi？食懵你啊！");
    else:
        aug()
        os.system("apt install git python2 python3")
        os.system("git clone https://github.com/derv82/wifite2")
        os.system('mv wifite2 {}'.format(homeDir))
        done("wifite2 安装完成")

def wifiphisher():
    if int(inputstream("id -u".split()).decode("utf8")) != 0: print("\n你设备都没Root还想黑别人家WiFi？食懵你啊！");
    else:
        aug()
        os.system("apt install git python3")
        os.system("git clone https://github.com/wifiphisher/wifiphisher")
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
    os.system("apt install python3")
    os.system("git clone https://github.com/ThoughtfulDev/EagleEye")
    os.system('mv EagleEye {}'.format(homeDir))
    os.system("cd ~/EagleEye")
    os.system("pip install -r requirements.txt")
    os.system("pip install --update beautifulsoup4 html5lib spry")
    done("EagleEye 安装完成")

def emailall():
    aug()
    os.system("git clone https://github.com/Taonn/EmailAll.git")
    os.system('mv EmailAll {}'.format(homeDir))
    os.system("pip3 install -r requirements.txt")
    done("EmailAll 安装完成")

def arl():
    aug()
    os.system("apt install wget")
    os.system("wget https://raw.githubusercontent.com/Aabyss-Team/ARL/master/misc/setup-arl.sh")
    os.system('mv setup-arl.sh {}'.format(homeDir))
    os.system("cd ~")
    os.system("chmod +x ./setup-arl.sh")
    os.system("./setup-arl.sh")
    done("ARL 安装完成\n使用浏览器输入 http://本设备IP:5003/ 登录后台\n账号：admin 密码：arlpass")

def mapeye():
    aug()
    os.system("git clone https://github.com/bhikandeshmukh/MapEye.git")
    os.system('mv MapEye {}'.format(homeDir))
    os.system("apt install python php")
    os.system("pip3 install requests")
    done("MapEye 安装完成")

def sqlscan():
    aug()
    os.system("apt install php curl")
    os.system("curl https://raw.githubusercontent.com/Cvar1984/sqlscan/dev/build/main.phar --output $PREFIX/bin/sqlscan")
    os.system("chmod +x $PREFIX/bin/sqlscan")
    done("Sqlscan 安装完成\n输入 sqlscan 使用")

def sqlmate():
    aug()
    os.system("git clone https://github.com/UltimateHackers/sqlmate")
    os.system('mv sqlmate {}'.format(homeDir))
    os.system("cd ~/sqlmate")
    os.system("pip install -r requirements.txt")
    done("sqlmate 安装完成")

def xsstrike():
    aug()
    os.system('apt install git python2')
    os.system('python2 -m pip install fuzzywuzzy prettytable mechanize HTMLParser')
    os.system('git clone https://github.com/s0md3v/XSStrike')
    os.system('mv XSStrike {}'.format(homeDir))
    done("XSStrike 安装完成")
# Chexo
def chexo():
    print("未完成")
    restart_program()
# cli-apk
def capk():
    os.system("python3 ./tool/capk/main.py")
    restart_program()