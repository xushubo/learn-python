from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('mysql+pymysql://root:kxc_2011@localhost:3306/testdb?charset=utf8', max_overflow=5)

Base = declarative_base()

'''
多对多连表操作
需求以及数据库结构

需求:

三张表:

主机表:包括nid hostname port ip
管理员表:包括:nid username
主机对应管理员表: nid 主机id,管理员id
一个管理员帐号(比如root),可以关联多台服务器,一个服务器也可以有多个管理员帐号
'''

# 多对多

class HostToHostUser(Base):
	__tablename__ = 'host_to_host_user'
	nid = Column(Integer, primary_key=True, autoincrement=True)
	host_id = Column(Integer, ForeignKey('host.nid'))
	host_user_id = Column(Integer, ForeignKey('host_user.nid'))
	#多对多操作
	host = relationship('Host', backref='h')
	host_user = relationship('HostUser', backref='u')

class Host(Base):
	__tablename__ = 'host'
	nid = Column(Integer, primary_key=True, autoincrement=True)
	hostname = Column(String(32))
	port = Column(String(32))
	ip = Column(String(32))
	####最简单的方式,添加此行就行:
	host_user = relationship('HostUser',secondary=HostToHostUser.__table__, backref='h')

class HostUser(Base):
	__tablename__ = 'host_user'
	nid = Column(Integer, primary_key=True, autoincrement=True)
	username = Column(String(32))

# 定义初始化数据库函数
def init_db():
	Base.metadata.create_all(engine)
# 定义删除数据库函数
def drop_db():
	Base.metadata.drop_all(engine)

drop_db()
init_db()

Session = sessionmaker(bind=engine)
session = Session()

# 插入数据
session.add_all([
	Host(hostname='c1',port='22',ip='1.1.1.1'),
	Host(hostname='c2',port='22',ip='1.1.1.2'),
	Host(hostname='c3',port='22',ip='1.1.1.3'),
	Host(hostname='c4',port='22',ip='1.1.1.4'),
	Host(hostname='c5',port='22',ip='1.1.1.5'),
])
session.commit()

session.add_all([
	HostUser(username='root'),
	HostUser(username='db'),
	HostUser(username='nb'),
	HostUser(username='sb'),
])
session.commit()

session.add_all([
	HostToHostUser(host_id=1,host_user_id=1),
	HostToHostUser(host_id=1,host_user_id=2),
	HostToHostUser(host_id=1,host_user_id=3),
	HostToHostUser(host_id=2,host_user_id=2),
	HostToHostUser(host_id=2,host_user_id=4),
	HostToHostUser(host_id=2,host_user_id=3),
])
session.commit()

# 无虚拟关系的原始方式 需求:查询主机C1的管理员帐号
#1.先在host表中查询c1的nid
host_obj = session.query(Host).filter(Host.hostname=='c1').first()

#2.查询host_to_host_uer表中的所有host_id等于c1的nid的对应的host_user_id
host_2_host_user = session.query(HostToHostUser.host_user_id).filter(HostToHostUser.host_id==host_obj.nid).all()
print(host_2_host_user)
r=zip(*host_2_host_user)
#通过查到的host_user_id查询hostuser表中的对应的管理员用户名
users = session.query(HostUser.username).filter(HostUser.nid.in_(list(list(r)[0]))).all()
print(users)
print(list(zip(*users))[0])

# 虚拟关系的查询
# 需求:同上,查询主机C1的管理员帐号
# 1.反向查找,查询host表中c1的信息,会得到一个对象,对象中存在一个已经设置好的虚拟关系:h
host_obj = session.query(Host).filter(Host.hostname == 'c1').first()
#2.正向查找,遍历对象属性
for item in host_obj.h: # host_obj.h为HostToHostUser对象
	print(item.host_user.username)

# 同一需求最简单的方式
# 需求还是同上:查询主机C1的管理员帐号
# 需要在两张表的一张表中加一条host_user=relationship('HostUser',secondary=HostToHostUser.__table__,backref='h'),我加到了host表中
# 最简单的查询方式:
host_obj = session.query(Host).filter(Host.hostname == 'c1').first()
print(host_obj.host_user)
for item in host_obj.host_user:
	print(item.username)

user_obj = session.query(HostUser).filter(HostUser.username == 'db').first()
print(user_obj.u)
for item in user_obj.u:
	print(item.host.hostname)