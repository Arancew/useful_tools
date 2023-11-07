
'''
老校区
one=2000
x = 2050  # x坐标
y = 1700 # y坐标
新校区
one=2300
x = 1050  # x坐标
y = 2150 # y坐标
'''

tiff_file = r'D:\code\uav_ponit\Position_correction\data\mapbox.tif'
import rasterio
import pickle
with rasterio.open(tiff_file) as src:
    transform = src.transform

# 将transform参数保存到文件
transform_file = "transform_data.pkl"
with open(transform_file, "wb") as file:
    pickle.dump(transform, file)

# 在需要时加载transform参数
with open(transform_file, "rb") as file:
    loaded_transform = pickle.load(file)

# 使用加载的transform参数计算经纬度坐标
lon, lat = loaded_transform * (1, 1)  # 例如，使用 (j, i) 像素坐标
print(f"经度: {lon}, 纬度: {lat}")