# 1. 求 1-100 内的所有数的和  答案：5050

# 2. 求1-2+3-4+5 ... 99的所有数的和  答案：50

# 3. 任意输入三个整数x,y,z，请把这三个数由小到大输出。  提示：用list
# 举例：输入：6，3，8	输出：[3,6,8]

# 4. 打印99乘法表（提示：print()还可以接受第二个参数end=''作为两次打印之间的分隔，引号之间如果是空格，则两次打印会空一隔）
# 1*1=1
# 2*1=2 2*2=4
# 3*1=3 3*2=6 3*3=9
# 4*1=4 4*2=8 4*3=12 4*4=16
# 5*1=5 5*2=10 5*3=15 5*4=20 5*5=25
# 6*1=6 6*2=12 6*3=18 6*4=24 6*5=30 6*6=36
# 7*1=7 7*2=14 7*3=21 7*4=28 7*5=35 7*6=42 7*7=49
# 8*1=8 8*2=16 8*3=24 8*4=32 8*5=40 8*6=48 8*7=56 8*8=64
# 9*1=9 9*2=18 9*3=27 9*4=36 9*5=45 9*6=54 9*7=63 9*8=72 9*9=81

# 5. 猜数字游戏
#     提示：自己手动创建一个secret数字，并且初始化一个猜的次数变量，然后开始猜
#     如果猜的数字小了，打印'小了'；大了则打印'大了'
#     猜中了，打印'Bingo，Secret数字是XX，你一共用了N次机会'


# sum = 0
# for i in range(101):
#     sum += i
# print(sum)

# sum = 0
# for i in range(100):
#     if i%2 == 0:
#         sum -= i
#     else:
#         sum += i
# print(sum)

# l = []
# for i in range(3):
#     x = int(input('> '))
#     l.append(x)
# l.sort()
# print(l)


# for i in range(1,10):
#     print('')
#     for j in range(1, i+1):
#         print(f'{i}*{j}={i*j}', end=' ')

secret = 28
count = 0

while True:
    x = int(input('> '))
    if x<secret:
        print('小了')
        count+=1
    elif x>secret:
        print('大了')
        count+=1
    else:
        count+=1
        print(f'Bingo! The secret number is {secret}, you have used {count} chances')
        break
