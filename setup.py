import os, json
print("Staxle 初始化向导")
print("正在安装 python 依赖...")
os.system("pip install pyyaml requests pywebio tqdm")
lang = input("请输入 Staxle 所运行的语言：")
config = {}
config["lang"] = lang
with open("./core/config.json","w") as f:
    f.write(json.dumps(config))
print("现在可以在该文件夹中输入 python stax.py 便可以运行了")