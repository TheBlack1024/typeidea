
import os, sys

# os.access()使用
# 假定 TXT.txt 文件存在，并有读写权限
ret = os.access("TXT.txt", os.F_OK) # 作为access()的mode参数，测试path是否存在
print ("F_OK - 返回值 %s"% ret)

ret = os.access("TXT.txt", os.R_OK) # 包含在access()的mode参数中 ， 测试path是否可读。
print ("R_OK - 返回值 %s"% ret)

ret = os.access("TXT.txt", os.W_OK) #包含在access()的mode参数中 ， 测试path是否可写
print ("W_OK - 返回值 %s"% ret)

ret = os.access("TXT.txt", os.X_OK)# 包含在access()的mode参数中 ，测试path是否可执行。
print ("X_OK - 返回值 %s"% ret)

print("="*100)


# os.chdir() 方法

import os, sys

#path = "/tmp"

# 查看当前工作目录
retval = os.getcwd()
print ("当前工作目录为 {}" .format(retval))

# 修改当前工作目录
#os.chdir( path )

# 查看修改后的工作目录
#retval = os.getcwd()

#print ("目录修改成功 %s" % retval)




