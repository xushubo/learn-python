import pickle
import json

d = dict(name='Bob', age=20, score=88)
pd_d = pickle.dumps(d)
print(pickle.dumps(d))
print(type(pd_d))

'''f = open('C:\\Users\\DestoryBlue\\Desktop\\h.txt', 'wb')
pickle.dump(d, f)
f.close()'''

with open('C:\\Users\\DestoryBlue\\Desktop\\h.txt', 'wb') as f:
	pickle.dump(d, f)


with open('C:\\Users\\DestoryBlue\\Desktop\\h.txt', 'rb') as file_for_read:
	dict1 = pickle.load(file_for_read)
print(dict1)
print(type(dict1))
pl_d = pickle.loads(pd_d)
print(pl_d)
print(type(pl_d))


jd_d = json.dumps(d)
jl_d = json.loads(jd_d)
print(jd_d)
print(type(jd_d))
print(jl_d)
print(type(jl_d))

with open('C:\\Users\\DestoryBlue\\Desktop\\l.txt', 'w') as f:
	json.dump(d, f)

with open('C:\\Users\\DestoryBlue\\Desktop\\l.txt', 'r') as file_for_read:
	dict2 = json.load(file_for_read)
print(dict2)
print(type(dict2))


class Student(object):
	def __init__(self, name, age, score):
		self.name = name
		self.age = age
		self.score = score

def student_dict(std):
	return {'name': std.name, 'age': std.age, 'score': std.score}

s = Student('Knight', 30, 100)
jd_s = json.dumps(s, default=student_dict)
print(jd_s)
print(type(jd_s))

jd_s_other = json.dumps(s, default=lambda obj: obj.__dict__)
print(jd_s_other)
print(type(jd_s_other))

def dict_student(d):
	return Student(d['name'], d['age'], d['score'])
json_str = '{"name": "Knight", "score": 100, "age": 30}'

jl_json_str = json.loads(json_str, object_hook=dict_student)
print(jl_json_str)


with open('C:\\Users\\DestoryBlue\\Desktop\\m.txt', 'w') as f:
	json.dump(s, f, default=lambda obj: obj.__dict__)


with open('C:\\Users\\DestoryBlue\\Desktop\\m.txt', 'r') as file_for_read:
	s1 = json.load(file_for_read, object_hook=dict_student)

print(s1)
print(type(s1))