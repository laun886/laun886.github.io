# main.py
import tkinter as tk
from kimiapi import get_kimi_response  # 导入get_kimi_response函数


 
# 定义 main 函数
def main():
    global root  # 如果你在函数外部使用了root，需要声明它为全局变量
    root = tk.Tk()
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


    root.title("与Kimi对话")
    user_input_text = tk.Text(root, width=50, height=3)
    user_input_text.pack()

    # 创建一个按钮，点击时发送用户输入的问题
    send_button = tk.Button(root, text="发送问题", command=send_message)
    send_button.pack()
    # 创建一个多行文本框，用于显示Kimi的回答
    root.text_box = tk.Text(root, width=50, height=10)
    root.text_box.pack()

    # 定义按钮点击时的动作
    def send_message():
        # 读取用户输入框的内容
        user_content = user_input_text.get("1.0", tk.END)
        # 清空用户输入框
        user_input_text.delete("1.0", tk.END)
        # 获取Kimi的回答
        response = get_kimi_response(user_content)
        # 将回答显示在文本框中
        response_text.insert(tk.END, response)

    root.mainloop()

# 定义更新文本框的函数
def update_text_box(response):
    root.text_box.delete(1.0, tk.END)  # 清除文本框中的旧内容
    root.text_box.insert(tk.END, response)  # 在文本框末尾插入新的回答

if __name__ == "__main__":
    main()