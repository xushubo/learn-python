import smtplib
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.utils import parseaddr, formataddr

def _format_addr(s):
	name, addr = parseaddr(s)
	return formataddr((Header(name, 'utf-8').encode(), addr))
from_addr = input('From:')
password = input('Passwd:')
to_addr = input('To:')
smtp_server = input('SMTP server:')

# 邮件对象: 利用MIMEMultipart就可以组合一个HTML和Plain，要注意指定subtype是alternative：
msg = MIMEMultipart('alternative')
msg['From'] = _format_addr('python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理者 <%s>' % to_addr)
msg['Subject'] = Header('来自STMP的问候...', 'utf-8').encode()

# 邮件正文是MIMEText:
msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))
# 发送html附上图片引用（在HTML中通过引用src="cid:0"就可以把附件作为图片嵌入了）
msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
   '<p><img src="cid:0"></p>' +
   '</body></html>', 'html', 'utf-8'))

# 添加附件就是加上一个MIMEBase，从本地读取一个图片:
with open('pillow_learn/IMG_1618.JPG', 'rb') as f:
	# 设置附件的MIME和文件名，这里是jpg类型:
	mime = MIMEBase('image', 'jpeg', filename='IMG_1618.JPG')
	# 加上必要的头信息:
	mime.add_header('Content-Disposition', 'attachment', filename='IMG_1618.JPG')
	mime.add_header('Content-ID', '<0>')
	mime.add_header('X-Attachment-Id', '0')
	# 把附件的内容读进来:
	mime.set_payload(f.read())
	# 用Base64编码:
	encoders.encode_base64(mime)
	# 添加到MIMEMultipart:
	msg.attach(mime)

server = smtplib.SMTP_SSL(smtp_server, 465)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()