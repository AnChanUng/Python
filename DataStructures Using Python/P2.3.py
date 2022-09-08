class myBag:
    def contaions(myBag, e): # bag에 항목 e가 있는지 검사하는 함수
        return e in myBag

    def insert(myBag, e):    # bag에 항목 e를 넣는 함수
        myBag.append(e)

    def remove(myBag, e):    # bag에 항목 e를 삭제하는 함수
        myBag.remove(e)

    def count(myBag):        # bag의 전체 항목 수를 계산하는 함수
        return len(myBag)

myBag = []
insert(myBag, '휴대폰');   
insert(myBag, '지갑')
insert(myBag, '손수건');    
insert(myBag, '빗')
insert(myBag, '자료구조');  
insert(myBag, '야구공')
print('가방속의 물건:', myBag)

myBag.insert('빗')
myBag.remove('손수건')
print('가방속의 물건:', myBag)