def fibo_dynamic(n):
    fibo_memo = [0,1]
    if n < 2:
        return fibo_memo[n]
    else :
        for i in range(2,n+1) :
            fibo_memo.append(fibo_memo[i - 1] + fibo_memo[i - 2])
        return fibo_memo[n]

print(fibo_dynamic(10))



