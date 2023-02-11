import time
import requests

import smtplib
from email.mime.text import MIMEText
from email.header import Header

import datetime
class Cjcx:
    def __init__(self,url,head,data):
        """
            url：请求的地址
            head：头文件
            data：携带参数
        """
        self.url = url
        self.head = head
        self.data = data

    def do(self):
        res = requests.post(url=self.url, headers=self.head, data=self.data)
        return res.text
class EmailOP:
    def __init__(self, host, port, user, password):
        """
        host：邮件服务器地址
        port：邮件服务器端口
        user：自己邮箱账户名
        password：自己邮箱账户的密码（注意是授权码，不是邮箱官网的登录密码）
        """
        self.user = user
        self.password = password
        self.smtp = smtplib.SMTP()  # 创建 SMTP 对象
        self.smtp.connect(host=host, port=port)  # 链接到服务器
        self.smtp.login(user=self.user, password=self.password)  # 登录自己邮箱账号

    def send(self, From, To, Subject, Context, to_addrs):
        """
        Context：邮件正文
        From：发送者昵称（随便取）
        To：接收者昵称（随便取）
        Subject：邮件主题
        to_addrs: 收件人邮箱地址
        """
        message = MIMEText(Context, 'plain', 'utf-8')
#         message['From'] = Header(From, 'utf-8')
        message['From'] = Header(From)
#         message['To'] = Header(To, 'utf-8')
        message['To'] = Header(To)
#         message['Subject'] = Header(Subject, 'utf-8')
        message['Subject'] = Header(Subject)
        self.smtp.sendmail(from_addr=self.user, to_addrs=to_addrs, msg=message.as_string())

#data https://yz.chsi.com.cn/apply/cjcx/t/xxxxx.dhtml xxxxx为目标院校代码，也就是准考证号前5位
url = "https://yz.chsi.com.cn/apply/cjcx/cjcx.do"
head1 = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Referer": "https://yz.chsi.com.cn/apply/cjcx/t/xxxxx.dhtml"
}
head2 = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0",
    "Referer": "https://yz.chsi.com.cn/apply/cjcx/t/xxxxx.dhtml"
}
data = {
    "xm": "姓名",
    "zjhm": "身份证号",
    "ksbh": "准考证号",
    "bkdwdm": "院校代码",
    "checkcode": ""
}
querytext = "无查询结果"
sendtext = "出成绩啦！点击查询https://yz.chsi.com.cn/apply/cjcx/t/xxxxx.dhtml。"
long = 3600 
if __name__ == '__main__':
    docjcx = Cjcx(url = url,head = head1,data = data)
    docjcx2 = Cjcx(url=url, head=head2, data=data)
    emailop = EmailOP(host="smtp.163.com", port=25, user="xxxxx@163.com", password="xxxxx")
    emailop.send(From="系统管理员", To="qq", Subject="通知", Context="已经开启监测！", to_addrs="xxxxx@qq.com")
    i = 1
    text = ''
    while True:
        print("<------------------------第"+str(i)+"次--------------html-------------------------")

        if i%2 == 0:
            text = docjcx.do()
        else :
            text = docjcx2.do()
        print(text)
        print("------------------------>")
        if querytext in text:
            pass
        elif len(str(text).strip())==0 :
            pass
        else:
            emailop.send(From="系统管理员", To="qq", Subject="通知", Context=sendtext, to_addrs="xxxxx@qq.com")
            print(sendtext)
            print("----------------------系统管理员通知-------------------------->")
        if i < 192:
            passi
        elif i < 264:
            long = 2700
        else:
            long = 1800
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        print("---------------------------------第" + str(i) + "次结束------------------------------->")
        time.sleep(long)
        i = i + 1
