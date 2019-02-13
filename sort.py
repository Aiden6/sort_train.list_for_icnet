# -*-coding:utf-8-*-
import os
import os.path

rootdir_image_dict = {0: "E:\BaiduLanelineDataset\ColorImage_road02",\
                    1: "E:\BaiduLanelineDataset\ColorImage_road03",\
                    2: "E:\BaiduLanelineDataset\ColorImage_road04"}


rootdir_label_dict = "E:\BaiduLanelineDataset\Gray_Label_New"

current_work_path =  os.path.abspath('.') #获取当前工作目录

#定义存储文件的函数
def save_to_file(file_name, contents):
    fh = open(file_name, 'a')   #追加内容
    fh.write(contents + '\n')
    fh.close()
#删除之前的残留文件
if os.path.exists("train1.list"):
    os.remove("train1.list")
if os.path.exists("train2.list"):
    os.remove("train2.list")

#image file path
for i in range(3):
    for parent,dirnames,filenames in os.walk(rootdir_image_dict[i]):    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
    #for dirname in  dirnames:                       #输出文件夹信息
        #print("parent is:"+parent) 
        #print("dirname is" + dirname)
        for filename in filenames:                        #输出文件信息
            #print("parent is:" + parent)
            #print("filename is:" + filename)
            print("the full name of the file is:" + os.path.join(parent,filename)) #输出文件路径信息
            save_to_file(current_work_path + "/train1.list", os.path.join(parent,filename))

#label file path
for parent,dirnames,filenames in os.walk(rootdir_label_dict):    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
    #for dirname in  dirnames:                       #输出文件夹信息
        #print("parent is:"+parent) 
        #print("dirname is" + dirname)
        for filename in filenames:                        #输出文件信息
            #print("parent is:" + parent)
            #print("filename is:" + filename)
            print("the full name of the file is:" + os.path.join(parent,filename)) #输出文件路径信息
            save_to_file(current_work_path + "/train2.list", os.path.join(parent,filename))

#删除残留文件
if os.path.exists("train.list"):
    os.remove("train.list")
#从当前目录打开文件
image_line_file = open("train1.list")
label_line_file = open("train2.list")
#读取文件内容
image_lines = image_line_file.read().splitlines()
label_lines = label_line_file.read().splitlines()

image_line_file.close()
label_line_file.close()
#拼接
for image_line, label_line in zip(image_lines,label_lines): #打包，同时遍历
    temp_line = image_line + ' ' + label_line
    print(temp_line)
    save_to_file(current_work_path + "/train.list", temp_line)

#删除中间文件
if os.path.exists("train1.list"):
    os.remove("train1.list")
if os.path.exists("train2.list"):
    os.remove("train2.list")






