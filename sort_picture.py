

import os

# 指定文件夹路径
folder_path = r'D:\code\py\尝试3-图片图片匹配\data\uav_image_low_size'

# 遍历文件夹中的文件
for filename in os.listdir(folder_path):
    # 检查文件名是否以数字开头且以.jpg结尾
    number = int(filename.split('.')[0])

    # 生成新的文件名，使用zfill函数将数字部分补齐到三位
    new_filename = str(number).zfill(3) + '.jpg'

    # 构建旧文件路径和新文件路径
    old_filepath = os.path.join(folder_path, filename)
    new_filepath = os.path.join(folder_path, new_filename)

    # 重命名文件
    os.rename(old_filepath, new_filepath)
