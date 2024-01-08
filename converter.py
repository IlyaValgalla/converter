import tkinter as tk
# Импортируем библиотеку tkinter для создания графического пользовательского интерфейса.

def callback(value_if_allowed):
             # Определяем функцию callback, которая будет использоваться для валидации вводимых данных в поле Entry.
             if value_if_allowed:
                             if value_if_allowed == '-':
                                             return True
                             try:
                                             value_if_allowed = value_if_allowed.replace(',', '.')
                                             float(value_if_allowed)
                                             return True
                             except ValueError:
                                             return False
             else:
                             return True

def lb1_selected():
             # Функция lb1_selected вызывается при выборе элемента в списке lb1.
             for i in lb1.curselection():
                             _from.config(text=lst[i])

def lb2_selected():
             # Функция lb2_selected вызывается при выборе элемента в списке lb2.
            for i in lb2.curselection():
                             _to.config(text=lst[i])

def from1to2():
             # Функция from1to2 выполняет конвертацию валют по нажатию кнопки "Перевести".
             res.config(text='')
             c = 0.0
             gr = float(e.get())
             if _to.cget('text') == 'Рубль':
                             c = gr
             elif _to.cget('text') == 'Доллар':
                             c = gr / 90.93
             elif _to.cget('text') == 'Евро':
                             c = gr / 99.35
             elif _to.cget('text') == 'Юань':
                             c = gr / 12.8
             elif _to.cget('text') == 'Тенге':
                             c = gr / 0.2
             elif _to.cget('text') == 'Лира':
                             c = gr / 3.04
             elif _to.cget('text') == 'Фунт стерлингов':
                             c = gr / 115.3
             elif _to.cget('text') == 'Франк':
                             c = gr / 106.78
             if c < 0.0:
                             res.config(text='Ниже нуля')
                             return
             if _from.cget('text') == 'Рубль':
                             fin = c
             elif _from.cget('text') == 'Доллар':
                             fin = c * 90.93
             elif _from.cget('text') == 'Евро':
                             fin = c * 99.35
             elif _from.cget('text') == 'Юань':
                             fin = c * 12.8
             elif _from.cget('text') == 'Тенге':
                             fin = c * 0.2
             elif _from.cget('text') == 'Лира':
                             fin = c * 3.04
             elif _from.cget('text') == 'Фунт стерлингов':
                             fin = c * 115.3
             elif _from.cget('text') == 'Франк':
                             fin = c * 106.78
             res.config(text=round(fin, 2))

root = tk.Tk()
# Создаем экземпляр класса Tk, который представляет основное окно приложения.

lst = ['Рубль', 'Доллар', 'Евро', 'Юань', 'Тенге', 'Лира', 'Фунт стерлингов', 'Франк']
# Создаем список доступных валют.

lst_var = tk.Variable(value=lst)
e = tk.Entry()
# Создаем поле ввода для ввода суммы в исходной валюте.

reg = root.register(callback)
e.config(validate='all', validatecommand=(reg, '%P'))
# Добавляем валидацию в поле ввода, используя функцию callback.

lb1 = tk.Listbox(listvariable=lst_var)
lb2 = tk.Listbox(listvariable=lst_var)
# Создаем два списка для выбора исходной и целевой валюты.

btnfrom = tk.Button(command=lb1_selected, text='Выбрать шкалу 1')
btnto = tk.Button(command=lb2_selected, text='Выбрать шкалу 2')
btnres = tk.Button(command=from1to2, text='Перевести')
# Создаем кнопки для выбора валют и выполнения конвертации.

_from = tk.Label()
_to = tk.Label()
res = tk.Label()
# Создаем метки для отображения выбранных валют и результата конвертации.

e.grid(row=0, columnspan=2)
lb1.grid(row=1, column=0)
lb2.grid(row=1, column=1)
btnfrom.grid(row=2, column=0)
btnto.grid(row=2, column=1)
_from.grid(row=3, column=0)
_to.grid(row=3, column=1)
btnres.grid(row=4, column=0)
res.grid(row=4, column=1)
# Размещаем элементы в графическом интерфейсе приложения.

root.mainloop()
# Запускаем основной цикл обработки событий для отображения графического интерфейса.