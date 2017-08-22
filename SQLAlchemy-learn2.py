from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine

# 链接数据库采用pymysq模块做映射，后面参数是最大连接数5
engine = create_engine('mysql+pymysql://root:kxc_2011@localhost:3306/testdb', max_overflow=5)

Base = declarative_base()

# 创建表单
class Users(Base):
	__tablename__ = 'users'
	id = Column(Integer, primary_key=True)
	name = Column(String(32))
	extra = Column(String(16))

	__table_args__ = (
		UniqueConstraint('id', 'name', name='uix_id_name'), 
		Index('ix_id_name', 'name', 'extra'),
	)
	def __repr__(self):
		temp = 'id:%s name:%s extra:%s' % (self.id, self.name, self.extra)
		return temp

# 一对多
class Favor(Base):
	__tablename__ = 'favor'
	nid = Column(Integer, primary_key=True)
	caption = Column(String(50), default='red', unique=True)
	def __repr__(self):
		temp = 'nid:%s caption:%s' % (self.nid, self.caption)
		return temp

class Person(Base):
	__tablename__ = 'person'
	nid = Column(Integer, primary_key=True)
	name = Column(String(32), index=True, nullable=True)
	favor_id = Column(Integer, ForeignKey('favor.nid'))
	def __repr__(self):
		temp = 'nid:%s name:%s favor_id:%s' % (self.nid, self.name, self.favor_id)
		return temp

# 多对多
class ServerToGroup(Base):
	__tablename__ = 'servertogroup'
	nid = Column(Integer, primary_key=True, autoincrement=True)
	server_id = Column(Integer, ForeignKey('server.id'))
	group_id = Column(Integer, ForeignKey('group.id'))

class Group(Base):
	__tablename__ = 'group'
	id = Column(Integer, primary_key=True)
	name = Column(String(64), unique=True, nullable=False)

class Server(Base):
	__tablename__ = 'server'
	id = Column(Integer, primary_key=True, autoincrement=True)
	hostname = Column(String(64), unique=True, nullable=False)
	port = Column(Integer, default=22)

# 定义初始化数据库函数
def init_db():
	Base.metadata.create_all(engine)

# 定义删除数据库函数
def drop_db():
	Base.metadata.drop_all(engine)

drop_db()
init_db()

# 创建mysql操作对象
Session = sessionmaker(bind=engine)
session = Session()

# 定义打印查询结果函数
def print_result(result):
	format_r = '%s%-8s%s%-8s%s%-8s%s'
	print('+', '-' * 24, '+')
	print(format_r % ('|', 'id'.center(8), '|', 'name'.center(8), '|', 'extra'.center(8), '|'))
	print('-' * 28)
	for n in range(len(result)):
		print(format_r % ('|', result[n].id, '|', result[n].name, '|', result[n].extra, '|'))
		print('-' * 28)
	print('\n')
'''
	if(isinstance(result, Favor)):
		format_r = '%s%-8s%s%-8s%s'
		print('+', '-' * 15, '+')
		print(format_r % ('|', 'nid'.center(8), '|', 'caption'.center(8), '|'))
		print('-' * 19)
		for n in range(len(result)):
			print(format_r % ('|', result[n].nid, '|', result[n].caption, '|'))
			print('-' * 19)
		print('\n')
'''

obj = Users(name='alex', extra='sb')
session.add(obj)

# add_all 增加多个 列表形式
session.add_all([Users(name='cc', extra='cow'), Users(name='dd', extra='cowcow')])

obj1 = Users(name='suki', extra='perra')
obj2 = Users(name='Anna', extra='perrb')
session.add_all([obj1, obj2])

# 提交
session.commit()

serch_result = session.query(Users).all()
print_result(serch_result)

# 删除user表中id大于4的条目
session.query(Users).filter(Users.id > 4).delete()
session.commit()
serch_result = session.query(Users).all()
print_result(serch_result)

# 更新user表中id小于2的name列为099
session.query(Users).filter(Users.id < 2).update({'name': '099'})

# 更新user表中id大于3的name列，在原字符串后边增加099
session.query(Users).filter(Users.id > 3).update({'name': Users.name + '099'}, synchronize_session=False)

# 更新user表中id等于2的id列，使最终值在原来数值基础上加1   数字相加，必须设置synchronize_session="evaluate"
# session.query(Users).filter(Users.id > 3).update({'id': Users.id + 4}, synchronize_session='evaluate')
# session.commit()

serch_result = session.query(Users).all()
print_result(serch_result)

# 查询生成的sql
sql = session.query(Users)
print(sql)

# 查询User表的name和extra列的所有数据
ret = session.query(Users.name, Users.extra).all() # 返回的是列表，列表元素是一个tuple
print(ret)

# 取全部name列为alex的数据
ret = session.query(Users).filter(Users.name == 'suki099').all()
print_result(ret)
ret = session.query(Users).filter_by(name='suki099').all()
print_result(ret)

# 第一个匹配name列为alex的数据 first()方法返回的是一个Users对象
ret = session.query(Users).filter_by(name='suki099').first()
print(ret.name, ret.extra)

# 且的关系
ret = session.query(Users).filter(Users.id > 1, Users.name == 'suki099').all()
print_result(ret)
ret = session.query(Users).filter(Users.id.between(7, 9), Users.name == 'suki099').all()
print_result(ret)

ret = session.query(Users).filter(Users.id.in_([1, 2, 4])).all()
print_result(ret)

ret = session.query(Users).filter(~Users.id.in_([1, 2, 4])).all() # ~表示非。就是not in的意思
print_result(ret)

# 联表查询
ret = session.query(Users).filter(Users.id.in_(session.query(Users.id).filter(Users.name == 'suki099'))).all()
print_result(ret)


from sqlalchemy import and_, or_  # 且和or的关系

# 条件以and方式排列  此处不能用filter_by()方法
ret = session.query(Users).filter(and_(Users.id > 3, Users.name == 'suki099')).all()
print_result(ret)
# 条件以or方式排列
ret = session.query(Users).filter(or_(Users.id < 2, Users.name == 'suki099')).all()
print_result(ret)

ret = session.query(Users).filter(
	or_( #这部分表示括号中的条件都以or的形式匹配
	Users.id < 2,
	and_(Users.id > 7, Users.name == 'suki099'), # 表示括号中这部分进行and匹配
	Users.extra == 'cow'
	)).all()
print_result(ret)

# 通配符  匹配name列以s开头的所有数据
ret = session.query(Users).filter(Users.name.like('s%')).all()
print_result(ret)
#匹配name列以s开头且extra列以a结尾的所有数据
ret = session.query(Users).filter(and_(Users.name.like('s%'), Users.extra.like('%a'))).all()
print_result(ret)
#匹配extra列中间有o的列的所有数据
ret = session.query(Users).filter(Users.extra.like('%o%')).all()
print_result(ret)

# 表示not like
ret = session.query(Users).filter(~Users.name.like('0%')).all()
print_result(ret)

ret = session.query(Users).filter(~and_(Users.name.like('s%'), Users.extra.like('%a'))).all()
print_result(ret)


# 限制 limit用法  相当于查询的结果为一个list 然后切片的作用
ret =session.query(Users)[0:2]
print_result(ret)

# 排序
ret = session.query(Users).order_by(Users.name.desc()).all()  # desc() 按降序排列 asc()按升序排列
print_result(ret)
# 按照name从大到小排列，如果name相同，按照id从小到大排列
ret = session.query(Users).order_by(Users.name.desc(), Users.id.asc()).all()
print_result(ret)

# 分组
from sqlalchemy.sql import func

obj = Users(name='cc', extra='over')
session.add(obj)
obj = Users(name='oo', extra='sb')
session.add(obj)
obj = Users(name='cc', extra='kk')
session.add(obj)
session.commit()

ret = session.query(Users).all()
print_result(ret)

ret = session.query(Users).group_by(Users.extra).all()
print_result(ret)

ret = session.query(Users).group_by(Users.name).all()
print_result(ret)

ret = session.query(
	func.max(Users.id),
	func.sum(Users.id),
	func.min(Users.id)).group_by(Users.name).all()
print(ret)

# having对聚合的内容再次进行过滤
ret = session.query(
	func.max(Users.id),
	func.sum(Users.id),
	func.min(Users.id)).group_by(Users.name).having(func.min(Users.id) > 2).all()
print(ret)

#添加favor表内容
obj = Favor()
session.add(obj)
obj1 = Favor(caption='blue')
obj2 = Favor(caption='yellow')
obj3 = Favor(caption='green')
obj4 = Favor(caption='orange')
session.add_all([obj1, obj2, obj3, obj4])
session.commit()

# 连表
ret = session.query(Users, Favor).filter(Users.id == Favor.nid).all()
print(ret)

#添加Person表内容
obj = Person(name='suki099', favor_id=4)
obj1 = Person(name='Anma1', favor_id=3)
obj2 = Person(name='Anma2', favor_id=2)
obj3 = Person(name='Anma3', favor_id=1)
session.add_all([obj, obj1, obj2, obj3])
session.commit()

#两表需设置外键关联方可使用join方法
# ret = session.query(Users).join(Favor).all()   # Users和Favor没有设置外键关联无法使用join()方法
ret = session.query(Person).join(Favor).all() # 返回的是Person类
print(ret)
ret= session.query(Favor).join(Person).all()
print(ret)

#查询Person表中人对应喜欢的颜色
ret = session.query(Person.nid, Person.name, Favor.caption).join(Favor).all()
print(ret)
#查询Favor表中颜色对应喜欢这种颜色的人的信息
ret = session.query(Favor.nid, Favor.caption, Person.name).join(Person).all()
print(ret)
ret = session.query(Favor.nid, Favor.caption, Person.name).join(Person, isouter=True).all()
print(ret)

#LEFT JOIN 关键字会从左表 (Persons) 那里返回所有的行，即使在右表 (Favor) 中没有匹配的行
ret = session.query(Person).join(Favor, isouter=True).all()  # isouter表示是left join
print(ret)
ret = session.query(Favor).join(Person, isouter=True).all()
print(ret)



# 组合
q1 = session.query(Users.name).filter(Users.id > 2)
q2 = session.query(Favor.caption).filter(Favor.nid < 2)
ret = q1.union(q2).all() #union默认会去重
print(ret)

q1 = session.query(Users.name).filter(Users.id > 2)
q2 = session.query(Person.name).filter(Person.favor_id > 2)
ret = q1.union(q2).all()
print(ret)

ret = q1.union_all(q2).all() # union_all不去重
print(ret)