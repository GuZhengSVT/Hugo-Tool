import os

# 设置要处理的目录路径
directory = '/Users/username/Hugo/content/post'  # 请替换为您的实际路径

# 定义旧的和新的文本
old_prefix = 'old text'
new_prefix = 'new text'

# 遍历目录及其子目录下的所有文件
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith('.md'): # 遍历.md文件（Hugo文章）
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            # 替换文本
            new_content = content.replace(old_prefix, new_prefix)
            # 如果内容有变化，则写回文件
            if new_content != content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f'replaced: {file_path}')

