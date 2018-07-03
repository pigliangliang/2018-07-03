#author_by zhuxiaoliang
#2018-07-03 上午11:42

#1、new方式创建

class Singleton(object):
    def new(cls,*args,**kwargs):
        if not hasattr(cls,"_instance"):
            orig = super(Singleton,cls)
            cls._instance = orig.new(cls,*args,**kwargs)
            return cls._instance

class Myclass(Singleton):
    def __init__(self):
        pass

#2、共享方式

class Borg(object):
    _state={}
    def new(cls,*args,**kwargs):
        ob = super(Borg,cls).new(cls,*args,**kwargs)
        ob.dict = cls._state
        return ob

#3、装饰器版本 4、import 方式 参考2018-07-01

#is 和== 区别
#is 地址值相等
#== 值相等
a = 2
b = 2
print(a is b)
print(a == b)
print(id(a),id(b))

