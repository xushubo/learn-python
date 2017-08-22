# -*- coding:utf-8 -*-

import re
from datetime import datetime, timezone, timedelta

def to_timestamp(dt_str, tz_str):
	temp_time = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
	if re.match(r'^UTC\+([0-9]|0[0-9]|1[0-2]):00$', tz_str):
		temp_timezone = timezone(timedelta(hours=int(re.match(r'^UTC\+([0-9]|0[0-9]|1[0-2]):00$', tz_str).group(1))))
	elif re.match(r'^UTC\-([0-9]|0[0-9]|1[0-2]):00$', tz_str):
		temp_timezone = timezone(timedelta(hours=-int(re.match(r'^UTC\-([0-9]|0[0-9]|1[0-2]):00$', tz_str).group(1))))
	dt = temp_time.replace(tzinfo=temp_timezone)
	dt_timestamp = dt.timestamp()
	return dt_timestamp

if __name__ == '__main__':
	t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
	assert t1 == 1433121030.0, t1

	t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
	assert t2 == 1433121030.0, t2

	print('Pass')
	print(t1)
	t3 = to_timestamp('2015-6-1 08:10:30', 'UTC+8:00')
	print(t3)