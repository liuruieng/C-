#用户输入和while循环
'''
height = int(input("How tell are you in inches?"))
if height >= 48:
    print("\n You are tall enough to ride!")
else:
    print("\n You'll be able to ride when you 're a little older.")
'''
# %  求模运算 将两个数相除并返回余数
#判断奇偶数
'''
number = int(input("Enter a number,and I'll tell you if it's even or odd:"))
if number % 2 == 0:
    print(f"\n The number{number} is even.")
else:
    print(f"\n The number {number} is odd.")
'''
#使用while循环
'''
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number +=1
'''
#用户选择退出
'''
prompt = "\n Tell me something,and I  will repeat it back to you!"
prompt += "\nEnter 'quit' to end the program."
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)
'''
#flag 当需要多个条件同时满足才可运行时 为了方便判断 可以设置flag
'''
prompt = "\nTell me somethings, and T will repeat it back to you !"
prompt+= "\n Enter 'quit' to end the program."
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
'''
#使用break退出循环
'''
prompt = "\n Please enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)"
while True:
    city = input(prompt)
    if city  == 'quit':
        break
    else:
        print(f"I'd love to go {city.title()}!")
'''
#再循环中使用continue 要返回循环开头  并根据测试条件结果决定是否继续执行循环
'''
打印奇数
current_num = 0
while current_num <10:
    current_num +=1
    if current_num % 2 == 0:
        continue
    print(current_num)
'''
#使用while循环处理列表和字典
#将已验证用户从未验证用户中提取出来
'''
unconfirmed_users = ['alice','brian','candace']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
print("\n The following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
'''
#删除为特定值的所有列表元素 remove()方法删除特定值 是因为仅在列表中出现过一次
'''
pets = ['cat','dog','rabbit','cat','fox','cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)
'''
#使用用户输入来填充字典
'''
responses = {}
polling_active = True
while polling_active:
    name = input("\n What is your name?")
    response = input("Which mountain would you like to climb someday")
    responses[name] = response
    repeat = input("Would you like to let another person respond?(Y/N)")
    if repeat == 'N':
        polling_active = False
print("\n---Poll Result---")
for name,response in responses.items():
    print(f"{name} would like to climb {responses}.")
'''
#函数
#定义函数
'''
def great_user():
"""文档字符串"""docstring
    print("Hello")
great_user()
'''
#向函数传递信息
'''
def great_user(username):
    print(f"Hello,{username.title()}!")
great_user('jesse')
'''
#实参虚参
'''
传递实参
位置实参 要求实参顺序与形参顺序相同
关键字实参  每个实参都由变量名和值组成
还可以使用列表和字典
'''
#位置实参 顺序很重要
'''
def describe_pet(animal_type,pet_name):
    print(f"\n I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('hanster','herry')
describe_pet("dog",'willie')
'''
#关键字实参 给函数传递名称值对 已在实参中将名称和值关联起来所以不用在乎顺序
'''
def describe_pet(animal_type,pet_name):
    print(f"\n I have a {animal_type}.")
    print(f"\n My {animal_type}'s name is {pet_name.title()}.")
describe_pet(animal_type='hamster',pet_name='harry')
describe_pet(animal_type='dog',pet_name='willie')
'''
#注意 在使用关键字实参时 务必准确指定函数定义中的形参
#默认值
'''
def describe_pet(pet_name,animal_type='dog'):
    print(f"\n I have a {animal_type}.")
    print(f"\n My {animal_type}'s name is {pet_name.title()}.")
describe_pet(pet_name="hamster")
'''
#返回值
'''
def get_formatted_name(first_name,last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('jimi','hendrix')
print(musician)
'''
#让实参变成可选的
'''
def get_formatted_name(first_name,middle_name,last_name):
    """返回整洁的姓名"""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('john','lee','hooker')
print(musician)
'''
'''
def get_formatted_name(first_name,last_name,middle_name = ''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('jimi', 'handex')
print(musician)
musician = get_formatted_name('jimi','hooker','hbyio')
print(musician)
'''
#返回字典 函数可以返回任何类型的值 包括列表和字典等复杂的数据结构
'''
def build_person(first_name,last_name):
    person = {'first':first_name,'last': last_name}
    return person
musician = build_person('jimi','hendexr')
print(musician)
'''
'''
def build_person(first_name,last_name,age = None):
    person = {'first':'first_name','last':'last_name'}
    if age:
        person['age'] = age
    return person
musician = build_person('jimi','henderx',age = 26)
print(musician)
'''
#结合使用函数和while循环
'''
def get_formatted_name(first_name,last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()
while True:
    print("\n Please tell  me your name:")
    print("(enter 'q' to quit at any time)")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name:")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name,l_name)
    print("\nHello,{formatted_name}")
'''
#传递列表
'''
def greet_user(names):
    for name in names:
        msg = f"Hello,{name.title()}!"
        print(msg)
usernames = ['haufbi','jui','hfbyu']
greet_user(usernames)
'''
#在函数中修改列表
'''
unprinted_designs = ['phone case','robot penent','denhujoirg']
completed_models = []
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)
print("\nThe following models hava been printed:")
for completed_model in completed_models:
    print(completed_model)
'''
#传递任意数量的实参  预先不知道函数需要接受几个实参 Python允许函数从调用语句中收集任意数量的实参
'''
def make_pizza(*toppings):
    print("toppings")
make_pizza('pepperoni')
make_pizza('mushroom','green peppers','extra chees')
'''
#形如*topping 星号让python 创建一个名为toppings的空元祖
#并将收集到的所有值都封装到这个元祖中
#结合使用位置实参和任意数量实参 先匹配对应实参 之后剩余的实参被*接受
#常见的*args 收集任意数量的位置实参
'''
def make_pizza(size,*toppings):
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")
make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')
'''
#使用任意数量的关键字实参
#预先不知道传递给函数的会是什么信息,此时可将函数编写为能够接受任意数量的键值对
#形如**创建空字典 经常见到的**kwargs 它用于收集任意数量的关键字实参
'''
def build_profile(first,last,**user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('albert','einstein',location = 'princeton',field = 'physics')
print(user_profile)
'''
#将函数存储在模块中
#导入整个模块
def make_pizza(size,*toppings):
    print(f"\n Making a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")
#只需在另一个文件中使用import 文件名 使用即可
#导入特定的函数使用from  文件  import 函数名1,函数名2,函数名3
#使用as给函数指定别名 要导入的函数名称可能与现有函数名称有冲突或者名称太长
#from pizza import make_pizza as mp 从文件pizza中导出make_pizza函数起别名为mp
#使用as给模块指定别名
#import pizza as p

#以下方法谨慎使用
#导入模块中的所有函数使用*可以让python导入模块中的所有函数
#from pizza import *    *号将模块pizza中的每个函数都复制到这个程序文件中
#因为导入了每一个函数 所以可以通过名称来调用每个函数(并非自己编写的大型模块谨慎使用)

#建议 要么只导入需要的函数 或者导入整个模块并使用句点表示法
#类 定义一大类对象都有的通用行为
#创建并使用类
'''
class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def sit(self):
        print(f"{self.name} is now sitting.")
    def roll_over(self):
        print(f"{self.name} rolled over!")
#根据类创建实例
my_dog = Dog('willie',9)
print(f"My dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()
'''
#使用类和实例
#修改实例的属性 可以直接修改实例的属性 也可以通过某种方式进行修改
'''
class Car:
    def __init__(self,make,model,year):
        self.make = make
       self.year = year
    def        self.model = model
  get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
my_new_car = Car('audi','a4',2019)
print(my_new_car.get_descriptive_name())
'''
#给属性指定默认值
'''
class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = make
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
my_new_car = Car('audi','a4',2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
#修改属性的值
#直接修改属性的值
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
#通过方法修改属性值
class Car:
    def updata_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
my_new_car.read_odometer()
#通过方法对属性的值进行递增
class Car:
    def increment_odometer(self,miles):
        self.odometer_reading += miles
my_used_car = Car('subaru','outback',2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23,500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()
'''
#继承
#子类继承父类的所有属性和方法 同时还可以自己定义自己的属性和方法
#子类的方法__init__()
class Car:
    def  __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return  long_name.title()
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self,miles):
        self.odometer_reading += miles
#创建电动汽车
class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
#给子类定义属性和方法
        self.battery_size = 75
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-KWH battery.")
my_tesla = ElectricCar('tesla','model s', 2000)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
'''
导入类
from car import Car  打开car模块并导入Car类
my_new_car = Car('audi','a4',2001)
print(my_neew_car.get_descriptive_name())

在一个模块中存储多个类
从一个模块中导入多个类  from car import Car,ElectricCar
导入整个模块import car
导入模块中的所有类 from module_name import *  (不推荐)
从一个模块中导入另一个模块 先导入父类
from car import Car
from electric_car import ElectricCar
My_beetle = Car('vdjio','fewg',2014)
My_tesla = ElectricCar('tesla','fewgerqhg',2015)
使用别名 as
from electric_car import ElectricCar as EC
my_tesla = EC('tesla','fewsgaqg',2015)
'''
#C:\Users\Administrator\Desktop\国开行贷款.txt
#r保持字符原始值 目的是避免转义
#python打开文件的方法windows平台是默认是gbk编码
'''
with open(r'\C:\Users\Administrator\Desktop国开行贷款.txt',encoding = 'utf-8') as file_object:
    contents = file_object.read()
print(contents)
'''
#关键字with在不需要访问文件后将其关闭
#read()方法到达文件末尾时返回一个空字符串,而将这个空字符串显示出来就是一个空行
#要删除多出来的空行  可以在函数调用print()中使用rstrip()
#print(contents.rstrip())
#使用for循环对文本进行逐行读取
'''
filename = 'Pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line)
#这样输出会出现很多空白行 一是原文件每行末尾都有一个看不见的换行符 者来自文件
#二是调用函数print()会有一个看不见的换行符 这来自函数调用
        print(line.rstrip())
'''
#创建一个包含文件各行内容的列表
#使用关键字with时open()返回的文件对象只在with包含的代码块中可用
#如果要在with代码块外访问文件的内容,可在with代码块内将文件各行存储在列表中
#并在with代码块外使用该列表
#file_name ='C:\Users\Administrator\Desktop\Pi_digits.txt'
#rawstring 原生字符串
'''
with open(r'\C:\Users\Administrator\Desktop国开行贷款.txt',encoding = 'utf-8') as file_object:
    contents = file_object.read()
print(contents)

    lines = file_object.readline()
for line in lines:
    print(line.rstrip())
'''
with open("\\c:\user\\administrator\\desktop国开行贷款.txt",encoding = 'utf-8') as file_object:
    contents = file_object.read()
print(contents)




















