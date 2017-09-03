# 导入MySQL驱动:
import pymysql

# 注意把password设为你的root口令:
conn = pymysql.connect('localhost', 'root', 'kxc_2011', 'testdb')
cursor = conn.cursor()
# 创建user表:
#cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s:
#cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
#cursor.execute('insert into user (id, name) values (%s, %s)', ('4', 'Jack'))
#user_id = '2'
#user_name = 'suki'
#cursor.execute('insert into user values("%s", "%s")' % (user_id, user_name))

#cursor.execute('insert into user (id, name) values ("%s", "%s")' % ('3', 'Adam'))

#插入多行记录：
#cursor.executemany('insert into user values (%s, %s)', [('6', 'Skey'), ('7', 'Qkte')])

print(cursor.rowcount)
# 提交事务:
conn.commit()
#开启自动提交SQL，如果这里不设置，以后的命令需要执行conn.commit()来提交执行，否则都在内存中
#conn.autocommit(True)
cursor.close()

# 运行查询:
#pymysql获取的结果，是以元组的形式输出，对于不了解表结构的人来说，无疑不知道每个元素对应的列。
#因此，如果想要获取字典类型的数据，需要创建游标的时候，设置返回的数据集类型，即：
# 游标设置为字典类型
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
#cursor = conn.cursor()
#cursor.execute('select * from user where id = %s', '4')
#cursor.execute('select * from user where id = "%s"' % '2')
cursor.execute('select * from user')
# 获取第一行数据
value = cursor.fetchone()
# 获取前n行数据  由于上面已经获取了第一行数据，所以此处再获取前2行数据，就是查询出来的数据的第2,3行数据
value_many = cursor.fetchmany(2)
# 获取所有数据
values = cursor.fetchall()
print(value)
print(value_many)
print(values)

# 在fetch数据时按照顺序进行，可以使用cursor.scroll(num,mode)来移动游标位置 如：
cursor.scroll(-1, mode='relative') # 相对当前位置移动，数字1 也可以为负数，只是移动方向不同而已
print(cursor.fetchall())
cursor.scroll(6,mode='absolute') # 相对绝对位置移动
print(cursor.fetchall())

cursor.close()
conn.close()