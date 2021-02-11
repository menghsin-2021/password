password = 'a123456'
x = 1

while x < 4:
    user_ps = input('請輸入密碼: ')
    if user_ps != 'a123456':
        print('密碼錯誤! 還有', 3-x, '次機會')
        x = x + 1
    else: 
        print('登入成功')
        break

if x == 4:
	print('此帳號已被鎖死')

        


