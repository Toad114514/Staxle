#!/data/data/com.termux/files/usr/bin/bash
# Staxle Bash Script (Start)
stax_global_path=$(pwd)
# Color
RED=$(printf '\033[31m')
GREEN=$(printf '\033[32m') 
YELLOW=$(printf '\033[33m') 
BLUE=$(printf '\033[34m') 
PURPLE=$(printf '\033[35m') 
CYAN=$(printf '\033[36m') 
RESET=$(printf '\033[m') 
BOLD=$(printf '\033[1m')

###### Menu
staxle_start(){
   SEL=$(whiptail --title "选择一个菜单" --menu "选择 Staxle 菜单" 0 50 0 \
   "1" "Python (stax.py)" \
   "2" "Bash" 3>&1 1>&2 2>&3)
   
   case ${SEL} in 
   1) staxle_python ;;
   2) staxle_bash_ready ;;
   esac
}

staxle_python(){
  local tmp=`pkg list-installed|grep -o python`
  local tmp2=0
  if test $? -eq 0
  then
    echo ${GREEN}已安装依赖，正在启动Python菜单..${RESET}
    sleep 1
    python ${stax_global_path}/stax.py
  else
    echo ${RED}未安装 Python 依赖！${RESET}正在自动安装...
    pkg install python
    staxle_python
  fi
}

staxle_bash_ready(){
  source ${stax_global_path}/bash/main.sh
}
######## 参数
staxle_command_help(){
  echo "Staxle v1.05.2"
  echo "用法：sh main.sh command"
  echo "如果没有向 command 传递参数，则启动菜单询问菜单选择"
  echo "可用的 command 参数："
  echo "  help - 打印帮助信息并退出"
  echo "  version - 打印版本信息并退出"
  echo "  py/python - 启动 Python 菜单"
  echo "  sh/bash - 启动 Bash 菜单"
}
staxle_command_version(){
  echo "v1.05.2"
}

case $1 in
  help) staxle_command_help ;;
  version) staxle_command_version ;;
  python) staxle_python ;;
  py) staxle_python ;;
  sh) staxle_bash_ready ;;
  bash) staxle_bash_ready ;;
  *) staxle_start ;;
esac
