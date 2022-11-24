from tkinter import *
import datetime
import time


window = Tk() #Создаём окно приложения.
window.title('TimeCounting') #Добавляем название приложения.
window.geometry('1000x700')
window.resizable(False, False)  # можно ли изменять размер окна - нет

heading = Label(text="TimeCounter",
                   fg = 'black',
                   font=('Arial', 20, 'bold'),)
heading.place(x=400, y=25)

heading = Label(text="*программа подсчитывает время эфирного регионального вещания из расчёта 37 часов в неделю",
                   fg = 'black',
                   font=('Arial', 15),)
heading.place(x=46, y=70)

heading = Label(text="введите дату понедельника в формате гггг-мм-дд",
                   fg = 'black',
                   foreground="#336",
                   font=('Arial', 15),)
heading.place(x=253, y=100)

text_1 = Label(text="Понедельник  ", font="15")
text_1.place(x=50, y=200)
text_2 = Label(text="Вторник", font="15")
text_2.place(x=85, y=240)
text_3 = Label(text="Среда", font="15")
text_3.place(x=95, y=280)
text_4 = Label(text="Четверг", font="15")
text_4.place(x=85, y=320)
text_5 = Label(text="Пятница", font="15")
text_5.place(x=83, y=360)
text_6 = Label(text="Суббота", font="15")
text_6.place(x=81, y=400)
text_7 = Label(text="Воскресение", font="15")
text_7.place(x=47, y=440)
text_8 = Label(text="Итого за неделю без субботы и воскресенья:", font="17")
text_8.place(x=610, y=250)
text_9 = Label(text="Рекомендуемое утреннее вещание в субботу и воскресение:", font="15")
text_9.place(x=50, y=570)

window_1 = Entry(font=("arial", 12), fg="black")
window_1.place(x=170, y=203)
window_2 = Entry(font=("arial", 12), fg="black")
window_2.place(x=170, y=243)
window_3 = Entry(font=("arial", 12), fg="black")
window_3.place(x=170, y=283)
window_4 = Entry(font=("arial", 12), fg="black")
window_4.place(x=170, y=323)
window_5 = Entry(font=("arial", 12), fg="black")
window_5.place(x=170, y=363)
window_6 = Entry(font=("arial", 12), fg="black")
window_6.place(x=170, y=403)
window_7 = Entry(font=("arial", 12), fg="black")
window_7.place(x=170, y=443)
window_8 = Entry(font=("arial", 13), fg="black")
window_8.place(x= 680, y=283)
window_9 = Entry(font=("arial", 13), fg="black")
window_9.place(x=550, y=570)


time_text = Label(text="Время вещания", font=15)
time_text.place(x=435, y=170)
time_window_1 = Entry(font=("arial", 12), fg="black")
time_window_1.place(x=400, y=203)
time_window_2 = Entry(font=("arial", 12), fg="black")
time_window_2.place(x=400, y=243)
time_window_3 = Entry(font=("arial", 12), fg="black")
time_window_3.place(x=400, y=283)
time_window_4 = Entry(font=("arial", 12), fg="black")
time_window_4.place(x=400, y=323)
time_window_5 = Entry(font=("arial", 12), fg="black")
time_window_5.place(x=400, y=363)
time_window_6 = Entry(font=("arial", 12), fg="black")
time_window_6.place(x=400, y=403)
time_window_7 = Entry(font=("arial", 12), fg="black")
time_window_7.place(x=400, y=443)

def new_time():
    with open('new_file_date.txt', 'r') as file_object_4:
        line = file_object_4.readline()
        file = (line)
    chipping = ['СМИ 101_2 КОРОТКО.mp3', 'СМИ РАДИО 101.2 ПОЛНЫЙ 2018.mp3']
    Jingle = 'Радиоканал Авторадио. Без ограничений.wav'
    secs_1 = 61
    secs_2 = 0
    secs_3 = 210
    news = ['Новости АВТОРАДИО 11-00', 'Новости АВТОРАДИО 13-00', 'Новости АВТОРАДИО 16-00', 'Новости АВТОРАДИО 18-00']

    news_timing = '0:03:30'
    n_1 = time.strptime(news_timing, '%H:%M:%S')
    n_2 = time.strftime('%H:%M:%S', n_1)
    (h, m, s) = n_2.split(':')
    n_3 = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

    news_sum = '0:00:00'
    y_1 = time.strptime(news_sum, '%H:%M:%S')
    y_2 = time.strftime('%H:%M:%S', y_1)
    (h, m, s) = y_2.split(':')
    y_3 = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

    mysum = '0:00:00'
    n_4 = time.strptime(mysum, '%H:%M:%S')
    n_5 = time.strftime('%H:%M:%S', n_4)
    (h, m, s) = n_5.split(':')
    n_6 = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))


    with open(file, 'r') as file_object:
        # Подсчёт новостей
        line = file_object.readline()
        while line:
            for x in news:
                if x in line:
                    word = line.split()
                    for i in word:
                        if i == word[2]:
                            i = word[2]
                            a = time.strptime(i, '%H:%M:%S')
                            b = time.strftime('%H:%M:%S', a)
                            (h, m, s) = b.split(':')
                            r = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                            secs = int(h) * 3600 + int(m) * 60 + int(s)
                            f = secs - secs_3
                            if f >= 250:
                                print(f"НОВОСТИ  время выхода: {i}    хроно: {news_timing}")
                                y_3 = y_3 + n_3
                            secs_3 = secs


            for x in chipping:
                if x in line:
                    word = line.split()
                    for i in word:
                        if i == word[2]:
                            i = word[2]
                            a = time.strptime(i, '%H:%M:%S')
                            b = time.strftime('%H:%M:%S', a)
                            (h, m, s) = b.split(':')
                            r = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                            secs = int(h) * 3600 + int(m) * 60 + int(s)
                            f = secs - secs_1
                            if f >= 60:
                                s_1 = r
                            secs_1 = secs

            if Jingle in line:
                word = line.split()
                for z in word:
                    if z == word[2]:
                        z = word[2]
                        w = time.strptime(z, '%H:%M:%S')
                        p = time.strftime('%H:%M:%S', w)
                        (h, m, s) = p.split(':')
                        u = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                        secs_3 = int(h) * 3600 + int(m) * 60 + int(s)
                        e = secs_3 - secs_2
                        if e >= 25:
                            s_2 = u
                            g = s_2 - s_1
                            n_6 = n_6 + g
                            print(f"Реклама  время выхода: {s_1}    Хроно: {g}")
                        secs_2 = secs_3
            line = file_object.readline()

    my_sum_total = n_6 + y_3
    file_name = 'my_sum_total.txt'
    with open(file_name, 'w') as file_object_1:
        file_object_1.write(str(my_sum_total))
    print(f"Итого за день: {my_sum_total}\n")

def new_timi_weekend_1():
    with open('new_file_date.txt', 'r') as file_object_4:
        line = file_object_4.readline()
        file = (line)
    chipping = ['СМИ 101_2 КОРОТКО.mp3', 'СМИ РАДИО 101.2 ПОЛНЫЙ 2018.mp3']
    Jingle = 'Радиоканал Авторадио. Без ограничений.wav'
    secs_1 = 61
    secs_2 = 60

    mysum = '0:00:00'
    n_4 = time.strptime(mysum, '%H:%M:%S')
    n_5 = time.strftime('%H:%M:%S', n_4)
    (h, m, s) = n_5.split(':')
    n_6 = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

    with open(file, 'r') as file_object:
        line = file_object.readline()
        while line:
            for x in chipping:
                if x in line:
                    word = line.split()
                    for i in word:
                        if i == word[2]:
                            i = word[2]
                            a = time.strptime(i, '%H:%M:%S')
                            b = time.strftime('%H:%M:%S', a)
                            (h, m, s) = b.split(':')
                            r = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                            secs = int(h) * 3600 + int(m) * 60 + int(s)
                            f = secs - secs_1
                            if f >= 60:
                                s_1 = r
                            secs_1 = secs

            if Jingle in line:
                word = line.split()
                for z in word:
                    if z == word[2]:
                        z = word[2]
                        w = time.strptime(z, '%H:%M:%S')
                        p = time.strftime('%H:%M:%S', w)
                        (h, m, s) = p.split(':')
                        u = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                        secs_3 = int(h) * 3600 + int(m) * 60 + int(s)
                        e = secs_3 - secs_2
                        if e >= 25:
                            s_2 = u
                            g = s_2 - s_1
                            n_6 = n_6 + g
                            print(f"Реклама  время выхода: {s_1}    Хроно: {g}")
                            saturday_name = 'saturday.txt'
                            with open(saturday_name, 'a') as file_object_2:
                                line_1 = (f"{s_1} {g} \n")
                                file_object_2.writelines(line_1)
                        secs_2 = secs_3
            line = file_object.readline()
    my_sum_total = n_6

    file_name = 'my_sum_total.txt'
    with open(file_name, 'w') as file_object_1:
        file_object_1.write(str(my_sum_total))
    print(f"Итого за день: {my_sum_total}\n")

def new_timi_weekend_2():
    with open('new_file_date.txt', 'r') as file_object_4:
        line = file_object_4.readline()
        file = (line)
    chipping = ['СМИ 101_2 КОРОТКО.mp3', 'СМИ РАДИО 101.2 ПОЛНЫЙ 2018.mp3']
    Jingle = 'Радиоканал Авторадио. Без ограничений.wav'
    secs_1 = 61
    secs_2 = 60

    mysum = '0:00:00'
    n_4 = time.strptime(mysum, '%H:%M:%S')
    n_5 = time.strftime('%H:%M:%S', n_4)
    (h, m, s) = n_5.split(':')
    n_6 = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

    with open(file, 'r') as file_object:
        line = file_object.readline()
        while line:
            for x in chipping:
                if x in line:
                    word = line.split()
                    for i in word:
                        if i == word[2]:
                            i = word[2]
                            a = time.strptime(i, '%H:%M:%S')
                            b = time.strftime('%H:%M:%S', a)
                            (h, m, s) = b.split(':')
                            r = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                            secs = int(h) * 3600 + int(m) * 60 + int(s)
                            f = secs - secs_1
                            if f >= 60:
                                s_1 = r
                            secs_1 = secs

            if Jingle in line:
                word = line.split()
                for z in word:
                    if z == word[2]:
                        z = word[2]
                        w = time.strptime(z, '%H:%M:%S')
                        p = time.strftime('%H:%M:%S', w)
                        (h, m, s) = p.split(':')
                        u = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                        secs_3 = int(h) * 3600 + int(m) * 60 + int(s)
                        e = secs_3 - secs_2
                        if e >= 25:
                            s_2 = u
                            g = s_2 - s_1
                            n_6 = n_6 + g
                            print(f"Реклама  время выхода: {s_1}    Хроно: {g}")
                            saturday_name = 'sanday.txt'
                            with open(saturday_name, 'a') as file_object_2:
                                line_1 = (f"{s_1} {g} \n")
                                file_object_2.writelines(line_1)
                        secs_2 = secs_3
            line = file_object.readline()
    my_sum_total = n_6

    file_name = 'my_sum_total.txt'
    with open(file_name, 'w') as file_object_1:
        file_object_1.write(str(my_sum_total))
    print(f"Итого за день: {my_sum_total}\n")


def date_recording(): # Объявляем функцию записи даты
    # Стираем содержимое файлов за субботу и восткесенье
    with open('saturday.txt', 'w') as file_object:
        file_object.write('')
    with open('sanday.txt', 'w') as file_object:
        file_object.write('')


    general_sum = '0:00:00'
    n_4 = time.strptime(general_sum, '%H:%M:%S')
    n_5 = time.strftime('%H:%M:%S', n_4)
    (h, m, s) = n_5.split(':')
    n_6 = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

    general_broadcasting = '01:13:00:00'
    t_1 = time.strptime(general_broadcasting, '%d:%H:%M:%S')
    t_2 = time.strftime('%d:%H:%M:%S', t_1)
    (d, h, m, s) = t_2.split(':')
    t_3 = datetime.timedelta(days=int(d), hours=int(h), minutes=int(m), seconds=int(s))

    # Понедельник
    date_pn = str(window_1.get())
    print(date_pn)
    new_date = '//AVTORADIO/Avtoradio/07_PLAYLIST/' + date_pn + '.dpm'
    file_name_date = 'new_file_date.txt'
    with open(file_name_date, 'w') as file_object_3:
        file_object_3.write(str(new_date))
    # import Time_Counting_2
    # Time_Counting_2.new_time()
    new_time()
    with open('my_sum_total.txt', 'r') as file_object_2:
        line = file_object_2.readline()
        time_window_1.insert(0, line)
        n_4 = time.strptime(line, '%H:%M:%S')
        n_5 = time.strftime('%H:%M:%S', n_4)
        (h, m, s) = n_5.split(':')
        n_7 = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        general_sum = n_6 + n_7
    # Вторник
    date_1 = datetime.datetime.strptime(date_pn, "%Y-%m-%d")
    date_2 = date_1 + datetime.timedelta(days=1)
    date_3 = str(date_2)
    print(date_3[:10])
    window_2.insert(0, date_3[:10])
    new_date = '//AVTORADIO/Avtoradio/07_PLAYLIST/' + date_3[:10] + '.dpm'
    file_name_date = 'new_file_date.txt'
    with open(file_name_date, 'w') as file_object_3:
        file_object_3.write(str(new_date))
    # import Time_Counting_2
    # Time_Counting_2.new_time()
    new_time()
    with open('my_sum_total.txt', 'r') as file_object_2:
        line = file_object_2.readline()
        time_window_2.insert(0, line)
        n_4 = time.strptime(line, '%H:%M:%S')
        n_5 = time.strftime('%H:%M:%S', n_4)
        (h, m, s) = n_5.split(':')
        n_7 = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        general_sum = general_sum + n_7

    # Среда
    date_4 = date_1 + datetime.timedelta(days=2)
    date_5 = str(date_4)
    print(date_5[:10])
    window_3.insert(0, date_5[:10])
    new_date = '//AVTORADIO/Avtoradio/07_PLAYLIST/' + date_5[:10] + '.dpm'
    file_name_date = 'new_file_date.txt'
    with open(file_name_date, 'w') as file_object_3:
        file_object_3.write(str(new_date))
    # import Time_Counting_2
    # Time_Counting_2.new_time()
    new_time()
    with open('my_sum_total.txt', 'r') as file_object_2:
        line = file_object_2.readline()
        time_window_3.insert(0, line)
        n_4 = time.strptime(line, '%H:%M:%S')
        n_5 = time.strftime('%H:%M:%S', n_4)
        (h, m, s) = n_5.split(':')
        n_7 = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        general_sum = general_sum + n_7
    # Четверг
    date_6 = date_1 + datetime.timedelta(days=3)
    date_7 = str(date_6)
    print(date_7[:10])
    window_4.insert(0, date_7[:10])
    new_date = '//AVTORADIO/Avtoradio/07_PLAYLIST/' + date_7[:10] + '.dpm'
    file_name_date = 'new_file_date.txt'
    with open(file_name_date, 'w') as file_object_3:
        file_object_3.write(str(new_date))
    # import Time_Counting_2
    # Time_Counting_2.new_time()
    new_time()
    with open('my_sum_total.txt', 'r') as file_object_2:
        line = file_object_2.readline()
        time_window_4.insert(0, line)
        n_4 = time.strptime(line, '%H:%M:%S')
        n_5 = time.strftime('%H:%M:%S', n_4)
        (h, m, s) = n_5.split(':')
        n_7 = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        general_sum = general_sum + n_7
    # Пятница
    date_8 = date_1 - datetime.timedelta(days=3)
    date_9 = str(date_8)
    print(date_9[:10])
    window_5.insert(0, date_9[:10])
    new_date = '//AVTORADIO/Avtoradio/07_PLAYLIST/' + date_9[:10] + '.dpm'
    file_name_date = 'new_file_date.txt'
    with open(file_name_date, 'w') as file_object_3:
        file_object_3.write(str(new_date))
    # import Time_Counting_2
    # Time_Counting_2.new_time()
    new_time()
    with open('my_sum_total.txt', 'r') as file_object_2:
        line = file_object_2.readline()
        time_window_5.insert(0, line)
        n_4 = time.strptime(line, '%H:%M:%S')
        n_5 = time.strftime('%H:%M:%S', n_4)
        (h, m, s) = n_5.split(':')
        n_7 = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        general_sum = general_sum + n_7
    # Суббота
    date_10 = date_1 - datetime.timedelta(days=2)
    date_11 = str(date_10)
    print(date_11[:10])
    window_6.insert(0, date_11[:10])
    new_date = '//AVTORADIO/Avtoradio/07_PLAYLIST/' + date_11[:10] + '.dpm'
    file_name_date = 'new_file_date.txt'
    with open(file_name_date, 'w') as file_object_3:
        file_object_3.write(str(new_date))
    # import Time_Counting_2
    # Time_Counting_2.new_timi_weekend_1()
    new_timi_weekend_1()
    with open('my_sum_total.txt', 'r') as file_object_2:
        line = file_object_2.readline()
        time_window_6.insert(0, line)
        n_4 = time.strptime(line, '%H:%M:%S')
        n_5 = time.strftime('%H:%M:%S', n_4)
        (h, m, s) = n_5.split(':')
        n_7 = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        # general_sum = general_sum + n_7
    # Воскресение
    date_12 = date_1 - datetime.timedelta(days=1)
    date_13 = str(date_12)
    print(date_13[:10])
    window_7.insert(0, date_13[:10])
    new_date = '//AVTORADIO/Avtoradio/07_PLAYLIST/' + date_13[:10] + '.dpm'
    file_name_date = 'new_file_date.txt'
    with open(file_name_date, 'w') as file_object_3:
        file_object_3.write(str(new_date))
    # import Time_Counting_2
    # Time_Counting_2.new_timi_weekend_2()
    new_timi_weekend_2()
    with open('my_sum_total.txt', 'r') as file_object_2:
        line = file_object_2.readline()
        time_window_7.insert(0, line)
        n_4 = time.strptime(line, '%H:%M:%S')
        n_5 = time.strftime('%H:%M:%S', n_4)
        (h, m, s) = n_5.split(':')
        n_7 = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        # general_sum = general_sum + n_7
    # print(general_sum)

    # Расчёт дневного времени в субботу
    sum_saturday = '0:00:00'
    f_4 = time.strptime(sum_saturday, '%H:%M:%S')
    f_5 = time.strftime('%H:%M:%S', f_4)
    (h, m, s) = f_5.split(':')
    f_6 = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

    with open('saturday.txt', 'r') as file_object:
        line = file_object.readline()
        while line:
            word = line.split()
            for i in word:
                if i == word[0]:
                    i = word[0]
                    a = time.strptime(i, '%H:%M:%S')
                    b = time.strftime('%H:%M:%S', a)
                    (h, m, s) = b.split(':')
                    r = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                    hours = datetime.timedelta(hours=6, minutes=1, seconds=1)
                    if r >= hours:
                        word_1 = word[1]
                        w_1 = time.strptime(word_1, '%H:%M:%S')
                        w_2 = time.strftime('%H:%M:%S', w_1)
                        (h, m, s) = w_2.split(':')
                        w_3 = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                        f_6 = f_6 + w_3 # Сумма дневного вещания за субботу
            # print(f_6)
            line = file_object.readline()
    # print(f"Дневное вещание в субботу: {sum_day_saturday}")


    # # Расчёт дневного времени в воскресенье
    mysum = '0:00:00'
    f_4 = time.strptime(mysum, '%H:%M:%S')
    f_5 = time.strftime('%H:%M:%S', f_4)
    (h, m, s) = f_5.split(':')
    f_7 = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

    with open('sanday.txt', 'r') as file_object:
        line = file_object.readline()
        while line:
            word = line.split()
            for i in word:
                if i == word[0]:
                    i = word[0]
                    a = time.strptime(i, '%H:%M:%S')
                    b = time.strftime('%H:%M:%S', a)
                    (h, m, s) = b.split(':')
                    r = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                    hours = datetime.timedelta(hours=6, minutes=1, seconds=1)
                    if r >= hours:
                        word_1 = word[1]
                        w_1 = time.strptime(word_1, '%H:%M:%S')
                        w_2 = time.strftime('%H:%M:%S', w_1)
                        (h, m, s) = w_2.split(':')
                        w_3 = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                        f_7 = f_7 + w_3
            line = file_object.readline()
    print(general_sum)

    # Итого за неделю
    window_8.insert(0, str(general_sum))

    # Расчёт утреннего вещания в выходные
    morning_broadcasting = t_3 - general_sum
    morning_broadcasting = morning_broadcasting - f_6 - f_7
    morning_broadcasting = morning_broadcasting / 2

    # Рекомендуемое утреннее вещание
    ee = str(morning_broadcasting)
    window_9.insert(0, str(ee[:7]))

btn1 = Button(text="генерировать", background="#555", foreground="#ccc", padx="15", pady="1", font="15",
              command=date_recording) # Позволяет запускать событие расчёта
btn1.place(x=190, y=490)


window.mainloop()

