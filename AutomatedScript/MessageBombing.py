import time
from pynput import mouse, keyboard
time.sleep(5)#你有5秒的时间移动鼠标到想要的坐标

m_mouse = mouse.Controller() #创建鼠标
m_keyboard = keyboard.Controller() #创建键盘
# m_mouse.position = (1,1) #将鼠标移动到指定位置

m_mouse.click(mouse.Button.left) #鼠标左键
while (True):
    m_keyboard.type("发送了一条消息") #打字
    m_keyboard.press(keyboard.Key.enter) #enter
    m_keyboard.release(keyboard.Key.enter) #松开
    time.sleep(1)