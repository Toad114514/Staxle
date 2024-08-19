#    懒人必备 Python 简易库
#     终端多彩输出库 ByToad114514
#   将该文件放在源码根文件夹中
#    然后在源码中导入即可使用
#  import ct
#
#  使用示例
#    print(ct.red(),'what can i say')
#  v1.67b

def error():
	return '\033[31m' + '[ERR]' + '\033[0m'
def done():
	return '\033[32m' + '[DONE]' + '\033[0m'
def warning():
	return '\033[33m' + '[WRN]' + '\033[0m'
def info():
    return '\033[34m' + '[INFO]' + '\033[0m'
def red():
	return '\033[31m'
def green():
	return '\033[32m'
def yellow():
	return '\033[33m'
def blue():
	return '\033[34m'
def white():
	return '\033[37m'
def clear():
	return '\033[0m'
def drop_line():
	return '\033[4m'
def light_on():
	return '\033[5m'
def recolor():
	return '\033[7m'
def visibi():
	return '\033[8m'