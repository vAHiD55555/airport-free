import os

# 获取当前工作目录
current_directory = os.getcwd()

# 列出当前目录下所有文件和文件夹
entries = os.listdir(current_directory)

# 过滤出所有以.txt结尾的文件
txt_files = [entry for entry in entries if entry.endswith('.txt')]

# 打印所有.txt文件的路径，只在文件名前加上斜杠 '/'
for i,txt_file in enumerate(txt_files,start=1):
    #print(f'<td align="center"><a href="https://github.com/xiaoji235/airport-free/blob/main/v2ray/{txt_file}">v2ray 机场{i}</a></td>')
    result = f'<td align="center"><a href="https://github.com/xiaoji235/airport-free/blob/main/v2ray/{txt_file}">v2ray 机场{i}</a></td>'
    print(result)


