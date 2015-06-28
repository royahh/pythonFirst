import os
import time 

print("文本文件操作器\n1: 控制面板输出文件内容 \n2：全部重写文件 \n3：直接打开文件 \n4: 从尾端续写文件")

class FileManager(object):
    def __init__(self,textName):
        self.tN = textName
    def openFile(self):
        f= open(self.tN,"r")
        print (f.read())
        f.close()
    def writeFileAll(self,rewrite):
        f= open(self.tN,"w")
        f.write(rewrite)
        f.close()
    def writeFileAfter(self,rewrite):
        f= open(self.tN,"a")
        f.write(rewrite)
        f.close()


txtName = input("Please input text name:\n")
k = FileManager(txtName + ".txt")

model = input("Please input model Number:\n")

if model == "1":
    k.openFile()
    time.sleep(150); 
elif model == "2":
    rewriteTxt = input("Please input rewrite :\n")
    k.writeFileAll(rewriteTxt)
    time.sleep(150); 
elif model == "3":
    os.popen(txtName + ".txt")
elif model == "4":
    rewriteTxt = input("Please input rewrite :\n")
    k.writeFileAfter(rewriteTxt)
    time.sleep(150); 
else:
    print("输入个有意义的数字啊！！")





