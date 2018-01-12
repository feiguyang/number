import xlrd
from matplotlib import pyplot as plt
from datetime import datetime
import pygal

testdata = xlrd.open_workbook('2017年收支总结.xlsx')
table = testdata.sheets()[0]

l =[]
rent = []
balance = []
a = table.col_values(1)
date = table.col_values(0)[2:14]
c = table.col_values(9)
d = table.col_values(10)

for i in a:
    if type(i) == float and i < 100000:
        l.append(i)
for i in c:
    if type(i) == float and i < 60000:
        rent.append(i)
for i in d:
    if type(i) == float and i <40000:
        balance.append(i)
print(l)
print(date)

hist = pygal.Line()

hist.title = "123"
hist.x_labels = date
hist.y_title = "元"
hist.x_title = "月"
hist.add('总收入', l)
hist.add('总支出', rent)
hist.render_to_file('123.svg')

hist1 = pygal.StackedBar()

hist1.title = "123"
hist1.x_labels = date
hist1.y_title = "元"
hist1.x_title = "月"
hist1.add('总收入', balance)
hist1.add('总支出', rent)
hist1.render_to_file('111.svg')