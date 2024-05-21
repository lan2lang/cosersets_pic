import os

from PIL import Image

# 指定源目录和目标目录
source_dir = 'G:\爬虫\code\Demo\cosersets\download\kaya萱_887'
target_dir = 'G:\爬虫\code\Demo\cosersets\download\kaya萱_887_PNG'

# 确保目标目录存在
os.makedirs(target_dir, exist_ok=True)

# 获取源目录中所有文件
files = os.listdir(source_dir)

# 遍历所有文件
for file in files:
    # 检查文件扩展名是否为.webp
    if file.lower().endswith('.webp'):
        # 构建文件路径
        source_path = os.path.join(source_dir, file)
        target_path = os.path.join(target_dir, os.path.splitext(file)[0] + '.png')

        # 打开WebP图像并保存为PNG
        img = Image.open(source_path)
        img.save(target_path, 'PNG')
        print(f"Converted {source_path} to {target_path}")

print("Conversion complete.")
