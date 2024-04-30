import tkinter as tk


def convertfunction(root):
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
