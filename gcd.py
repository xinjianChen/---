#最经典的不就是欧几里得算法啦
#欧几里得算法，gcd(a,b)，b==0的话，a为最大公约数
def gcd(a,b):
    #存好求最大公倍数用
    c=a
    d=b
    #第一次取余后，总是最大的
    while b!=0:
        temp = a % b
        a = b
        b =temp
    #最大公倍数：c=x * a , d=y * a , max = x * a * y 
    return a , int(c/a)*d
