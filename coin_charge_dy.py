def coin_charge (n) :
    money = [0]
    coin = [1, 4, 5, 6]
    for i in range(1,n+1) :
        money.append(999)
    for i in range(4) :
        print(coin[i], "원짜리 동전 사용")
        for j in range(coin[i], n+1) :
            money[j] = min(money[j], money[j - coin[i]] + 1)
            print("바꾸고자하는 돈:", j,"동전 갯수" ,money[j])

coin_charge(14)