# staxle menu.py
# ByToad114514
# 仓库 in toad114514/Staxle
# 部分代码使用 Gameye98/Lazymux
# v1.05.2
import os
import requests
import time
import sys
import readline
from core.staxcore import *

def main():
    banner()
    print("""
  - 输入选项选择
1) 服务器管理工具
2) 桌面环境管理
3) Termux 工具
4) 虚拟机 (Qemd)
5) 安装包管理
6) 千年软件老字店
7) 仓库源管理器
8) Hacker 工具
9) PyList
10) 各种小工具
11) Staxle 面板后台
  - 其他选项
01) 获取公告     02) 更新 Staxle
03) 关于         99) 退出
注：大部分程序文件都将安装到你的 home 目录
注：如遇到部分选项点击后显示未初始化xxxx，则需要启动 setup.sh
""")
    sel = input("Staxle/ $:")
    if sel.strip() == "1":
        print("  服务器菜单  ")
        print("  - 安装服务器")
        print("1) Nginx: 一款速度快，cpu占用小的C++开源自由服务器")
        print("2) Apache: 世界服务器排名第一的服务器，拥有跨平台、安全性高、稳定性好之称")
        print("3) PHP: 动态网站的重要一环，也是CMS和框架的必需品")
        print("4) Mysql: 动态网站不可缺失的服务器数据库")
        print("5) 安装其他类型的服务器")
        print("  ---------  ")
        print("01) Server2me: Staxle 配套安装工具")
        print("00) 返回菜单")
        sel = input("Staxle/Server $:")
        if sel == "@":
            sel = ""
            for x in range(1,201):
                sel += f"{x} "
        if len(sel.split()) > 1:
            writeStatus(1)
        else:
            writeStatus(0)
        for sel in sel.split():
            if sel.strip() == "1": nginxins()
            elif sel.strip() == "2": apacheins()
            elif sel.strip() == "3": phpins()
            elif sel.strip() == "4": mysql()
            elif sel.strip() == "01":
                if staxconf.server2me == False:
                    print("未初始化 Server2me。")
                    restart_program()
                else:
                    os.system("python ./tools/server2me/main.py")
                    restart_program()
            elif sel.strip() == "5":
                print("  其他类型的服务器")
                print("1) Ngircd: IRC 服务器")
                print("2) pocketmine: 我的世界 Java 服务器")
                print("3) BSD: 我的世界基岩版服务器")
                print("4) icecast2: 网络流媒体服务器")
                print("5) sshd")
                print("6) ftp")
                print("7) lighttpd: 简易服务器+文件下载")
                print("99) 回到主页面")
                sel = input("Staxle/Server/Other $:")
                if sel == "@":
                    sel = ""
                    for x in range(1,201):
                        sel += f"{x} "
                if len(sel.split()) > 1:
                    writeStatus(1)
                else:
                    writeStatus(0)
                for osfor in sel.split():
                    if osfor.strip() == "1": ircins()
                    elif osfor.strip() == "5": sshd()
                    elif osfor.strip() == "7": lighttpd()
                    elif osfor.strip() == "99": restart_program()
                    else: print("\n错误：无效输入");time.sleep(1);restart_program()
                if readStatus():
                    writeStatus(0)
            elif sel.strip() == "99": restart_program()
            else: print("\n错误：无效输入");time.sleep(1);restart_program()
        if readStatus():
            writeStatus(0)
    # 桌面环境
    if sel.strip() == "2":
        print("termux图形化可玩性低，建议安装发行版然后在上面安装")
        print("  - 输入选项选择")
        print("1) termux-desktop: 安装 xfce4 在您的 termux 上")
        print("2) 安装 WM (窗口管理器)")
        print("3) 安装 DE (桌面环境)")
        print("  - 桌面管理")
        print("99) 退出")
        sel = input("Staxle/DEManager $:")
        if sel.strip() == "2" or sel.strip() == "02":
            print(" 运行一些窗口在上面然后管理它们，有轻量的优点")
            print("1) openbox: lxde桌面环境原装wm")
            print("2) fvwm: 轻量且高度自定义")
            print("3) wmaker: 类似 NextSTeP 的窗口管理器")
            print("99) 返回")
            sel = input("Staxle/WM $:")
            if sel == "@":
                sel = ""
                for x in range(1,201):
                    sel += f"{x} "
            if len(sel.split()) > 1:
                writeStatus(1)
            else:
                writeStatus(0)
            for wmifor in sel.split():
                if wmifor.strip() == "1": openbox()
                if wmifor.strip() == "2": fvwm()
                elif wmifor.strip() == "99": restart_program()
                else: print("\n错误：无效输入");time.sleep(1);restart_program()
            if readStatus():
                writeStatus(0)
        if sel.strip() == "3":
            print(" 桌面环境全家桶，面板、窗口管理器、桌面、文件管理器、会话、设置面板一应俱全")
            print("1) xfce4: 兼容性最高的桌面环境")
            print("99) 返回")
            sel = input("Staxle/WM $:")
            for deifor in sel.split():
                if deifor.strip() == "1": xfce4_main()
                elif deifor.strip() == "99": restart_program()
                else: print("\n错误：无效输入");time.sleep(1);restart_program()
        elif demfor.strip() == "99": restart_program()
        else: print("\n错误：无效输入");time.sleep(1);restart_program()
    # Termux
    if sel.strip() == "3":
        print("termux 一些工具")
        print("1) proot-distro: 在 termux 上安装发行版 linux")
        print("2) termux 换源")
        print("3) 获取外部权限")
        print("4) 安装 qurxin (装b工具)")
        print("5) Tool-X: 为 termux 准备的多功能工具")
        print("6) Lazymux: 为 termux 准备了更多的黑客工具")
        print("7) Tmoe: 为 termux 准备的多语言纯 bash 工具集")
        print("8) Neofetch: termux 终端上的设备查询")
        print("9) termux wake-lock 防杀后台")
        print("10) termux-desktop: 安装 xfce4 在您的 termux 上")
        print("11) termux.properties: termux 的一些配置")
        print("12) termux.motd: termux 欢迎语设置")
        print("99) 返回上一菜单")
        sel = input("Staxle/Termux $:")
        if sel == "@":
            sel = ""
            for x in range(1,201):
                sel += f"{x} "
        if len(sel.split()) > 1:
            writeStatus(1)
        else:
            writeStatus(0)
        for infor in sel.split():
            if infor.strip() == "1" : proot_distro()
            elif infor.strip() == "2": termux_repo()
            elif infor.strip() == "3": termux_storage()
            elif infor.strip() == "4": qurxin()
            elif infor.strip() == "5": toolx()
            elif infor.strip() == "6": lazymux()
            elif infor.strip() == "8": neofetch()
            elif infor.strip() == "9": os.system("termux-wake-lock"); restart_program()
            elif infor.strip() == "11": os.system("vim ~/.termux/termux.properties"); restart_program()
            elif infor.strip() == "12": os.system("vim $PREFIX/etc/motd"); restart_program()
            elif infor.strip() == "99": restart_program()
            else: print("\n错误：无效输入");time.sleep(1);restart_program()
        if readStatus():
            writeStatus(0)
    # 软件小子
    if sel.strip() == "6":
        print("\n各种各样的玩意")
        print("注：本店中带*号的选项为桌面环境使用，这些应用需要提前安装好桌面环境")
        print("1) IDE/开发环境/编辑器")
        print("2) 多媒体")
        print("3) 网络/互联网")
        print("4) 终端")
        print("5) x11 应用")
        print("6) 游戏")
        print("7) 无聊东西")
        print("99) 返回主菜单")
        sel = input("Staxle/Software $:")
        if sel.split() == "1":
            # 01
            print(" i wanna be the creator(")
            print("1) vim: 目前最强大的linux编辑器")
            print("2) Emacs: 神的编辑器")
            print("3) code-server: 网页版 VSCode")
            print("4) Clang: 编译，爽！")
            print("5) Lazygit: 可视化 git")
            print("99) 返回主菜单")
            sel = input("Staxle/Software/Code $:")
            if sel == "@":
                sel = ""
                for x in range(1,201):
                    sel += f"{x} "
            if len(sel.split()) > 1:
                writeStatus(1)
            else:
                writeStatus(0)
            for infor in sel.split():
                if infor.strip() == "1": vim()
                elif infor.strip() == "2": emacs()
                elif infor.strip() == "3": code-server()
                elif infor.strip() == "4": clang()
                elif infor.strip() == "5": lazygit()
                elif infor.strip() == "99": restart_program()
                else: print("\n错误：无效输入");time.sleep(1);restart_program()
            if readStatus():
                writeStatus(0)
        elif sel.strip() == "2":
            print(" 多媒体的快乐")
            print("1) timg: 终端图片/视频查看器")
            print("2) mpd: music player deamon")
            print("3) mpv: 最强开源媒体播放器")
            print("4) musicfox: 网易云音乐命令行客户端")
            print("99) 返回主菜单")
            for infor in sel.split():
                if infor.strip() == "1": timg()
                elif infor.strip() == "2": mpd()
                elif infor.strip() == "3": mpv()
                elif infor.strip() == "4": musicfox()
                elif infor.strip() == "99": restart_program()
                else: print("\n错误：无效输入");time.sleep(1);restart_program()
        elif sel.split() == "3":
            # 03
            print(" 网上冲浪")
            print("1) w3m: 终端式网页浏览器")
            print("2) weechat: 简单的 IRC 聊天室")
            print("3) lynx: 比 w3m 更靓的终端网页浏览器")
            print("4) firefox: 桌面环境下的经典浏览器 [*]")
            print("99) 返回主菜单")
            sel = input("Staxle/Software/Internet $:")
            if sel == "@":
                sel = ""
                for x in range(1,201):
                    sel += f"{x} "
            if len(sel.split()) > 1:
                writeStatus(1)
            else:
                writeStatus(0)
            for infor in sel.split():
                if infor.strip() == "1": w3m()
                elif infor.strip() == "2": weechat()
                elif infor.strip() == "3": lynx()
                elif infor.strip() == "3": firefox()
                elif infor.strip() == "99": restart_program()
                else: print("\n错误：无效输入");time.sleep(1);restart_program()
            if readStatus():
                writeStatus(0)
        elif sel.strip() == "99": restart_program()
        else: print("\n错误：无效输入");time.sleep(1);restart_program()
        
    # Hacker
    if sel.strip() == "8":
        print("\ntermux + 黑客 = ?\n本菜单大部分工具全部需要 root!")
        print("1) 信息分析")
        print("2) 网络工具")
        print("3) 设备渗透")
        print("4) 数据分析")
        print("5) WiFi 攻击")
        print("6) 密码爆破")
        print("7) 逆向工程")
        print("8) 试炼靶场")
        print("99) 返回上一菜单")
        sel = input("Staxle/Hacker $:")
        if sel == "@":
            sel = ""
            for x in range(1,201):
                sel += f"{x} "
        if len(sel.split()) > 1:
            writeStatus(1)
        else:
            writeStatus(0)
        for infor in sel.split():
            if infor.strip() == "1":
                print("\n  信息分析 + 获取，越来越nb")
                print("1) nmap: 局域网 ip 及端口信息获取")
                print("2) sqlmap: SQL 数据库注入")
                print("3) EvilUrl: 检测隐藏的恶意链接")
                print("4) EagleEye: 通过好友图像反向找到你朋友ins、X和Face book")
                print("5) ---")
                print("6) EHole: 指纹识别")
                print("7) Emailall: 自动化邮箱收集工具")
                print("8) ARL: 通过关联的互联网资产构建基础资产库")
                print("9) MapEye: GPS 定位工具")
                print("10) sqlmate: sqlmap 的朋友，拥有比sqlmap更多的功能")
                print("11) sqlscan: SQL 数据库查找")
                print("99) 回到 Staxle 菜单")
                sel = input("Staxle/Hacker/Infomation $:")
                if sel == "@":
                    sel = ""
                    for x in range(1,201):
                        sel += f"{x} "
                if len(sel.split()) > 1:
                    writeStatus(1)
                else:
                    writeStatus(0)
                for infor in sel.split():
                    if infor.strip() == "1" or infor.strip() == "01": nmap()
                    elif infor.strip() == "2" or infor.strip() == "02": sqlmap()
                    elif infor.strip() == "3" or infor.strip() == "03": evilurl()
                    elif infor.strip() == "4" or infor.strip() == "04": eagleeye()
                    elif infor.strip() == "6" or infor.strip() == "06": ehole()
                    elif infor.strip() == "7" or infor.strip() == "07": emailall()
                    elif infor.strip() == "8" or infor.strip() == "08": arl()
                    elif infor.strip() == "9" or infor.strip() == "09": mapeye()
                    elif infor.strip() == "10": sqlmate()
                    elif infor.strip() == "11": sqlscan()
                    elif infor.strip() == "99": restart_program()
                    else: print("\n错误：无效输入");time.sleep(1);restart_program()
                if readStatus():
                    writeStatus(0)
            elif infor.strip() == "2":
                print("\n  网络攻击 服务器全部给我坐下")
                print("1) sqlmap: SQL 数据库注入")
                print("2) goldeneye: DDoS 攻击服务器")
                print("3) HPB: Html 页面构建")
                print("4) WebDAV: webdav文件上传工具")
                print("5) CMSeek: CMS 扫描工具，支持 WordPress 等 180+ 种 CMS")
                print("6) Websploit: 高级 MITM 网络攻击框架")
                print("7) XSStrike: XSS 扫描工具")
                print("8) Shellphish: 18种社交媒体的钓鱼工具")
                print("99) 回到 Staxle 菜单")
                sel = input("Staxle/Hacker/WebAtt $:")
                if sel == "@":
                    sel = ""
                    for x in range(1,201):
                        sel += f"{x} "
                if len(sel.split()) > 1:
                    writeStatus(1)
                else:
                    writeStatus(0)
                for infor in sel.split():
                    if infor.strip() == "1": nmap()
                    elif infor.strip() == "2": goldeneye()
                    elif infor.strip() == "3": evilurl()
                    elif infor.strip() == "4": cmseek()
                    elif infor.strip() == "7": xsstrike()
                    elif infor.strip() == "99": restart_program()
                    else: print("\n错误：无效输入");time.sleep(1);restart_program()
                if readStatus():
                    writeStatus(0)
            elif infor.strip() == "3":
                print("\n  只要终端有漏洞 渗透直接把你家偷")
                print("1) Metasploit: 开源免费的漏洞渗透工具")
                print("2) Easysploit: Metasploit 自动化工具")
                print("3) PhoneSploit: 通过 adb 控制安卓设备")
                print("99) 回到 Staxle 菜单")
                sel = input("Staxle/Hacker/Sploit $:")
                if sel == "@":
                    sel = ""
                    for x in range(1,201):
                        sel += f"{x} "
                if len(sel.split()) > 1:
                    writeStatus(1)
                else:
                    writeStatus(0)
                for infor in sel.split():
                    if infor.strip() == "1": metasploit()
                    elif infor.strip() == "2": easysploit()
                    elif infor.strip() == "3": phonesploit()
                    elif infor.strip() == "99": restart_program()
                    else: print("\n错误：无效输入");time.sleep(1);restart_program()
                if readStatus():
                    writeStatus(0)
            elif infor.strip() == "4": 
                print("\n  信息分析 + 获取，越来越nb")
                print("1) nmap: 局域网 ip 及端口信息获取")
                print("2) sqlmap: SQL 数据库分析")
                print("3) EvilUrl: 检测隐藏的恶意链接")
                print("99) 回到 Staxle 菜单")
                sel = input("Staxle/Termux $:")
                if sel == "@":
                    sel = ""
                    for x in range(1,201):
                        sel += f"{x} "
                if len(sel.split()) > 1:
                    writeStatus(1)
                else:
                    writeStatus(0)
                for infor in sel.split():
                    if infor.strip() == "1": nmap()
                    elif infor.strip() == "2": sqlmap()
                    elif infor.strip() == "3": evilurl()
                    elif infor.strip() == "99": restart_program()
                    else: print("\n错误：无效输入");time.sleep(1);restart_program()
                if readStatus():
                    writeStatus(0)
            elif infor.strip() == "99": restart_program()
            else: print("\n错误：无效输入");time.sleep(1);restart_program()
        if readStatus():
            writeStatus(0)
    # 在线更新
    if sel.strip() == "02":
        update()
        os._exit(0)
    if sel.strip() == "01":
        resp = requests.get('https://toad114514.github.io/staxle/board.txt')
        if resp.status_code == 200:
            print(resp.text)
        input("回车键继续")
        restart_program()
    if sel.strip() == "03": about()
    if sel.strip() == "10":
        print("\n  各种各样的工具，这些脚本都存储在了 tools 文件夹")
        print("1) Chexo: TUI 化的 cli-hexo")
        print("2) Server2me: 终端服务器面板")
        print("99) 回到 Staxle 菜单")
        sel = input("Staxle/Termux $:")
        if sel.strip() == "1":
            if staxconf.chexo == False:
                print("未初始化 Chexo。")
                restart_program()
            else:
                os.system("cd ./tools/chexo/ && python main.py")
                restart_program()
        if sel.strip() == "2":
            if staxconf.server2me == False:
                print("未初始化 Server2me。")
                restart_program()
            else:
                os.system("python ./tools/server2me/main.py")
                restart_program()
        elif sel.strip() == "99": restart_program()
        else: print("无效输入。");restart_program()
    if sel.strip() == "11":
        if staxconf.webpy == False:
            print("未初始化 web.py。")
            restart_program()
        else:
            os.system("python web.py")
            restart_program()
    if sel.strip() == "4": 
        if staxconf.qemd == False:
            print("未初始化 Qemd。")
            restart_program()
        else:
            os.system("cd tools/qemd && python main.py")
            restart_program()
    if sel.strip() == "99":
        os.system("clear && cd ~")
        sys.exit()
    else:
        print("无效输入")
        time.sleep(0.5)
        restart_program()

# loop
if __name__ == "__main__":
    os.system("clear")
    config_get()
    main()