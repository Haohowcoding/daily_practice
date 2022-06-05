#celsius = input('請輸入攝氏溫度: ')
#celsius = int(celsius)

#fahrenheit = celsius * 9 / 5 + 32
#print('華氏溫度為: ', fahrenheit)


#age = input('請輸入你的年齡: ')
#age = int(age)
#if age < 13:
#	print('你是小學生')
#elif age >=13 and age < 18:
#	print('你是國高中生')
#elif age >=18 and age < 22:
#	print('你是大學生')
#else:
#	print('你該工作了')


weight = input('請輸入你的體重: ')
height = input('請輸入你的身高: ')
weight = float(weight)
height = float(height)

bmi = weight/(height*height)

if bmi < 18.5:
	print('過輕')
elif bmi >= 18.5 and bmi < 24:
	print('正常')
elif bmi >= 24 and bmi < 27:
	print('過重')
elif bmi >= 27 and bmi < 30:
	print('輕度肥胖')
elif bmi >= 30 and bmi < 35:
	print('中度肥胖')
elif bmi >= 35:
	print('重度肥胖')