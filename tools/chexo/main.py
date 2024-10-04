import os
import time
import json

print("检查 PyYAML 库是否安装...")
try:
    import yaml
except ImportError:
    print("未安装 PyYAML！")
    os.system("pip install pyyaml")
    print("请重新启动 Chexo！")
    os._exit(0)
else:
    print("已安装 PyYAML")

debug_skip_check = False

def info(hexo_dir):
    print("============博客信息=============")
    with open(hexo_dir+"/package.json","r") as fe:
        hexo_json = json.loads(fe.read())
    hexo_version = hexo_json["hexo"]["version"]
    print("Hexo 版本："+hexo_version)
    with open(hexo_dir+"/_config.yml","r") as cread:
        document = cread.read()
    hconf = yaml.load(document, Loader=yaml.Loader)
    blog = hconf["title"]
    print("博客标题："+blog)
    sub = hconf["subtitle"]
    print("博客副标题："+sub)
    url = hconf["url"]
    print("博客地址："+url)
    author = hconf["author"]
    print("博客作者："+author)
    theme = hconf["theme"]
    if theme == "butterfly":
        theme = theme + " (butterfly.js.org)"
    if theme == "next":
        theme = theme + " (themes-next.js.org/docs)"
    if theme == "fluid":
        theme = theme + " (fliud-dev.com)"
    print("主题："+theme)
    if hconf["deploy"]["type"] == "git":
        dept = "Git 部署 (Pages)"
        dep_repo = hconf["deploy"]["repository"]
        dep_branch = hconf["deploy"]["branch"]
        print(dept)
        print("  部署仓库："+dep_repo)
        print("  部署分支："+dep_branch)
    else:
        dept = "其他部署方式"
        print(dept)    
    input("回车键继续")

def inithexo():
    os.system("clear")
    os.system("toilet Chexo")
    print("Chexo - v1.02")
    print("===================")
    print("请选择以下初始化方式")
    print("1) 直接新建")
    print("2) 使用原有 Hexo 目录")
    print("3) 退出/返回 Staxle")
    sel = input("输入选项：")
    if sel == "1":
        path = input("输入该文件夹路径，没有则创建\n请选择没有任何文件和文件夹的文件夹，否则hexo会报错\n输入：")
        path = path.replace("~",home_dir)
        if os.path.exists(path) == False:
            os.mkdir(path)
        os.system("hexo init "+path)
        with open("./hexo-dir","w") as k:
            k.write(path)
        print("初始化完成，Chexo 将退出")
        os._exit(1)
    elif sel == "2":
        path = input("输入该 Hexo 文件夹路径：")
        with open("./hexo-dir","w") as k:
            k.write(path)
        print("初始化完成，Chexo 将退出")
        os._exit(1)
    elif sel == "3":
        os._exit(1)
    else:
        inithexo()
    
def main():
    os.system("clear")
    os.system("toilet Chexo")
    print("Chexo - v1.02")
    print("===================")
    print("1) 新建文章/页面")
    print("2) 编辑文章")
    print("3) 编辑 _config.yaml")
    print("4) 主题安装")
    print("5) Git 推送")
    print("5) Git 推送设置")
    print("7) 启动自带服务器")
    print("8) 创建静态页面")
    print("9) 查看本博客信息")
    print("99) 退出/返回 Staxle")
    sel = input("输入选项：")
    if sel.strip() == "1":
        pname = input("输入该文章文件名：")
        sel = input("输入类型(1=文章  2=页面  其他东西=文章)：")
        if sel.strip() == "1":
            os.system("cd "+hexo_dir+" && hexo new post "+pname)
            print("新建完成！请回车")
            input()
            main()
        if sel.strip() == "2":
            os.system("cd "+hexo_dir+" && hexo new page "+pname)
            print("新建完成！请回车")
            input()
            main()
        else:
            os.system("cd "+hexo_dir+" && hexo new post "+pname)
            print("新建完成！请回车")
            input()
            main()
    if sel.strip() == "2":
        print("正在遍历文章列表...")
        listfile = os.listdir(hexo_dir+"/source/_posts")
        filetitle = []
        for lfe1 in listfile:
            getline = os.popen("sed -n 2p "+hexo_dir+"/source/_posts/"+lfe1).read()
            getline = getline.replace("title: ","")
            getline = getline.replace("\n","")
            filetitle.append(getline)
        os.system("clear")
        print("以下是你的文章，你要选择哪个来编辑？")
        print("序号       文章标题      文章名")
        for listdisp in range(0,len(listfile)):
            ttmp = filetitle[listdisp]
            fntmp = listfile[listdisp]
            print(str(listdisp)+"        "+ttmp+"          "+fntmp)
        getback = input("输入序号（输入其他则返回主菜单）：")
        if int(getback) < 0 or int(getback) > len(listfile):
            print("无效输入")
            time.sleep(0.7)
            main()
        else:
            print("你选择了文章 \""+filetitle[int(getback)]+"\"，你要对该文章干什么？")
            print("1) 编辑该文章")
            print("2) 删除该文章")
            print("3) 退出编辑")
            sel = input("输入选项：")
            if sel == "1":
                os.system("vim "+hexo_dir+"/source/_posts/"+listfile[int(getback)])
            elif sel == "2":
                sel = input("你确定要删除它吗？[y/n]")
                if sel =="y": os.system("rm "+hexo_dir+"/source/_posts/"+listfile[int(getback)])
                else: print("取消操作"); time.sleep(1)
            else: print("正在返回主页面")
            main()
    if sel.strip() == "3":
        os.system("vim "+hexo_dir+"/_config.yml")
        main()
    if sel.strip() == "5":
        os.system("hexo d -g")
        main()
    if sel.strip() == "7":
        os.system("hexo s")
        main()
    if sel.strip() == "8":
        os.system("hexo g")
        main()
    if sel.strip() == "9":
        info(hexo_dir)
        main()
    if sel.strip() == "99":
        os.system("clear")
        os._exit(1)
    else: main()

home_dir = os.popen("echo $HOME").read()
home_dir = home_dir.replace("\n","")
if debug_skip_check == True:
    with open("./hexo-dir","r") as file_check:
        hexo_dir = file_check.read()
        hexo_dir = hexo_dir.replace("~",home_dir)
    main()
print("正在检查 npm 环境...")
time.sleep(1)
if "nodejs-lts" not in os.popen("pkg list-installed|grep nodejs-lts").read():
    os.system("[!] 没有 nodejs 环境!自动安装")
    os.system("pkg install nodejs-lts -y")
print("正在检查 hexo 环境...")
if "hexo-cli" not in os.popen("npm ls -g|grep hexo-cli").read():
    os.system("[!] 缺失 hexo-cli 包！")
    os.system("npm install hexo-cli")

print("检查 CHexo 文件配置")
time.sleep(1)
if os.path.exists("./hexo-dir") == False:
    print("[!] 没有配置文件！已经创建了一个")
    os.system("touch ./hexo-dir")
with open("./hexo-dir","r") as file_check:
    hexo_dir = file_check.read()
    hexo_dir = hexo_dir.replace("~",home_dir)

print("检查是否为 Hexo 文件夹")
time.sleep(1)
hc = hexo_dir + "/package.json"
try:
    check_dir = open(hc,"r")
except IOError:
    print("不是 Hexo 文件夹，将转至 初始化界面")
    time.sleep(1)
    inithexo()
else:
    checkd = json.loads(check_dir.read())
finally:
    if check_dir:
        check_dir.close()

if checkd["name"] == "hexo-site":
    print("一切检查完成！准备进入主菜单！")
else:
    print("不是 Hexo 文件夹，将转至 初始化界面")
    time.sleep(1)
    inithexo()
    
if __name__ == "__main__":
    main()