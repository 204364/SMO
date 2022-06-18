def edit_val_row():#сформировать
    N =[ float(e_11.get()), float(e_21.get()), float(e_31.get()) ]
    prom =[ float(e_12.get()), float(e_22.get()), float(e_32.get()) ]
    intense =[ float(e_13.get()), float(e_23.get()), float(e_33.get()) ]
    t =[ float(e_16.get()), float(e_26.get()), float(e_36.get()) ]
    intense1 =[ float(e_17.get()), float(e_27.get()), float(e_37.get()) ]
    ro =[ float(e_19.get()), float(e_29.get()), float(e_39.get()) ]
    n = float(e_110.get())
    m = float(e_111.get())
    Lb_130['text'] = ('N=', N, 'prom=', prom, 'intense=', intense, 't=', t, 'intense1=', intense1, 'ro=', ro, 'n=',n, 'm=',m)
        
#Основная программа форма
from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title('Ввод данных')
root.geometry('600x450')

nb = ttk.Notebook(root)
nb.pack(fill='both', expand='yes')
f1 = Text(root)
f2 = Text(root)
nb.add(f1, text='Ввод данных')
nb.add(f2, text='Расчет')

#закладка Ввод данных
fr1_0 = Frame(f1)
fr1_0.pack(expand = 0 , fill = BOTH)

Lb_0= Label(fr1_0, text="Входной поток заявок", fg ='red', font='bold') 
Lb_0.grid(column=0, row=0, columnspan=3) 
# строка 1
Lb_1= Label(fr1_0, text="1 Утро \n (с 8-00 по 12 -00)", fg ='blue')  
Lb_1.grid(column=1, row=1)  

Lb_2= Label(fr1_0, text="2 День \n (с 13-00 по 16 -00)", fg ='green')  
Lb_2.grid(column=2, row=1)

Lb_3= Label(fr1_0, text="3 Вечер \n (с 17-00 по 22 -00)")  
Lb_3.grid(column=3, row=1)  
# строка 2
Lb_11= Label(fr1_0, text="Количество клиентов N=")  
Lb_11.grid(column=0, row=2)  

e_11 =Entry(fr1_0, width=10, fg ='blue')
e_11.grid(column=1, row=2)
e_11.insert(0, 5)

e_21 =Entry(fr1_0, width=10, fg ='green')
e_21.grid(column=2, row=2)
e_21.insert(0, 15)

e_31 =Entry(fr1_0, width=10)
e_31.grid(column=3, row=2)
e_31.insert(0, 9)

# строка 3
Lb_12= Label(fr1_0, text="Время (мин) prom=")  
Lb_12.grid(column=0, row=3)  

e_12 =Entry(fr1_0, width=10, fg ='blue')
e_12.grid(column=1, row=3)
e_12.insert(0, 10)

e_22 =Entry(fr1_0, width=10, fg ='green')
e_22.grid(column=2, row=3)
e_22.insert(0, 10)

e_32 =Entry(fr1_0, width=10)
e_32.grid(column=3, row=3)
e_32.insert(0, 10)

# строка 4
Lb_12= Label(fr1_0, text="Интенсивность входного \n потока  (клиентов\мин) intense =")  
Lb_12.grid(column=0, row=4)  

e_13 =Entry(fr1_0, width=10, fg ='blue')
e_13.grid(column=1, row=4)
v1 = float(e_11.get())/ float(e_12.get())
e_13.insert(0, v1)

e_23 =Entry(fr1_0, width=10, fg ='green')
e_23.grid(column=2, row=4)
v2 = float(e_21.get())/ float(e_22.get())
e_23.insert(0, v2)

e_33 =Entry(fr1_0, width=10)
e_33.grid(column=3, row=4)
v3 = float(e_31.get())/ float(e_32.get())
e_33.insert(0, v3)

# строка 5
Lb_0= Label(fr1_0, text="Выходной поток заявок", fg ='red', font='bold') 
Lb_0.grid(column=0, row=5, columnspan=3)

# строка 6
Lb_16= Label(fr1_0, text="Время обслуживания  \n одного клиента (мин) t=")  
Lb_16.grid(column=0, row=6)  

e_16 =Entry(fr1_0, width=10, fg ='blue')
e_16.grid(column=1, row=6)
e_16.insert(0, 2)

e_26 =Entry(fr1_0, width=10, fg ='green')
e_26.grid(column=2, row=6)
e_26.insert(0, 5)

e_36 =Entry(fr1_0, width=10)
e_36.grid(column=3, row=6)
e_36.insert(0, 3)

# строка 7
Lb_17= Label(fr1_0, text="Интенсивность выходного \n  потока (клиент\мин) intense1=")  
Lb_17.grid(column=0, row=7)  

e_17 =Entry(fr1_0, width=10, fg ='blue')
e_17.grid(column=1, row=7)
v1 = 1/ float(e_16.get())
e_17.insert(0, v1)

e_27 =Entry(fr1_0, width=10, fg ='green')
e_27.grid(column=2, row=7)
v2 = 1/ float(e_26.get())
e_27.insert(0, v2)

e_37 =Entry(fr1_0, width=10)
e_37.grid(column=3, row=7)
v3 = 1/ float(e_36.get())
e_37.insert(0, v3)

# строка 8
Lb_0= Label(fr1_0, text="Нагруженность системы", fg ='red', font='bold') 
Lb_0.grid(column=0, row=8, columnspan=3)

# строка 9
Lb_19= Label(fr1_0, text="Показатель нагруженности ro=")  
Lb_19.grid(column=0, row=9)  

e_19 =Entry(fr1_0, width=10, fg ='blue')
e_19.grid(column=1, row=9)
v1 = float(e_13.get())/ float(e_17.get())
e_19.insert(0, v1)

e_29 =Entry(fr1_0, width=10, fg ='green')
e_29.grid(column=2, row=9)
v2 =  float(e_23.get())/ float(e_27.get())
e_29.insert(0, v2)

e_39 =Entry(fr1_0, width=10)
e_39.grid(column=3, row=9)
v3 =  float(e_33.get())/ float(e_37.get())
e_39.insert(0, v3)

# строка 10
Lb_110= Label(fr1_0, text='Количество касс (шт) n=')  
Lb_110.grid(column=0, row=10)  

e_110 =Entry(fr1_0, width=10)
e_110.grid(column=1, row=10)
e_110.insert(0, 5)

# строка 11
Lb_111= Label(fr1_0, text='Максимальная длина очереди \n (клиенты)  m=')  
Lb_111.grid(column=0, row=11)  

e_111 =Entry(fr1_0, width=10)
e_111.grid(column=1, row=11)
e_111.insert(0, 10)

# строка 12
button4 = Button(fr1_0, text="Сформировать",  width=20, command=edit_val_row)
button4.grid(column=2, row=12)

# строка 13
Lb_130= Label(fr1_0, text="Исходные данные", fg ='red') 
Lb_130.grid(column=0, row=13, columnspan=20)

root.mainloop()
