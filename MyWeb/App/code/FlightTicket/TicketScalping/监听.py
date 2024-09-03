import smtplib
import sys
from email.message import Message
from pynput import mouse
import time


def sent_email(title, content):
    smtpserver = 'smtp.gmail.com'
    username = 'legendtravel004@gmail.com'
    password = 'duooevejgywtaoka'
    from_addr = 'legendtravel004@gmail.com'
    # toAddr = ['legend.ticketing@gmail.com']
    toAddr = ['651748264@qq.com']
    # ccAddr = ['zhangzhuan516@gmail.com', 'legendtravel006@gmail.com', 'legend.ticking@gmail.com']
    # ccAddr = ['zhangzhuan516@gmail.com', 'legend.ticking@gmail.com', '']
    ccAddr = ['zhangzhuan516@gmail.com']
    message = Message()
    message['Subject'] = f'my computer：{title}'  # 邮件标题
    message['From'] = from_addr
    message['To'] = ','.join(toAddr)
    message['Cc'] = ','.join(ccAddr)

    message.set_payload(content)  # 邮件正文
    msg = message.as_string().encode('utf-8')

    sm = smtplib.SMTP(smtpserver, port=587, timeout=20)
    sm.set_debuglevel(1)  # 开启debug模式
    sm.ehlo()
    sm.starttls()  # 使用安全连接
    sm.ehlo()
    sm.login(username, password)
    sm.sendmail(from_addr, (toAddr + ccAddr), msg)
    time.sleep(2)  # 避免邮件没有发送完成就调用了quit()
    sm.quit()


# 鼠标点击事件处理程序
def on_click(x, y, button, pressed):
    title = "computer clicked"
    content = f"computer clicked {x}, {y}"
    # print(content)

    if pressed:

        if x < 5 and y < 5:
            sys.exit()
        sent_email(title, content)
        time.sleep(15)  # 等待5秒
        return True  # 继续监听


# 监听鼠标点击事件
with mouse.Listener(on_click=on_click) as listener:
    listener.join()
