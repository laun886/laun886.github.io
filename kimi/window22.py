# main.py
import tkinter as tk
#from file_handler import choose_file  # 导入另一个文件中定义的choose_file函数
from kimiapi import get_kimi_response
def main():
    # 创建Tkinter窗口的根实例
    root = tk.Tk()
    
    # 设置窗口标题
    root.title("文件大小分析器")

    # 获取屏幕尺寸，用于后续设置窗口大小和位置
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # 根据屏幕尺寸设置窗口大小为屏幕的四分之一
    window_width = screen_width // 4
    window_height = screen_height // 4

    # 计算窗口位置参数，使窗口居中显示
    x_pos = (screen_width - window_width) // 2
    y_pos = (screen_height - window_height) // 2

    # 使用geometry方法设置窗口的初始大小和位置
    root.geometry(f"{window_width}x{window_height}+{x_pos}+{y_pos}")
    # 创建一个按钮，点击时会触发choose_file函数
    # 使用lambda表达式传递root作为参数给choose_file函数
    #root.choose_button = tk.Button(root, text="选择文件", command=lambda: choose_file(root))
    #root.choose_button.pack(pady=20)
 
    # 创建一个多行文本框，用于显示文件大小
    # 这里将文本框的高度设置为4行
    root.file_size_text = tk.Text(root, width=50, height=4, font=("Arial", 14))
    # 使文本框在垂直方向上可以滚动
    scroll = tk.Scrollbar(root, command=root.file_size_text.yview)
    root.file_size_text.config(yscrollcommand=scroll.set)
    
    # 将滚动条与文本框关联
    scroll.pack(side=tk.RIGHT, fill='y')  # 使用字符串 'y' 而不是 tk.y
    root.file_size_text.pack(pady=20)

    # 创建一个按钮，点击时获取Kimi的回答并显示
    get_response_button = tk.Button(root, text="获取Kimi的回答", command=lambda: update_text_box("你好，请问你有什么功能"))
    get_response_button.pack(pady=20)

    # 进入Tkinter的事件循环，显示窗口并等待用户操作
    root.mainloop()
    def update_text_box(user_message):
        # 获取Kimi的回答
        response = get_kimi_response(user_message)
        # 将回答更新到文本框中
        root.file_size_text.delete(1.0, tk.END)  # 清除文本框中的旧内容
        root.file_size_text.insert(tk.END, response + "\n")  # 在文本框末尾插入回答
        
# 检查这个脚本是否作为主程序运行


if __name__ == "__main__":
    main()  # 如果是，则调用main函数启动程序