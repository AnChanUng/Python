# [실습4-3] 고정 길이 큐 클래스 FixedQueue 구현하기

from typing import Any

class FixedQueue:

    class Empty(Exception):
        """비어 있는 FixedQueue에서 인큐할 때 내보내는 예외 처리"""
        pass
    
    class Full(Exception):
        """가득 차 있는 FixedQueue에서 인큐할 때 내보내는 예외 처리"""
        pass
    
    def __init__(self, capacity: int) -> None:
        """큐 초기화"""
        self.no = 0                     # 현재 데이터 개수
        self.front = 0                  # 맨 앞 원소 커서
        self.rear = 0                   # 맨 끝 원소 커서
        self.capacity = capacity        # 큐의 크기
        self.que = [None] * capacity    # 큐의 본체
    
    def __len__(self) -> int:
        """큐가 비어 있는 모든 데이터 개수를 반환"""
        return self.no
    
    def is_empty(self) -> bool:
        """큐가 비어 있는지 판단"""
        return self.no <= 0
    
    def is_full(self) -> bool:
        """큐가 가득 차 있는지 판단"""
        return self.no >= self.capacity


    def enque(self, x: Any) -> None:
        """데이터 x를 인큐"""
        if self.is_full():
            raise FixedQueue.Full       # 큐가 가득 차 있는 경우 예외처리 발생
        self.que[self.rear] = x
        self.rear += 1
        self.no += 1
        if self.rear == self.capacity:
            self.rear = 0
    
    def deque(self) -> Any:
        """데이터를 디큐"""
        if self.is_empty():
            raise FixedQueue.Empty      # 큐가 비어 있는 경우 예외 처리 발생
        x = self.que[self.front]
        self.front += 1
        self.no -= 1
        if self.front == self.capacity:
            self.front = 0
        return x

    def peek(self) -> Any:
        """큐에서 데이터를 피크"""
        if self.is_empty():
            raise FixedQueue.Empty
        return self.que[self.front]

    def find(self, value: Any) -> Any:
        """큐에서 value를 찾아 인덱스를 반환(없으면 -1을 반환)"""
        for i in range(self.no):
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value:          # 검색 성공
                return idx
        return -1                               # 검색 실패

    def count(self, value: Any) -> bool:
        """큐에 있는 value의 개수를 반환"""
        c = 0                   
        for i in range(self.no):                # 큐 데이터를 선형검색
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value:          # 검색 성공
                c += 1                          # 들어 있음
        return c

    def __contains__(self, value: Any) -> bool:
        """큐에 value가 있는지를 판단"""
        return self.count(value)
    
    def clear(self) -> None:
        """큐에 모든 데이터를 비움"""
        self.no = self.fornt = self.rear = 0

    def dump(self) -> None:
        """모든 데이터를 맨 앞부터 맨 끝 순으로 출력"""
        if self.is_empty():
            print('큐가 비어있습니다.')
        else:
            for i in range(self.no):
                print(self.que[(i + self.front) % self.capacity], end ='')
            print()