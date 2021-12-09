print("Задание №1")

push_second = int(input('введите секунды '))
if push_second <= 59:
 print(push_second ,"сек")
elif push_second > 59 and push_second <= 3599:
 print(push_second // 60 , "мин", push_second % 60, "сек")
elif push_second > 3599 and push_second <= 86400:
 print(push_second // 3600, "час", (push_second % 3600) // 60, "мин" ,push_second%60, "сек")
else:
 print("Дальше только отчет в днях")