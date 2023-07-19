f=open('Пр1.txt')
s=f.readline()
digits='0123456789'
series,numbers=0,0
for x in s:
    if x not in digits:
        s=s.replace(x,'*') #заменяем все лишние символы, если они не цифры
s=' '.join(s.split('*')).split() #сплитуем по звёздам, получается список с пустотами, с помощью join склеиваем в строку,
#потом опять сплитуем по пробелам и получаем список с числами в виде строки
for i in s:
    if len(i)==4 and i[0]!='0':
        series+=1
    if len(i)==6 and i[0]!='0':
        numbers+=1
print(min(numbers,series))
