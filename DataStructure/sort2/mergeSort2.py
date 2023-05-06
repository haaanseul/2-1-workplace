def mergeSort2(C, p:int, r:int):
    if p < r:
        q = (p+r) // 2
        mergeSort2(C, p, q)
        mergeSort2(C, q+1, r)
        merge(C, p, q, r)

def merge(C, p:int, q:int, r:int):
    i = p; j = q+1; t = 0
    tmp = [0 for i in range(len(C))]
    while i <= q and j <= r:
        if C[i][1] <= C[j][1]:
            tmp[t] = C[i]; t += 1; i += 1
        else:
            tmp[t] = C[j]; t += 1; j += 1

    while i <= q:
        tmp[t] = C[i]; t += 1; i += 1

    while j <= r:
        tmp[t] = C[j]; t += 1; j += 1

    i = p; t= 0

    while i <= r:
        C[i] = tmp[t]; t += 1; i += 1
