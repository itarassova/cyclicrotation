def solution(K,A):
    b = [-1] * len(A)
    for i in range(0, len(A)):
        new_index = (i+K)%len(A)
        b[i] = A[i]
    return b
