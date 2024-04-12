#with open(r'C:\Users\Administrator\Desktop\国开行贷款.txt',encoding = 'utf-8')as file_object:
  #  contents = file_object.read()
#print(contents)
#filename = r'C:\Users\Administrator\Desktop\国开行贷款.txt'
#with open(filename,encoding = 'utf-8') as file_object:
#    lines = file_object.readlines()
#for line in lines:
#    print(line.rstrip())

#使用文件的内容
#filename = r"C:\Users\Administrator\Desktop\国开行贷款.txt"
#with open(filename,encoding='utf-8') as file_object:
#    lines = file_object.readlines()
#Nei_string = ''
#for line in lines:
#    Nei_string += line.rstrip()
#print(Nei_string)
#打印字符长度
#print(len(Nei_string))
#读取文本时 Python将其中所有文本都解读为字符串
#如果读取的是数,并要将其作为数值使用 就必须使用函数int()或者float()转换
#写入文件
#filename = r'C:\Users\Administrator\Desktop\programming.txt'
#with open (filename,'w') as file_object:
#    file_object.write("I love programming.")
#    file_object.write("若有战  召必回\n")
#    file_object.write("清澈的爱,只为中国\n")
#Tip 调用open()时提供两个实参 第一个实参是要打开文件的名称
#第二个实参是('w')告诉python以什么模式打开这个文件
#模式包括 'r'读模式 'w'写模式 'a'附加模式 'r+'读写模式
#如果省略了模式实参,Python将以默认的只读模式打开文件
#如果要写入的文件不存在 open()函数会自动创建
#'w'的模式要小心 若果指定的文件已经存在,python将在返回文件对象前清空该文件内容
#Python只能将字符串写入文本文件 要将数值数据存储到文本文件,必须先使用函数
#str()将其转换为字符串格式
#写入多行 会发现文件内容挤在一起 若要单独成行需要方法调用write()中包含换行符
#附加到文件
#如果要给文件添加内容,而不是覆盖原有的内容 可以以附加模式打开文件
#python会将要加入的内容添加到文件末尾
#filename = r"C:\Users\Administrator\Desktop\progamming.txt"
#with open(filename,'a') as file_object:
#    file_object.write("T also love finding meaning in large datasets\n")
#    file_object.write("I loveg creating apps that can run in a browser\n")
#异常
#异常是使用try-except代码块处理的 若果未处理异常程序将会停止并显示traceback
#处理ZeroDivisionError异常
#print(5/0)
#try:
 #   print(5/0)
#except ZeroDivisionError:
#    print("You can't divide by zero!")
#处理FileNotFoundError 文件不存在 文件名错误 文件路径错误
#filename = 'alice.txt'
#try:
#    with open(filename,encoding='utf-8') as f:
#        contents = f.read()
#except FileNotFoundError:
#    print(f"sorry,the file {filename} does not exist.")
#split()方法以空格为分隔符将字符串拆分为多个部分并将这些部分存储到一个列表中
#filename = r"C:\Users\Administrator\Desktop\programming.txt"
#filename = r"C:\Users\Administrator\Desktop\国开行贷款.txt"
#try:
#    with open(filename,encoding='utf-8')as f:
#        contents = f.read()
#except FileNotFoundError:
#    print(f"sorry,the file {filename} does not exits.")
#else:
#    words = contents.split()
#    num_words = len(words)
#    print(f"The file {filename} has about {num_words} words.")
#UnicodeDecodeError: ‘utf-8’ codec can’t decode byte
#在程序中设定文件打开的编码格式为“utf-8”,
# 但是在保存文件时却发现原文件的编码方式是“ANSI”
#解决办法：
#打开文件，点击另存为
#在编码一栏选择UTF-8，保存
#静默失败 表示出现错误时并不想作出任何行为此时 pass
#except FileNotFoundError:
#   pass
#存储数据  json
#json模块 能够将简单的python数据结构转储到文件中
#并在程序再次运行时加载该文件中的数据
#使用json.dump()  和  json.load()
#json.dump()接收两个实参 一个是要存储的数据 一个是可用于存储数据的文件对象
#import  json
#numbers = [1,2,5,8,6,7,5]
#filename = r'C:\Users\Administrator\Desktop\numbers.json'
#with open(filename,'w')as f:
#    json.dump(numbers,f)
#使用json.load()将列表读取到内存中
#import json
#filename = r"C:\Users\Administrator\Desktop\numbers.json"
#with open(filename)as f:
#    numbers = json.load(f)
#print(numbers)
#保存和读取用户生成的数据
#提醒用户首次运行程序时输入自己的名字 并在再次运行程序时记住他
#import json
#username = input("What is your name? ")
#filename = r'C:\Users\Administrator\Desktop\numbers.json'
#with open(filename,'w')as f:
#    json.dump(username,f)
#    print(f"we'll remember you when you come back,{username}")
#向已存储的用户发出问候
#import  json
#filename = r'C:\Users\Administrator\Desktop\numbers.json'
#with open(filename) as f:
#    username = json.load(f)
#    print(f"Welcome back,{username}!")
#将两个程序合并为一个程序
#import json
#filename = r"C:\Users\Administrator\Desktop\numbers.json"
#try:
#    with open(filename)as f:
#        username = json.load(f)
#except FileNotFoundError:
#    username = input("What is your name? ")
#    with open(filename,'w')as f:
#        json.dump(username,f)
#        print(f"We'll remeber you when you come back,{username}!")
#else:
#    print(f"Welcome back,{username}!")
