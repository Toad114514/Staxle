#!/data/data/com.termux/files/usr/bin/bash
# Setup.sh by toad
stax_ver="v1.05.3"
setup_ver="ver.113"
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

setup_language(){
 option=$(whiptail --title "设置语言" --menu "选择你所能看懂的语言 Select your Language" 15 60 10 \
 "1" "zh_CN 中文" \
 "2" "en_US English" \
 3>&1 1>&2 2>&3)
 case option in
  "zh_CN 中文")
    echo "zh_CN" > ./core/config/lang
    ;;
  "en_US English")
    echo "en_US" > ./core/config/lang
    ;;
  *)
    echo "zh_CN" > ./core/config/lang
 esac
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
setgm(){
  if $(whiptail --title "设置gitmirror" --yesno "设置 Staxle 部分需要通过GitHub获取工具的镜像，GitHub 国内访问速度慢下载慢，KKGitHub 速度快但无法保证稳定性（有时会无法使用）" --yes-button "Github" --no-button "KKGithub" 15 60 3>&1 1>&2 2>&3)
  then
    gitmirror="github"
  else
    gitmirror="kkgithub"
  fi
  echo ${gitmirror} > ./core/config/gitmirror
}
set_user(){
 user=$(whiptail --title "用户配置" --inputbox "你叫什么✓8名？（留空则使用termux分配的用户名）" 10 70 3>&1 1>&2 2>&3)
 echo ${user} > ./core/config/user
}

setskaug(){
  if $(whiptail --title "跳过更新源和软件包" --yesno "设置使用 Staxle 安装软件包时是否更新源和软件包，可加快安装速度，但很有可能因为其依赖包过老而导致兼容性问题" --yes-button "跳过" --no-button "不跳过" 15 60 3>&1 1>&2 2>&3)
  then
    saug="y"
  else
    saug="n"
  fi
  echo ${saug} > ./core/config/skip_aug
}
setup_set(){
  
  set_user
  setgm
  setskaug
  setup_language
  
  setup_mem
}

setup_mem(){
  mem=0
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
  
  echo 正在 ${GREEN}添加全局命令${RESET}...
  # bin
  termux_bin="$PREFIX/bin"
  echo "python ${stax_path}/stax.py" > ${termux_bin}/staxle
  echo "python ${stax_path}/stax.py" > ${termux_bin}/stax
  echo "bash ${stax_path}/setup.sh $1" > ${termux_bin}/stax-setup
  chmod +x ${termux_bin}/staxle
  chmod +x ${termux_bin}/stax
  chmod +x ${termux_bin}/stax-setup
  
  echo "python ${stax_path}/web.py" > ${termux_bin}/stax-webpanel
  chmod +x ${termux_bin}/stax-webpanel
  echo ${YELLOW}Tips:${GREEN} 输入stax-webpanel可以快速启动面板后台
  
  echo "python ${stax_path}/tools/chexo/main.py" > ${termux_bin}/chexo
  chmod +x ${termux_bin}/chexo
  echo ${YELLOW}Tips:${GREEN} 输入chexo可以快速启动Chexo工具

  echo "python ${stax_path}/tools/server2me/main.py" > ${termux_bin}/server2me
  chmod +x ${termux_bin}/server2me
  echo ${YELLOW}Tips:${GREEN} 输入server2me可以快速启动Server2me服务器管理
  
  echo "python ${stax_path}/tools/qemd/main.py" > ${termux_bin}/qemd
  chmod +x ${termux_bin}/qemd
  echo ${YELLOW}Tips:${GREEN} 输入qemd可以快速启动Qemd虚拟机管理工具
  
  echo ${BLUE}================================
  echo ${GREEN}您的 Staxle ${stax_ver} 已经完成初始化操作！
  echo ${YELLOW}Tips:${GREEN} 输入staxle或stax启动 Staxle 主菜单
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

com_set(){
  case $1 in
    gitmirror) setgm ;;
    user) set_user ;;
    skip_aug) setskaug ;;
    lang) setup_language ;;
    *) echo "${RED}未找到对应设置项。${RESET}" ;;
  esac
  exit 0
}

###############
## command
###############
com_help(){
  echo Staxle Setup Wizard ${setup_ver}
  echo 用法：bash setup.sh command
  echo 如果没有任何参数传递则直接启动 Staxle 初始化向导
  echo 
  echo 可用的 command 选项：
  echo "    help - 打印帮助文档并退出"
  echo "    version - 打印版本号并退出"
  echo "    update - 升级 Staxle（包括 Staxle 本体、所有工具和本初始化向导）"
  echo "    set - 设置 Staxle 选项"
  echo "    lang - Set your Language"
  echo
  echo set 命令用法：
  echo "    bash setup.sh set <设置项>"
  echo 可用的设置项：
  echo "    gitmirror - 设置克隆仓库时使用的镜像地址，值只能输 github 和 kkgithub"
  echo "    user - 设置 Staxle 用户名，留空则使用 termux 终端名"
  echo "    skip_aug - 跳过 apt 源更新和软件包更新"
  echo "    lang - 设置语言"
  exit 0
}

com_version(){
  echo Staxle Setup Wizard ${setup_ver}
  echo Staxle ${stax_ver}
  mkdir ./core/config
}

com_update(){
  git pulll
  echo 升级完成
}

case $1 in
  help) com_help ;;
  version) com_version ;;
  update) com_update ;;
  lang) setup_language ;;
  set) com_set ${2} ;;
  setshow) com_set_show ;;
  *) setup_run ;;
esac