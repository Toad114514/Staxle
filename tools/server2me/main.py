import os, time

def show_fast():
    with os.popen("pkg list-installed|grep nginx") as f:
        ng = f.read()
    with os.popen("pkg list-installed|grep apache2") as f:
        ap = f.read()
    with os.popen("pkg list-installed|grep php-fpm") as f:
        phf = f.read()
    with os.popen("pkg list-installed|grep php-apache") as f:
        aph = f.read()
    with os.popen("pkg list-installed|grep ngircd") as f:
        ircd = f.read()
    with os.popen("pkg list-installed|grep mariadb") as f:
        sql = f.read()
    with os.popen("pkg list-installed|grep ssh") as f:
        ssh = f.read()
    with os.popen("pkg list-installed|grep ftp") as f:
        ftp = f.read()
    if "nginx" in ng:
        if os.system("pgrep nginx") == 0:
            with os.popen("pgrep nginx") as pid:
                pidr = pid.read()
            print("Nginx 进程 PID: ",pidr)
        else:
            print("已安装 Nginx")
    if "apache2" in ap:
        if os.system("pgrep apache") == 0:
            with os.popen("pgrep apache") as pid:
                pidr = pid.read()
            print("Apache 进程 PID: ",pidr)
        else:
            print("已安装 apache")
    if "php-fpm" in phf:
        if os.system("pgrep php-fpm") == 0:
            with os.popen("pgrep php-fpm") as pid:
                pidr = pid.read()
            print("php-fpm 进程 PID: ",pidr)
        else:
            print("已安装 php-fpm")
    if "php-apache" in aph:
        if os.system("pgrep php-apache") == 0:
            with os.popen("pgrep php-apache") as pid:
                pidr = pid.read()
            print("php-apache 进程 PID: ",pidr)
        else:
            print("已安装 php-apache")
    if "ngircd" in ircd:
        if os.system("pgrep ngircd") == 0:
            with os.popen("pgrep ngircd") as pid:
                pidr = pid.read()
            print("Ngircd 进程 PID: ",pidr)
        else:
            print("已安装 ngircd")
        
def main():
    print("Server2me")
    print("        Server2me")
    print("  Server2me")
    print("=========================")
    print("显示目前服务器状态")
    time.sleep(0.7)
    show_fast()
    print("=========================")
    print("1: 启动服务器")
    print("2: 关闭服务器")
    print("3: 配置服务器")
    print("4: 管理服务器")
    print("5: 查看进程")
    print("6: 退出 Server2me/返回 Staxle")
    sel = input("Staxle/Server2me: ")
    if sel.strip() == "1":
        print("选择需要启动的服务器")
        print("选择需要启动的服务器")
        print("=========================")
        print("[1] Nginx")
        print("[2] Apache")
        print("[3] php-fpm")
        print("[4] php-apache")
        print("[5] ngircd")
        print("[99] 返回")
        sel == input("Staxle/Server2me/start: ")
        if sel.strip() == "1":
            if "nginx" not in os.popen("pkg list-installed|grep nginx").read():
                print("未安装 Nginx，请退出 Server2me 然后通过 Staxle 安装\n返回...")
                time.sleep(1)
                main()
            else:
                os.system("nginx")
                main()
        if sel.strip() == "2":
            if "apache2" not in os.popen("pkg list-installed|grep apache2").read():
                print("未安装 Apache2，请退出 Server2me 然后通过 Staxle 安装\n返回...")
                time.sleep(1)
                main()
            else:
                os.system("httpd")
                main()
        if sel.strip() == "3":
            if "php-fpm" not in os.popen("pkg list-installed|grep apache2").read():
                print("未安装 php-fpm，请退出 Server2me 然后通过 Staxle 安装\n返回...")
                time.sleep(1)
                main()
            else:
                os.system("php-fpm")
                main()
        if sel.strip() == "4":
            if "php-apache" not in os.popen("pkg list-installed|grep php-apache").read():
                print("未安装 php-apache，请退出 Server2me 然后通过 Staxle 安装\n返回...")
                time.sleep(1)
                main()
            else:
                os.system("php-apache")
                main()
        if sel.strip() == "5":
            if "ngircd" not in os.popen("pkg list-installed|grep ngircd").read():
                print("未安装 ngircd，请退出 Server2me 然后通过 Staxle 安装\n返回...")
                time.sleep(1)
                main()
            else:
                os.system("ngircd")
                main()
        if sel.strip() == "99":
            main()
        else:
            main()
    if sel.strip() == "2":
        print("选择需要关闭的服务器")
        print("选择需要关闭的服务器")
        print("=========================")
        print("[1] Nginx")
        print("[2] Apache")
        print("[3] php-fpm")
        print("[4] php-apache")
        print("[5] ngircd")
        print("[99] 退出")
        if sel.strip() == "1":
            if os.system("pgrep nginx") == 1:
                print("未启动或者未安装 Nginx")
                time.sleep(1)
                main()
            else:
                os.system("nginx -s stop")
                main()
        if sel.strip() == "2":
            if os.system("pgrep httpd") == 1:
                print("未启动或者未安装 Apache2")
                time.sleep(1)
                main()
            else:
                os.system("httpd stop")
                main()
        if sel.strip() == "3":
            if os.system("pgrep php-fpm") == 1:
                print("未启动或者未安装 php-fpm")
                time.sleep(2)
                main()
            else:
                os.system("pkill php-fpm")
                main()
        if sel.strip() == "4":
            if os.system("pgrep php-apache") == 1:
                print("未启动或者未安装 php-apache")
                time.sleep(1)
                main()
            else:
                os.system("pkill php-apache")
                main()
        if sel.strip() == "5":
            if os.system("pgrep ngircd") == 1:
                print("未启动或者未安装 Ngircd")
                time.sleep(1)
                main()
            else:
                os.system("pkill ngircd")
                main()
        else:
            main()
    if sel.strip() == "6":
        os._exit(0)

main()
    