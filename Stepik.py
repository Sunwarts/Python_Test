a = int(input())
b = input()

for i in b:
    if ord(i) - a <97:
        print(chr(ord(i)-a+26), end='')
    else:
        print(chr(ord(i) - a), end='')



# a = input()
# for i in a:
#     print(ord(i), end=' ')


# a = int(input())
# b = int(input())
#
# for i in range(a,b+1,1):
#     print(chr(i), end=' ')


# day = int(input()) #<номер дня>
# weight = float(input()) #<текущий вес Гвидо>
#
# start_weight = 100
# end_weight = 88
# total_days = 60
#
# daily_lost = (start_weight-end_weight)/total_days
# current_weight = start_weight - daily_lost*day
#
# if weight <= current_weight:
#     print("Все идет по плану")
# else:
#     print("Что-то пошло не так")
#
# print(f'#{day} ДЕНЬ: ТЕКУЩИЙ ВЕС = {weight} кг, ЦЕЛЬ по ВЕСУ = {current_weight} кг')



# a = int(input())
# b = int(input())
# print(f'Для чисел {a} и {b}:')
# print(f'  Сумма кубов: {a}**3 + {b}**3 = {a**3+b**3}')
# print(f'  Куб суммы: ({a} + {b})**3 = {(a+b)**3}')

# a = int(input())
# b = int(input())
# c = a**3+b**3
# d = (a+b)**3
#
# print(f"Для числа {a} и {b}:")
# print(f'  Сумма кубов: {a}**3 + {b}**3 = {c}')
# print(f'  Куб суммы: ({a} + {b})**3 = {d}')


# data = input()
# curUSD = float(input())
# curYAN = float(input())
#
# s = f'На {data}: 1$ = {curUSD}₽, 1¥ = {curYAN}₽'
# print(s)

# s = input()
# if s[0] == "@" and 5 <= len(s) <= 15 and s == s.lower() and s[1:].isalnum():
#     print("Correct")
# else:
#     print("Incorrect")


# n = input()
# flag = "NO"
# k = "АВЕКМНОРСТУХ"
#
# if 9 <= len(n) <= 10 :
#     letters = n[0] + n[4:6]
#     digits = n[1:4] + n[7:]
#     pos_6 = n[6]
#
#     if digits.isdigit() and pos_6 == "_":
#         flag = "YES"
#
#     for i in letters:
#         if i not in k:
#             flag = "NO"
#             break
# print(flag)


# for i in range (1,int(input())+1):
#     comment = input()
#
#     if comment == "" or comment.isspace():
#         print(f"{i}: COMMENT SHOULD BE DELETED")
#     else:
#         print(f"{i}: {comment}")

# print('2024-05-19'.islower())
# print('2024-05-19'.isupper())

# s = input()
# s1 = s[: s.find('h')]
# s2 = s[s.rfind('h')+1:]
# print(s1 + s2)


# s = input()
# if s.count('f') == 1:
#     print(s.find('f'))
# elif s.count('f') > 1 :
#     print(s.find('f'), s.rfind('f'))
# else:
#     print("NO")

# print(s.find('f'), s.rfind('f'))



# s = input()
# counter = 0
# x = ''
# for i in range(len(s)):
#     s2 = s.count(s[i]) # - считает кол-во каждого элемента в созданном индексе I
#     if s2 >= counter:
#         counter = s2
#         x = s[i]
# print(counter)
# print(x)


# s = input()
# if s.endswith('.com') or s.endswith('.ru') :
#     print("YES")
# else:
#     print("NO")

# n = input()
# counter = 0
# for i in range(10):
#     counter += n.count(str(i))
# print(counter)

# n = int(input())
# counter = 0
#
# for i in range(n):
#     s = input()
#     if s.count("11") >= 3:
#         counter +=1
# print(counter)





# n = input().lower()
# print("Аденин:", n.count('а'))
# print("Гуанин:", n.count('г'))
# print("Цитозин:", n.count('ц'))
# print("Тимин:", n.count('т'))


#a = n.count('а')
# g = n.count('г')
# c = n.count('ц')
# t = n.count('т')
#
# print(f"Аденин: {a}", '\n',f"Гуанин: {g}", '\n',f"Цитозин: {c}")


# n = input()
# print(n.count(' ')+1)

# s = 'foo bar foo baz foo qux'
# print(s.rfind('foo'))
# print(s.rfind('bar'))
# print(s.rfind('qu'))
# print(s.rfind('python'))


# s = input()
# s2 = s.upper()
# counter=0
#
# for i in range (len(s)):
#     if s[i] != s2[i]:
#         counter +=1
# print(counter)


# s = input()
#
# if "хорош" in s.lower():
#     print("YES")
# else:
#     print("NO")


# s = input()
# print(s.swapcase())


# s = input()
# if s == s.title():
#     print ("YES")
# else:
#     print("NO")

# n = input()
# x = len(n) // 2
#
# if len(n) % 2 == 0:
#     print(n[x:] + n[:x])
# else:
#     print(n[x+1:] + n[:x+1])



# n = input()
#
# print(n[2])
# print(n[-2])
# print(n[:5])
# print(n[:len(n)-2])
# print(n[::2])
# print(n[1::2])
# print(n[::-1])
# print(n[::-2])



# n = input()
#
# print(len(n))
# print(n*3)
# print(n[0])
# print(n[:3])
# print(n[-3:])
# print(n[::-1])
# print(n[1:len(n)-1])


# n = input()
# if n == n[::-1]:
#     print("YES")
# else:
#     print("NO")


# s = 'abcdefg'
# print(s[::-3])



# n = int(input())
# s = ''
# s2 = ''
# while n > 0 :
#     s += str(n % 2)
#     n //=2
# for i in range (-1, -len(s)-1,-1):
#     s2 += s[i]
# print(s2)







# n = input()
# n = n.lower()
# counter1 = 0
# counter2 = 0
# for i in range (0, len(n),1):
#     if n[i] in "ауоыиэяюе":
#         counter1 +=1
#     elif n[i] in "бвгджзйклмнпрстфхцчшщ":
#         counter2 +=1
#
# print("Количество гласных букв равно", counter1)
# print("Количество согласных букв равно", counter2)


# n = input()
# counter = 0
#
# for i in range(len(n)-1):
#     if n[i] == n[i+1]:
#         counter+=1
#
# print(counter)

# n = input()
# counter1 = 0
# counter2 = 0
#
# for i in range (len(n)):
#     if n[i] in '+':
#         counter1 += 1
#     elif n[i] in '*':
#         counter2 += 1
#
# print('Символ + встречается', counter1, 'раз')
# print('Символ * встречается', counter2, 'раз')

# n = input()
# flag = True
#
# for i in range(0,len(n)):
#     if n[i] in "0123456789":
#         print("Цифра")
#         flag = False
#         break
# if flag:
#     print("Цифр нет")

# n = input()
# s=0
# for i in range(0,len(n)):
#     s += int(n[i])
# print(s)

# i = input() #Имя
# f = input() #Фамилия
# o = input() #Отчество
#
# print(f[0]+i[0]+o[0])


# n = input()
# for i in range(-1, -len(n)-1,-1):
#     print(n[i])

# s = '01234567891011121314151617'
# for i in range(0, len(s), 5):
#     print(s[i], end='')

# a = int(input())
# b = int(input())
#
# counter = 0
#
# for i in range (a, b+1):
#     for x in range(1, i+1):
#         if i % x == 0:
#             counter +=1
#     if counter == 2:
#         print(i)
#     counter = 0


# n = int(input())
# counter = 0
# product = 1
# for i in range (1,n+1):
#     product*=i
#     counter += product
# print(counter)



# n = int(input())
#
# while n > 9:
#     sum = 0
#     while n != 0:
#         sum += n % 10
#         n //= 10
#     n = sum
#
# print(n)




# n = int(input())
# a = ""
# counter = 0
# for i in range (1, n+1):
#     for x in range (1,i+1):
#         if i % x == 0:
#             counter += 1
#     print(str(i) + "+"*counter)
#     counter = 0


# a = int(input())
# b = int(input())
#
# total = 0
# max_total = 0
# x = 0
#
# for i in range(a,b+1):
#     for k in range (1,i+1):
#         if i % k == 0:
#             total +=k
#     if total >= max_total:
#         max_total = total
#         x = i
#     total = 0
# print(x,max_total)




# n = int(input())
# for i in range(1,n+1):
#     for q in range (i):
#         print(q+1, end="")
#     for w in range (i-1,0,-1):
#         print(w, end="")
#     print ()



# n = int(input())
# counter = 0
# for i in range(1,n+1):
#     for q in range (i):
#         counter += 1
#         print(counter, end=" ")
#     print ()





# for a in range(1,151):
#     for b in range(1,151):
#         for c in range(1,151):
#             for d in range(1, 151):
#                 for e in range(1, 151):
#                     if a**5+b**5+c**5+d**5 == e**5:
#                         print("A = ", a)
#                         print("Б = ", b)
#                         print("С = ", c)
#                         print("Д = ", d)
#                         print("Е = ", e)




# for b in range(1,101):
#     for k in range(1,101):
#         for t in range(1,101):
#             if 10*b+5*k+0.5*t == 100:
#                 print("Быков = ", b)
#                 print("Коров = ", k)
#                 print("Телят = ", t)


# for n in range(1,14):
#     for k in range(1,13):
#         for m in range(1,14):
#             if 28*n+30*k+31*m == 365:
#                 print("Количество N= ", n,"Количество K= ", k,"Количество M= ", m)


# n = int(input())
#
# for i in range(1, n+1):
#
#     if i in range (5, 10):
#         continue
#     if i in range(17, 38):
#         continue
#     if i in range(78, 88):
#         continue
#     print(i)



# n = int(input())
#
# for i in range(2, n+1):
#     if n % i == 0:
#         print(i)
#         break



# n = int(input())
# flag = True
# while n >= 10:
#     last_digit = n % 10
#     predlast_digit = n % 100 // 10
#     if last_digit > predlast_digit:
#         flag = False
#         break
#     n //= 10
# if flag:
#     print("YES")
# else:
#     print("NO")


# n = int(input())
# last_digit = n % 10
# flag = True
# while n != 0:
#     l_digit = n % 10
#     if last_digit != l_digit:
#         flag = False
#         break
#     n //=10
# if flag:
#     print("YES")
# else:
#     print("NO")


# n = int(input())
# while n >= 10:
#     digit = n % 10
#     n //= 10
# print(digit)


# n = int(input())
# total = 0
# counter = 0
# product = 1
# last_digit = n % 10
# while n != 0:
#     x = n % 10
#     total += x
#     counter +=1
#     product *= x
#     first_digit = n
#     n = n // 10
# n_str = str(n)
#
# print(total)
# print(counter)
# print(product)
# print(total/counter)
# print(first_digit)
# print(first_digit+last_digit)


# n = int(input())
# x_max = -1
# x_min = 10
# while n != 0:
#     last_digit = n % 10
#     if last_digit > x_max :
#         x_max = last_digit
#     if last_digit < x_min:
#         x_min = last_digit
#     n = n //10
# print("Максимальная цифра равна", x_max)
# print("Минимальная цифра равна", x_min)
# АЛЬТЕРНАТИВНОЕ РЕШЕНИЕ
# n = int(input())
# a = str(n)
# print ("Минимальная цифра равна",min(a))
# print("Максимальная цифра равна", max(a))



# n = int(input())
#
# while n!=0:
#     last_digit = n % 10
#     print(last_digit, end = "")
#     n = n //10



# n = int(input())
#
# while n != 0:
#     last_digit = n % 10
#     n = n //10
#     print(last_digit)


# n = int(input())
# count = 0
# while n != 0:
#     if n >= 25:
#         n -= 25
#         count += 1
#     elif  n >= 10:
#         n -= 10
#         count += 1
#     elif  n >= 5:
#         n -= 5
#         count += 1
#     elif  n >= 1:
#         n -= 1
#         count += 1
# print(count)


# n = int(input())
# total = 0
# while 0 < n < 6:
#     if n == 5:
#         total += 1
#     n = int(input())
# print(total)


# n = int(input())
# total = 0
# while n>=-1:
#     total +=n
#     n = int(input())
# print(total)


# n = int(input())
# while n // 7 != 0:
#     print(n)
#     n = int(input())
# print(n)



# n = input()
# while n != 'КОНЕЦ' and n != 'конец': # не (А и Б) = не А и не Б закон де Морган
#     print(n)
#     n = input()


# text = input()
# while text != 'КОНЕЦ':
#     print(text)
#     text = input()



# text = input()
# total =0
# while text != 'stop':
#     total += int(text)
#     text = input()
#
# print('Сумма чисел равна', total)





 #ВСЕ ЗАДАЧИ ПО FOR STEPIK

# n = int(input())
#
# x1 , x2 = 1 , 1
# for i in range(1,n+1):
#     print(x1, end=" ")
#     x1, x2 = x2 , x1 + x2




# total = 0
#
# for i in range(1,11):
#     n = int(input())
#     if n %2 == 0:
#         total +=1
# if total == 10:
#     print("YES")
# else:
#     print("NO")

# flag = True
#
# for i in range(1,11):
#     n = int(input())
#     if n % 2 != 0:
#         flag = False
# if flag:
#     print("YES")
# else:
#     print("NO")



# n = int(input())
# max1, max2 = 0,0
# for i in range(1,n+1):
#     x = int(input())
#     if x > max1:
#         max1, max2 = x, max1
#     elif x > max2:
#         max2 = x
# print(max1)
# print(max2)



# n = int(input())
# total = 0
# for i in range(1, n+1):
#     if i % 2 != 0:
#         total += i
#     else:
#         i % 2 == 0
#         total -= i
# print(total)


# n = int(input())
# total = 0
# for i in range(1, n+1):
#     if n % i == 0:
#         total += i
# print(total)


# total = 1
# for i in range(10):
#     n = int(input())
#     if n != 0:
#         total *= n
# print(total)


# n = int(input())
# total = 1
# for i in range(1,n+1):
#     total *= i
# print(total)


# n = int(input())
# total = 0
# for i in range(1, n+1):
#     if i**2% 10 ==2:
#         total+=i
#     if i**2% 10 ==5:
#         total+=i
#     if i**2% 10 ==8:
#         total+=i
# print(total)
# # x = "258"
# # for i in range (1, n+1):
# #     if str(i**2 % 10) in x:
# #         total += i
# # print(total)




# from math import log
#
# n = int(input())
# total = 0
# for i in range(1, n+1):
#     total += 1/i
# a = total - log(n)
# print(a)




# n = int(input())
# total = 0
# for i in range(n):
#     x = int(input())
#     total += x
# print(total)


# a = int(input())
# b = int(input())
#
# counter1 = 0
# counter2 = 0
# for i in range (a,b+1):
#     if i % 10 == 4:
#         counter1 +=1
#     if i % 10 == 9:
#         counter2 += 1
# counter = counter1 + counter2
# print(counter)


# largest = int(input())  # принимаем первое число за максимальное
# for _ in range(9):
#     num = int(input())
#     if num < largest:
#         largest = num
#
# print('Наибольшее число равно', largest)



# num = int(input())
# flag = True
#
# for i in range(2, num):
#     if num % i == 0:  #  если исходное число делится на какое-либо отличное от 1 и самого себя
#         flag = False
#
# if num == 1:
#     print('Это единица, она не простая и не составная')
# elif flag == True:
#     print('Число простое')
# else:
#     print('Число составное')


# n = int(input())
#
# for i in range(1,11):
#     a = n*i
#     print(f'{n} x {i} = {a}')


# m = int(input())
# n = int(input())
#
# for i in range(m,n+1):
#     if i % 17 == 0:
#         print(i)
#     # elif i % 15 == 0:
#     #     print(i)
#     elif i % 3 == 0 and i % 5 == 0:
#         print(i)
#     elif i % 10 == 9:
#         print(i)




# m = int(input())
# n = int(input())
#
# for i in range (m, n-1, -1):
#     if i % 2 !=0:
#         print(i)


# m = int(input())
# n = int(input())
# if m < n :
#     for i in range(m,n+1):
#         print(i)
# else:
#     for i in range(m,n-1, -1):
#         print(i)



# m = int(input())
# n = int(input())
#
# for i in range(m,n+1):
#     print(i)

# for i in range(5, 0, -1):
#     print(i, end=' ')
# print('Взлетаем!!!')


# # Расчет инвестиций (себе геометрическая прог)
# money = int(input("Введит сумму инвестирования"))
# percent_year = int(input("Годовой процент:"))
# number_year = int(input("Введите кол-во инвест.лет: "))
# p = percent_year/ 100
# for i in range(number_year):
#     print(f"На начало {i+1} года:",money)
#     money += money * p


# m = int(input())
# p = int(input())
# n = int(input())
# for i in range (n):
#     print(i+1, m)
#     m += m*(p/100)



# n = int(input())
# for i in range (n):
#     a = "*"*n
#     n-=1
#     print(a)


# n = int(input())
# a = n+1
# for i in range (a):
#     print(f'Квадрат числа {i} равен {i**2}')

# n = input()
# for i in range(10):
#     print(i, n)


# n = int(input())
# for i in range(n):
#     a = "*******************"
#     print(a)



# for i in range(6):
#     print("AAA")
# for i in range(5):
#     print("BBBB")
# print("E")
# for i in range(9):
#     print("TTTTT")
# print("G")

# a = input()
# b = int(input())
# for i in range(b):
#     print(a)


# for i in range(10):
#     print("Python is awesome!")

# for i in range(5):
#     num = int(input())
#     num2 = int(input())
#     print("Квадрат вашего числа равен:", num * num)
#     print("Квадрат вашего числа равен:", num2 * num2)
#
# print("Цикл завершен")



# # ЗКАНИТЬ ЗАДАЧУ МНОГОУГОЛЬНИК
# from math import *
#
# n = int(input())
# a = float(input())
#
# S = ((n*pow(a,2)) / (4 * tan(pi/n) ))
#
# print(float(S))
#
#
#
# #  ЗАКИНУТЬ ЗАДАЧУ ДИСКРИМЕНАНТ
# from math import *
#
# a, b, c = float(input()), float(input()), float(input())
#
# d = pow(b,2)-4*a*c
#
# if d > 0:
#     x1 = (-b + sqrt(d)) / (2*a)
#     x2 = (-b - sqrt(d)) / (2*a)
#     print(min(x1,x2))
#     print(max(x1,x2))
# elif d == 0:
#     print(-b / (2*a))
# else:
#     print("Нет корней")

# from math import ceil, floor
# x = float(input())
#
# # x1 = ceil(x)
# # x2 = floor(x)
# # a = x1+x2
# a = ceil(x)+floor(x)
# print(a)


# from math import cos, sin, tan, pi
#
# x = float(input()) #x=radians(float(input()))
# r = (x*pi)/180
#
# trigonometria = sin(r)+cos(r)+(tan(r))**2
# print(trigonometria)


# from math import sqrt
#
# a = float(input())
# b = float(input())
#
# av_arif = (a+b)/2
# av_geom = sqrt(a*b)
# av_garm = (2*a*b)/(a+b)
# av_sqrt = sqrt((a**2+b**2)/2)
#
# print(av_arif)
# print(av_geom)
# print(av_garm)
# print(av_sqrt)



# from math import pi
#
# R = float(input())
#
# S=pi*(R**2)
# C=2*pi*R
# print(S)
# print(C)


# x1 = float(input())
# y1 = float(input())
# x2 = float(input())
# y2 = float(input())
#
# p=((x1-x2)**2+(y1-y2)**2)**0.5
# print(p)



# a = input()
#
# if "@" in a and "." in a:
#     print("YES")
# else:
#     print("NO")



# a = input()
#
# if "суббота" in a:
#     print("YES")
# elif "воскресенье" in a:
#     print("YES")
# else:
#     print("NO")



# a = input()
#
# if "синий" in a:
#     print("YES")
# else:
#     print("NO")


# a1 = input()
# a2 = input()
# a3 = input()
# len_str1 = len(a1)
# len_str2 = len(a2)
# len_str3 = len(a3)
#
# max_len = max(len_str1,len_str2,len_str3)
# min_len = min(len_str1,len_str2,len_str3)
# av_len = (len_str1+len_str2+len_str3-max_len-min_len)
#
# if (av_len-min_len) == (max_len - av_len):
#     print("YES")
# else:
#     print("NO")



# town1 = input()
# town2 = input()
# town3 = input()
# count1 = len(town1)
# count2 = len(town2)
# count3 = len(town3)
#
# if min(count1,count2,count3) == count1:
#     print(town1)
# elif min(count1,count2,count3) == count2:
#     print(town2)
# elif min(count1,count2,count3) == count3:
#     print(town3)
#
# if max(count1,count2,count3) == count1:
#     print(town1)
# elif max(count1,count2,count3) == count2:
#     print(town2)
# elif max(count1,count2,count3) == count3:
#     print(town3)



# teamname = input()
# count = len(teamname)
# print(f"Футбольная команда {teamname} имеет длину {count} символов")


# firstname = input('Ваше имя: ')
# lastname = input('Ваша фамилия: ')
#
# print("Hello " + firstname+" "+lastname+"! "+"You have just delved into Python")




# p1 = '"Python is a great language!", said Fred.'
# p2 = ''' "I don't ever remember having this much fun before." '''
# p = p1+p2
# print(p)




# p1 = float(input())
# p2 = float(input())
# q1 = float(input())
# q2 = float(input())
#
# x1 = abs(p1-q1)+abs(p2-q2)
#
# print(int(x1))


# a = float(input())
# b = float(input())
# c = float(input())
# d = float(input())
# e = float(input())
#
# x1 = abs(a)+abs(b)+abs(c)+abs(d)+abs(e)
#
# print(x1)



# a = int(input())
#
# x1 = a % 10
# x2 = (a // 10) % 10
# x3 = (a // 100) % 10
#
# x4 = max(x1,x2,x3)
# x5 = min(x1,x2,x3)
# x6 = (x1 + x2 + x3 - x4 - x5)
#
# if (x4 - x5) == x6:
#     print("Число интересное")
# else:
#     print("Число неинтересное")
# print(x1)
# print(x2)
# print(x3)
# print(x4)
# print(x5)
# print(x6)

# a = int(input())
# b = int(input())
# c = int(input())
#
# print(max(a,b,c))
# print(a+b+c - max(a,b,c)-min(a,b,c))
# print(min(a,b,c))

#Альтернатирвное решение сразу ниже

# a = float(input())
# b = float(input())
# c = float(input())
#
#
# if a>=b>=c:
#     print(int(a))
#     print(int(b))
#     print(int(c))
# elif a>=c>=b:
#     print(int(a))
#     print(int(c))
#     print(int(b))
# elif b>=a>=c:
#     print(int(b))
#     print(int(a))
#     print(int(c))
# elif b>=c>=a:
#     print(int(b))
#     print(int(c))
#     print(int(a))
# elif c>=a>=b:
#     print(int(c))
#     print(int(a))
#     print(int(b))
# elif c>=b>=a:
#     print(int(c))
#     print(int(b))
#     print(int(a))


# a = float(input())
# b = float(input())
# c = float(input())
# d = float(input())
# e = float(input())
#
# x1 = int (max (a,b,c,d,e))
# x2 = int(min (a,b,c,d,e))
# print("Наименьшее число =", x2)
# print("Наибольшее число =", x1)

# a = float(input())
# x = (a *10) % 10
# x1 = x /10
# print(x1)


# a = float(input())
# x = (a *10) % 10 //1
# x1 = int(x)
# print(x1)



# dog = float(input())
#
# if dog <=2:
#     x1=dog*10.5
#     print(x1)
# elif dog>2:
#     x2 = 2*10.5+4*(dog-2)
#     print(x2)




# f = float(input())
# C=5/9*(f - 32)
# print(C)


# a = float(input())
#
# if a !=0 :
#     t = a**(-1)
#     print(t)
# else:
#     print("Обратного числа не существует")


# s = float(input())
# v1 = float(input())
# v2 = float(input())
#
# t = s/(v1+v2)
# print(t)



# a = float(input())
# b = float(input())
#
# s = 1/2*a*b
# s=float(s)
# print(s)



# num1 = 25_000_000
# num2 = 25000000
# print(num1)
# print(num2)


# atom = 10 ** 80  # количество атомов во вселенной
# print('Количество атомов =', atom)

# a1 = int(input())
# b1 = int(input())
# a2 = int(input())
# b2 = int(input())
#
# if b1 < a2 or b2 < a1:
#     print("пустое множество")
# elif b1 == a2:
#     print(a2)
# elif b2 == a1:
#     print(a1)
# elif a2 > a1 and b1 < b2:
#     print(a2, b1)
# elif a2 < a1 and b1 > b2:
#     print(a1, b2)
# elif a1 >= a2 and b2 >= b1:
#     print(a1,b1)
# elif a1<=a2 and b2<=b1:
#     print(a2,b2)


# a = int(input())
#
# if a == 0:
#     print("зеленый")
# elif (1 <= a <= 10 or 19 <= a <= 28) and a % 2 == 0:
#     print("черный")
# elif (1 <= a <= 10 or 19 <= a <= 28) and a % 2 != 0:
#     print("красный")
# elif (11 <= a <= 18 or 29 <= a <= 36)  and a % 2 == 0:
#     print("красный")
# elif (11 <= a <= 18 or 29 <= a <= 36) and a % 2 != 0:
#     print("черный")
# else:
#     print("ошибка ввода")



# Альтернатива решения выше
# a = int(input())
#
# if a == 0:
#     print("зеленый")
# elif 1 <= a <= 10 and a % 2 == 0:
#     print("черный")
# elif 1 <= a <= 10 and a % 2 != 0:
#     print("красный")
# elif 11 <= a <= 18 and a % 2 == 0:
#     print("красный")
# elif 11 <= a <= 18 and a % 2 != 0:
#     print("черный")
# elif 19 <= a <= 28 and a % 2 == 0:
#     print("черный")
# elif 19 <= a <= 28 and a % 2 != 0:
#     print("красный")
# elif 29 <= a <= 36 and a % 2 == 0:
#     print("красный")
# elif 29 <= a <= 36 and a % 2 != 0:
#     print("черный")
# else:
#     print("ошибка ввода")


# color_1 = input()
# color_2 = input()
#
# if (color_1 == "красный" or color_2 == "красный") and (color_1 == "синий" or color_2 == "синий"):
#     print ("фиолетовый")
# elif (color_1 == "красный" or color_2 == "красный") and (color_1 == "желтый" or color_2 == "желтый"):
#     print ("оранжевый")
# elif (color_1 == "синий" or color_2 == "синий") and (color_1 == "желтый" or color_2 == "желтый"):
#     print ("зеленый")
# elif color_1 == color_2 and (color_1 == "синий" or color_1 == "красный" or color_1 == "желтый" ):
#     print(color_1)
# else:
#     print("ошибка цвета")


# a, b = int(input()),  int(input())
# c = input()
#
# if c == "+":
#     print(a+b)
# elif c == "-":
#     print(a-b)
# elif c == "*":
#     print(a*b)
# elif c == "/":
#     if b == 0:
#         print("На ноль делить нельзя!")
#     else:
#         print(a / b)
# else:
#     print("Неверная операция")



# a = int(input())
# if a < 60:
#     print("Легкий вес ")
# elif 60 <= a <64:
#     print("Первый полусредний вес")
# elif 64 <= a < 69:
#     print("Полусредний вес")


# a = int(input())
#
# if a == 12 or a == 5 or a == 1 or a == 3 or a == 7 or a == 8 or a == 10:
#     print ("31")
# elif a == 6 or a == 9 or a == 4 or a == 11:
#     print("30")
# else:
#     print("28")


# a = int(input())
# b = int(input())
# c = int(input())
# if c < a < b or b < a < c:
#     print(a)
# elif a < c < b or b < c < a:
#      print(c)
# else:
#     print(b)



# a = int(input())
# b = int(input())
# c = int(input())
#
# if a == b == c:
#     print("Равносторонний")
# elif a == b or b ==c or a == c:
#     print("Равнобедренный")
# elif a != b and b !=c and a != c:
#     print("Разносторонний")

# else:
#     a != b and b != c and a != c
#     print("Разносторонний")



# n = int(input()) #ZOOM
# k = int(input()) #FLASH
#
# if n > k:
#     print("NO")
# elif n < k:
#     print("YES")
# else:
#     n = k
#     print("Don't know")


# grade = int(input('Введите вашу отметку по 100-балльной системе: '))
#
# if grade >= 90:
#     print(5)
# else:
#     if grade >= 80:
#         print(4)
#     else:
#         if grade >= 70:
#             print(3)
#         else:
#             if grade >= 60:
#                 print(2)
#             else:
#                 print(1)


# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
#
# if -1 <= a - c <=1 and -1 <= b - d <= 1:
#     print("YES")
# else:
#     print("NO")


# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
#
# if a == c or b == d:
#     print("YES")
# else:
#     print("NO")


# x = int(input())
# if x % 4 == 0 and (x % 100 !=0 or x % 400 ==0) :
#     print("YES")
# else:
#     print("NO")


# a = int(input())
# b = int(input())
# c = int(input())
#
# if a + b > c and a+c>b and b+c>a:
#     print("YES")
# else:
#     print("NO")




# x = int(input())
# if 1000 <= x <= 9999 and (x % 7 == 0 or x % 17 == 0):
#     print("YES")
# else:
#     print("NO")

# num = int(input())
# d3 = num % 10
# d2 = num % 100 // 10
# d1 = num // 100
# print(d3)
# print(d2)
# print(d1)

# x = int(input())
#
# if -30 < x <= -2 or 7 < x <=25:
#     print("Принадлежит")
# else:
#     print("Не принадлежит")


# x = int(input())
#
# if x <= -3 or x >= 7:
#     print("Принадлежит")
# else:
#     print("Не принадлежит")



# a = int(input())
#
# if a >= 2 and a <= 17:
#     b = 3
#     p = a * a + b * b
# else:
#     b = 5
#
# p = (a + b) * (a + b)
# print(p)


# num1 = 34
# num2 = 81
# if num1 // 9 == 0 or num2 % 9 == 0:
#     print('число', num1, 'выиграло')
# else:
#     print('число', num2, 'выиграло')


# a = int(input())
# b = int(input())
# c = int(input())
#
# if a <= 0:
#     a = 0
# if b <= 0:
#     b = 0
# if c <= 0:
#     c = 0
# x = a+b+c
# print(x)


# a = int(input())
#
# if a <=13:
#     print("детство")
# elif 14 <= a <= 24:
#     print("молодость")
# elif 25 <= a <= 59:
#     print("зрелость")
# elif a >= 60:
#     print("старость")




# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# if a > b:
#     a = b
# if c > d:
#     c = d
# if a > c:
#     a = c
# print(a)


# a = int(input('1' ))
# b = int(input("2" ))
# c = int(input("3" ))
# d = int(input("4" ))
#
# if a <= b <= c <= d:
#     print(a)
# else:
#     print(c)


# a = int(input())
# b = int(input())
# c = int(input())
#
# d = c-b
# e = b-a
#
# if e == d:
#     print('YES')
# else:
#     print('NO')



# a = int(input())
#
# if a>= 18:
#     print("Доступ разрешен")
# else:
#     print("Доступ запрещен")


# a = int(input())
# b = a % 10
# c = (a//10) % 10
# d = (a//100) % 10
# e = a // 1000
#
# sumFL = e+b
# sumMM = abs(d-c) #abs - модуль +-
#
# if sumFL == sumMM:
#     print("Да")
# else:
#     print("Нет")
#
# x = int(input())
#
# x1 = x // 1000
# x2 = x // 100 % 10
# x3 = x % 100 // 10
# x4 = x % 10
#
# if x1 + x4 == x2 - x3:
#     print("Да")
# else:
#     print("Нет")
#
#


# if a % 2 == 0:
#     print('Четное')
# else:
#     print('Не четное')


