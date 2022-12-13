'''
Поэкспериментируйте с модулем time. Выведите в консоль текущее время, попробуйте вывести следующие данные:

        только время;
        только минуты;
        только дату;
        только месяц.
'''
import time

#print(time.time())


cur_time = time.localtime() # получить struct_time
#only_time = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
only_time = time.strftime("%H:%M:%S", cur_time)
only_minutes = time.strftime("%M", cur_time)
only_date = time.strftime("%d.%m.%Y", cur_time)
only_month = time.strftime("%m", cur_time)


print('only_time is', only_time)
print('only_minutes is', only_minutes)
print('only_date is', only_date)
print('only_month is', only_month)
