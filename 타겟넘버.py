from collections import deque

def push(x):
    global q
    q.append(x)

def dfs(numbers, target):
    global q
    
    operations = ['+', '-']
    result_count = 0  # 목표 숫자에 도달한 횟수
    
    while q:
        current_sum, index = q.popleft()  # 큐에서 현재 값과 인덱스를 꺼냄
        
        # 모든 숫자를 다 썼을 때, 목표 값에 도달하면 카운트 증가
        if index == len(numbers):
            if current_sum == target:
                result_count += 1
            continue
        
        # 다음 숫자를 더하거나 빼는 두 가지 경우
        next_number = numbers[index]
        
        # + 연산
        push((current_sum + next_number, index + 1))
        
        # - 연산
        push((current_sum - next_number, index + 1))
    
    return result_count


def solution(numbers, target):
    global q
    
    q = deque([(0, 0)])  # 시작 값은 0, 인덱스는 0부터 시작
    return dfs(numbers, target)
    
