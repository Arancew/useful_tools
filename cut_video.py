import re

import cv2
import os
import pandas as pd

# 视频文件的路径
video_path = r'D:\code\uav_ponit\data_process\data'
target_mp4=['DJI_0004.MP4']
# 创建保存帧的文件夹
output_folder = './frames'

def get_locate_by_frame(idx,file):
    print("idx={}".format(idx))
    # 读取文本文件
    with open(file, 'r',encoding='utf-8') as file:
        text = file.read()
    text_list=text.split("\n\n")

    text=text_list[idx-1]
    latitude = re.search(r'latitude: ([\d.]+)', text).group(1)
    longitude = re.search(r'longitude: ([\d.]+)', text).group(1)

    print("纬度:", latitude)
    print("经度:", longitude)
    return latitude,longitude
def change_siez_to_1080(image):
    # 获取原始图片的尺寸
    height, width, _ = image.shape

    # 计算截取的区域左上角和右下角坐标，以使其居中
    x = (width - 1080) // 2
    y = (height - 1080) // 2
    w = 1080
    h = 1080

    # 截取中心部分
    center_cropped = image[y:y + h, x:x + w]

    # 截取中心部分
    return  center_cropped

os.makedirs(output_folder, exist_ok=True)
# 打开视频文件
# 设置帧采样间隔（例如，每隔5帧保存一帧）
frame_interval = 20
image_name = 0
start_frame=211
file = {"image": [], "frame": [],'latitude':[],'longitude':[]}
for i in target_mp4:
    now_path=os.path.join(video_path,i)
    cap = cv2.VideoCapture(now_path)
    frame_count = 0
    # 检查视频是否成功打开
    if not cap.isOpened():
        print("无法打开视频文件")
        exit()
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame_count += 1
        if image_name==0:
            image_name+=1
            file["image"].append("{:03d}".format(image_name))
            file["frame"].append(frame_count)
            latitude,longitude=get_locate_by_frame(frame_count,os.path.join(video_path,i.split('.')[0]+".SRT"))
            file["latitude"].append(latitude)
            file["longitude"].append(longitude)
            frame_filename = os.path.join(output_folder, f'{frame_count:03d}.jpg')
            # 保存帧为图片
            # frame=change_siez_to_1080(frame)
            cv2.imwrite(frame_filename, frame)
        # 仅保留每隔frame_interval帧
        if frame_count % frame_interval == 0:
            # 生成文件名，例如：frame_001.jpg, frame_002.jpg, ...
            image_name+=1
            print(image_name)
            file["image"].append("{:03d}".format(image_name))
            file["frame"].append(frame_count)
            latitude,longitude=get_locate_by_frame(frame_count,os.path.join(video_path,i.split('.')[0]+".SRT"))
            file["latitude"].append(latitude)
            file["longitude"].append(longitude)
            frame_filename = os.path.join(output_folder, f'{frame_count:03d}.jpg')
            # 保存帧为图片
            # frame = change_siez_to_1080(frame)
            cv2.imwrite(frame_filename, frame)

# 释放视频对象和关闭输出文件夹
df=pd.DataFrame(file)
df.to_csv("uav_infos.csv",index=False)
cap.release()
cv2.destroyAllWindows()
