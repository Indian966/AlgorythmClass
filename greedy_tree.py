names = ['wine', 'beer', 'pizza', 'burger', 'fries', 'cola', 'apple', 'donut', 'cake']
values = [89, 90, 95, 100, 90, 79, 50, 10]
calories = [123, 154, 258, 354, 365, 150, 95, 195]

class Food(object) : # Food객체 생성
    def __init__(self, n, v, c):
        self.name = n
        self.value = v
        self.calories = c

    def getValue(self):
        return self.value

    def getCost(self):
        return self.calories

    def density(self): # 가성비
        return self.getValue()/self.getCost()

    def __str__(self): # taken 객체를 출력하기 위한 함수
        return self.name + ': <' + str(self.value) + ', ' + str(self.calories) + '>' # \자리

def searchTree(toConsider, avail) :
    if toConsider == [] or avail == 0 :
        result = (0,())
    elif toConsider[0].getCost() > avail :
        result = searchTree(toConsider[1:], avail)
    else :
        nextItem = toConsider[0]
        withVal, withToTake = searchTree(toConsider[1:], avail - nextItem.getCost())
        withVal += nextItem.getValue()
        withoutVal, withoutToTake = searchTree(toConsider[1:],avail)
        if withVal > withoutVal :
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    return result

def testMaxVal(foods, maxUnits, printItems=True): # keyFunction에 따라 다른 값 출력
    val, taken = searchTree(foods, maxUnits) # searchTree 리턴값을 taken, val에 넣음
    print('Total value of items taken =', val) # val은 최종 비용
    if printItems :
        for item in taken:  # taken은 결과 배열
            print('  ', item)

def test_greedys(maxUnits):
    foods = []
    for i in range(len(values)):
        foods.append(Food(names[i], values[i], calories[i])) # 음식 배열에 객체 넣음
    print('Use search tree by value to allocate', maxUnits, 'calories')
    testMaxVal(foods, maxUnits)

test_greedys(800)