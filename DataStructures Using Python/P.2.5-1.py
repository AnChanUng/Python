class Bag:
    def contaions(bag, e): # bag에 항목 e가 있는지 검사하는 함수
        return e in bag

    def insert(bag, e):    # bag에 항목 e를 넣는 함수
        bag.append(e)

    def remove(bag, e):    # bag에 항목 e를 삭제하는 함수
        bag.remove(e)

    def count(bag):        # bag의 전체 항목 수를 계산하는 함수
        return len(bag)

myBag = Bag()
Bag.insert('휴대폰');    Bag.insert('지갑')
Bag.insert('손수건');    Bag.insert('빗')
Bag.insert('자료구조');  Bag.insert('야구공')
print('가방속의 물건:', myBag.bag)

Bag.insert('빗')
Bag.remove('손수건')
print('가방속의 물건:', myBag.bag)