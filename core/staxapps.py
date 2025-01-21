import os
from core.staxcore import *
import core.i18n.i18n as lang
# 自动更新源和软件包
def aug():
    if staxconf.skip_aug == False:
        os.system("apt update -y && apt upgrade -y")
        
def gitc(repo):
    if staxconf.git_clone_mirror == "kkgithub":
        os.system("git clone https://kkgithub.com/"+repo)
    else:
        os.system("git clone https://github.com/"+repo)

# 服务器命令
def nginxins():
    aug()
    os.system("pkg install nginx")
    done(lang.get("ok.nginx"))

def apacheins():
    aug()
    os.system("apt install httpd -y")
    done(lang.get("ok.apache"))

def phpins():
    aug()
    os.system("apt install php -y")
    sel = input("输入你目前使用的服务器\n1) Nginx\n2) Apache\n输入：")
    if sel == "1":
        os.system("apt install php-fpm -y")
    elif sel == "2":
        os.system("apt install apache-php -y")
    done(lang.get("ok.php"))

def ircins():
    aug()
    os.system("apt install ngircd -y")
    done(lang.get("ok.ngircd"))

def sshd():
    aug()
    os.system("apt install sshd -y")
    done(lang.get("ok.sshd"))

def lighttpd():
    aug()
    os.system("apt install lighttpd -y")
    done(lang.get("ok.lighttpd"))

def mysql():
    aug()
    os.system("apt install mariadb -y")
    done(lang.get("ok.mysql"))

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
    print("你想要在使用什么方式输出图形？\n[1] VNC \n[2] termux-x11 (图形加速，建议）\n[3] noVNC（网页vnc，可以尝鲜）")
    sel = input("选择：")
    if sel.strip() == "1":
        disp = "vnc"
        print("设置 vnc 密码，这个密码在连接时需要用到（长度必须是 5-8 位）")
        vnc_passwd = input("输入密码：")
    if sel.strip() == "3":
        disp = "novnc"
        print("设置 vnc 密码，这个密码在连接时需要用到（长度必须是 5-8 位）")
        vnc_passwd = input("输入密码：")
    elif sel.strip() == "2":
        disp = "tx11"
        print("\n请在你的手机上面安装好 termux-x11\n还未安装的请移到 https://pan.huang1111.cn/s/m78eS1?path=%2F%E5%AE%89%E5%8D%93APK%2Ftermux-x11 下载并安装")
        input("如果已经安装好 termux-x11 的按下回车键继续")
        is_legacy = input("\n你的设备是不是为老手机/战神机？（例如oppoa5）\n因为termux-x11默认使用新的绘画方式，导致老手机/战神机只会显示一个鼠标就没有了，解决方法就是使用传统绘画模式\n要启用传统绘画模式吗？[y/n]：")
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
    # novnc
    if disp == "novnc":
        output("i","开始安装 xfce4...")
        aug()
        os.system("pkg install x11-repo")
        os.system("pkg install xfce4 tigervnc -y")
        output("i","设置 vnc 服务器...")
        os.system("mkdit ~/.vnc")
        os.system(f"echo {vnc_passwd} > ~/.vnc/passwd")
        with open("~/.vnc/xstartup","w") as f:
            f.write("startxfce4")
        gitc("novnc/noVNC")
        os.system('mv noVNC {}'.format(homeDir))
        os.system(f"chmod +755 {homeDir}/noVNC/utils/novnc_proxy")
        os.system("chmod +x ~/.vnc/xstartup")
        os.system("touch $PREFIX/bin/xfce4")
        with open(os.path.join(prefix, "bin", "xfce4"),"w") as f:
            bash_setup = f"#type-bash novnc\n# 请不要删除上方注释！\necho xfce4的图形输出在 localhost:5902，你可以使用任何 vnc 服务连接，但现在还没打开 noVNC\nvncserver :2 -geometry 1920x1080 &\necho noVNC 启动！接下来会打印出一个地址，使用浏览器访问即可\n{homeDir}/noVNC/utils/novnc_proxy --vnc localhost:5902"
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
            elif type in "vnc" or type in "novnc":
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

def lxqt():
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
        is_legacy = input("\n你的设备是不是为老手机/战神机？（例如oppoa5）\n因为termux-x11默认使用新的绘画方式，导致老手机/战神机只会显示一个鼠标就没有了，解决方法就是使用传统绘画模式\n要启用传统绘画模式吗？[y/n]：")
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
        output("i","开始安装 lxqt...")
        aug()
        os.system("pkg install x11-repo")
        os.system("pkg install lxqt tigervnc -y")
        output("i","设置 vnc 服务器...")
        os.system("mkdit ~/.vnc")
        os.system(f"echo {vnc_passwd} > ~/.vnc/passwd")
        with open("~/.vnc/xstartup","w") as f:
            f.write("startxfce4")
        os.system("chmod +x ~/.vnc/xstartup")
        os.system("touch $PREFIX/bin/xfce4")
        with open(os.path.join(prefix, "bin", "xfce4"),"w") as f:
            bash_setup = "#type-bash vnc\n# 请不要删除上方注释！\necho lxqt的图形输出在 localhost:5902，请使用任意 vnc 客户端访问 localhost:5902\nvncserver :2 -geometry 1920x1080"
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
        os.system("pkg install lxqt xwayland termux-x11-nightly -y")
        output("i","设置 termux-x11...")
        os.system("touch $PREFIX/bin/lxqt")
        if is_legacy == "y":
            with open(os.path.join(prefix, "bin", "lxqt"),"w") as f:
                bash_setup = "# vnc\ntermux-x11 :0 -legacy-drawing &\nenv DISPLAY=:0 startlxqt &\necho lxqt的图形输出在 termux-x11 服务器上，请打开 termux-x11 应用"
                f.write(bash_setup)
        if is_legacy == "n":
            with open(os.path.join(prefix, "bin", "lxqt"),"w") as f:
                bash_setup = "#type-bash tx11\n#请不要删除上方注释！\ntermux-x11 :0 &\nenv DISPLAY=:0 startlxqt &\necho lxqt的图形输出在 termux-x11 服务器上，请打开 termux-x11 应用"
                f.write(bash_setup)
        os.system("chmod +x $PREFIX/bin/xfce4")
        print("lxqt 安装完成\n以后只需输入 lxqt 便可启动\n你现在要：")
        sel = input("[1] 现在启动\n[2] 返回 Staxle")
        if sel == "1":
            os.system("xfce4")
            restart_program()
        else:
            restart_program()

def lxqt_main():
    if "lxqt" in os.popen("pkg list-installed|grep lxqt").read():
        sel = input("检测到已安装 lxqt，你要\n[1] 启动\n[2] 卸载\n[3] 重装\n[4] 设置\n[5] 退出")
        if sel == "2":
            sel = input("确定卸载lxqt？[y/n]：")
            if sel == "y":
                os.system("pkg remove lxqt -y")
                print("卸载完成。")
                time.sleep(0.7)
                restart_program()
            else:
                restart_program()
        elif sel == "1":
            os.system("lxqt")
            restart_program()
        elif sel == "3":
            lxqt()
        elif sel == "4":
            with open(os.path.join(prefix, "bin", "lxqt"),"r") as f:
                type = f.read()
            type = os.popen("cat $PREFIX/bin/xfce4|grep type-bash").read()
            if type in "tx11":
                sel = input("使用传统绘画模式？（老设备/战神机需要使用 否则黑屏只有鼠标显示 例如oppoa5）\n[y/n](任意内容取消修改): ")
                if sel == "y":
                    os.system("sed -i '3s/.*/termux-x11 :0 -legacy-drawing &' $PREFIX/bin/lxqt")
                    restart_program()
                elif sel == "n":
                    os.system("sed -i '3s/.*/termux-x11 :0 &' $PREFIX/bin/lxqt")
                    restart_program()
                else:
                    restart_program()
            elif type in "vnc":
                sel = input("修改显示分辨率（长x宽，中间的x是必须是字母小写x，例如 1920x1080、800x600 等）：")
                temp = "vncserver :2 -geometry "+sel
                os.system(f"sed -i '3s/.*/{temp}' $PREFIX/bin/lxqt")
                restart_program()
            else:
                print("程序不知道你的 lxqt 使用了什么方式显示（你是不是删掉那行注释了！），自动返回")
                time.sleep(1)
                restart_program()
        elif sel == "5":
            restart_program()
        else:
            print("无效输入")
            time.sleep(0.7)
            restart_program()
    else:
        lxqt()

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

def termux_s9():
    print("解决 [Process completed (signal 9) - press Enter]（Android 12以上的PhantomProcesskiller限32个子进程问题）")
    print("如果搞桌面环境或其他情况时确实出现该问题杀你后台，则输入y，否则输入n返回（其他内容也是返回）")
    sel=input("[y/n]: ")
    if sel == "y":
        aug()
        os.system("pkg install android-tools")
        print("接下来到你操作了：\nStep1 开发者模式：\n根据自己手机系统找到关于手机（部分可能需要查看详细信息才能继续）-> 点击“版本号”多次启动开发者模式\nStep2 无线调试：\n设置主页 -> 根据手机系统找到开发者模式 -> 打开无线调试开关 -> 使用配对码配对设备\nStep3 给我记：\n记住此时弹出的 IP地址（包括端口，全部照搬）和配对码")
        ip = input("如果已完成所有操作，请在这里输入IP地址\n弹出 “Enter pairing code：”时，请输入上述记住的配对码\n[ip地址]: ")
        os.system(f"adb pair {ip}")
        print("连接到 adb\n回到刚才的无线调试界面，复制“IP地址和端口”这一项下面的ip地址和端口，并在这里重新输入新的ip地址和端口")
        ip = input("adb connect: ")
        os.system(f"adb connect {ip}")
        os.system("adb shell device_config set_sync_disabled_for_tests persistent && adb shell device_config put activity_manager max_phantom_processes 65536")
        os.system("adb kill-server")
        done("现在你的手机不会莫名其妙给你干没了\n放心搞桌面环境吧（回车键返回）")
    else:
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

def ttyd():
    os.system("pkg install ttyd -y")
    done("ttyd 安装成功\n输入 ttyd bash 便可以在网页上启动终端")

def python():
    aug()
    os.system("pkg install python -y")
    done("Python 安装成功，可！\n输入 python 进入 ipython 界面")
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

def aria2():
    aug()
    os.system("pkg install aria2")
    done("Aria2 安装成功！\n输入 aria2c <链接> 可本地下载")
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

def cmus():
    aug()
    os.system("pkg install cmus -y")
    done("cmus 安装成功！\n输入 cmus 启动本体")
# x11-apps
def firefox():
    aug()
    os.system("pkg install firefox -y")
    done("firefox 安装成功，请在 X11 桌面环境下运行")
def audacious():
    aug()
    os.system("pkg install audacious -y")
    done("audacious 安装成功，请在 X11 桌面环境下运行")
def gimp():
    aug()
    os.system("pkg install gimp -y")
    done("gimp 安装成功，请在 X11 桌面环境下运行")
def gvim():
    aug()
    os.system("pkg install vim-gtk -y")
    done("gvim 安装成功，请在 X11 桌面环境下运行")
def vlcqt():
    aug()
    os.system("pkg install vlc vlc-qt -y")
    done("vlc-qt 安装成功，请在 X11 桌面环境下运行")