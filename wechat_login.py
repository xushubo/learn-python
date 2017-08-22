# 加载包
import itchat
# 登陆
itchat.auto_login()
# 发送文本消息，发送目标是“文件传输助手”
itchat.send('hello world!', toUserName='filehelper')