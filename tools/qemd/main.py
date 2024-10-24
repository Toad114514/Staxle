# Qemd v1.01(100)
# Code by Toad114514(2024/10/24-2024/10/25)

import os, time, json

# config template
template = """
{
    "qemd": ["v1.01", 100],
    "name": "none",
    "type": "x86-64",
    "memory": 256,
    "cdrom": false,
    "disk": {
        "drive-virtio-disk0": [
            "img.qcow",
            "qcow"
        ]
    },
    "card": {
        "net": "rtl8139",
        "video": "vmware",
        "sound": "sb16"
    },
    "graphic": "vnc",
    "vnc": {
        "host": ":0"
    }
}
"""
global template_dict 
template_dict = json.loads(template)

#############
# VM Create Function
#############

def create():
    os.system("clear")
    print("====================\n     快速创建虚拟机\n==============")
    virtual_name = input("输入虚拟机名字：")
    virtual_framework = input("输入cpu架构\ni386: 使用i386架构，适合32位系统（早期Linux/win9x/2k）\nx86-64: 使用x86-64系统，适合64位系统（win7/8/10/11和各种Linux发行版）\n输入：")
    # qemu install
    if virtual_framework == "i386":
        if "qemu-system-i386" not in os.popen("pkg list-installed|grep qemu-system-i386").read():
            print("正在安装 qemu-system-i386...")
            os.system("pkg install qemu-system-i386")
    if virtual_framework == "x86-64":
        if "qemu-system-x86-64" not in os.popen("pkg list-installed|grep qemu-system-x86-64").read():
            print("正在安装 qemu-system-x86-64...")
            os.system("pkg install qemu-system-x86-64")
    else:
        print("无效输入")
        time.sleep(1)
        main()
    # create virtual
    os.system("mkdir vm/"+virtual_name)
    os.system("touch vm/"+virtual_name+"/qemd_config.json")
    sel = input("虚拟硬盘你要选择：\n[1] 新建空硬盘并使用 \n[2] 使用已有的")
    if sel.strip() == "1":
        img_size = input("输入硬盘大小（单位GB）：")
        img_name = input("输入虚拟硬盘名：")
        os.system("qemu-img create -f qcow2 ./vm/"+virtual_name+"/"+img_name+".qcow2 "+img_size+"G")
        img_path = "./vm/"+virtual_name+"/"+img_name+".qcow2"
        img_type = "qcow2"
    elif sel.strip() == "2":
        img_path = input("输入虚拟硬盘的绝对路径（仅支持 img、qcow、qcow2和vhd格式的硬盘）：")
        img_bname = os.path.splitext(img_path)[-1]
        img_type = ""
        if img_bname == ".img":
            img_type = "raw"
        elif img_bname == ".qcow":
            img_type = "qcow"
        elif img_bname == ".qcow2":
            img_type = "qcow2"
        elif img_bname == ".vhd":
            img_type = "vhd"
        else:
            print("该虚拟硬盘格式不正确，默认使用raw（运行可能问题）")
            img_type = "raw"
    tmp = template_dict
    tmp["name"] = virtual_name
    tmp["type"] = virtual_framework
    tmp["disk"]["drive-virtio-disk0"][0] = img_path
    tmp["disk"]["drive-virtio-disk0"][1] = img_type
    write_f = json.dumps(tmp)
    with open("./vm/"+virtual_name+"/qemd_config.json","w") as f:
        f.write(write_f)
    print("虚拟机创建完成！")
    time.sleep(1)
    main()

def vmanage_check(path):
    qemdc = open(path+"/qemd_config.json","r")
    qconfig = json.loads(qemdc.read())
    try:
        config_version = qconfig["qemd"]
        name = qconfig["name"]
        type = qconfig["type"]
        mem = qconfig["memory"]
        cdrom = qconfig["cdrom"]
        disk = qconfig["disk"]
        card = qconfig["card"]
        graphic = qconfig["graphic"]
        if graphic == "vnc":
            vnc = qconfig["vnc"]
    except KeyError:
        print("[!] "+path+"/qemd_config.json 缺失配置项！")
        qemdc.close()
        time.sleep(0.7)
        main()
    else:
        qemdc.close()
        vmanage(path)

def vmanage(path):
    with open(path+"/qemd_config.json","r") as vmanage_f:
        qconfig_vm = json.loads(vmanage_f.read())
    os.system("clear")
    print("====================\n     管理虚拟机\n==============")
    print("正在管理的虚拟机："+qconfig_vm["name"]+"\n=======================")
    print("[1] 虚拟机内存")
    print("[2] 硬盘设备管理")
    print("[3] 虚拟驱动（网卡/声卡/显卡）")
    print("[4] 视频输出方式")
    print("==============================")
    print("[r] 启动虚拟机")
    print("[c] 设置虚拟机启动脚本")
    print("[q] 退出")
    print("==============================")
    sel = input("请输入：")
    if sel.strip() == "1":
        print("虚拟机内存设置\n目前虚拟机设置的内存："+str(qconfig_vm["memory"]))
        input_mem = input("输入虚拟机内存大小（单位为M）：")
        qconfig_vm["memory"] = int(input_mem)
        with open(path+"/qemd_config.json","w+") as vmanage_f:
            vmanage_f.write(json.dumps(qconfig_vm))
        vmanage(path)
    elif sel.strip() == "2":
        print("硬盘设备管理")
        print("[1] 设置 CD-Rom(虚拟光盘)\n[2] 虚拟硬盘\n[q] 返回")
        sel = input("输入：")
        if sel.strip() == "1":
            input_cdrom = input("输入虚拟光盘镜像绝对路径：")
            if os.path.splitext(input_cdrom)[-1] != ".iso":
                print("所选的文件不是 ISO 文件！")
                time.sleep(0.8)
                vmanage(path)
            else:
                qconfig_vm["cdrom"] = input_cdrom
                with open(path+"/qemd_config.json","w+") as vmanage_f:
                    vmanage_f.write(json.dumps(qconfig_vm))
                vmanage(path)
        elif sel.strip() == "2":
            print("虚拟硬盘管理\n=========================")
            disk_dict = qconfig_vm["disk"]
            disk_id = []
            disk_path = []
            disk_type = []
            for key in disk_dict.keys():
                disk_id.append(key)
            for id in disk_id:
                disk_path.append(disk_dict[id][0])
                disk_type.append(disk_dict[id][1])
            for num in range(0,len(disk_id)):
                print("["+str(num)+"] "+disk_id[num]+" ("+disk_path[num]+")")
            print("===========================")
            print("输入上方其中一个序号来修改对应虚拟硬盘的绝对路径")
            print("或者你也可以：")
            print("[a] 挂载新的虚拟硬盘")
            print("[r] 卸载对应的虚拟硬盘")
            print("[q] 返回")
            sel = input("请输入：")
            try:
                sel_int = int(sel.strip())
            except ValueError:
                if sel.strip() == "a":
                    disk_path_new = input("输入新的虚拟硬盘镜像绝对路径：")
                    img_bname = os.path.splitext(disk_path_new)[-1]
                    if img_bname == ".img":
                        img_type = "raw"
                    elif img_bname == ".qcow":
                        img_type = "qcow"
                    elif img_bname == ".qcow2":
                        img_type = "qcow2"
                    elif img_bname == ".vhd":
                        img_type = "vhd"
                    else:
                        print("该虚拟硬盘格式未找到对应的类型，默认使用raw（运行可能有问题）")
                        time.sleep(1)
                        img_type = "raw"
                    qconfig_vm["disk"]["drive-virtio-disk"+str(len(disk_id)+1)] = []
                    qconfig_vm["disk"]["drive-virtio-disk"+str(len(disk_id)+1)].append(disk_path_new)
                    qconfig_vm["disk"]["drive-virtio-disk"+str(len(disk_id)+1)].append(img_type)
                    with open(path+"/qemd_config.json","w+") as vmanage_f:
                        vmanage_f.write(json.dumps(qconfig_vm))
                elif sel.strip() == "r":
                    print("卸载虚拟磁盘")
                    print("===========================")
                    for num in range(0,len(disk_id)):
                        print("["+str(num)+"] "+disk_id[num]+" ("+disk_path[num]+")")
                    print("===========================")
                    print("在上方选项中选择一个去卸载，如果输错了可以：\n[任意文字] 返回")
                    sel = input("输入：")
                    try:
                        sel_int = int(sel)
                    except ValueError:
                        print("返回...")
                    else:
                        if int(sel.strip()) >= 0 and int(sel.strip()) < len(disk_id):
                            del qconfig_vm["disk"]["drive-virtio-disk"+str(sel.strip())]
                            print("已卸载 drive-virtio-disk"+str(sel.strip()))
                            with open(path+"/qemd_config.json","w+") as vmanage_f:
                                vmanage_f.write(json.dumps(qconfig_vm))
                elif sel.strip() == "q":
                    print("退出中")
                else: print("无效输入");
            else:
                if int(sel.strip()) >= 0 and int(sel.strip()) < len(disk_id):
                    disk_path_new = input("输入 "+disk_id[int(sel.strip())]+" 的新虚拟磁盘镜像的绝对路径：")
                    img_bname = os.path.splitext(disk_path_new)[-1]
                    if img_bname == ".img":
                        img_type = "raw"
                    elif img_bname == ".qcow":
                        img_type = "qcow"
                    elif img_bname == ".qcow2":
                        img_type = "qcow2"
                    elif img_bname == ".vhd":
                        img_type = "vhd"
                    else:
                        print("该虚拟硬盘格式未找到对应的类型，默认使用raw（运行可能有问题）")
                        time.sleep(1)
                        img_type = "raw"
                    tmp6 = disk_id[int(sel.strip())]
                    qconfig_vm["disk"][tmp6][0] = disk_path_new
                    qconfig_vm["disk"][tmp6][1] = img_type
                    with open(path+"/qemd_config.json","w+") as vmanage_f:
                        vmanage_f.write(json.dumps(qconfig_vm))
                else:
                    print("无效输入")
            finally:
                time.sleep(0.5)
                vmanage(path)
    elif sel == "3":
        print("==============================")
        print("虚拟驱动设置")
        print("==============================")
        print("[1] 设置网卡")
        print("[2] 设置显卡")
        print("[3] 设置声卡")
        print("[q] 返回")
        seld = input("输入：")
        if seld.strip() == "1":
            netcard = input("输入网卡型号（建议 rtl8139）：")
            qconfig_vm["card"]["net"] = netcard
            with open(path+"/qemd_config.json","w+") as vmanage_f:
                vmanage_f.write(json.dumps(qconfig_vm))
            vmanage(path)
        elif seld.strip() == "2":
            soundcard = input("输入型号（可选 vmware(NT系列)、cirrus(win9x)）：")
            qconfig_vm["card"]["sound"] = soundcard
            with open(path+"/qemd_config.json","w+") as vmanage_f:
                vmanage_f.write(json.dumps(qconfig_vm))
            vmanage(path)
        elif seld.strip() == "3":
            soundcard = input("输入显卡型号（可选 sb16(win9x)、ac97(winnt)、all(使用所有声音驱动)）：")
            qconfig_vm["card"]["sound"] = soundcard
            with open(path+"/qemd_config.json","w+") as vmanage_f:
                vmanage_f.write(json.dumps(qconfig_vm))
            vmanage(path)
        elif seld.strip() == "q": vmanage(path)
        else: print("无效输入"); time.sleep(0.5); vmanage(path)
    elif sel.strip() == "4":
        print("==============================")
        print("视频（graphics）输出设备选择")
        print("==============================")
        print("[1] -nograpic (无gui输出，通过终端显示命令)")
        print("[2] -vnc (VNC 服务器输出)")
        print("[q] 返回")
        if sel.strip() == "1":
            qconfig_vm["graphic"] = False
            with open(path+"/qemd_config.json","w+") as vmanage_f:
                vmanage_f.write(json.dumps(qconfig_vm))
            vmanage(path)
        elif sel.strip() == "2":
            vnc_port = input("输入 VNC 服务器监听端口（建议0）：")
            qconfig_vm["graphic"] = "vnc"
            qconfig_vm["vnc"]["host"] = ":"+vnc_port
            with open(path+"/qemd_config.json","w+") as vmanage_f:
                vmanage_f.write(json.dumps(qconfig_vm))
            vmanage(path)
        elif seld.strip() == "q": vmanage(path)
        else: print("无效输入"); time.sleep(0.5); vmanage(path)
    elif sel.strip() == "r":
        # frame
        if qconfig_vm["type"] == "i386": com_head = "qemu-system-i386"
        elif qconfig_vm["type"] == "x86-64": com_head = "qemu-system-x86-64"
        else: print("[!] 配置文件错误！未找到或本工具不适配架构 " + qconfig_vm["type"] + " ，使用默认架构 x86-64 (64位架构)"); com_head = "qemu-system-x86-64"
        # memory
        com_m = " -m "+str(qconfig_vm["memory"])
        # cdrom
        if qconfig_vm["cdrom"] != False:
            com_cd = " -cdrom "+qconfig_vm["cdrom"]
        else:
            com_cd = ""
        # disk command
        disk_dict = qconfig_vm["disk"]
        disk_id = []
        disk_path = []
        disk_type = []
        com_disk = ""
        for key in disk_dict.keys():
            disk_id.append(key)
        for id in disk_id:
            disk_path.append(disk_dict[id][0])
            disk_type.append(disk_dict[id][1])
        print(disk_id)
        print(disk_path)
        print(disk_type)
        for i in range(len(disk_id)-1):
            com_disd = " -drive file="+disk_path[i]+",if=virtio,format="+disk_type[i]+",id="+disk_id[i]
            com_disk = com_disk + com_disd
        # net, video, sound
        com_net = " -net user -net nic,model="+qconfig_vm["card"]["net"]
        com_video = " -vga "+qconfig_vm["card"]["video"]
        com_sound = " -soundhw "+qconfig_vm["card"]["sound"]
        # graphic
        if qconfig_vm["graphic"] == False:
            com_grap = " -nographic"
        elif qconfig_vm["graphic"] == "vnc":
            com_grap = " -vnc "+qconfig_vm["vnc"]["host"]
        command_send = com_head + com_m + com_cd + com_disk + com_net + com_video + com_sound + com_grap
        print(command_send)
        os.system(command_send)
        vmanage(path)
    elif sel.strip() == "c":
        # frame
        if qconfig_vm["type"] == "i386": com_head = "qemu-system-i386"
        elif qconfig_vm["type"] == "x86-64": com_head = "qemu-system-x86-64"
        else: print("[!] 配置文件错误！未找到或本工具不适配架构 " + qconfig_vm["type"] + " ，使用默认架构 x86-64 (64位架构)"); com_head = "qemu-system-x86-64"
        # memory
        com_m = " -m "+str(qconfig_vm["memory"])
        # cdrom
        if qconfig_vm["cdrom"] != False:
            com_cd = " -cdrom "+qconfig_vm["cdrom"]
        else:
            com_cd = ""
        # disk command
        disk_dict = qconfig_vm["disk"]
        disk_id = []
        disk_path = []
        disk_type = []
        com_disk = ""
        for key in disk_dict.keys():
            disk_id.append(key)
        for id in disk_id:
            disk_path.append(disk_dict[id][0])
            disk_type.append(disk_dict[id][1])
        print(disk_id)
        print(disk_path)
        print(disk_type)
        for i in range(len(disk_id)-1):
            com_disd = " -drive file="+disk_path[i]+",if=virtio,format="+disk_type[i]+",id="+disk_id[i]
            com_disk = com_disk + com_disd
        # net, video, sound
        com_net = " -net user -net nic,model="+qconfig_vm["card"]["net"]
        com_video = " -vga "+qconfig_vm["card"]["video"]
        com_sound = " -soundhw "+qconfig_vm["card"]["sound"]
        # graphic
        if qconfig_vm["graphic"] == False:
            com_grap = " -nographic"
        elif qconfig_vm["graphic"] == "vnc":
            com_grap = " -vnc "+qconfig_vm["vnc"]["host"]
        command_send = com_head + com_m + com_cd + com_disk + com_net + com_video + com_sound + com_grap
        print(command_send)
        os.system("echo "+command_send+" > $PREFIX/bin/"+qconfig_vm["name"])
        os.system("chmod +x $PREFIX/bin/"+qconfig_vm["name"])
        input("已设置命令，现在可以在终端输入"+qconfig_vm["name"]+"启动虚拟机了")
        vmanage(path)
    elif sel.strip() == "q": main()
    else: print("无效输入"); time.sleep(0.5); vmanage(path)

def manage():
    path = "./vm"
    vm_folder = []
    for item in os.scandir(path):
        if item.is_dir():
            vm_folder.append(item.path)
    vm_list = []
    qemdc = ""
    for pathd in vm_folder:
        try:
            qemdc = open(pathd+"/qemd_config.json","r")
        except IOError:
            print("[!] 文件夹 "+pathd+" 里没有 qemd_config.json")
        else:
            vm_list.append(pathd)
        finally:
            if qemdc:
                qemdc.close()
    
    for pathd in vm_list:
        qemdc = open(pathd+"/qemd_config.json","r")
        qemdcj = json.loads(qemdc.read())
        try:
            tryget = qemdcj["qemd"]
        except KeyError:
            print("[!] "+pathd+"/qemd_config.json 遗漏配置项！")
            vm_list.remove(pathd)
        qemdc.close()
    
    print("==========================")
    print("虚拟机列表")
    print("==========================")
    for listd in range(0,len(vm_list)):
        print("["+str(listd)+"] "+vm_list[listd])
    print("[q] 退出")
    sel = input("请输入其中一个以管理虚拟机：")
    if sel == "q": main()
    elif int(sel) >= 0 and int(sel) <= len(vm_list):
        vmanage_check(vm_list[int(sel)])
    else: print("无效输入"); time.sleep(1); main()
        

def main():
    os.system("toilet -t --metal 'Qemd'")
    print("Qemu 虚拟机管理器")
    time.sleep(1)
    print("[1] 创建虚拟机")
    print("[2] 管理虚拟机")
    print("[3] 退出/返回到 Staxle")
    sel = input("请输入：")
    if sel.strip() == "1": create()
    elif sel.strip() == "2": manage()
    elif sel.strip( )== "3": os._exit(0)
    else: print("无效输入"); time.sleep(0.7); main()

def check():
    if "qemu-utils" not in os.popen("pkg list-installed|grep qemu-utils").read():
        print("[i] 正在安装 qemu-utils")
        os.system("pkg install qemu-utils")
    main()
if __name__ == "__main__":
    check()