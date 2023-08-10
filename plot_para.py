import scipy.io
from mpl_toolkits.axes_grid1 import host_subplot
from mpl_toolkits import axisartist
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt


############################################ para ########################################
mat = scipy.io.loadmat('data\BV18_SimData_25Deg_MaxMinCell_LoSoC_Plus_CLTC.mat') 
mat = mat["SimData_BV18"]

# 输入  电流I、端电压Ucell、温度t
time = mat[:,0]
I = mat[:,1]   
Ucell_max = mat[:,2]
Ucell_min = mat[:,3]
t_avrg = mat[:,4]
t_min = mat[:,5]


# 输出   
SOC_pack = mat[:,6]
SOC_max = mat[:,7]
SOC_min = mat[:,8]

OCV_max = mat[:,9]
OCV_min = mat[:,10]



############################################ plot 多坐标轴曲线 ########################################
"""
host就是原始右边的y轴；
par1是新添加的与host对称的左边y轴；
par2、par3可以自己设置位置（loc="left"或“right”）和偏置长度（offset:正值应该是往右偏，负值是往左偏）
"""

host = host_subplot(111, axes_class=axisartist.Axes) 

par1 = host.twinx()
par2 = host.twinx() 

par2.axis["right"] = par2.new_fixed_axis(loc="right", offset=(60, 0))

par1.axis["right"].toggle(all=True)
par2.axis["right"].toggle(all=True)

p1, = host.plot(time, t_avrg)    # I、Ucell_max、Ucell_min、t_avrg、t_min
p2, = par1.plot(time, SOC_min)
p3, = par2.plot(time, OCV_min)

host.set_xlabel("time")
host.set_ylabel("t_avrg")
par1.set_ylabel("SOC_min")
par2.set_ylabel("OCV_min")

host.legend()
host.axis["left"].label.set_color(p1.get_color())
par1.axis["right"].label.set_color(p2.get_color())
par2.axis["right"].label.set_color(p3.get_color())




############################################ plot 竖线 ########################################
x_index_SOC = []
SOC_min_list = SOC_min.tolist()
for i,value in enumerate(SOC_min_list):
    if value == 30:
        x_index_SOC.append(i)
x_SOC_min = time[x_index_SOC]
plt.vlines(x_SOC_min, 20, 30, linestyles='dashed', colors='red', zorder=1)


plt.show()
#plt.savefig('saved/t_avrg/12.png', dpi=600, bbox_inches='tight') 





