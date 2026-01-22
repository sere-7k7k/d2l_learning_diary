import os
def calculateArrayXOR(arr):
    n = len(arr)

    # if n is even, answer is 0
    if n % 2 == 0:
        return 0

    # if n is odd, XOR all elements at even indices
    answer = 0
    for i in range(0, len(arr), 2):   # 0,2,4,...
        answer ^= arr[i]

    return answer
if __name__ == '__main__':

    arr_count = int(input().strip())
    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = calculateArrayXOR(arr)

    print(result)