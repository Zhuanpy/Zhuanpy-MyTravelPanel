import tkinter as tk
from Visa_Gui import get_input


def create_table():
    # 这里可以编写创建表格的代码
    pass


def show_passport_window():
    passport_window = tk.Toplevel(root)
    passport_window.title("中国护照更换")
    passport_window.geometry("500x200")

    def generate_table():
        name = name_entry.get()
        order = order_entry.get()

        get_input(name, order)
        print("姓名：", name)
        print("订单号：", order)

        # 这里可以编写生成表格的代码

    name_label = tk.Label(passport_window, text="姓名：")
    name_label.pack()
    name_entry = tk.Entry(passport_window)
    name_entry.pack()

    order_label = tk.Label(passport_window, text="订单号：")
    order_label.pack()
    order_entry = tk.Entry(passport_window)
    order_entry.pack()

    generate_button = tk.Button(passport_window, text="生成表格", command=generate_table)
    generate_button.pack()


# 创建主窗口
root = tk.Tk()
root.geometry("300x250")
root.resizable(False, False)  # 禁止改变窗口大小
root.title("签证表格处理")

# 创建按钮
visa_button = tk.Button(root, text="马来西亚签证", padx=10, pady=5, command=create_table)
visa_button.grid(row=0, column=0, padx=10, pady=10)

passport_button = tk.Button(root, text="中国护照更换", padx=10, pady=5, command=show_passport_window)
passport_button.grid(row=1, column=0, padx=10, pady=10)

# 将窗口中心设置为按钮的中心
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

# 进入消息循环
root.mainloop()
