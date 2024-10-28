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

def git_push():
    print("开始进行 Git 部署推送设置前，请注册一个 GitHub 账号用于推送静态页面仓库")
    print("本操作将覆盖原先设置好的选项，请注意！")
    print("如果你已经准备好进行部署设置，请输入y并回车")
    print("如果你已经提前配置好了 Git 推送设置或者手滑，请输入n并回车")
    sel = input("[y/n]")
    if sel == "y":
        input("现在请通过 GitHub 在你的账号中新建一个仓库\n仓库名为<username>.github.io\n<username>是你的 GitHub 账号名\n例如你的GitHub用户名为toad114，那么仓库就命名为 toad114.github.io\n完成操作后请回车")
        email = input("请输入在 GitHub 注册时使用的邮箱")
        username = input("请输入你的 GitHub 账号名")
        print("请稍后")
        if "git" not in os.popen("pkg list-installed|grep git").read():
            os.system("pkg install git")
        if "openssh" not in os.popen("pkg list-installed|grep openssh").read():
            os.system("pkg install openssh")
        os.system("pkg update")
        os.system("git config --global user.name "+username)
        os.system("git config --global user.email "+email)
        print("接下来生成 ssh key\n回车继续之后请连按三次回车使用默认值")
        input("回车键继续")
        os.system("ssh-keygen -t rsa -C "+email)
        push2()
    if sel == "n":
        print("取消操作")
    else:
        git_push()

def push2():
    print("添加 SSH Key")
    print("请将下方的所有的文字复制下来，复制完成后回车")
    os.system("cat ~/.ssh/id_rsa.pub")
    input("")
    print("接着进入 GitHub –> Settings –> SSH and GPG keys –> NEW SSH key 新建 ssh key\n title 一项中随便填，将刚才在上面复制的内容粘贴到 Key 里面\n然后点击 Add SSH Key 完成添加")
    input("添加完成后请回车进行验证")
    if "You've successfully authenticated" not in os.popen("ssh -T git@github.com"):
        input("验证失败，请重新操作")
        push2()
    else:
        print("ssh 通信成功！")
    print("安装 hexo-deployer-git ...")
    os.system("cd "+hexo_dir)
    os.system("npm install hexo-deployer-git --save")
    print("接下来回车将转到配置文件，拉到最下面改成如下（也可以复制）：")
    change = "deploy:\n  type: git\n  repository: https://github.com/"+username+"/"+username+".github.io.git\n  branch: main"
    print(change)
    input("回车进行修改")
    os.system("vim "+hexo_dir+"/config.yaml")
    print("恭喜你完成了所有 Git 部署（不一定）！")
    print("可以回到主页选择 立即 Git 部署 选项便可以部署了！")
    print("如果无法部署，请检查配置文件")
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
        with open(chexopy+"/hexo-dir","w") as k:
            k.write(path)
        print("初始化完成，Chexo 将退出")
        os._exit(1)
    elif sel == "2":
        path = input("输入该 Hexo 文件夹路径：")
        with open(chexopy+"/hexo-dir","w") as k:
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
    print("5) 立即 Git 部署")
    print("6) Git 部署设置")
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
    if sel.strip() == "6":
        git_push()
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

script_path = os.path.realpath(__file__)
# 获取脚本所在的目录
chexopy = os.path.dirname(script_path)

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
if os.path.exists(chexopy+"/hexo-dir") == False:
    print("[!] 没有配置文件！已经创建了一个")
    os.system("touch "+chexopy+"/hexo-dir")
with open(chexopy+"/hexo-dir","r") as file_check:
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