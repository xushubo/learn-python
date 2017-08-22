from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib


def _format_addr(s):
	name, addr = parseaddr(s)
	return formataddr((Header(name, 'utf-8').encode(), addr))

# 输入Email地址和口令:
from_addr = input('From:')
password = input('password:')
# 输入收件人地址:
to_addr = input('To:')
# 输入SMTP服务器地址:
smtp_server = input('SMTP server:')

# msg = MIMEText('hello, send by python...', 'plain', 'utf-8')
msg = MIMEText('<html><body><h1>Hello</h1>' +
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '</body></html>', 'html', 'utf-8')
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候...', 'utf-8').encode()

# SMTP协议默认端口是25
server = smtplib.SMTP_SSL(smtp_server, 465)
#打印出和SMTP服务器交互的所有信息
server.set_debuglevel(1)
server.login(from_addr, password)
#as_string()把MIMEText对象变成str
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
