from PIL import Image, ImageEnhance

# 打开图像文件
image = Image.open('tmp.png')

# 创建一个对比度增强对象
enhancer = ImageEnhance.Contrast(image)

# 增加对比度（1.0表示原始对比度，大于1.0表示增加对比度，小于1.0表示减小对比度）
contrast_factor = 1.5  # 你可以根据需要调整这个值
enhanced_image = enhancer.enhance(contrast_factor)

# 保存增加对比度后的图像
enhanced_image.save('enhanced_image.png')

# 关闭原始图像
image.close()
