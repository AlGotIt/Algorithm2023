# python 3.9

def solution(sticker) -> int:
    """
    Args:
        sticker (list): 스티커 값 리스트

    Returns:
        int: 규칙대로 스티커를 제거했을 때 얻을 수 있는 최댓값
    """

    # case 0 : 스티커가 한 개일 때
    if len(sticker) < 2:
        return sticker[0]

    # dp 세팅
    maximum_0 = [0 for _ in range(len(sticker))]
    maximum_1 = maximum_0[:]

    maximum_0[0], maximum_0[1] = sticker[0], sticker[0]
    maximum_1[0], maximum_1[1] = 0, sticker[1]

    for i in range(2, len(sticker)):
        # case 1 : index 0을 포함
        maximum_0[i] = max(maximum_0[i-2] + sticker[i], maximum_0[i-1])
        # case 2 : index 1을 포함
        maximum_1[i] = max(maximum_1[i-2] + sticker[i], maximum_1[i-1])

    return max(maximum_0[-2], maximum_1[-1])


sticker = [14, 6, 5, 11, 3, 9, 2, 10]
print(solution(sticker))
