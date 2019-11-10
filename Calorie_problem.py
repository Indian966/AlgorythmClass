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

def test_greedys(maxUnits):
    foods = []
    for i in range(len(values)):
        foods.append(Food(names[i], values[i], calories[i])) # 음식 배열에 객체 넣음

    print('Use greedy by value to allocate', maxUnits, 'calories') #칼로리
    testGreedy(foods, maxUnits, Food.getValue)
    print('\nUse greedy by cost to allocate', maxUnits, 'calories') #비용
    testGreedy(foods, maxUnits, lambda x: 1 / Food.getCost(x))
    print('\nUse greedy by density to allocate', maxUnits, 'calories') # 가성비
    testGreedy(foods, maxUnits, Food.density)

def testGreedy(items, constraint, keyFunction): # keyFunction에 따라 다른 값 출력
    taken, val = greedy(items, constraint, keyFunction) # greedy 리턴값을 taken, val에 넣음
    print('Total value of items taken =', val) # val은 최종 비용
    for items in taken: # taken은 결과 배열
        print('  ', items)

def greedy(items, constraint, keyFunction):
    itemsList = sorted(items, key=keyFunction, reverse=True) # 음식 객체를 keyFunction에 따라 정렬 해서 넣음
    result = []
    totalValue, totalCost = 0.0, 0.0

    for i in range(len(itemsList)):
        if (totalCost + itemsList[i].getCost()) <= constraint: # 총 비용 + 음식 비용 <= 최대 비용
            result.append(itemsList[i])
            totalCost += itemsList[i].getCost()
            totalValue += itemsList[i].getValue() # 계속 result[i]에 될때까지 집어넣음
    return (result, totalValue) # 결과를 담은 배열과 최종 비용을 리턴

test_greedys(800)