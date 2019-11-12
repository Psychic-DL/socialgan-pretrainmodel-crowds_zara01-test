'''
fa = open('data2ID.txt')
a = fa.readlines()
fa.close()
fb = open('pred_traj_gt2.txt')
b = fb.readlines()
fb.close()
c = [i for i in a[2][3] if i in b[0][1]]
fc = open('id.txt', 'w')
fc.writelines(c)
fc.close()
'''
'''
import re
import sys
import os

str1 = []
str2 = []
str_dump = []
fa = open("data2ID.txt", 'r')
fb = open("pred_traj_gt2.txt", 'r')
fc = open("id.txt", 'w+')

# 将A.txt的内容逐行读到str1中
for line in fa.readlines():
    str1.append(line.replace("\n", ''))  # line.replace("\n",'') 去掉换行符\n
    #print(str1)
# 将B.txt中的内容逐行读到str2中
for line in fb.readlines():
    str2.append(line.replace("\n", ''))

# 将两个文件中重复的行，添加到str_dump中
for i in str1:
    if i in str2:
        str_dump.append(i)
        fc.write(i + '\n')


fa.close()
fb.close()
fc.close()
'''

#打开文件1，逐行读取
f1=open('pred_traj_gt2.txt', 'r')
lines_a=f1.readlines()
#print(lines_a[1])#9.4514	4.3123
#print(len(lines_a))#1008

#打开文件2，逐行读取
f2=open('data2ID.txt', 'r')
lines_b=f2.readlines()
#print(lines_b)

out_file = open('id.txt', 'w')

#遍历并分割
for line_a in lines_a:
    column_a= line_a.strip().split('\t')
    #print(column_a[0])
    for line_b in lines_b:
        column_b=line_b.strip('\t').split('\t')
        #print(column_b[2])
        #根据列的内容判断
        if float(column_a[0]) == float(column_b[2]):
            out_file.write(str(line_b))#.write()中写入文件的内容必须是str数据类型
            #out_file.flush()#强制刷新缓冲区，或者添加out_file.close()
        else:
            continue

#关闭文件
f1.close()
f2.close()
out_file.close()
