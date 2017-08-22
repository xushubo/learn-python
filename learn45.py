class Chain(object):
    def __init__(self, path="path"):
        self._path = path

    def __getattr__(self, item):  # 使用实例不存在的属性时，会尝试用该函数解释
        print("got")
        return Chain("%s/%s" % (self._path, item))

    def __str__(self):
        return self._path

    def __call__(self, *args, **kwargs):  #可以直接对实例进行调用
        print("called")
        return Chain("%s=%s" % (self._path, args))



print(Chain(), Chain()(), Chain()()())
print(Chain().status)
print(Chain().status.user("ksven"))
print(Chain().status.user("ksven").timeline)