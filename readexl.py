import xlrd
from matplotlib import pyplot as plt
from datetime import datetime

testdata = xlrd.open_workbook('2017年收支总结.xlsx')
table = testdata.sheets()[0]
#a = table.cell(2,2).value
rows = table.nrows
cols = table.ncols
#逐行打印数据
# for i in range(rows):
#     print(table.row_values(i))
print(table.col_values(3))
l =[]
rent = []
a = table.col_values(1)
b = table.col_values(0)
c = table.col_values(9)
print(b)
for i in a:
    if type(i) == float and i < 100000:
        l.append(i)
for i in c:
    if type(i) == float and i < 20000:
        rent.append(i)
# for i in b[2:13]:
#     cut_date = datetime.strptime(str(i), "%m")
#     dates.append(cut_date)
print(l)
print(rent)
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(l ,c='red')
plt.plot(rent ,c='blue')

plt.title('123', fontsize=24)
plt.xlabel(' ', fontsize=16)
# plt.autofmt_xdate()
plt.ylabel(' ', fontsize=10)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()