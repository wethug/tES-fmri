# 水膜成像
import matplotlib
import matplotlib.pyplot as plt

bar_width = 0.2
y1 = [809.09, 877.94, 867.09, 883.01, 932.71]
y2 = [761.59, 827.83, 840.8, 858.43, 914.81]
y3 = [748.34, 809.32, 832.77, 853.66, 911.58]
rate1 = [5.87, 5.71, 3.03, 2.78, 1.92]
rate2 = [7.51, 7.82, 3.96, 3.32, 2.27]
x_text = ['slice1', 'slice2', 'slice3', 'slice4', 'slice5']
x_list = range(len(x_text))

# 定义中文格式
font = {'family': 'MicroSoft Yahei', 'size': 24}
matplotlib.rc('font', **font)

_, ax1 = plt.subplots(figsize=(14.4, 10.8))
ax2 = ax1.twinx()

b1 = ax1.bar([x - bar_width for x in x_list], y1, bar_width, color='red')
b2 = ax1.bar(x_list, y2, bar_width, color='blue')
b3 = ax1.bar([x + bar_width for x in x_list], y3, bar_width, color='green')
l1, = ax2.plot(x_list, rate1, color='pink')
l2, = ax2.plot(x_list, rate2, color='purple')

label_font = {'family': 'MicroSoft Yahei', 'size': 26}
plt.xticks(range(len(x_list)), x_text)
plt.xlabel('水膜成像层数', font=label_font)
ax1.set_ylabel('SNR', font=label_font)
ax1.set_ylim(700, 1000)
ax2.set_ylabel('相比于对照组下降占比/%', font=label_font)

legend_font = {'family': 'MicroSoft Yahei', 'size': 16}
plt.title('核磁兼容套件对水膜成像的影响')
plt.legend(handles=[b1, b2, b3, l1, l2], labels=['对照组', 'A组', 'B组', 'line1', 'line2'], prop=legend_font)

plt.show()
