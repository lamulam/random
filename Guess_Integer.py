''' 猜數字
	讓使用者猜數字
	猜錯 告訴大小
'''

import random


start = input('請輸入隨機數開始值: ')
end = input('請輸入隨機數結束值: ')
r = random.randint(int(start), int(start))
count = 0

while True:
	num = input('請猜數字: ')
	num = int(num)
	count += 1
	print('現在猜了', count, '次')
	if num == r:
		print('correct')
		break
	elif num < r:
		print('比答案小')
	else:
		print('比答案大')