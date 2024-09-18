echo "===============install Staxle==================="
echo "欢迎安装 Staxle!"
echo "接下来将开始安装 Staxle"
echo "===============Staxle Info==================="
echo "Termux 的懒人安装和管理脚本工具，快速让你上手 Termux"
echo "===============Start Install==================="
sleep 3
echo "[INFO] 安装依赖..."
pkg install python git -y
echo "[INFO] 安装pip依赖..."
pip install requests pywebio tqdm pyyaml lolcat
echo "[INFO] 拉取远程仓库..."
git clone https://github.com/Toad114514/Staxle
mv Staxle $PREFIX/etc/staxle
echo "[INFO] 创建启动脚本..."
echo "python $PREFIX/etc/staxle/stax.py" > $PREFIX/bin/staxle
chmod +x $PREFIX/bin/staxle
echo "===============Staxle Installed==================="
echo "安装完成！接下来输入 staxle 开启本脚本！"
echo "===============Staxle Installed==================="