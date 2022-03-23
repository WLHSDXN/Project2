# AutomatedScript

这是一个自动化脚本的程序，可以处理一些重复的事情。如果你有更好的意见，可以提交PR来丰富这个Project2

## MessageBombing

这个程序参考了[用python编程实现消息轰炸](https://www.xiaohongshu.com/discovery/item/62387b1d000000002103e44e?share_from_user_hidden=true)和[python控制鼠标和键盘](https://www.cnblogs.com/to-red/p/9916668.html) 。

下面摘录了一些教程：

### PyMouse的用法

```python
myMouse = PyMouse()

#获取当前的鼠标位置
nowP = myMouse.position()
print(nowP)

#鼠标移动到坐标(x,y)处
myMouse.move(x,y)

#鼠标点击，x,y是坐标位置 button 1表示左键，2表示点击右键 n是点击次数，默认是1次，2表示双击
myMouse.click(x,y,button,n)

#最简单的用法
myMouse.click(x,y)
```

### PyKeyboard的用法

#### 键盘

```python
k.type_string(‘Hello, World!’) #模拟键盘输入字符串 
k.press_key(‘H’) #模拟键盘按H键 
k.release_key(‘H’) #模拟键盘松开H键 
k.tap_key(“H”) #模拟点击H键 
k.tap_key(‘H’,n=2,interval=5) #模拟点击H键，2次，每次间隔5秒 
k.tap_key(k.function_keys[5]) #点击功能键F5 
k.tap_key(k.numpad_keys[5],3) #点击小键盘5,3次
```

#### 组合键

```python
#例如同时按alt+tab键盘 
k.press_key(k.alt_key) #按住alt键 
k.tap_key(k.tab_key) #点击tab键 

k.tap_key(k.enter_key) #点击回车键

k.release_key(k.alt_key) #松开alt键
```

