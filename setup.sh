#!/data/data/com.termux/files/usr/bin/bash
# Setup.sh by toad
stax_ver="v1.05.1"
setup_ver="ver.106"
stax_info="    这是一个为快速上手 termux 的新手，以及不想输入命令的 termux 佬特地提供的脚本工具，提供了各种 termux 中可运行的服务安装及配置\\n    他的性质犹如类似于 Lazymux 这一类的仓库，但 Staxle 这个脚本目标是将termux中各种服务的安装与配置集结起来，只需要一个脚本就能全自动或者半自动的完成大部分所想要的服务的安装与配置"

stax_path=$(pwd)

terminal_color(){
  RED=$(printf '\033[31m')
  GREEN=$(printf '\033[32m')
  YELLOW=$(printf '\033[33m')
  BLUE=$(printf '\033[34m')
  PURPLE=$(printf '\033[35m')
  CYAN=$(printf '\033[36m')
  RESET=$(printf '\033[m')
  BOLD=$(printf '\033[1m')
}

setup_ready(){
  if test -e ./core/stax.json
  then
    setup_config
  else
    whiptail --title "Staxle Setup Wizard" --msgbox "欢迎使用 Staxle 安装向导，这将引导你初始化并安装 Staxle 在你的 Termux 中" --ok-button "继续" 10 60
    
    # get version in github
    curl -o version.latest https://api.github.com/repos/toad114514/staxle/releases/latest
    latest_version=$(cat version.latest | grep -E 'tag_name\": \"v[0-9]+\.[0-9]+\.[0-9]+' -o |head -n 1| tr -d 'tag_name\": \"')
    rm -rf version.latest
    printf "${GREEN}Staxle 的简单介绍${RESET}：\\n${stax_info}\\n======================================\\n"
    printf "${RED}即将初始化的版本：${stax_ver}\\n${GREEN}Github 仓库最新版本：${stax_ver}\\n${CYAN}如果版本较低，可能需要在初始化完成后进入脚本进行更新${RESET}"
    printf "\\n${BLUE}<回车键>${RESET} 继续"
    read sonofabitsh
    setup_set
  fi
}

setup_set(){
  user=$(whiptail --title "用户配置" --inputbox "你叫什么✓8名？（留空则使用termux分配的用户名）" 10 70 3>&1 1>&2 2>&3)
  
  if $(whiptail --title "设置gitmirror" --yesno "设置 Staxle 部分需要通过GitHub获取工具的镜像，GitHub 国内访问速度慢下载慢，KKGitHub 速度快但无法保证稳定性（有时会无法使用）" --yes-button "Github" --no-button "KKGithub" 15 60 3>&1 1>&2 2>&3)
  then
    gitmirror="github"
  else
    gitmirror="kkgithub"
  fi
  
  tools=$(whiptail --title "选择所需工具" --checklist "根据你的所需去选择你的工具（按下空格键选中选项，回车继续）" 15 75 4 \
  "web.py" "Staxle 工具的面板后台（用于服务器管理和后台部署）" OFF \
  "chexo" "可视化的 Hexo 博客部署工具" OFF \
  "server2me" "服务器管理工具" OFF \
  "qemd" "Qemu 虚拟机管理工具" OFF \
  3>&1 1>&2 2>&3
  )
  
  if test "$(echo $tools|grep web.py)" != ""
  then
    webpy="true"
  else
    webpy="false"
  fi
  if test "$(echo $tools|grep chexo)" != ""
  then
    chexo="true"
  else
    chexo="false"
  fi
  if test "$(echo $tools|grep server2me)" != ""
  then
    s2m="true"
  else
    s2m="false"
  fi
  if test "$(echo $tools|grep qemd)" != ""
  then
    qemd="true"
  else
    qemd="false"
  fi
  
  setup_mem
}

setup_mem(){
  mem=0
  printf "${GREEN}这将准备初始化以下东西/安装对应依赖：${RESET}\\n"
  printf "Staxle 主菜单本体\\n  - Python 包依赖（60mb）\\n  - Python 库依赖\\n    - requests\\n    - tqdm\\n"
  if test $webpy = "true"
  then
    printf "web.py 工具面板后台\\n  - Python 库依赖\\n    - pywebio\\n"
  fi
  if test $chexo = "true"
  then
    printf "Chexo 博客可视化管理器\\n  - Python 库依赖\\n    - PyYAML\\n  - 前置依赖\\n    - nodejs-lts\\n      - hexo-cli\\n"
  fi
  if test $s2m = "true"
  then
    printf "Server2me 服务器管理工具\\n"
  fi
  if test $qemd = "true"
  then
    printf "Qemd 虚拟机管理工具\\n"
  fi
  printf "\\n${BLUE}<回车键>${RESET} 继续"
  read sbaheixk
  if $(whiptail --title "继续进行初始化吗？" --yesno "选择继续将开始初始化，否则选择重新设置" --yes-button "继续" --no-button "重新设置（关闭脚本）" 10 70 3>&1 1>&2 2>&3)
  then
    start_setup
  else
    printf "${RED}请重新输入 sh setup.sh 进行设置${RESET}"
    exit 1
  fi
}

start_setup(){
  echo ${GREEN}开始进行初始化操作...${RESET}
  sleep 0.6
  # main
  if test "$(pkg installed|grep python)" = ""
  then
    echo 正在安装依赖包 ${GREEN}Python${RESET}...
    pkg install python -y
  fi
  echo 正自动为 ${GREEN}pip 换源（清华源）${RESET}...
  pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
  tests=$(pip show requests)
  err=1
  if test $? -eq $[err]
  then
    echo 正在安装依赖库 ${GREEN}requests${RESET}...
    pip install requests
  fi
  tests=$(pip show tqdm)
  if test $? -eq $[err]
  then
    echo 正在安装依赖库 ${GREEN}tqdm${RESET}...
    pip install tqdm
  fi
  # webpy required
  if test $webpy = "true"
  then
    echo 正在安装${GREEN}面板后台${RESET}所需依赖
    tests=$(pip show pywebio)
    if test $? -eq $[err]
    then
      echo 正在安装依赖库 ${GREEN}pywebio${RESET}...
      pip install pywebio
    fi
  fi
  # chexo required
  if test $chexo = "true"
  then
    echo 正在安装${GREEN} Chexo ${RESET}所需依赖
    if test "$(pkg installed|grep nodejs-lts)" = ""
    then
      echo 正在安装前置依赖包 ${GREEN}nodejs-lts${RESET}...
      pkg install nodejs-lts -y
      node -v
    fi
    if test "$(npm ls -g|grep hexo-cli)" = ""
    then
      echo 正在安装前置nodejs包 ${GREEN}hexo-cli${RESET}...
      npm install hexo-cli
    fi
    tests=$(pip show PyYAML)
    if test $? -eq $[err]
    then
      echo 正在安装依赖库 ${GREEN}PyYAML${RESET}...
      pip install PyYAML
    fi
  fi
  
  echo 正在设置 ${GREEN}配置文件${RESET}...
  # config
   if test "$user" = ""
  then
    configbase="{'user': false,"
  else
    configbase="{'user': '$user',"
  fi
  configbase=$configbase"'git_mirror': '${gitmirror}',"
  configbase=$configbase"'tools':{"
  configbase=$configbase"'webpy': ${webpy},"
  configbase=$configbase"'qemd': ${qemd},"
  configbase=$configbase"'server2me': ${s2m},"
  configbase=$configbase"'chexo': ${chexo}}}"
  echo $configbase > ${stax_path}/core/config.json
  # setdisable
  if test $webpy = "false"
  then
    mv ${stax_path}/web.py ${stax_path}/web.py.disable
  else
    mv ${stax_path}/web.py.disable ${stax_path}/web.py
  fi
  if test $chexo = "false"
  then
    mv ${stax_path}/tools/chexo/main.py ${stax_path}/tools/chexo/main.py.disable
  else
    mv ${stax_path}/tools/chexo/main.py.disable ${stax_path}/tools/chexo/main.py
  fi
  if test $s2m = "false"
  then
    mv ${stax_path}/tools/server2me/main.py ${stax_path}/tools/server2me/main.py.disable
  else
    mv ${stax_path}/tools/server2me/main.py.disable ${stax_path}/tools/server2me/main.py
  fi
  if test $qemd = "false"
  then
    mv ${stax_path}/tools/qemd/main.py ${stax_path}/tools/qemd/main.py.disable
  else
    mv ${stax_path}/tools/qemd/main.py.disable ${stax_path}/tools/qemd/main.py
  fi
  
  echo 正在 ${GREEN}添加全局命令${RESET}...
  # bin
  termux_bin="$PREFIX/bin"
  echo "python ${stax_path}/stax.py" > ${termux_bin}/staxle
  echo "python ${stax_path}/stax.py" > ${termux_bin}/stax
  echo "bash ${stax_path}/setup.sh $1" > ${termux_bin}/stax-setup
  chmod +x ${termux_bin}/staxle
  chmod +x ${termux_bin}/stax
  chmod +x ${termux_bin}/stax-setup
  if test $webpy = "true"
  then
    echo "python ${stax_path}/web.py" > ${termux_bin}/stax-webpanel
    chmod +x ${termux_bin}/stax-webpanel
    echo ${YELLOW}Tips:${GREEN} 输入stax-webpanel可以快速启动面板后台
  fi
  if test $chexo = "true"
  then
    echo "python ${stax_path}/tools/chexo/main.py" > ${termux_bin}/chexo
    chmod +x ${termux_bin}/chexo
    echo ${YELLOW}Tips:${GREEN} 输入chexo可以快速启动Chexo工具
  fi
  if test $s2m = "true"
  then
    echo "python ${stax_path}/tools/server2me/main.py" > ${termux_bin}/server2me
    chmod +x ${termux_bin}/server2me
    echo ${YELLOW}Tips:${GREEN} 输入server2me可以快速启动Server2me服务器管理
  fi
  if test $qemd = "true"
  then
    echo "python ${stax_path}/tools/qemd/main.py" > ${termux_bin}/qemd
    chmod +x ${termux_bin}/qemd
    echo ${YELLOW}Tips:${GREEN} 输入qemd可以快速启动Qemd虚拟机管理工具
  fi
  echo ${BLUE}================================
  echo ${GREEN}您的 Staxle ${stax_ver} 已经完成初始化操作！
  echo ${YELLOW}Tips:${GREEN} 输入staxle/stax启动 Staxle 主菜单
  echo ${YELLOW}Tips:${GREEN} 输入stax-setup启动本界面
  echo ${BLUE}================================
  echo ${PURPLE}祝你${GREEN}使用${CYAN}愉快！
  echo ${BLUE}================================${RESET}
  exit
}

setup_check(){
  echo 正在检测环境..
  scheck_com=`apt show whiptail`
  if test $[$?] -eq 0
  then
    setup_ready
  else
    echo ${RED}未检测到 whiptail 包！正在自动安装${RESET}
    apt install whiptail
    setup_ready
  fi
}

setup_run(){
  terminal_color
  echo ${GREEN}Staxle ${PURPLE} Setup ${YELLOW} Wizard${RESET}
  echo ${PURPLE}Staxle ${YELLOW} Setup ${BLUE} Wizard${RESET}
  echo ${YELLOW}Staxle ${BLUE} Setup ${RED} Wizard${RESET}
  echo ${BLUE}Staxle ${RED} Setup ${CYAN} Wizard${RESET}
  echo ${RED}Staxle ${CYAN} Setup ${GREEN} Wizard${RESET}
  echo ver.102
  echo ${CYAN}请稍后...${RESET}
  sleep 0.7
  setup_check
}

## command
com_help(){
  echo Staxle Setup Wizard ${setup_ver}
  echo 用法：bash setup.sh command
  echo 如果没有任何参数传递则直接启动 Staxle 初始化向导
  echo 
  echo 可用的 command 选项：
  echo     help - 打印帮助文档并退出
  echo     version - 打印版本号并退出
  echo     update - 升级 Staxle（包括 Staxle 本体、所有工具和本初始化向导）
  exit 0
}

com_version(){
  echo Staxle Setup Wizard ${setup_ver}
  echo Staxle ${stax_ver}
}

com_update(){
  git pull
  echo 升级完成
}

case $1 in
  help) com_help ;;
  version) com_version ;;
  update) com_update ;;
  *) setup_run ;;
esac