#求质素的函数
#筛选法，筛选掉当前素数的所有倍数，大于当前素数的剩下的最小数为下一个素数
def getPrimeNumber(num):
    #手写3以下的，减少一半筛选
    if num <= 1:
        return prime
    prime = []
    prime.append(2)
    if num == 2:
        return prime
    #从3开始，初始化奇数
    i = 3
    while i<=num:
        prime.append(i)
        i+=2
    #开始筛选
    i=1
    while i<len(prime):
        j = i+1
        while j<len(prime):
            if prime[j] % prime[i] == 0:
                prime.pop(j)
            j+=1
        i+=1
    return prime
    
#判断一个数是不是素数
#素数总是在6x的两侧，6x的两侧不是素数的数能被6x两侧的数整除
import math
def isPrimeNumber(num):
    #直接写出0,1,2,3,4
    if num <=1 or num ==4:
        return False
    if num ==3 :
        return True
    #判断是不是在6x两侧
    if num % 6!=1 and num % 6!=5:
        return False
    #在开方范围测试因数
    n = math.floor(math.sqrt(num))
    i = 5
    #只测试6x两侧的
    while i<=n:
        if num % i ==0 or num % (i+2) ==0:
            return False
        i+=6
    return True
   
   
#扒到的新的优化的筛选法，目前最快
def getPrimeVIP(n):
    primeList = []
    for i in range(n+1):
        primeList.append(False)
    j = 4
    i = 2
    while j <= n: 
        primeList[j] = True
        j = j + i
    for i in range(3,n+1): 
        if not primeList[i]:
            #小于i自己的数的倍数已被去掉，所以不用从i * (小于i的数) 开始，因为会得到小于i的数的倍数
            j = i * i 
        if j > n: 
            break 
        while j <= n: 
            primeList[j] = True 
            #i * i 为奇数，再加i为偶数，偶数已被排除，所以加两次i
            j = j + i + i
    #取出标记为质数的数
    rs = []
    i=0
    for b in primeList:
        if not b:
            rs.append(i)
        i+=1
    if 0 in rs:
        rs.remove(0)
    if 1 in rs:
        rs.remove(1)
    return rs
