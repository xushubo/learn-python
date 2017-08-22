import os, sqlite3

db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
	os.remove(db_file)

# 初始数据：
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
cursor.close()
conn.commit()
conn.close()

def get_score_in(low, high):
	conn_getscore = sqlite3.connect('test.db')
	cursor_getscore = conn_getscore.cursor()
	cursor_getscore.execute("select name from user where score between ? and ? order by score", (low, high))
	values = cursor_getscore.fetchall()
	cursor_getscore.close()
	conn_getscore.close()
	result_list = []
	for name in values:
		result_list.append(name[0])
	return result_list


if __name__ == '__main__':
	assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
	assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
	assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)
	print('Pass')