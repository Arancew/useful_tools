import rasterio

# 打开TIF图像文件
'''
读取一张tif地图，通过像素坐标来获取对应的经纬度信息。
'''
class read_tid:
    def __init__(self,path):
        self.tif_path = path
        self.src=rasterio.open(tif_path)
    def get_locate(self,x,y):
        lon, lat = src.xy(x, y)
        return lon,lat
