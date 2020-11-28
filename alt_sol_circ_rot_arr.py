def solution(K,A):
    if len(A) == 0:
        return A
    if K == 0: 
        return A
    start = len(A) - K%len(A)
    b = A[start:] + A[:start] 
    return b
