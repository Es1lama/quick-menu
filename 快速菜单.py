import os
import sys
import pathlib
import tkinter
# 存储路径的字典结构，键是连续的数字，值是对应的路径
paths_dict = {}

def write_path_to_txt():
    with open('paths.txt', 'w') as file:
        for num, path in sorted(paths_dict.items()):
            file.write(f'{num}: {path}\n')

def read_and_open_path(num):
    if num in paths_dict:
        path = paths_dict[num]
        if os.path.isdir(path):
            os.startfile(path)  # 对于Windows系统
        elif os.path.isfile(path):
            os.system(f'start {path}')  # 对于Windows系统
        else:
            print(f"路径无效：{path}")
        sys.exit(0)  # 打开地址后自动退出程序
    else:
        print(f"未找到与数字 {num} 对应的路径。")

def delete_path(num):
    if num in paths_dict:
        del paths_dict[num]
        write_path_to_txt()
    else:
        print(f"未找到与数字 {num} 对应的路径。")

def display_menu():
    global paths_dict
    print("请选择一个操作：")
    print("0. 退出程序")
    print("1. 添加地址")
    print("2. 删除地址")
    for num, path in sorted(paths_dict.items(), key=lambda x: int(x[0])):
        print(f"{num + 2}. 打开已存地址: {os.path.basename(path)}")
    choice = input("请输入您的选择（数字）：")

    if choice == '0':
        sys.exit(0)
    elif choice == '1':
        path = input("请输入一个文件夹或程序地址：")
        max_num = max(paths_dict.keys()) + 1 if paths_dict else 1
        paths_dict[max_num] = path
        write_path_to_txt()
    elif choice == '2':
        num = int(input("请输入要删除的地址序号（数字）："))
        if num >= 3 and num - 2 in paths_dict:
            delete_path(num - 2)
        else:
            print("无效的选择，请重新输入。")
    elif choice.isdigit() and int(choice) >= 3 and int(choice) - 2 in paths_dict:
        read_and_open_path(int(choice) - 2)
    else:
        print("无效的选择，请重新输入。")

def load_saved_paths():
    if os.path.exists('paths.txt'):
        with open('paths.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                parts = line.strip().split(': ')
                # 检查是否有至少两个部分（数字和路径）
                if len(parts) >= 2:
                    paths_dict[int(parts[0])] = parts[1].strip()

def main():
    load_saved_paths()
    while True:
        display_menu()

if __name__ == "__main__":
    main()