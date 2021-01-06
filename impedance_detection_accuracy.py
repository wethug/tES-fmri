# 阻抗检测精度
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# 负载/kΩ
x_list = ["1", "1.5", "2", "3", "3.6", "4.3", "5.1", "6.2", "7.5", "8.2",
          "9.1", "10", "11", "12", "13", "15", "16", "18", "20", "24"]
# 误差/%
y_list = [8, 7.33, 5, 1, 0, 0, 0.19, 0.97, 0.67, 0.61,
          0.44, 1.3, 1.45, 2.5, 2.69, 1.93, 3.19, 5.67, 7, 8.54]

line1 = [1] * (len(x_list) + 2)
line5 = [5] * (len(x_list) + 2)

# 定义中文格式
font = {'family': 'MicroSoft Yahei', 'size': 10}
matplotlib.rc('font', **font)

index = range(len(x_list))
line_index = range(-1, len(x_list) + 1)
plt.bar(index, y_list)
l1, = plt.plot(line_index, line1, 'k--')
l5, = plt.plot(line_index, line5, 'r--')

ax = plt.gca()

plt.xticks(index, x_list)
plt.xlabel("负载/kΩ")
plt.xlim(-0.75, index[-1] + 0.75)

plt.ylabel("误差/%")
plt.ylim(0, 10.5)
y_major_locator = plt.MultipleLocator(1)
ax.yaxis.set_major_locator(y_major_locator)
ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f'))

plt.title("阻抗检测误差")
plt.legend(handles=[l1, l5], labels=['误差1%', '误差5%'], prop=font)

plt.show()
