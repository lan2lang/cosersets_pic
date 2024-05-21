import os
import pyheif
from PIL import Image

def convert_png_to_heif(source_dir, target_dir):
    # 确保目标目录存在
    os.makedirs(target_dir, exist_ok=True)

    # 获取源目录中所有文件
    files = os.listdir(source_dir)

    # 遍历所有文件
    for file in files:
        # 检查文件扩展名是否为.png
        if file.lower().endswith('.png'):
            # 构建文件路径
            source_path = os.path.join(source_dir, file)
            target_path = os.path.join(target_dir, os.path.splitext(file)[0] + '.heif')

            # 打开PNG图像并保存为HEIF
            img = Image.open(source_path)
            heif_img = pyheif.read(source_path)
            heif_img.save(target_path, format='heif')
            print(f"Converted {source_path} to {target_path}")

    print("Conversion complete.")

# 指定源目录和目标目录
source_dir = '/path/to/source/directory'
target_dir = '/path/to/target/directory'

convert_png_to_heif(source_dir, target_dir)
