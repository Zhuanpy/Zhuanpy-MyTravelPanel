import tkinter as tk
from ButtonsName import *
from Visa.Malaysia.MalaysiavisaFile import *
from Visa.Korea.KoreavisaFun import fill_korea_visa_form, create_korea_visa_folder
from Visa.Janpan.japanvisa import japan_visa_copy_all_files
from tkinter import messagebox
from FlightTicket.ConvertFlight.ConvertFlightItinerary import translate_text


class MyVisa:

    @classmethod
    def fun01(cls):
        new_window = tk.Toplevel(root)
        new_window.title("PDF文件处理")
        new_window.geometry('300x100')

        label1 = tk.Label(new_window, text="文件路径:")
        label1.grid(row=0, column=0, padx=2, pady=5, sticky='w')

        entry1 = tk.Entry(new_window, width=30)
        entry1.grid(row=0, column=1, columnspan=2, padx=2, pady=5)  # , sticky='w'

        label2 = tk.Label(new_window, text="转化功能:")
        label2.grid(row=1, column=0, padx=2, pady=5, sticky='w')

        def pdf_merge_pdf():
            # 添加PDF合并功能的代码
            # 获取输入文件夹路径
            input_folder = entry1.get()

            # 使用PdfFileMerger合并PDF文件
            try:
                merger = MalaysiaVisa(input_folder)
                merger.merge_pdf()
                messagebox.showinfo("成功", "PDF文件合并完成！")

            except Exception as e:
                messagebox.showerror("错误", str(e))

        def jpg_convert_to_pdf():
            # 添加图片转化为PDF功能的代码
            # pass
            # 获取输入文件夹路径
            input_folder = entry1.get()

            try:
                merger = MalaysiaVisa(input_folder)
                merger.combine2Pdf()
                messagebox.showinfo("成功", "图片合成PDF完成！")

            except Exception as e:
                messagebox.showerror("错误", str(e))

        button1 = tk.Button(new_window, text="PDF合并", command=pdf_merge_pdf)
        button1.grid(row=1, column=1, padx=2, pady=5)
        #
        button2 = tk.Button(new_window, text="图片转化", command=jpg_convert_to_pdf)
        button2.grid(row=1, column=2, padx=2, pady=5)

    @classmethod
    def fun02(cls):

        new_window = tk.Toplevel(root)
        new_window.title("韩国签证文件处理")
        new_window.geometry('300x100')

        label1 = tk.Label(new_window, text="文件路径:")
        label1.grid(row=0, column=0, padx=2, pady=5, sticky='w')

        entry1 = tk.Entry(new_window, width=20)
        entry1.grid(row=0, column=1, columnspan=3, padx=2, pady=5)  # , sticky='w'

        """ 创建韩国签证  文件文件夹功能 """
        label2 = tk.Label(new_window, text="创建文件：")
        label2.grid(row=1, column=0, padx=2, pady=5, sticky='w')

        # todo add command function
        def create_folder():
            f = entry1.get()
            f = f.upper()
            create_korea_visa_folder(f)

        button2 = tk.Button(new_window, text="确认创建", command=create_folder)
        button2.grid(row=1, column=1)

        """ 生成韩国签证表格 """
        label3 = tk.Label(new_window, text="生成表格：")  # label 3  资料文件夹
        label3.grid(row=2, column=0, padx=2)

        # todo add command function
        def fill_form():
            f = entry1.get()
            f = f.upper()
            fill_korea_visa_form(f)

        button3 = tk.Button(new_window, text="确认生成", command=fill_form)
        button3.grid(row=2, column=1)

    @classmethod
    def fun03(cls):

        def convert_text():

            input_text = text_entry_a.get("1.0", "end-1c")

            selected_result = result_var.get()

            if selected_result == "中文行程":
                converted_text = translate_text(input_text, 'CN')

            elif selected_result == "英文行程":
                converted_text = translate_text(input_text, 'EN')

            else:
                converted_text = "Invalid result selection"

            text_output.delete("1.0", "end")
            text_output.insert("1.0", converted_text)

        master = tk.Toplevel(root)

        master.title("机票行程转化")

        label_a = tk.Label(master, text="输入行程")
        label_a.pack()

        text_frame_a = tk.Frame(master, padx=10, pady=5)
        text_frame_a.pack()

        text_entry_a = tk.Text(text_frame_a, height=8, width=65, wrap=tk.WORD)
        text_entry_a.pack()

        label_result = tk.Label(master, text="输出行程")
        label_result.pack()

        text_frame_output = tk.Frame(master, padx=10, pady=5)
        text_frame_output.pack()

        text_output = tk.Text(text_frame_output, height=18, width=65, wrap=tk.WORD, state=tk.NORMAL)
        text_output.pack()

        result_var = tk.StringVar()
        result_var.set("Result B")  # 默认选择结果B

        result_b_radio = tk.Radiobutton(master, text="中文行程", variable=result_var, value="中文行程")
        result_b_radio.pack()

        result_c_radio = tk.Radiobutton(master, text="英文行程", variable=result_var, value="英文行程")
        result_c_radio.pack()

        convert_button = tk.Button(master, text="  转 化  ", command=convert_text)
        convert_button.pack()

    @classmethod
    def fun04(cls):
        new_window = tk.Toplevel(root)
        new_window.title("日本签证处理")
        new_window.geometry('300x100')

        label1 = tk.Label(new_window, text="文件路径:")
        label1.grid(row=0, column=0, padx=2, pady=5, sticky='w')

        entry1 = tk.Entry(new_window, width=20)
        entry1.grid(row=0, column=1, columnspan=3, padx=2, pady=5)  # , sticky='w'

        """ 创建日本签证  文件文件夹功能 """
        label2 = tk.Label(new_window, text="创建文件：")
        label2.grid(row=1, column=0, padx=2, pady=5, sticky='w')

        def create_folder():
            f = entry1.get()
            f = f.upper()
            japan_visa_copy_all_files(f)

        button2 = tk.Button(new_window, text="确认创建", command=create_folder)
        button2.grid(row=1, column=1)

    @classmethod
    def fun05(cls):
        new_window = tk.Toplevel(root)
        new_window.title("日本签证文件处理")
        new_window.geometry('300x100')

    @classmethod
    def fun06(cls):
        new_window = tk.Toplevel(root)
        new_window.title("美国签证文件处理")
        new_window.geometry('300x100')

    @classmethod
    def fun07(cls):
        new_window = tk.Toplevel(root)
        new_window.title("澳洲签证文件处理")
        new_window.geometry('300x100')

    @classmethod
    def fun08(cls):
        new_window = tk.Toplevel(root)
        new_window.title("申根签证文件处理")
        new_window.geometry('300x100')

    @classmethod
    def fun09(cls):
        new_window = tk.Toplevel(root)
        new_window.title("申根签证文 件处理")
        new_window.geometry('300x100')


# 创建主窗口
root = tk.Tk()
root.title("工作面板")

# 创建按钮并布局
for i in range(3):

    k = i * 3

    for j in range(3):
        k1 = k + j
        button = tk.Button(root,
                           text=visa_buttons[k1][0],
                           command=eval(visa_buttons[k1][1]))
        button.grid(row=i, column=j, padx=10, pady=10)

# 启动主循环
root.mainloop()
