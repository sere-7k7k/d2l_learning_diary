def getMaximumSubarray(arr):
    n = len(arr)
    if n == 1:
        return 0

    idx_1 = arr.index(1)
    if idx_1 == 0 or idx_1 == n - 1:
        return n - 1

    # helper: expand an interval until it becomes a valid permutation
    # validity condition for a permutation segment containing 1 is:
    # max(segment) == len(segment)
    def expand(L, R, direction):
        current_max = 0
        for i in range(L, R + 1):
            if arr[i] > current_max:
                current_max = arr[i]

        while (R - L + 1) != current_max:
            if direction == "left":
                L -= 1
                if arr[L] > current_max:
                    current_max = arr[L]
            else:  # direction == "right"
                R += 1
                if arr[R] > current_max:
                    current_max = arr[R]

        return (R - L + 1)


    kept1 = expand(0, idx_1, "right")     # keep prefix, expand right
    kept2 = expand(idx_1, n - 1, "left")  # keep suffix, expand left

    kept_len = min(kept1, kept2)
    return n - kept_len
if __name__ == '__main__':
    n = int(input().strip())
    arr = [int(input().strip()) for _ in range(n)]
    print(getMaximumSubarray(arr))
