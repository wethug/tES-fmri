# 水膜成像
import matplotlib
import matplotlib.pyplot as plt

bar_width = 0.15
y1 = [809.09, 877.94, 867.09, 883.01, 932.71]
y2 = [743.34, 805.86, 808.02, 842.59, 899.36]
y3 = [742.76, 806.66, 806.97, 843.01, 897.21]
y4 = [745.04, 807.94, 806.09, 841.32, 900.14]
y5 = [745.32, 808.32, 809.76, 844.23, 897.98]
y6 = [745.76, 805.89, 804.98, 845.72, 899.34]
rate1 = [8.13, 8.21, 6.81, 4.58, 3.58]
rate2 = [8.20, 8.12, 6.93, 4.53, 3.81]
rate3 = [7.92, 7.97, 7.04, 4.72, 3.49]
rate4 = [7.88, 7.93, 6.61, 4.39, 3.72]
rate5 = [7.83, 8.21, 7.16, 4.22, 3.58]
x_text = ['slice1', 'slice2', 'slice3', 'slice4', 'slice5']
x_list = range(len(x_text))

# 定义中文格式
font = {'family': 'MicroSoft Yahei', 'size': 24}
matplotlib.rc('font', **font)

_, ax1 = plt.subplots(figsize=(15.84, 10.8))
ax2 = ax1.twinx()

b1 = ax1.bar([x - 2.5 * bar_width for x in x_list], y1, bar_width)
b2 = ax1.bar([x - 1.5 * bar_width for x in x_list], y2, bar_width)
b3 = ax1.bar([x - 0.5 * bar_width for x in x_list], y3, bar_width)
b4 = ax1.bar([x + 0.5 * bar_width for x in x_list], y4, bar_width)
b5 = ax1.bar([x + 1.5 * bar_width for x in x_list], y5, bar_width)
b6 = ax1.bar([x + 2.5 * bar_width for x in x_list], y5, bar_width)
l1, = ax2.plot(x_list, rate1)
l2, = ax2.plot(x_list, rate2)
l3, = ax2.plot(x_list, rate3)
l4, = ax2.plot(x_list, rate4)
l5, = ax2.plot(x_list, rate5)

label_font = {'family': 'MicroSoft Yahei', 'size': 26}
plt.xticks(range(len(x_list)), x_text)
plt.xlabel('水膜成像层数', font=label_font)
ax1.set_ylabel('SNR', font=label_font)
ax1.set_ylim(700, 950)
ax2.set_ylabel('相比于对照组下降占比/%', font=label_font)

legend_font = {'family': 'MicroSoft Yahei', 'size': 15}
plt.title('不同刺激电流对水膜成像的影响')
plt.legend(handles=[b1, b2, b3, b4, b5, b6, l1, l2, l3, l4, l5],
           labels=['对照组', 'A组', 'B组', 'C组', 'D组', 'E组', 'line1', 'line2', 'line3', 'line4', 'line5'],
           prop=legend_font, loc=2, bbox_to_anchor=(1.08, 1.0), borderaxespad=0.)

plt.show()
