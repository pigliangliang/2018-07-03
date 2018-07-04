#author_by zhuxiaoliang
#2018-07-03 下午11:39

#一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
#方法一：递归+lambda函数

fib  = lambda n:n if n <=2 else fib(n-1)+fib(n-2)
print(fib(4))
#方法二：装饰器

def memo(func):
    cache={}
    def warp(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return warp

@memo
def fib(i):
    if i <2:
        return 1
    return fib(i -1) +fib(i-2)

print(fib(4))


# 方法三

def fib(n):
    a,b = 0,1
