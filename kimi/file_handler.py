# 1.py
import tkinter as tk

# 导入os模块，用于获取文件大小
import os
# 从tkinter模块导入filedialog，用于打开文件选择对话框
from tkinter import Tk, filedialog

# 定义choose_file函数，它接收一个参数root，代表Tkinter窗口的根实例
def choose_file(root):
    # 使用filedialog.askopenfilename函数弹出文件选择对话框，让用户选择文件
    # title参数设置对话框的标题
    # filetypes参数定义可选择的文件类型，这里包括文本文件(.txt)和Excel文件(.xlsx)
    file_path = filedialog.askopenfilename(
        title="请选择",
        filetypes=(("txt", "*.txt"), ("Excel", "*.xlsx"), ("所有文件", "*.*"))
    )
    
    # 如果用户选择了文件（即file_path不为空字符串）
    if file_path:
        # 使用os.path.getsize函数获取用户选择的文件的大小，单位是字节
        file_size = os.path.getsize(file_path)
        

            # 将文件大小更新到多行文本框中
            # 插入文本到文本框的末尾
        #root.file_size_text.delete(1.0, tk.END)  # 清除文本框中的旧内容
        root.file_size_text.insert(tk.END, f"文件大小: {file_size} 字节\n")
        
        
        
        # 更新root窗口中的file_size_label标签，显示文件大小
        # 这里使用root.file_size_label.config来配置标签的文本内容
        # f-string格式化文本，显示文件大小
        #root.file_size_label.config(text=f"文件大小为: {file_size} 字节")
        
        # 调用update方法刷新标签的显示，确保新的内容能够立即展示出来
        #root.file_size_label.update()