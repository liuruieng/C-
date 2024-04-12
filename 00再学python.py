#print("再学python");
#import  random
'''
计算PI值
NUMBER_OF_TRIALS = 1000000
numberOfHits = 0;
for i in range(NUMBER_OF_TRIALS):
    x = random.random()*2-1
    y = random.random()*2-1
    if x * x + y * y <=1:
        numberOfHits += 1;
pi = 4 * numberOfHits /NUMBER_OF_TRIALS
print("PI is ",pi)
'''
'''
python之禅
import  this
print(this)
'''
'''
列表
'''
bicycles = ['trek','cannondale','resline','specialized']
print(bicycles)
#访问列表元素
print(bicycles[1])
#访问列表最后一个元素
print(bicycles[-1])
#仅当列表为空时 使用-1访问最后一个元素时 会出错
#使用f字符串根据列表中的值创建消息
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)
'''
#练习列表
name = ['张三',"李四","王五","赵六","钱七"]
print(name[-1])
'''
#修改 添加 删除元素
motorcycles = ['honda','yamaha','suzuki']
motorcycles[0] = "ducati"
print(motorcycles[0])
#添加元素 append追加元素至列表末尾
motorcycles.append("labuladu")
print(motorcycles)
#列表中插入元素 insert
motorcycles.insert(0,'ducati123')
print(motorcycles)
#在列表中删除元素 del(须知元素在列表中的索引)
del motorcycles[0]
print(motorcycles)
#使用pop()删除元素 相当于栈 删除栈顶元素  删除末尾元素并能够接着使用它
print(motorcycles.pop())
#弹出列表中的任何位置处的元素 使用pop+ 在括号中添加指定元素的索引
Names = ["张三","李四","王五","赵六"]
Names_own = Names.pop(1)
print(f"弹出的第二个人的名字是: {Names_own.title()}.")
#此时李四的名字已经不在列表中了
#判断使用del 还是pop 如果从列表中删除一个元素并且不再以任何方式使用它,使用del语句
#如果再删除元素之后还能继续使用它就使用pop语句
#根据值删除元素 remove语句 在删除该元素时,也可接着使用它的值
Car = ["小米","理想","蔚来"];
Exp_Car = "小米"
Car.remove(Exp_Car);
print(Car)
print(f"\n{Exp_Car.title()}is too expensive for me")
#remove语句只能删除第一个指定的元素 若在列表中出现多次,则需要配合for循环使用
#组织列表
#使用sort()方法对列表永久排序
cars = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)
#现在列表是按照字母顺序排列,再也无法恢复到原来的顺序
#使用 reverse = True 表示按照字母顺序相反的顺序排列
cars.sort(reverse=True)
print(cars)
#同样的这也是永久性的排列,不可复原
#使用sorted()对列表进行临时性排序 不影响原来顺序 只是临时显示特定顺序
'''
cars = ['bmw','audi','toyota','subaru']
print("Here is the original list:")
print(cars)
print("Here is the sorted list:")
print(sorted(cars))
print("下面是翻转之后的顺序")
print(sorted(cars,reverse = True))
'''
#倒着打印列表顺序
che = ['bmw','audi','toyota']
print(che)
che.reverse()
print("这就是",che)
#reverse翻转列表元素不是按照字母顺序是按照元素的排列顺序 同样该方法是永久性修改排列顺序
#但可以随时复原原来的顺序 只要重新reverse()即可
#确定列表长度 len()
print(len(che))
#操作列表
#遍历列表
magicians = ['alice','david','caroline']
#不要遗漏for循环后面的冒号
for magician in magicians:
    print(magician)
    print(f"{magician.title()},that was a great trick!")
    print(f"I can't wait to see you next trick,{magician.title()}.")
print("Thank you ,everyone.That was a great magic show!")
#练习动物循环
pets = ['cat','dog','rabbit','fox']
for pet in pets:
    print(f"A {pet.title()},would make a great pet.")
print("Any of these animals would make a great pet!")
#创建数值列表
#range()也存在-1行为
for value in range(1,5):
    print(value)
#使用range()创建数字列表
numbers = list(range(1,6))
print(numbers)
#range(开始,结束,增长幅度(步长))
even_numbers = list(range(1,11,2))
print(even_numbers)
#计算1-10得平方根
squares = []
#for循环不要忘记冒号
for val in range(1,11):
    square = val ** 2
    squares.append(square)
print(squares)
#对数字列表进行简单的统计计算
digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))
#列表解析 将for循环和创建新元素合并成一行  以求平方为例
pingfang = [vals ** 2 for vals in range(1,11)]
print(pingfang)
#练习 立方
lifang = [lfs **3 for lfs in range(1,11)]
print(lifang)
#使用列表的一部分  切片 起始位 终止位(不会显示出来)
players = ['charles','martina','michael','florence','eli']
print(players)
print(players[0:3])
print(players[1:4])
#若果没有指定第一个索引  则python将从第一个元素开始
print(players[:4])
#同样 若果提取列表元素的第二个到最后一个
print(players[1:])
#使用负数  例如输出列表中的后三位
print(players[-3:])
#遍历切片
print("Here are the first three players in my team:")
for player in players[:3]:
    print(player.title())
#复制列表[:]
my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]
#注意 如果去掉[:]这两个列表的结果将一样这和初衷不符
my_foods.append("cannoli")
friend_foods.append(("ice cream"))
print("My favorite foods are: ")
print(my_foods)
print("My friend favorite foods are: ")
print(friend_foods)
#定义元组 很相列表但使用()标识,可以使用索引访问其元素 元组中的数据不可修改
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])
'''
修改元组的数据是禁止的,因此报错
dimensions[0] = 250
print(dimensions[0])
'''
#元组是由,标识的,如果想要只包含一个元素的元组要用,标识
my_t = [2,]
print(my_t)
#遍历元组中的所有值
for dimension in dimensions:
    print(dimension)
#修改元组变量  元组中的元素不能修改 但可以给存储元素的变量赋值
dimensions = (400,100)
for dimension in dimensions:
    print(dimension)
#if语句
ches = ['audi','bmw','subaru','toyota']
for che in ches:
    if che == 'bmw':
        print(che.upper())
    else:
        print(che.title())
# ==表示检查是否相等  python检查时忽略大小写
# !=表示两个值是否不等
#检查多个条件 and  只有同时成立才为正确否则为false
#or检查至少一个条件成立即为true
#检查特定值是否在其中使用in
#检查特定值是否不在其中使用not in
'''
age = 17
if age >= 18:
    print("You are old enough to vote!")
#if else
else:
    print("Sorry,you are too young to vote!")
'''
#if-elif-else 中间可以有多个elif 最后可以省略else代码块
age =12
if age<4:
    print("Your admission cost is $0")
elif age <18:
    print("Your admission cost is $25")
else:
    print("Your admission cost is $40.")
#判断列表是否为空
requested_toppings =[]
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}")
    print("\n Finished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
#使用多个列表
nums1 = [1,2,3,4]
res_nums1 = [3,5,7]
for res_num1 in res_nums1:
    if res_num1 in nums1:
        print("numsl中存在这个数字",res_num1)
    else:
        print("nums1中不存在这个数字",res_num1)
print("\n 判断结束!")
#字典 {} 一系列键值对 值可以是数字 字符串 列表 字典
#一个简单的字典
alien_0 = {'color':'green','point':5}
print(alien_0['color'],alien_0['point'])
new_point = alien_0['point']
print(f"You just earned {new_point} points!")
#添加键值对
#字典是一种动态结构 添加键值对时依次指定字典名  用方括号括起来键和相关联的值
#alien_0['x_position'] = 0
alien_0['y_position'] = 25
alien_0['x_position'] = 0
print(alien_0)
#python3.7中 字典元素的排列顺序与定义时相同  如果将字典打印出来或者遍历元素
#则会发现 元素的排列顺序和其添加顺序相同
#创建空字典
#alien_0 = {}
#align_0['color'] = 'green'
#align_0['point'] = 5
#修改字典中的值 可以依次指定字典名,用方括号括起的键以及与该键相关联的新值
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}")
alien_0 = {'x_position':0,'y_position':25,'speed':'medium'}
print(f"Original position:{alien_0['x_position']}")
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_position'] = alien_0['x_position']+x_increment
print(f"New position:{alien_0['x_position']}")
#删除键值对
alien_0 = {'color':'green','point':5}
print(alien_0)
del alien_0['point']
print(alien_0)
#由类似对象组成的字典
favorite_languages = {'jen':'python','sarah':'c','edward':'ruby','phil':'python'}
language = favorite_languages['sarah'].title()
print(f"sarah 's favorite language is {language}")
#使用get()来访问值 get()的第一个参数用于指定键 是必不可少的  第二个参数为指定的键不存在时返回的值
alien_0 = {'color':'green','speed':'slow'}
point_value = alien_0.get('point','No point value assigned')
print(point_value)
#如果 调用get()时 没有指定第二个参数且指定的键不存在  python将返回None
#None并非错误 只是一个表示所需值不存在的特殊值
#遍历字典 遍历所有的键值对
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
}
for key,value in user_0.items():
    print(f"\n key:{key}")
    print(f"value:{value}")
favorite_languages = {
    'jen': 'Python',
    'sarah': 'C',
    'edward': 'ruby',
    'phil': 'python'
}
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
#遍历所有的键
for name in favorite_languages.keys():
#显示的使用 for name in favorite_languages.keys():可以
#因为遍历字典时默认遍历所有元素 for name in favorite_languages:效果一样
#keys()实际上并非只能遍历 它返回一个列表 其中包含字典中的所有键
    print(name.title())
#遍历所有的值
for language in favorite_languages.values():
    print(language.title())
#values()方法并没有考虑重复的情况 为剔除重复项可以使用set()
for language in set(favorite_languages.values()):
    print(language.title())
print("set方法可以去除重复项")
#按特定顺序遍历字典中的所有键
#从python3.7开始 遍历字典时将按照插入的顺序返回其中的元素
#一种方法是在for循环中使用sorted()获得按特定顺序排列的副本
favorite_languages = {
    'jem':"Python",
    'sarah':'c',
    'edward':'ruby'
}
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()},thank you for taking the poll.")
#字典嵌套
alien_0 = {'color':'green','point':5}
alien_1 = {'color':'yellow','point':10}
alien_2 = {'color':'red','point':15}
aliens = [alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)
#创建30个绿色的外星人
aliens = []
for alien_number in range(30):
    new_alien = {'color':'green','point':5,'speed':'slow'}
    aliens.append(new_alien)
#显示前五个
for alien in aliens[:5]:
    print(alien)
print("...")
#显示创建了多少个外星人
print(f"Total number of aliens:{len(aliens)}")
#在字典中存储列表
pizza = {
    'crust':'thick',
    'toppings':['mushroom','extra cheese'],
}
print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")
for topping in pizza['toppings']:
    print(topping)
#另一个例子
favorite_languages = {
    'jen':['python','ruby'],
    'sarah':['c'],
    'adward':['ruby','go'],
    'phil':['python','haskell']
}
for name,languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite_languages are: ")
    for language in languages:
        print(f"\t{language.title()}")
#在字典中存储字典
users = {
    'asfedev':{
        'first':'albert',
        'last':'efnsia',
        'location':'princefe'
    },
    'fbdhuif':{
        'first':'fedjhi',
        'last':'fwfghj',
        'location':'hupasy'
    },
}
for username,user_info in users.items():
    print(f"\nusername:{username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\t Full name: {full_name.title()}")
    print(f"\tLocation:{location.title()}")
#用户输入和while循环
#函数input()让程序暂停运行,等待用户输入消息,之后python将其赋值给一个变量,以便使用
message = input("Tell me something,and i will repeat it back to you!")
print(message)
#过长的prompt
promet = " If you tell us who you are,we can personalize the messages"
promet += '\n What is your first name? '
name = input(promet)
print(f"\n Hello,{name}!")
#使用int()来获取数值输入 python将输入都视为字符串 为显示是数字 可用int(输入数值)
height = int(input("How tall are you,in inches?"))
if height >= 48:
    print("\n You 're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you 're a little older.")
