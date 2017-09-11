#列表 list
classname = ['phpdever','asp','php']
hhh ='aaa'
classname.insert(1,hhh)#向索引插入内容
classname.pop(1)#删除索引内容
for x in classname:
	print(x)

#二维列表
s1 = ['asp','php','python']
s2 = ['language',s1]
print(s2)

#元组 tuple

s3 = (1,2,s1)
s3[2][1] = 'change'
print(s3)