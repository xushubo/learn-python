from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('mysql+pymysql://root:kxc_2011@localhost:3306/testdb?charset=utf8', max_overflow=5)

Base = declarative_base()

# 一对多

class School(Base):
	__tablename__ = 'school'
	id_sc = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String(32))

class Student(Base):
	__tablename__ = 'student'
	id_st = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String(32))
	school_id = Column(Integer, ForeignKey('school.id_sc'))
	# 虚拟创建关系,relationship  一般是跟foreginkey 在一起使用
	school = relationship('School', backref='sdt')
	# 自定义输出方式
	def __repr__(self):
		temp = 'id_st:%s name:%s school_id:%s' % (self.id_st, self.name, self.school_id)
		return temp

# 定义初始化数据库函数
def init_db():
	Base.metadata.create_all(engine)
# 定义删除数据库函数
def drop_db():
	Base.metadata.drop_all(engine)

drop_db()
init_db()

# 插入数据
Session = sessionmaker(bind=engine)
session = Session()

session.add_all([
	School(name='东荟幼儿园'), 
	School(name='加拿达幼儿园')
	])

session.add_all([
	Student(name='吴彦祖', school_id=1),
	Student(name='金城武', school_id=1),
	Student(name='吴亦凡', school_id=2),
	Student(name='鹿晗', school_id=2)
	])
session.commit()

# 无虚拟关系的原始查询方式 需求:查询student表中姓名并且显示各自的学校
ret = session.query(Student.name, School.name).join(School, isouter=True).all()
print(ret)

# 反向查询原始方式 需求:查询school表中属于东荟幼儿园的学生名
ret = session.query(Student.name, School.name).join(School, isouter=True).filter(School.name=='东荟幼儿园').all()
print(ret)

# 虚拟关系的查询方式
# 正向查询
# 需求:查询student表中所有数据,并且显示对应的学校表中的数据
# 首先肯定要设定一个虚拟关系: school = relationship("School",backref='std')
ret = session.query(Student).all()
for obj in ret:
#    #obj 代指student表的每一行数据
#    #obj.school 代指school对象
	print(obj.id_st, obj.name, obj.school_id, obj.school, obj.school.id_sc, obj.school.name)
# 注意:多对一正向查询,一条命令即可,直接看对象中的属性即可

# 反向查询
# 需求:查询学生组中属于东荟幼儿园的学生名
# school中得到一个对象
obj = session.query(School).filter(School.name=='东荟幼儿园').first() #first()返回一个对象 all()返回一个列表
print(obj.id_sc, obj.name)
print(obj.sdt)
# 注意:多对一反向查询,需要遍历对象属性