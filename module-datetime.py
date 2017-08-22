from datetime import datetime, timedelta, timezone

now = datetime.now()
print(now)
print(type(now))

dt = datetime(2017, 5, 12, 12, 15, 11)
print(dt)
t = dt.timestamp()
print(t)

dt1 = datetime.fromtimestamp(t) #上述转换是在timestamp和本地时间做转换
print(dt1)

dt2 = datetime.utcfromtimestamp(t) #timestamp也可以直接被转换到UTC标准时区的时间
print(dt2)

#很多时候，用户输入的日期和时间是字符串，要处理日期和时间，首先必须把str转换为datetime。
#转换方法是通过datetime.strptime()实现，需要一个日期和时间的格式化字符串：
cday = datetime.strptime('2017-5-12 12:00:09', '%Y-%m-%d %H:%M:%S')
print(cday)

#如果已经有了datetime对象，要把它格式化为字符串显示给用户，就需要转换为str，
#转换方法是通过strftime()实现的，同样需要一个日期和时间的格式化字符串：
print(now.strftime('%y %a %b %d %H:%M:%S'))

#对日期和时间进行加减实际上就是把datetime往后或往前计算，
#得到新的datetime。加减可以直接用+和-运算符，不过需要导入timedelta这个类：
print(now)
print(now + timedelta(hours=10))
print(now + timedelta(days=1))
print(now + timedelta(days=2, hours=12))

#一个datetime类型有一个时区属性tzinfo，但是默认为None，
#所以无法区分这个datetime到底是哪个时区，除非强行给datetime设置一个时区：
tz_utc_8 = timezone(timedelta(hours=8))# 创建时区UTC+8:00
tempt = now.replace(tzinfo=tz_utc_8)# 强制设置为UTC+8:00
print(tempt)

#我们可以先通过utcnow()拿到当前的UTC时间，再转换为任意时区的时间：
# 拿到UTC时间，并强制设置时区为UTC+0:00:
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)

# astimezone()将转换时区为北京时间:
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)

# astimezone()将转换时区为东京时间
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)

# astimezone()将bj_dt转换时区为东京时间:
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt2)

print(utc_dt.timestamp())
print(bj_dt.timestamp())
print(tokyo_dt.timestamp())