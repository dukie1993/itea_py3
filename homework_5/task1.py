'''
Alarm clock manager. Уявіть, що на протязі трьох наступних тижнів ви плануєте 
щодня прокидатися на 15 хвилин раніше, ніж попереднього дня. Проте на вихідних 
ви хочете прокидатися не раніше, а поспати стільки ж, скільки у п`ятницю. 
Напишіть програму, яка порахує і виведе на екран, на котру годину вам потрібно 
поставити будильник, щоб прокинутися вчасно протягом наступних трьох тижнів, якщо 
зазвичай ви просиналися о 08:00 ранку. 
Формат виводу наступний: http://i.imgur.com/SNDo2GO.png
'''
import datetime
from datetime import date
from datetime import timedelta
import calendar

day_lst = []
wakeup_lst = []

my_date = date.today()
current_wake_time = 480

# Run a loop for 3 weeks
for day in range(0, 21):
    # Write 21 days names to list, starting from tomorrow
    next_day = my_date + datetime.timedelta(days=day+1)
    day_name = calendar.day_name[next_day.weekday()]
    day_lst.insert(day, day_name)

    if day_name == "Saturday" or day_name == "Sunday":
        next_day_time = current_wake_time
    else:
        next_day_time = current_wake_time - 15

    # Write time to array in H:MM format
    wake_time_delta = str(timedelta(minutes=next_day_time))[:-3]
    wakeup_lst.insert(day, wake_time_delta)
    current_wake_time = next_day_time

    print(day_lst[day], wakeup_lst[day])