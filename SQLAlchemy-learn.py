from sqlalchemy import create_engine

# 使用 Engine/ConnectionPooling/Dialect 进行数据库操作
# Engine使用ConnectionPooling连接数据库，然后再通过Dialect执行SQL语句。
engine = create_engine('mysql+pymysql://root:kxc_2011@localhost:3306/testdb', max_overflow=5)
'''
# 执行SQL
cur = engine.execute("insert into user (id, name) values ('8', 'Hearg')")

# 新插入行自增ID
print(cur.lastrowid)

# 执行SQL
cur = engine.execute('insert into user values (%s, %s)', [('9', 'Qref'), ('10', 'Pter')])

# 执行SQL
cur = engine.execute('insert into user values (%(id)s, %(name)s)', id='11', name='Gert')
'''
# 执行SQL
cur = engine.execute('select * from user')
# 获取第一行数据
# print(cur.fetchone())
# 获取前n行数据
# print(cur.fetchmany(3))
# 获取所有数据
# print(cur.fetchall())