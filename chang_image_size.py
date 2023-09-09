from PIL import Image
import os

# 指定输入文件夹和输出文件夹
input_folder = r'C:\Users\49470\Desktop\code\py\遥感地图直接匹配\data\uav_image'
output_folder = r'C:\Users\49470\Desktop\code\py\遥感地图直接匹配\data\uav_image_low_size'

# 确保输出文件夹存在，如果不存在则创建它
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 指定目标大小
target_size = (318, 318)

# 遍历输入文件夹中的所有文件
for filename in os.listdir(input_folder):
    # 检查文件是否是图片文件
    if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):
        # 打开图片
        with Image.open(os.path.join(input_folder, filename)) as img:
            # 调整大小
            img = img.resize(target_size, Image.ANTIALIAS)

            # 保存到输出文件夹
            output_path = os.path.join(output_folder, filename)
            img.save(output_path)

print("图片已调整大小并保存到输出文件夹。")
