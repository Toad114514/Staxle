# staxle menu.py
import os
import requests
import time
import json
import sys
import readline
from core.staxcore import *

def main():
    banner()
    print("""
  - 输入选项选择
1) 服务器管理工具
2) 桌面环境管理
3) Termux/ut/zt
4) 虚拟机
5) 安装包管理工具
6) 高级软件安装器
7) 仓库源管理器
8) 快捷启动菜单
9) Hacker 工具
10) 代码环境管理工具
11) 脚本工具
12) 网络检测
13) VNC 管理
14) 终端游戏
15) PyList
16) CHexo
17) Staxle 面板后台
18) 小工具
  - 其他选项
01) 获取公告     02) 更新 Staxle
03) 关于         99) 退出
注：大部分程序文件都将安装到你的 home 目录
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
        print("  - 服务器管理工具")
        print("01) 启动服务器")
        print("02) 关闭服务器")
        print("03) 配置引导")
        print("04) Mysql 数据库管理器")
        print("05) 重装服务器")
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
                    if sel.strip() == "1": ircins()
                    elif sel.strip() == "1": sshd()
                    elif sel.strip() == "99": restart_program()
                    else: print("\n错误：无效输入");time.sleep(1);restart_program()
                if readStatus():
                    writeStatus(0)
            elif sel.strip() == "99": restart_program()
            else: print("\n错误：无效输入");time.sleep(1);restart_program()
        if readStatus():
            writeStatus(0)
    # 桌面环境
    if sel.strip == "2":
        print("  - 输入选项选择")
        print("1) termux-desktop: 安装 xfce4 在您的 termux 上")
        print("2) 安装 VNC 服务器")
        print("  - 桌面管理")
        print("01) VNC 配置")
        print("99) 退出")
        sel = input("Staxle/DEManager $:")
    # Termux
    if sel.strip() == "3":
        print("有关于一系列termux的小工具")
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
            elif infor.strip() == "8": neofetch()
            elif infor.strip() == "9": os.system("termux-wake-lock")
            elif infor.strip() == "99": restart_program()
            else: print("\n错误：无效输入");time.sleep(1);restart_program()
        if readStatus():
            writeStatus(0)
    # 软件小子
    if sel.strip() == "6":
        print("\n各种各样的玩意")
        print("1) IDE")
        print("2) 图像管理")
        print("3) 视频多媒体")
        print("4) 终端")
        print("5) zsh")
        print("6) 小游戏")
        print("7) 无聊东西")
        print("99) 返回主菜单")
        sel = input("Staxle/Software $:")
    # Hacker
    if sel.strip() == "9":
        print("\ntermux + 黑客 = ?\n本菜单大部分工具全部需要 root!")
        print("1) 信息分析")
        print("2) 网络工具")
        print("3) 设备渗透")
        print("4) 数据分析")
        print("5) WiFi 攻击")
        print("6) 密码爆破")
        print("7) 逆向工程")
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
                print("5) CMSeek: CMS 爆破工具，支持 WordPress 等 180+ 种 CMS")
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
                    elif infor.strip() == "99": restart_program()
                    else: print("\n错误：无效输入");time.sleep(1);restart_program()
                if readStatus():
                    writeStatus(0)
            elif infor.strip() == "3":
                print("\n  只要终端有漏洞 渗透直接把你家偷")
                print("1) Metasploit: 开源免费的漏洞渗透工具")
                print("2) Easysploit: 自动化 Metasploit 工具")
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
                    if infor.strip() == "1": nmap()
                    elif infor.strip() == "2": sqlmap()
                    elif infor.strip() == "3": evilurl()
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
        resp = requests.get('https://toad114514.github.io/staxle/version.json')
        if resp.status_code == 200:
            getback = json.loads(resp.text)
            if getback["version-code"] >= stax.version_num:
                print("有新版本更新")
                print("版本", getback["version"])
                print("版本号", getback["version-code"])
                print("版本类型", getback["version-type"])
                print("版本描述", getback["version-desc"])
                backnew = input("您是否需要更新?[y/n]")
                if backnew == "y":
                    os.system("clear")
                    print("\n更新向导")
                    print("正在更新 Staxle 至", getback["version"])
                    time.sleep(1)
                    os.system("git pull")
                    print("更新完成，重新启动 staxle 即可")
                    sys.exit()
            else:
                print("恭喜，你现在使用的就是最新版本！")
                backnew = input("按下任意键返回")
                restart_program()
    if sel.strip() == "01":
        resp = requests.get('https://toad114514.github.io/staxle/board.txt')
        if resp.status_code == 200:
            print(resp.text)
        restart_program()
    if sel.strip() == "03": about()
    if sel.strip() == "17":
        os.system("python web.py")
        restart_program()
    if sel.strip() == "99":
        os.system("clear")
        sys.exit()
    else:
        print("无效输入")
        time.sleep(0.5)
        restart_program()

# loop
if __name__ == "__main__":
    os.system("clear")
    main()