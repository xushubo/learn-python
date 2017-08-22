import itchat
from echarts import Echart, Legend, Pie
itchat.login() #登录
friends = itchat.get_friends(update=True)[0:] #获取好友列表
male = female = other = 0 #初始化计数器，男、女、不填的
for i in friends[1:]:  #遍历好友列表，列表第一个是自己，所以从1开始计算  1表示男性，2女性
	sex = i['Sex']
	if sex == 1:
		male +=1
	elif sex == 2:
		female += 1
	else:
		other += 1
total = len(friends[1:])
print('wechat好友总数：%d' % total)
print('男性好友： %.2f%%' % (float(male)/total*100))
print('女性好友： %.2f%%' % (float(female)/total*100))
print('其他： %.2f%%' % (float(other)/total*100))

'''
chart = Echart('%s的微信好友性别比例' % (friends[0]['NickName']), 'from WeChat')
chart.use(Pie('WeChat', [{'value': male, 'name': '男性 %.2f%%' % (float(male) / total * 100)}, {'value': female, 'name': '女性 %.2f%%' % (float(female) / total * 100)}, {'value': other, 'name': '其他 %.2f%%' % (float(other) / total * 100)}], radius=["50%", "70%"]))
chart.use(Legend(['male', 'female', 'other']))
del chart.json['xAxis']
del chart.json['yAxis']
chart.plot()
'''