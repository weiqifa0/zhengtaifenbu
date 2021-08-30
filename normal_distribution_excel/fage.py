import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import xlrd


# import time


def get_excel_value(j, filename):  # j代表列0是第一列,j,filename 为文件名
    row_list = []  # 建立空列表插入尺寸数据
    excel = xlrd.open_workbook(r"%s" % filename)
    sheet = excel.sheet_by_index(0)  #根据下标获取对应的sheet表
    #sheet = excel.sheet_by_name("Sheet1")  # 根据表名获取对应的sheet表
    # for  j in range(0,sheet.ncols):
    for i in range(0, sheet.nrows):  # 从表的第6行开始到
        if sheet.row_values(i, start_colx=j, end_colx=j + 1):  # 内循环
            row_list.append(sheet.row_values(i, start_colx=j, end_colx=j + 1)[0])  # 每次循环取一个单元格数据插入列表中
    arr_mean = np.mean(row_list)
    arr_std = np.std(row_list, ddof=1)

    return row_list, arr_mean, arr_std  # 函数返回数据,均值,标准差

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

        plt.xlabel("区间")  # 显示纵轴标签

        plt.ylabel("fage_v")  # 显示图标题

        plt.title(self.dimension + "_正态分布图")
        plt.subplots_adjust(left=0.10)  # 把画的图从左边0.10(整个为1)处开始, 要不把y轴的label显示不出来

        plt.show()


if __name__ == "__main__":
    # s=time.time()
    data = get_excel_value(0, "1.txt")[0]  # 数据
    mu = get_excel_value(0, "1.txt")[1]  # 均值
    sigma = get_excel_value(0, "1.txt")[2]  # 标准差
    Dimension = "fage"
    # e=time.time()
    # t=e-s
    # print(t)
    '''print("result:",data)
    print("mean:",mu)
    print("std:",sigma)
    print("Dimension:",Dimension)'''
    h = higram(Dimension, "ext.xls", mu, sigma, data,  num_bins=100)
    h.creatchart()
