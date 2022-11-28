def getPairsCount(arr, N, K):
    count = 0  # Initialize result

    # Consider all possible pairs
    # and check their sums
    for i in range(0, N):
        for j in range(i + 1, N):
            if arr[i] + arr[j] == K:
                count += 1

    return count


# Driver function
arr = [1,1,1,1]
N = len(arr)
K = 2
print("Count of pairs is",
      getPairsCount(arr, N, K))