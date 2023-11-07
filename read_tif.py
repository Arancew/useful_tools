import pickle

import rasterio

# 打开TIF图像文件
'''
读取一张tif地图，通过像素坐标来获取对应的经纬度信息。
'''
class read_tid:
    def __init__(self,path):
        with open(path, "rb") as file:
            self.transform= pickle.load(file)
    def get_locate(self,x,y):
        lon, lat = self.transform*(x, y)
        return lon/1e5,lat/1e5
