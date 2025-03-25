def solution(array):
    if not array:  # 빈 배열 처리
        return None
    if len(array) == 1:
        return array[0]

    counts = {}  # 딕셔너리 초기화
    for num in array:
        counts[num] = counts.get(num, 0) + 1  # defaultdict 대신 get() 사용

    max_count = max(counts.values(), default=0)  # 값이 없을 경우 대비
    modes = [key for key, value in counts.items() if value == max_count]

    return -1 if len(modes) > 1 else modes[0]
