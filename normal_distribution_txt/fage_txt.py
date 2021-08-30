import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import xlrd

# import time

URL = "common_network_slave_data_callback():" #需要计算的关键字
FILE = "3.txt" #分析的文件
YNAME = "权重"
XNAME = "时间（us）"

def get_txt_value(filename):  # j代表列0是第一列,j,filename 为文件名
    
    out_filename = 'programing.txt'
    with open (out_filename,'w') as file_object:
        with open(filename, "r") as f:
            for line in f.readlines():
                if line.find(URL) >= 0:
                    line = line.split(URL)[1]
                    #line = line.strip('\n')
                    #numt = int(line)
                    #print(line)
                    file_object.write(line+"\n")

    data = np.loadtxt(out_filename)  # 将文件中数据加载到data数组里
    arr_mean = np.mean(data)
    arr_std = np.std(data, ddof=1)
    return data, arr_mean, arr_std  # 函数返回数据,均值,标准差

class higram:

    def __init__(self, dimension, filename, mu, sigma, data,num_bins):
        self.dimension = dimension
        self.filename = filename
        self.mu = mu
        self.sigma = sigma
        self.data = data
        self.num_bins = num_bins

    def creatchart(self):
        # 设置matplotlib正常显示中文和负号
        matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文
        matplotlib.rcParams['axes.unicode_minus'] = False  # 正常显示负号

        def norm_pdf(x, mu, sigma):
            pdf = np.exp(-((x - mu) ** 2) / (2 * sigma ** 2)) / (sigma * np.sqrt(2 * np.pi))  # 正态分布函数
            return pdf

        n, bins, patches = plt.hist(self.data, self.num_bins, density=1, facecolor="blue", edgecolor="black",
                                    alpha=0.5)  # facecolor直方填充颜色edgecolor直方边框颜色

        # FFC0CB Pink 粉红 #E6E6FA Lavender 淡紫色/熏衣草淡紫

        y = norm_pdf(bins, mu, sigma)  # 概率分布图
        # print(y)

        plt.plot(bins, y, 'r--', linestyle='-')  # 概率分布图"_"代表实线,"r--"代表红色

        plt.xlabel(XNAME)  # 显示纵轴标签

        plt.ylabel(YNAME)  # 显示图标题

        plt.title(self.dimension + "_正态分布图")
        plt.subplots_adjust(left=0.10)  # 把画的图从左边0.10(整个为1)处开始, 要不把y轴的label显示不出来

        plt.show()


if __name__ == "__main__":
    # s=time.time()
    data = get_txt_value(FILE)[0]  # 数据

    mu = get_txt_value(FILE)[1]  # 均值
    sigma = get_txt_value(FILE)[2]  # 标准差
    print(data)
    print(mu)
    print(sigma)
    Dimension = "网络传输时间-正态分布图"
    
    print("result:",data)
    print("mean:",mu)
    print("std:",sigma)
    print("Dimension:",Dimension)
    h = higram(Dimension, FILE, mu, sigma, data,  num_bins=100)
    h.creatchart()
    
