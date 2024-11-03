#!/data/data/com.termux/files/usr/bin/bash
####################
# Ready set
####################
$stax_sys_


####################
# Main Menu By Toad114
####################
staxle_menu(){
  OPTION=$(whiptail --title "Staxle-Bash" --menu "Staxle Shell 脚本菜单" 15 60 4 \
  "1" "💻服务器安装/管理" \
  "2" "🔗启动网络后台" \
  "3" "🚪退出 Shell 菜单" 3>&1 1>&2 2>&3)
  
  case ${OPTION} in
    1) staxle_menu_server ;;
    2) staxle_web_panel ;;
  esac
}
