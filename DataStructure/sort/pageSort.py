def pageSort(A, B):
    for page in A:
        B[page] += 1

    C = sorted(B.items(), key=lambda x: x[1])

    return C
